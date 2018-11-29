import igraph
import copy
from igraph import *

def make_trees(vertices):
    trees = [Graph.Tree(vertices, 1),
            Graph.Tree(vertices, 3),
            Graph.Tree(vertices, 2)]
    trees.extend(copy.deepcopy(trees))
    trees.extend(copy.deepcopy(trees))
    pos = [j for j in range(4) for i in range(3)]; # [0,0,0,1,1,1,2,2,2,3,3,3]
    for index in range(4*3):
        trees[index].vs["root"] = [i.index == pos[index] for i in trees[index].vs]
    return trees

def join_graphs(*graphs):
    ret = Graph()
    offset = 0
    for g in graphs:
        ret.add_vertices(g.vcount())
        ret.add_edges([(e[0]+offset,e[1]+offset) for e in g.get_edgelist()])
        offset += g.vcount()
    return ret


if __name__ == "__main__":
    trees = make_trees(4)

    forest = join_graphs(*trees)

    visual_style = {}
    visual_style["vertex_label"] = [(i.index % 4)+1 for i in forest.vs]
    visual_style["layout"] = forest.layout_reingold_tilford(root=[1, 4, 8], mode="all")
    #visual_style["vertex_color"] = ["blue" if is_root else "red" for is_root in forest.vs["root"]]
    plot(forest, "forest.png", **visual_style)
    
    pos = 0
    for t in trees:
        pos += 1
        visual_style = {}
        visual_style["vertex_label"] = [i.index+1 for i in t.vs]
        #print(t.vs["root"])
        #print(i.index for i in t.vs("root"))
        visual_style["layout"] = t.layout_reingold_tilford(root=[i.index for i in t.vs("root")], mode="all")
        visual_style["vertex_color"] = ["blue" if is_root else "red" for is_root in t.vs["root"]]
        plot(t, "tree" + str(pos) + ".png", **visual_style)
