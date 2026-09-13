from gen.NNGraphVisitor import NNGraphVisitor
from compiler.models import Model, Node, Edge


class ModelVisitor(NNGraphVisitor):

    def __init__(self):
        super().__init__()
        self.model = Model()

    def getModel(self):
        return self.model

    def visitModelDecl(self, ctx):
        self.model.name = ctx.ID().getText()
        return self.visitChildren(ctx)

    def visitInputDecl(self, ctx):
        self.model.input_name = ctx.ID().getText()
        return self.visitChildren(ctx)

    def visitOutputDecl(self, ctx):
        self.model.output_name = ctx.ID().getText()
        return None

    def visitShape(self, ctx):
        self.model.input_shape = [
            int(i.getText())
            for i in ctx.INT()
        ]
        return None

    def visitNodeDecl(self, ctx):

        node_id = ctx.ID().getText()

        node_type = ctx.nodeType().getText().split("(")[0]

        params = self.visit(ctx.nodeType())

        if params is None:
            params = {}

        node = Node(
            node_id=node_id,
            node_type=node_type,
            params=params
        )

        self.model.nodes.append(node)

        return None

    def visitNodeType(self, ctx):

        if ctx.layer():
            return self.visit(ctx.layer())

        if ctx.activation():
            return self.visit(ctx.activation())

        if ctx.operation():
            return self.visit(ctx.operation())

        return {}

    def _visitLayerWithParams(self, ctx):

        plist = ctx.parameterList()

        if plist:
            return self.visit(plist)

        return {}

    def visitLinearLayer(self, ctx):
        return self._visitLayerWithParams(ctx)

    def visitConv2dLayer(self, ctx):
        return self._visitLayerWithParams(ctx)

    def visitConv1dLayer(self, ctx):
        return self._visitLayerWithParams(ctx)

    def visitBatchNormLayer(self, ctx):
        return self._visitLayerWithParams(ctx)

    def visitLayerNormLayer(self, ctx):
        return self._visitLayerWithParams(ctx)

    def visitMaxPoolLayer(self, ctx):
        return self._visitLayerWithParams(ctx)

    def visitAvgPoolLayer(self, ctx):
        return self._visitLayerWithParams(ctx)

    def visitDropoutLayer(self, ctx):
        return self._visitLayerWithParams(ctx)

    def visitFlattenLayer(self, ctx):
        return self._visitLayerWithParams(ctx)

    def visitEmbeddingLayer(self, ctx):
        return self._visitLayerWithParams(ctx)

    def visitMultiHeadLayer(self, ctx):
        return self._visitLayerWithParams(ctx)

    def visitLstmLayer(self, ctx):
        return self._visitLayerWithParams(ctx)

    def visitGruLayer(self, ctx):
        return self._visitLayerWithParams(ctx)

    def visitReluLayer(self, ctx):
        return {}

    def visitSigmoidLayer(self, ctx):
        return {}

    def visitTanhLayer(self, ctx):
        return {}

    def visitGeluLayer(self, ctx):
        return {}

    def visitSoftmaxLayer(self, ctx):
        return self._visitLayerWithParams(ctx)

    def visitLeakyReluLayer(self, ctx):
        return self._visitLayerWithParams(ctx)

    def visitEluLayer(self, ctx):
        return self._visitLayerWithParams(ctx)

    def visitAddLayer(self, ctx):
        return {}

    def visitConcatLayer(self, ctx):
        return self._visitLayerWithParams(ctx)

    def visitResidualLayer(self, ctx):
        return {}

    def visitSplitLayer(self, ctx):
        return self._visitLayerWithParams(ctx)


    def visitParameterList(self, ctx):

        params = {}

        for parameter in ctx.parameter():
            key, value = self.visit(parameter)

            params[key] = value

        return params

    def visitParameter(self, ctx):

        key = ctx.parameterName().getText()

        value = self.visit(ctx.value())

        return key, value

    def visitValue(self, ctx):

        if ctx.INT():
            return int(ctx.INT().getText())

        if ctx.FLOAT():
            return float(ctx.FLOAT().getText())

        if ctx.STRING():
            return ctx.STRING().getText()[1:-1]

        if ctx.TRUE():
            return True

        if ctx.FALSE():
            return False

        if ctx.NONE():
            return None

        if ctx.tuple_():
            return self.visit(ctx.tuple_())

        return None

    def visitTuple(self, ctx):

        return [
            self.visit(value)
            for value in ctx.value()
        ]

    def visitEdgeDecl(self, ctx):

        source = ctx.ID(0).getText()
        destination = ctx.ID(1).getText()

        label = None

        if ctx.edgeLabel():
            label = ctx.edgeLabel().STRING().getText()[1:-1]

        edge = Edge(
            source,
            destination,
            label
        )

        self.model.edges.append(edge)

        return None

    def visitConfigItem(self, ctx):

        key = ctx.getChild(0).getText()
        value = ctx.getChild(2).getText()

        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]

        elif value.isdigit():
            value = int(value)

        if hasattr(self.model.config, key):
            setattr(self.model.config, key, value)

        return None