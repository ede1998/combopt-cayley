import igraph
from igraph import *

def make_F210():
    return Graph(n=10, edges=[(7,1),(7,2),(2,6),(6,0),(6,8),(8,9),(3,4),(4,5)], directed=True)

def make_F310():
    return Graph(n=10, edges=[(7,1),(7,2),(6,0),(6,8),(8,9),(3,4),(4,5)], directed=True)

def join_graphs(*graphs):
    ret = Graph()
    offset = 0
    for g in graphs:
        ret.add_vertices(g.vcount())
        ret.add_edges([(e[0]+offset,e[1]+offset) for e in g.get_edgelist()])
        offset += g.vcount()
    return ret

def plot_graphs(graph, filename, **vs):
    bbox=(500,500)
    if len(filename) == 0:
        plot(forest, bbox=bbox, **visual_style)
    else:
        plot(forest, filename, bbox=bbox, **visual_style)


if __name__ == "__main__":
    # plot F_2,10
    forest = make_F210()
    print(forest)

    visual_style = {}
    visual_style["vertex_size"] = 45
    visual_style["margin"] = 80

    roots = [7,3]
    visual_style["vertex_label"] = [i.index+1 for i in forest.vs]
    visual_style["layout"] = forest.layout_reingold_tilford(root=roots)
    visual_style["vertex_color"] = ["red" if i in roots else "gray" for i in range(10)]
    plot_graphs(forest, "ff210.png", **visual_style)

    # plot F_3,10
    forest = make_F310()
    print(forest)

    roots = [7,3,6]
    visual_style["vertex_label"] = [i.index+1 for i in forest.vs]
    visual_style["layout"] = forest.layout_reingold_tilford(root=roots)
    visual_style["vertex_color"] = ["red" if i in roots else "gray" for i in range(10)]
    plot_graphs(forest, "ff310.png", **visual_style)

