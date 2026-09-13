
class SemanticAnalyzer:

    def __init__(self, model):
            self.model = model
            self.errors = []

            self.layer_rules = {

                "Linear": {
                    "required": ["in_features", "out_features"],
                    "types": {
                        "in_features": int,
                        "out_features": int,
                        "bias": bool
                    }
                },

                "Conv1d": {
                    "required": ["in_ch", "out_ch", "kernel"],
                    "types": {
                        "in_ch": int,
                        "out_ch": int,
                        "kernel": int,
                        "stride": int,
                        "padding": int
                    }
                },

                "Conv2d": {
                    "required": ["in_ch", "out_ch", "kernel"],
                    "types": {
                        "in_ch": int,
                        "out_ch": int,
                        "kernel": int,
                        "stride": int,
                        "padding": int
                    }
                },

                "BatchNorm2d": {
                    "required": ["num_features"],
                    "types": {
                        "num_features": int
                    }
                },

                "LayerNorm": {
                    "required": ["normalized_shape"],
                    "types": {
                        "normalized_shape": int
                    }
                },

                "MaxPool2d": {
                    "required": ["kernel"],
                    "types": {
                        "kernel": int,
                        "stride": int,
                        "padding": int
                    }
                },

                "AvgPool2d": {
                    "required": ["kernel"],
                    "types": {
                        "kernel": int,
                        "stride": int,
                        "padding": int
                    }
                },

                "Dropout": {
                    "required": ["p"],
                    "types": {
                        "p": float
                    }
                },

                "Embedding": {
                    "required": ["num_embeddings", "embedding_dim"],
                    "types": {
                        "num_embeddings": int,
                        "embedding_dim": int
                    }
                },

                "MultiHeadAttn": {
                    "required": ["embed_dim", "num_heads"],
                    "types": {
                        "embed_dim": int,
                        "num_heads": int
                    }
                },

                "LSTM": {
                    "required": ["input_size", "hidden_size"],
                    "types": {
                        "input_size": int,
                        "hidden_size": int,
                        "num_layers": int,
                    }
                },

                "GRU": {
                    "required": ["input_size", "hidden_size"],
                    "types": {
                        "input_size": int,
                        "hidden_size": int,
                        "num_layers": int,
                    }
                },

                "Softmax": {
                    "required": ["dim"],
                    "types": {
                        "dim": int
                    }
                },

                "LeakyReLU": {
                    "required": ["negative_slope"],
                    "types": {
                        "negative_slope": float
                    }
                },

                "Concat": {
                    "required": ["dim"],
                    "types": {
                        "dim": int
                    }
                },

                "Split": {
                    "required": ["chunks", "dim"],
                    "types": {
                        "chunks": int,
                        "dim": int
                    }
                },

                "Residual": {
                    "required": [],
                    "types": {}
                }
            }

    def error(self, message):
        self.errors.append("Semantic Error: " + message)

    def analyze(self):

        self.checkDuplicateNodes()
        self.checkEdges()
        self.checkOutputNode()
        self.checkLayerParameters()
        self.checkOrphanNodes()
        self.checkInputReachability()
        self.checkOutputReachability()
        self.checkCycle()
        self.checkResidualArity()
        self.checkParameterTypes()
        self.checkParameterRanges()
        return self.errors

    def checkDuplicateNodes(self):
        names = set()

        for node in self.model.nodes:
            if node.id in names:
                self.error(f"Duplicate node '{node.id}'")
            else:
                names.add(node.id)

    def checkEdges(self):
        nodes = {node.id for node in self.model.nodes}

        nodes.add(self.model.input_name)
        nodes.add(self.model.output_name)

        for edge in self.model.edges:
            if edge.source not in nodes:
                self.error(f"Undefined source node '{edge.source}'")

            if edge.destination not in nodes:
                self.error(f"Undefined destination node '{edge.destination}'")

    def checkOutputNode(self):

        exists = False

        for node in self.model.nodes:

            if node.id == self.model.output_name:
                exists = True
                break

        if not exists:
            self.error(
                f"Output node '{self.model.output_name}' is not defined"
            )

    def checkLayerParameters(self):

        for node in self.model.nodes:

            if node.type not in self.layer_rules:
                continue

            rules = self.layer_rules[node.type]

            for param in rules["required"]:

                if param not in node.params:
                    self.error(
                        f"Node '{node.id}' ({node.type}) is missing required parameter '{param}'"
                    )

    def checkOrphanNodes(self):

        used = set()

        for edge in self.model.edges:
            used.add(edge.source)
            used.add(edge.destination)

        for node in self.model.nodes:
            if node.id not in used:
                self.error(
                    f"Orphan node '{node.id}' is not connected to the graph"
                )

    def checkInputReachability(self):

        graph = {}

        for edge in self.model.edges:
            graph.setdefault(edge.source, []).append(edge.destination)

        visited = set()

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for nxt in graph.get(node, []):
                dfs(nxt)

        dfs(self.model.input_name)

        for node in self.model.nodes:
            if node.id not in visited:
                self.error(
                    f"Node '{node.id}' is not reachable from input"
                )

    def dfs(self, node, graph, visited):

        if node in visited:
            return

        visited.add(node)

        for nxt in graph.get(node, []):
            self.dfs(nxt, graph, visited)

    def checkOutputReachability(self):

        graph = {}

        for edge in self.model.edges:

            if edge.source not in graph:
                graph[edge.source] = []

            graph[edge.source].append(edge.destination)

        visited = set()

        self.dfs(
            self.model.input_name,
            graph,
            visited
        )

        if self.model.output_name not in visited:
            self.error(
                f"Output node '{self.model.output_name}' is not reachable from input"
            )

    def hasCycle(self, node, graph, visited, stack):

        visited.add(node)
        stack.add(node)

        for nxt in graph.get(node, []):

            if nxt not in visited:

                if self.hasCycle(nxt, graph, visited, stack):
                    return True

            elif nxt in stack:
                return True

        stack.remove(node)

        return False

    def checkCycle(self):

        graph = {}

        for edge in self.model.edges:

            if edge.source not in graph:
                graph[edge.source] = []

            graph[edge.source].append(edge.destination)

        visited = set()
        stack = set()

        for node in graph:

            if node not in visited:

                if self.hasCycle(node, graph, visited, stack):
                    self.error("Cycle detected in graph")

                    return

    def checkResidualArity(self):

        for node in self.model.nodes:

            if node.type != "Residual":
                continue

            inputs = 0

            for edge in self.model.edges:

                if edge.destination == node.id:
                    inputs += 1

            if inputs != 2:
                self.error(
                    f"Residual node '{node.id}' must have exactly 2 input edges"
                )

    def checkParameterTypes(self):

        for node in self.model.nodes:

            if node.type not in self.layer_rules:
                continue

            rules = self.layer_rules[node.type]
            types = rules.get("types", {})

            for param_name, expected_type in types.items():

                if param_name not in node.params:
                    continue

                value = node.params[param_name]

                if expected_type == bool:

                    if not isinstance(value, bool):
                        self.error(
                            f"Node '{node.id}' ({node.type}) parameter '{param_name}' must be bool"
                        )

                elif expected_type == int:

                    if not isinstance(value, int):
                        self.error(
                            f"Node '{node.id}' ({node.type}) parameter '{param_name}' must be int"
                        )

                elif expected_type == float:

                    if not isinstance(value, float):
                        self.error(
                            f"Node '{node.id}' ({node.type}) parameter '{param_name}' must be float"
                        )

    def checkParameterRanges(self):

        for node in self.model.nodes:

            if node.type == "Dropout":

                p = node.params.get("p")

                if p is not None:

                    if not (0 <= p <= 1):
                        self.error(
                            f"Dropout '{node.id}' parameter 'p' must be between 0 and 1"
                        )

            if node.type == "Linear":

                for name in ["in_features", "out_features"]:

                    value = node.params.get(name)

                    if value is not None and value <= 0:
                        self.error(
                            f"Linear '{node.id}' parameter '{name}' must be greater than zero"
                        )

            if node.type in ["Conv1d", "Conv2d"]:

                for name in ["kernel", "stride"]:

                    value = node.params.get(name)

                    if value is not None and value <= 0:
                        self.error(
                            f"{node.type} '{node.id}' parameter '{name}' must be greater than zero"
                        )