grammar NNGraph;

program
    : modelDecl
      graphDecl
      configDecl?
      EOF
    ;

modelDecl
    : MODEL ID
      LBRACE
        inputDecl
        outputDecl
      RBRACE
    ;

inputDecl
    : INPUT ID COLON tensorType
    ;

outputDecl
    : OUTPUT ID
    ;

tensorType
    : TENSOR LPAREN shape RPAREN
    ;

shape
    : INT (COMMA INT)*
    ;

graphDecl
    : GRAPH
      LBRACE
        graphStatement*
      RBRACE
    ;

graphStatement
    : nodeDecl
    | edgeDecl
    ;

nodeDecl
    : NODE ID COLON nodeType
    ;

nodeType
    : layer
    | activation
    | operation
    ;

edgeDecl
    : EDGE ID ARROW ID edgeLabel?
    ;

edgeLabel
    : LBRACKET
      LABEL
      ASSIGN
      STRING
      RBRACKET
    ;

configDecl
    : CONFIG
      LBRACE
        configItem*
      RBRACE
    ;

configItem
    : BATCH_SIZE ASSIGN INT
    | DEVICE ASSIGN STRING
    ;

value
    : INT
    | FLOAT
    | STRING
    | TRUE
    | FALSE
    | NONE
    | tuple
    ;

tuple
    : LPAREN value (COMMA value)* RPAREN
    ;

parameterList
    : parameter (COMMA parameter)*
    ;

parameter
    : parameterName ASSIGN value
    ;
parameterName
    : IN_FEATURES
    | OUT_FEATURES
    | IN_CH
    | OUT_CH
    | KERNEL
    | STRIDE
    | PADDING
    | BIAS
    | NUM_FEATURES
    | NORMALIZED_SHAPE
    | START_DIM
    | END_DIM
    | NUM_EMBEDDINGS
    | EMBEDDING_DIM
    | EMBED_DIM
    | NUM_HEADS
    | INPUT_SIZE
    | HIDDEN_SIZE
    | NUM_LAYERS
    | P
    | DIM
    | CHUNKS
    | NEGATIVE_SLOPE
    | ALPHA
    ;

layer
    : linearLayer
    | conv2dLayer
    | conv1dLayer
    | batchNormLayer
    | layerNormLayer
    | maxPoolLayer
    | avgPoolLayer
    | dropoutLayer
    | flattenLayer
    | embeddingLayer
    | multiHeadLayer
    | lstmLayer
    | gruLayer
    ;
activation
    : reluLayer
    | sigmoidLayer
    | tanhLayer
    | geluLayer
    | softmaxLayer
    | leakyReluLayer
    | eluLayer
    ;
operation
    : addLayer
    | concatLayer
    | residualLayer
    | splitLayer
    ;

linearLayer
    : LINEAR
      LPAREN
      parameterList?
      RPAREN
    ;

conv2dLayer
    : CONV2D
      LPAREN
      parameterList?
      RPAREN
    ;

conv1dLayer
    : CONV1D
      LPAREN
      parameterList?
      RPAREN
    ;

batchNormLayer
    : BATCHNORM2D
      LPAREN
      parameterList?
      RPAREN
    ;

layerNormLayer
    : LAYERNORM
      LPAREN
      parameterList?
      RPAREN
    ;

maxPoolLayer
    : MAXPOOL2D
      LPAREN
      parameterList?
      RPAREN
    ;

avgPoolLayer
    : AVGPOOL2D
      LPAREN
      parameterList?
      RPAREN
    ;

dropoutLayer
    : DROPOUT
      LPAREN
      parameterList?
      RPAREN
    ;

flattenLayer
    : FLATTEN
      LPAREN
      parameterList?
      RPAREN
    ;

embeddingLayer
    : EMBEDDING
      LPAREN
      parameterList?
      RPAREN
    ;

multiHeadLayer
    : MULTIHEADATTN
      LPAREN
      parameterList?
      RPAREN
    ;

lstmLayer
    : LSTM
      LPAREN
      parameterList?
      RPAREN
    ;

gruLayer
    : GRU
      LPAREN
      parameterList?
      RPAREN
    ;

reluLayer
    : RELU
      LPAREN
      RPAREN
    ;

sigmoidLayer
    : SIGMOID
      LPAREN
      RPAREN
    ;

tanhLayer
    : TANH
      LPAREN
      RPAREN
    ;

geluLayer
    : GELU
      LPAREN
      RPAREN
    ;

softmaxLayer
    : SOFTMAX
      LPAREN
      parameterList?
      RPAREN
    ;

leakyReluLayer
    : LEAKYRELU
      LPAREN
      parameterList?
      RPAREN
    ;

eluLayer
    : ELU
      LPAREN
      parameterList?
      RPAREN
    ;

addLayer
    : ADD
      LPAREN
      RPAREN
    ;

concatLayer
    : CONCAT
      LPAREN
      parameterList?
      RPAREN
    ;

residualLayer
    : RESIDUAL
      LPAREN
      RPAREN
    ;

splitLayer
    : SPLIT
      LPAREN
      parameterList?
      RPAREN
    ;

MODEL           : 'model';
INPUT           : 'input';
OUTPUT          : 'output';
GRAPH           : 'graph';
NODE            : 'node';
EDGE            : 'edge';
CONFIG          : 'config';
TENSOR          : 'tensor';
LABEL           : 'label';

LINEAR          : 'Linear';
CONV2D          : 'Conv2d';
CONV1D          : 'Conv1d';

BATCHNORM2D     : 'BatchNorm2d';
LAYERNORM       : 'LayerNorm';

MAXPOOL2D       : 'MaxPool2d';
AVGPOOL2D       : 'AvgPool2d';

DROPOUT         : 'Dropout';
FLATTEN         : 'Flatten';

EMBEDDING       : 'Embedding';

MULTIHEADATTN   : 'MultiHeadAttn';

LSTM            : 'LSTM';
GRU             : 'GRU';

RELU            : 'ReLU';
SIGMOID         : 'Sigmoid';
TANH            : 'Tanh';

GELU            : 'GELU';

SOFTMAX         : 'Softmax';

LEAKYRELU       : 'LeakyReLU';

ELU             : 'ELU';

ADD             : 'Add';

CONCAT          : 'Concat';

RESIDUAL        : 'Residual';

SPLIT           : 'Split';

TRUE            : 'true';

FALSE           : 'false';

NONE            : 'None';

ARROW           : '->';

ASSIGN          : '=';

COLON           : ':';

COMMA           : ',';

LPAREN          : '(';

RPAREN          : ')';

LBRACE          : '{';

RBRACE          : '}';

LBRACKET        : '[';

RBRACKET        : ']';

IN_FEATURES      : 'in_features';
OUT_FEATURES     : 'out_features';

IN_CH            : 'in_ch';
OUT_CH           : 'out_ch';

KERNEL           : 'kernel';
STRIDE           : 'stride';
PADDING          : 'padding';

BIAS             : 'bias';

NUM_FEATURES     : 'num_features';

NORMALIZED_SHAPE : 'normalized_shape';

START_DIM        : 'start_dim';
END_DIM          : 'end_dim';

NUM_EMBEDDINGS   : 'num_embeddings';
EMBEDDING_DIM    : 'embedding_dim';

EMBED_DIM        : 'embed_dim';
NUM_HEADS        : 'num_heads';

INPUT_SIZE       : 'input_size';
HIDDEN_SIZE      : 'hidden_size';
NUM_LAYERS       : 'num_layers';

P                : 'p';

DIM              : 'dim';

CHUNKS           : 'chunks';

NEGATIVE_SLOPE   : 'negative_slope';

ALPHA            : 'alpha';

BATCH_SIZE       : 'batch_size';

DEVICE           : 'device';

FLOAT
    : DIGIT+ '.' DIGIT+
    ;

INT
    : DIGIT+
    ;

fragment DIGIT
    : [0-9]
    ;

STRING
    : '"' (ESC | ~["\\])* '"'
    ;

fragment ESC
    : '\\' .
    ;

ID
    : LETTER (LETTER | DIGIT | '_')*
    ;

fragment LETTER
    : [a-zA-Z_]
    ;

LINE_COMMENT
    : '//' ~[\r\n]* -> skip
    ;

BLOCK_COMMENT
    : '/*' .*? '*/' -> skip
    ;

WS
    : [ \t\r\n]+ -> skip
    ;