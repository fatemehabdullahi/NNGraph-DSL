class GraphvizExporter:

    def __init__(self, model):
        self.model = model

    def export(self, filename="graph.dot"):

        lines = []

        lines.append("digraph NNGraph {")
        lines.append("    rankdir=LR;")
        lines.append('    node [shape=box, style="rounded,filled", fillcolor=lightblue];')
        lines.append("")

        # Input
        lines.append(
            f'    "{self.model.input_name}" [shape=ellipse, fillcolor=lightgreen];'
        )

        # Nodes
        for node in self.model.nodes:
            label = f"{node.id}\\n{node.type}"
            lines.append(f'    "{node.id}" [label="{label}"];')

        lines.append(
            f'    "{self.model.output_name}" [shape=doublecircle, fillcolor=gold];'
        )

        lines.append("")

        # Edges
        for edge in self.model.edges:

            if edge.label:
                lines.append(
                    f'    "{edge.source}" -> "{edge.destination}" '
                    f'[label="{edge.label}"];'
                )
            else:
                lines.append(
                    f'    "{edge.source}" -> "{edge.destination}";'
                )

        lines.append("}")

        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))