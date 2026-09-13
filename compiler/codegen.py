from collections import defaultdict, deque


class CodeGenerator:

    def __init__(self, model):
        self.model = model
        self.lines = []

    def generate(self):

        self.lines = []

        self._generate_header()
        self._generate_layers()
        self._generate_forward()

        return "\n".join(self.lines)

    def _generate_header(self):

        self.lines.append("import torch")
        self.lines.append("import torch.nn as nn")
        self.lines.append("")
        self.lines.append(f"class {self.model.name}(nn.Module):")
        self.lines.append("")
        self.lines.append("    def __init__(self):")
        self.lines.append("        super().__init__()")

    def _build_graph(self):

        children = defaultdict(list)
        parents = defaultdict(list)

        for edge in self.model.edges:
            children[edge.source].append(edge.destination)
            parents[edge.destination].append(edge.source)

        return children, parents

    def _topological_sort(self):

        children, parents = self._build_graph()

        indegree = defaultdict(int)

        all_nodes = {node.id for node in self.model.nodes}
        all_nodes.add(self.model.input_name)

        for node in all_nodes:
            indegree[node] = len(parents[node])

        queue = deque()

        for node in all_nodes:
            if indegree[node] == 0:
                queue.append(node)

        order = []

        while queue:

            current = queue.popleft()

            order.append(current)

            for child in children[current]:

                indegree[child] -= 1

                if indegree[child] == 0:
                    queue.append(child)

        return order, children, parents

    def _generate_layers(self):

        for node in self.model.nodes:

            layer = self._node_to_layer(node)

            if layer:
                self.lines.append(
                    f"        self.{node.id} = {layer}"
                )

    def _node_to_layer(self, node):

        p = node.params

        if node.type == "Linear":

            return (
                f"nn.Linear("
                f"{p['in_features']}, "
                f"{p['out_features']})"
            )

        elif node.type == "Dropout":

            rate = p.get("p", 0.5)

            return f"nn.Dropout({rate})"

        elif node.type == "ReLU":

            return "nn.ReLU()"

        elif node.type == "Softmax":

            dim = p.get("dim", 1)

            return f"nn.Softmax(dim={dim})"

        elif node.type == "Sigmoid":

            return "nn.Sigmoid()"

        elif node.type == "Tanh":

            return "nn.Tanh()"

        elif node.type == "GELU":

            return "nn.GELU()"


        elif node.type == "LeakyReLU":

            slope = p.get("negative_slope", 0.01)

            return f"nn.LeakyReLU(negative_slope={slope})"


        elif node.type == "ELU":

            alpha = p.get("alpha", 1.0)

            return f"nn.ELU(alpha={alpha})"

        elif node.type == "Flatten":

            start = p.get("start_dim", 1)
            end = p.get("end_dim", -1)

            return f"nn.Flatten(start_dim={start}, end_dim={end})"

        elif node.type == "Conv2d":

            stride = p.get("stride", 1)
            padding = p.get("padding", 0)

            return (
                f"nn.Conv2d("
                f"{p['in_ch']}, "
                f"{p['out_ch']}, "
                f"{p['kernel']}, "
                f"stride={stride}, "
                f"padding={padding})"
            )

        elif node.type == "Conv1d":

            stride = p.get("stride", 1)
            padding = p.get("padding", 0)

            return (
                f"nn.Conv1d("
                f"{p['in_ch']}, "
                f"{p['out_ch']}, "
                f"{p['kernel']}, "
                f"stride={stride}, "
                f"padding={padding})"
            )

        elif node.type == "BatchNorm2d":

            return (
                f"nn.BatchNorm2d("
                f"{p['num_features']})"
            )

        elif node.type == "LayerNorm":

            return (
                f"nn.LayerNorm("
                f"{p['normalized_shape']})"
            )

        elif node.type == "MaxPool2d":

            kernel = p["kernel"]
            stride = p.get("stride", kernel)

            return (
                f"nn.MaxPool2d("
                f"{kernel}, "
                f"stride={stride})"
            )

        elif node.type == "AvgPool2d":

            kernel = p["kernel"]
            stride = p.get("stride", kernel)

            return (
                f"nn.AvgPool2d("
                f"{kernel}, "
                f"stride={stride})"
            )

        elif node.type == "Embedding":

            return (
                f"nn.Embedding("
                f"{p['num_embeddings']}, "
                f"{p['embedding_dim']})"
            )

        elif node.type == "LSTM":

            layers = p.get("num_layers", 1)

            return (
                f"nn.LSTM("
                f"{p['input_size']}, "
                f"{p['hidden_size']}, "
                f"num_layers={layers})"
            )

        elif node.type == "GRU":

            layers = p.get("num_layers", 1)

            return (
                f"nn.GRU("
                f"{p['input_size']}, "
                f"{p['hidden_size']}, "
                f"num_layers={layers})"
            )

        elif node.type == "MultiHeadAttn":

            embed_dim = p["embed_dim"]
            num_heads = p["num_heads"]

            dropout = p.get("dropout", 0.0)

            return (
                f"nn.MultiheadAttention("
                f"embed_dim={embed_dim}, "
                f"num_heads={num_heads}, "
                f"dropout={dropout}, "
                f"batch_first=True)"
            )

        elif node.type in ["Concat", "Add", "Residual", "Split"]:

            return None

        raise ValueError(
            f"Unsupported layer type: {node.type}"
        )

    def _generate_forward(self):

        self.lines.append("")
        self.lines.append("    def forward(self, x):")
        self.lines.append("")

        self.lines.append("        outputs = {}")
        self.lines.append(f'        outputs["{self.model.input_name}"] = x')
        self.lines.append("")

        order, children, parents = self._topological_sort()

        node_map = {
            node.id: node
            for node in self.model.nodes
        }

        for node_id in order:

            if node_id == self.model.input_name:
                continue

            if node_id not in node_map:
                continue

            node = node_map[node_id]

            parent_outputs = parents[node_id]

            if node.type in ["LSTM", "GRU"]:
                parent = parent_outputs[0]

                self.lines.append(
                    f'        outputs["{node_id}"], _ = '
                    f'self.{node_id}(outputs["{parent}"])'
                )

                continue

            if node.type == "MultiHeadAttn":
                parent = parent_outputs[0]

                self.lines.append(
                    f'        outputs["{node_id}"], _ = '
                    f'self.{node_id}(outputs["{parent}"], '
                    f'outputs["{parent}"], '
                    f'outputs["{parent}"])'
                )

                continue


            if node.type == "Concat":
                inputs = ", ".join(
                    [f'outputs["{p}"]' for p in parent_outputs]
                )

                dim = node.params.get("dim", 1)

                self.lines.append(
                    f'        outputs["{node_id}"] = torch.cat([{inputs}], dim={dim})'
                )

                continue
            if node.type == "Add":

                if len(parent_outputs) != 2:
                    raise ValueError(
                        f"Add node '{node_id}' must have exactly 2 inputs"
                    )

                self.lines.append(
                    f'        outputs["{node_id}"] = outputs["{parent_outputs[0]}"] + outputs["{parent_outputs[1]}"]'
                )

                continue
            if node.type == "Residual":

                if len(parent_outputs) != 2:
                    raise ValueError(
                        f"Residual node '{node_id}' must have exactly 2 inputs"
                    )

                self.lines.append(
                    f'        outputs["{node_id}"] = outputs["{parent_outputs[0]}"] + outputs["{parent_outputs[1]}"]'
                )

                continue

            if node.type == "Split":

                if len(parent_outputs) != 1:
                    raise ValueError(
                        f"Split node '{node_id}' must have exactly 1 input"
                    )

                chunks = node.params.get("chunks", 2)
                dim = node.params.get("dim", 1)

                split_children = [
                    edge.destination
                    for edge in self.model.edges
                    if edge.source == node_id
                ]

                if len(split_children) != chunks:
                    raise ValueError(
                        f"Split node '{node_id}' has {chunks} outputs but {len(split_children)} edges"
                    )

                self.lines.append(
                    f'        _tmp = torch.chunk(outputs["{parent_outputs[0]}"], chunks={chunks}, dim={dim})'
                )

                for i, child in enumerate(split_children):
                    self.lines.append(
                        f'        outputs["{child}"] = _tmp[{i}]'
                    )

                continue

            if len(parent_outputs) == 1:

                parent = parent_outputs[0]

                self.lines.append(
                    f'        outputs["{node_id}"] = self.{node_id}(outputs["{parent}"])'
                )



        self.lines.append("")
        self.lines.append(
            f'        return outputs["{self.model.output_name}"]'
        )

    def save(self, filename):

        code = self.generate()

        with open(filename, "w", encoding="utf-8") as f:
            f.write(code)
