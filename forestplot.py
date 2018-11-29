import igraph
from igraph import *

def make_FF31():
    trees = [Graph(n=3, edges=[(0,1),(0,2)], directed=False),
             Graph(n=3, edges=[(1,0),(1,2)], directed=False),
	     Graph(n=3, edges=[(2,0),(2,1)], directed=False)]
    return join_graphs(*[t.copy() for t in trees for i in range(3)])

def make_FF32():
    trees = [Graph(n=3, edges=[(0,2)], directed=False),
             Graph(n=3, edges=[(0,1)], directed=False),
	     Graph(n=3, edges=[(1,2)], directed=False)]
    return join_graphs(*[t.copy() for t in trees for i in range(2)])

def join_graphs(*graphs):
    ret = Graph()
    offset = 0
    for g in graphs:
        ret.add_vertices(g.vcount())
        ret.add_edges([(e[0]+offset,e[1]+offset) for e in g.get_edgelist()])
        offset += g.vcount()
    return ret


if __name__ == "__main__":
    # plot FF_3,1
    forest = make_FF31()
    print(forest)

    roots=[4*i-(i//3)*3 for i in range(9)]
    visual_style = {}
    visual_style["vertex_label"] = [(i.index % 3)+1 for i in forest.vs]
    visual_style["layout"] = forest.layout_reingold_tilford(root=[3*i+(i//3) for i in range(9)])
    visual_style["vertex_color"] = ["red" if i in roots else "gray" for i in range(27)]
    plot(forest, bbox=(600,150), **visual_style)

    # plot FF_3,2
    forest = make_FF32()
    print(forest)

    roots=[0,1,4,5,6,8,10,11,12,13,15,17]
    visual_style = {}
    visual_style["vertex_label"] = [(i.index % 3)+1 for i in forest.vs]
    visual_style["layout"] = forest.layout_reingold_tilford()
    visual_style["vertex_color"] = ["red" if i in roots else "gray" for i in range(18)]
    plot(forest, bbox=(600,150), **visual_style)
