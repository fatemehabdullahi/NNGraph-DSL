class Node:
    def __init__(self, node_id, node_type, params=None):
        self.id = node_id
        self.type = node_type
        self.params = params if params else {}

    def __repr__(self):
        return f"Node(id={self.id}, type={self.type}, params={self.params})"


class Edge:
    def __init__(self, source, destination, label=None):
        self.source = source
        self.destination = destination
        self.label = label

    def __repr__(self):
        return f"Edge({self.source} -> {self.destination}, label={self.label})"


class Config:
    def __init__(self):
        self.batch_size = None
        self.device = None

    def __repr__(self):
        return f"Config(batch_size={self.batch_size}, device={self.device})"


class Model:
    def __init__(self):
        self.name = ""
        self.input_name = ""
        self.input_shape = []
        self.output_name = ""

        self.nodes = []
        self.edges = []

        self.config = Config()

    def __repr__(self):
        return (
            f"Model(name={self.name}, "
            f"input={self.input_name}, "
            f"output={self.output_name}, "
            f"nodes={self.nodes}, "
            f"edges={self.edges}, "
            f"config={self.config})"
        )