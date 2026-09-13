# Generated from C:/Users/Lenovo/PycharmProjects/Final Project/NNGraph.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .NNGraphParser import NNGraphParser
else:
    from NNGraphParser import NNGraphParser

# This class defines a complete listener for a parse tree produced by NNGraphParser.
class NNGraphListener(ParseTreeListener):

    # Enter a parse tree produced by NNGraphParser#program.
    def enterProgram(self, ctx:NNGraphParser.ProgramContext):
        pass

    # Exit a parse tree produced by NNGraphParser#program.
    def exitProgram(self, ctx:NNGraphParser.ProgramContext):
        pass


    # Enter a parse tree produced by NNGraphParser#modelDecl.
    def enterModelDecl(self, ctx:NNGraphParser.ModelDeclContext):
        pass

    # Exit a parse tree produced by NNGraphParser#modelDecl.
    def exitModelDecl(self, ctx:NNGraphParser.ModelDeclContext):
        pass


    # Enter a parse tree produced by NNGraphParser#inputDecl.
    def enterInputDecl(self, ctx:NNGraphParser.InputDeclContext):
        pass

    # Exit a parse tree produced by NNGraphParser#inputDecl.
    def exitInputDecl(self, ctx:NNGraphParser.InputDeclContext):
        pass


    # Enter a parse tree produced by NNGraphParser#outputDecl.
    def enterOutputDecl(self, ctx:NNGraphParser.OutputDeclContext):
        pass

    # Exit a parse tree produced by NNGraphParser#outputDecl.
    def exitOutputDecl(self, ctx:NNGraphParser.OutputDeclContext):
        pass


    # Enter a parse tree produced by NNGraphParser#tensorType.
    def enterTensorType(self, ctx:NNGraphParser.TensorTypeContext):
        pass

    # Exit a parse tree produced by NNGraphParser#tensorType.
    def exitTensorType(self, ctx:NNGraphParser.TensorTypeContext):
        pass


    # Enter a parse tree produced by NNGraphParser#shape.
    def enterShape(self, ctx:NNGraphParser.ShapeContext):
        pass

    # Exit a parse tree produced by NNGraphParser#shape.
    def exitShape(self, ctx:NNGraphParser.ShapeContext):
        pass


    # Enter a parse tree produced by NNGraphParser#graphDecl.
    def enterGraphDecl(self, ctx:NNGraphParser.GraphDeclContext):
        pass

    # Exit a parse tree produced by NNGraphParser#graphDecl.
    def exitGraphDecl(self, ctx:NNGraphParser.GraphDeclContext):
        pass


    # Enter a parse tree produced by NNGraphParser#graphStatement.
    def enterGraphStatement(self, ctx:NNGraphParser.GraphStatementContext):
        pass

    # Exit a parse tree produced by NNGraphParser#graphStatement.
    def exitGraphStatement(self, ctx:NNGraphParser.GraphStatementContext):
        pass


    # Enter a parse tree produced by NNGraphParser#nodeDecl.
    def enterNodeDecl(self, ctx:NNGraphParser.NodeDeclContext):
        pass

    # Exit a parse tree produced by NNGraphParser#nodeDecl.
    def exitNodeDecl(self, ctx:NNGraphParser.NodeDeclContext):
        pass


    # Enter a parse tree produced by NNGraphParser#nodeType.
    def enterNodeType(self, ctx:NNGraphParser.NodeTypeContext):
        pass

    # Exit a parse tree produced by NNGraphParser#nodeType.
    def exitNodeType(self, ctx:NNGraphParser.NodeTypeContext):
        pass


    # Enter a parse tree produced by NNGraphParser#edgeDecl.
    def enterEdgeDecl(self, ctx:NNGraphParser.EdgeDeclContext):
        pass

    # Exit a parse tree produced by NNGraphParser#edgeDecl.
    def exitEdgeDecl(self, ctx:NNGraphParser.EdgeDeclContext):
        pass


    # Enter a parse tree produced by NNGraphParser#edgeLabel.
    def enterEdgeLabel(self, ctx:NNGraphParser.EdgeLabelContext):
        pass

    # Exit a parse tree produced by NNGraphParser#edgeLabel.
    def exitEdgeLabel(self, ctx:NNGraphParser.EdgeLabelContext):
        pass


    # Enter a parse tree produced by NNGraphParser#configDecl.
    def enterConfigDecl(self, ctx:NNGraphParser.ConfigDeclContext):
        pass

    # Exit a parse tree produced by NNGraphParser#configDecl.
    def exitConfigDecl(self, ctx:NNGraphParser.ConfigDeclContext):
        pass


    # Enter a parse tree produced by NNGraphParser#configItem.
    def enterConfigItem(self, ctx:NNGraphParser.ConfigItemContext):
        pass

    # Exit a parse tree produced by NNGraphParser#configItem.
    def exitConfigItem(self, ctx:NNGraphParser.ConfigItemContext):
        pass


    # Enter a parse tree produced by NNGraphParser#value.
    def enterValue(self, ctx:NNGraphParser.ValueContext):
        pass

    # Exit a parse tree produced by NNGraphParser#value.
    def exitValue(self, ctx:NNGraphParser.ValueContext):
        pass


    # Enter a parse tree produced by NNGraphParser#tuple.
    def enterTuple(self, ctx:NNGraphParser.TupleContext):
        pass

    # Exit a parse tree produced by NNGraphParser#tuple.
    def exitTuple(self, ctx:NNGraphParser.TupleContext):
        pass


    # Enter a parse tree produced by NNGraphParser#parameterList.
    def enterParameterList(self, ctx:NNGraphParser.ParameterListContext):
        pass

    # Exit a parse tree produced by NNGraphParser#parameterList.
    def exitParameterList(self, ctx:NNGraphParser.ParameterListContext):
        pass


    # Enter a parse tree produced by NNGraphParser#parameter.
    def enterParameter(self, ctx:NNGraphParser.ParameterContext):
        pass

    # Exit a parse tree produced by NNGraphParser#parameter.
    def exitParameter(self, ctx:NNGraphParser.ParameterContext):
        pass


    # Enter a parse tree produced by NNGraphParser#parameterName.
    def enterParameterName(self, ctx:NNGraphParser.ParameterNameContext):
        pass

    # Exit a parse tree produced by NNGraphParser#parameterName.
    def exitParameterName(self, ctx:NNGraphParser.ParameterNameContext):
        pass


    # Enter a parse tree produced by NNGraphParser#layer.
    def enterLayer(self, ctx:NNGraphParser.LayerContext):
        pass

    # Exit a parse tree produced by NNGraphParser#layer.
    def exitLayer(self, ctx:NNGraphParser.LayerContext):
        pass


    # Enter a parse tree produced by NNGraphParser#activation.
    def enterActivation(self, ctx:NNGraphParser.ActivationContext):
        pass

    # Exit a parse tree produced by NNGraphParser#activation.
    def exitActivation(self, ctx:NNGraphParser.ActivationContext):
        pass


    # Enter a parse tree produced by NNGraphParser#operation.
    def enterOperation(self, ctx:NNGraphParser.OperationContext):
        pass

    # Exit a parse tree produced by NNGraphParser#operation.
    def exitOperation(self, ctx:NNGraphParser.OperationContext):
        pass


    # Enter a parse tree produced by NNGraphParser#linearLayer.
    def enterLinearLayer(self, ctx:NNGraphParser.LinearLayerContext):
        pass

    # Exit a parse tree produced by NNGraphParser#linearLayer.
    def exitLinearLayer(self, ctx:NNGraphParser.LinearLayerContext):
        pass


    # Enter a parse tree produced by NNGraphParser#conv2dLayer.
    def enterConv2dLayer(self, ctx:NNGraphParser.Conv2dLayerContext):
        pass

    # Exit a parse tree produced by NNGraphParser#conv2dLayer.
    def exitConv2dLayer(self, ctx:NNGraphParser.Conv2dLayerContext):
        pass


    # Enter a parse tree produced by NNGraphParser#conv1dLayer.
    def enterConv1dLayer(self, ctx:NNGraphParser.Conv1dLayerContext):
        pass

    # Exit a parse tree produced by NNGraphParser#conv1dLayer.
    def exitConv1dLayer(self, ctx:NNGraphParser.Conv1dLayerContext):
        pass


    # Enter a parse tree produced by NNGraphParser#batchNormLayer.
    def enterBatchNormLayer(self, ctx:NNGraphParser.BatchNormLayerContext):
        pass

    # Exit a parse tree produced by NNGraphParser#batchNormLayer.
    def exitBatchNormLayer(self, ctx:NNGraphParser.BatchNormLayerContext):
        pass


    # Enter a parse tree produced by NNGraphParser#layerNormLayer.
    def enterLayerNormLayer(self, ctx:NNGraphParser.LayerNormLayerContext):
        pass

    # Exit a parse tree produced by NNGraphParser#layerNormLayer.
    def exitLayerNormLayer(self, ctx:NNGraphParser.LayerNormLayerContext):
        pass


    # Enter a parse tree produced by NNGraphParser#maxPoolLayer.
    def enterMaxPoolLayer(self, ctx:NNGraphParser.MaxPoolLayerContext):
        pass

    # Exit a parse tree produced by NNGraphParser#maxPoolLayer.
    def exitMaxPoolLayer(self, ctx:NNGraphParser.MaxPoolLayerContext):
        pass


    # Enter a parse tree produced by NNGraphParser#avgPoolLayer.
    def enterAvgPoolLayer(self, ctx:NNGraphParser.AvgPoolLayerContext):
        pass

    # Exit a parse tree produced by NNGraphParser#avgPoolLayer.
    def exitAvgPoolLayer(self, ctx:NNGraphParser.AvgPoolLayerContext):
        pass


    # Enter a parse tree produced by NNGraphParser#dropoutLayer.
    def enterDropoutLayer(self, ctx:NNGraphParser.DropoutLayerContext):
        pass

    # Exit a parse tree produced by NNGraphParser#dropoutLayer.
    def exitDropoutLayer(self, ctx:NNGraphParser.DropoutLayerContext):
        pass


    # Enter a parse tree produced by NNGraphParser#flattenLayer.
    def enterFlattenLayer(self, ctx:NNGraphParser.FlattenLayerContext):
        pass

    # Exit a parse tree produced by NNGraphParser#flattenLayer.
    def exitFlattenLayer(self, ctx:NNGraphParser.FlattenLayerContext):
        pass


    # Enter a parse tree produced by NNGraphParser#embeddingLayer.
    def enterEmbeddingLayer(self, ctx:NNGraphParser.EmbeddingLayerContext):
        pass

    # Exit a parse tree produced by NNGraphParser#embeddingLayer.
    def exitEmbeddingLayer(self, ctx:NNGraphParser.EmbeddingLayerContext):
        pass


    # Enter a parse tree produced by NNGraphParser#multiHeadLayer.
    def enterMultiHeadLayer(self, ctx:NNGraphParser.MultiHeadLayerContext):
        pass

    # Exit a parse tree produced by NNGraphParser#multiHeadLayer.
    def exitMultiHeadLayer(self, ctx:NNGraphParser.MultiHeadLayerContext):
        pass


    # Enter a parse tree produced by NNGraphParser#lstmLayer.
    def enterLstmLayer(self, ctx:NNGraphParser.LstmLayerContext):
        pass

    # Exit a parse tree produced by NNGraphParser#lstmLayer.
    def exitLstmLayer(self, ctx:NNGraphParser.LstmLayerContext):
        pass


    # Enter a parse tree produced by NNGraphParser#gruLayer.
    def enterGruLayer(self, ctx:NNGraphParser.GruLayerContext):
        pass

    # Exit a parse tree produced by NNGraphParser#gruLayer.
    def exitGruLayer(self, ctx:NNGraphParser.GruLayerContext):
        pass


    # Enter a parse tree produced by NNGraphParser#reluLayer.
    def enterReluLayer(self, ctx:NNGraphParser.ReluLayerContext):
        pass

    # Exit a parse tree produced by NNGraphParser#reluLayer.
    def exitReluLayer(self, ctx:NNGraphParser.ReluLayerContext):
        pass


    # Enter a parse tree produced by NNGraphParser#sigmoidLayer.
    def enterSigmoidLayer(self, ctx:NNGraphParser.SigmoidLayerContext):
        pass

    # Exit a parse tree produced by NNGraphParser#sigmoidLayer.
    def exitSigmoidLayer(self, ctx:NNGraphParser.SigmoidLayerContext):
        pass


    # Enter a parse tree produced by NNGraphParser#tanhLayer.
    def enterTanhLayer(self, ctx:NNGraphParser.TanhLayerContext):
        pass

    # Exit a parse tree produced by NNGraphParser#tanhLayer.
    def exitTanhLayer(self, ctx:NNGraphParser.TanhLayerContext):
        pass


    # Enter a parse tree produced by NNGraphParser#geluLayer.
    def enterGeluLayer(self, ctx:NNGraphParser.GeluLayerContext):
        pass

    # Exit a parse tree produced by NNGraphParser#geluLayer.
    def exitGeluLayer(self, ctx:NNGraphParser.GeluLayerContext):
        pass


    # Enter a parse tree produced by NNGraphParser#softmaxLayer.
    def enterSoftmaxLayer(self, ctx:NNGraphParser.SoftmaxLayerContext):
        pass

    # Exit a parse tree produced by NNGraphParser#softmaxLayer.
    def exitSoftmaxLayer(self, ctx:NNGraphParser.SoftmaxLayerContext):
        pass


    # Enter a parse tree produced by NNGraphParser#leakyReluLayer.
    def enterLeakyReluLayer(self, ctx:NNGraphParser.LeakyReluLayerContext):
        pass

    # Exit a parse tree produced by NNGraphParser#leakyReluLayer.
    def exitLeakyReluLayer(self, ctx:NNGraphParser.LeakyReluLayerContext):
        pass


    # Enter a parse tree produced by NNGraphParser#eluLayer.
    def enterEluLayer(self, ctx:NNGraphParser.EluLayerContext):
        pass

    # Exit a parse tree produced by NNGraphParser#eluLayer.
    def exitEluLayer(self, ctx:NNGraphParser.EluLayerContext):
        pass


    # Enter a parse tree produced by NNGraphParser#addLayer.
    def enterAddLayer(self, ctx:NNGraphParser.AddLayerContext):
        pass

    # Exit a parse tree produced by NNGraphParser#addLayer.
    def exitAddLayer(self, ctx:NNGraphParser.AddLayerContext):
        pass


    # Enter a parse tree produced by NNGraphParser#concatLayer.
    def enterConcatLayer(self, ctx:NNGraphParser.ConcatLayerContext):
        pass

    # Exit a parse tree produced by NNGraphParser#concatLayer.
    def exitConcatLayer(self, ctx:NNGraphParser.ConcatLayerContext):
        pass


    # Enter a parse tree produced by NNGraphParser#residualLayer.
    def enterResidualLayer(self, ctx:NNGraphParser.ResidualLayerContext):
        pass

    # Exit a parse tree produced by NNGraphParser#residualLayer.
    def exitResidualLayer(self, ctx:NNGraphParser.ResidualLayerContext):
        pass


    # Enter a parse tree produced by NNGraphParser#splitLayer.
    def enterSplitLayer(self, ctx:NNGraphParser.SplitLayerContext):
        pass

    # Exit a parse tree produced by NNGraphParser#splitLayer.
    def exitSplitLayer(self, ctx:NNGraphParser.SplitLayerContext):
        pass



del NNGraphParser