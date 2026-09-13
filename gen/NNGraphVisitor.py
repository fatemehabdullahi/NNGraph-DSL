# Generated from C:/Users/Lenovo/PycharmProjects/Final Project/NNGraph.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .NNGraphParser import NNGraphParser
else:
    from NNGraphParser import NNGraphParser

# This class defines a complete generic visitor for a parse tree produced by NNGraphParser.

class NNGraphVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by NNGraphParser#program.
    def visitProgram(self, ctx:NNGraphParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#modelDecl.
    def visitModelDecl(self, ctx:NNGraphParser.ModelDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#inputDecl.
    def visitInputDecl(self, ctx:NNGraphParser.InputDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#outputDecl.
    def visitOutputDecl(self, ctx:NNGraphParser.OutputDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#tensorType.
    def visitTensorType(self, ctx:NNGraphParser.TensorTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#shape.
    def visitShape(self, ctx:NNGraphParser.ShapeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#graphDecl.
    def visitGraphDecl(self, ctx:NNGraphParser.GraphDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#graphStatement.
    def visitGraphStatement(self, ctx:NNGraphParser.GraphStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#nodeDecl.
    def visitNodeDecl(self, ctx:NNGraphParser.NodeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#nodeType.
    def visitNodeType(self, ctx:NNGraphParser.NodeTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#edgeDecl.
    def visitEdgeDecl(self, ctx:NNGraphParser.EdgeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#edgeLabel.
    def visitEdgeLabel(self, ctx:NNGraphParser.EdgeLabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#configDecl.
    def visitConfigDecl(self, ctx:NNGraphParser.ConfigDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#configItem.
    def visitConfigItem(self, ctx:NNGraphParser.ConfigItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#value.
    def visitValue(self, ctx:NNGraphParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#tuple.
    def visitTuple(self, ctx:NNGraphParser.TupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#parameterList.
    def visitParameterList(self, ctx:NNGraphParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#parameter.
    def visitParameter(self, ctx:NNGraphParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#parameterName.
    def visitParameterName(self, ctx:NNGraphParser.ParameterNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#layer.
    def visitLayer(self, ctx:NNGraphParser.LayerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#activation.
    def visitActivation(self, ctx:NNGraphParser.ActivationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#operation.
    def visitOperation(self, ctx:NNGraphParser.OperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#linearLayer.
    def visitLinearLayer(self, ctx:NNGraphParser.LinearLayerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#conv2dLayer.
    def visitConv2dLayer(self, ctx:NNGraphParser.Conv2dLayerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#conv1dLayer.
    def visitConv1dLayer(self, ctx:NNGraphParser.Conv1dLayerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#batchNormLayer.
    def visitBatchNormLayer(self, ctx:NNGraphParser.BatchNormLayerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#layerNormLayer.
    def visitLayerNormLayer(self, ctx:NNGraphParser.LayerNormLayerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#maxPoolLayer.
    def visitMaxPoolLayer(self, ctx:NNGraphParser.MaxPoolLayerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#avgPoolLayer.
    def visitAvgPoolLayer(self, ctx:NNGraphParser.AvgPoolLayerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#dropoutLayer.
    def visitDropoutLayer(self, ctx:NNGraphParser.DropoutLayerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#flattenLayer.
    def visitFlattenLayer(self, ctx:NNGraphParser.FlattenLayerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#embeddingLayer.
    def visitEmbeddingLayer(self, ctx:NNGraphParser.EmbeddingLayerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#multiHeadLayer.
    def visitMultiHeadLayer(self, ctx:NNGraphParser.MultiHeadLayerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#lstmLayer.
    def visitLstmLayer(self, ctx:NNGraphParser.LstmLayerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#gruLayer.
    def visitGruLayer(self, ctx:NNGraphParser.GruLayerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#reluLayer.
    def visitReluLayer(self, ctx:NNGraphParser.ReluLayerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#sigmoidLayer.
    def visitSigmoidLayer(self, ctx:NNGraphParser.SigmoidLayerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#tanhLayer.
    def visitTanhLayer(self, ctx:NNGraphParser.TanhLayerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#geluLayer.
    def visitGeluLayer(self, ctx:NNGraphParser.GeluLayerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#softmaxLayer.
    def visitSoftmaxLayer(self, ctx:NNGraphParser.SoftmaxLayerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#leakyReluLayer.
    def visitLeakyReluLayer(self, ctx:NNGraphParser.LeakyReluLayerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#eluLayer.
    def visitEluLayer(self, ctx:NNGraphParser.EluLayerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#addLayer.
    def visitAddLayer(self, ctx:NNGraphParser.AddLayerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#concatLayer.
    def visitConcatLayer(self, ctx:NNGraphParser.ConcatLayerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#residualLayer.
    def visitResidualLayer(self, ctx:NNGraphParser.ResidualLayerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#splitLayer.
    def visitSplitLayer(self, ctx:NNGraphParser.SplitLayerContext):
        return self.visitChildren(ctx)



del NNGraphParser