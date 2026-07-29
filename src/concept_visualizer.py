import networkx as nx
import matplotlib.pyplot as plt

def create_concept_graph(concept):
    G = nx.Graph()

    # Simple example relationships
    relations = {
        "Transformer": ["Encoder", "Decoder", "Self-Attention", "Positional Encoding"],
        "Machine Learning": ["Supervised Learning", "Unsupervised Learning", "Reinforcement Learning"],
        "Deep Learning": ["Neural Networks", "CNN", "RNN", "Transformer"]
    }

    G.add_node(concept)

    if concept in relations:
        for related in relations[concept]:
            G.add_edge(concept, related)

    fig, ax = plt.subplots(figsize=(6, 4))
    nx.draw(
        G,
        with_labels=True,
        node_size=3000,
        font_size=10,
        ax=ax
    )

    return fig