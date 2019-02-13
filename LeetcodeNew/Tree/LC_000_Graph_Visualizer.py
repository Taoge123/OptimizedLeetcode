import pygraphviz

def build_graph(root):
    # https://pygraphviz.github.io/documentation/latest/tutorial.html
    G = pygraphviz.AGraph(strict=True, directed=True)

    # http://www.graphviz.org/content/attrs#dordering
    G.graph_attr["rankdir"] = "TB"
    #G.graph_attr["splines"] = "ortho"
    G.graph_attr["splines"] = "curved"
    #G.graph_attr["size"] = "10,3"
    G.graph_attr["ordering"] = "out"
    G.layout(prog='dot')

    # http://stackoverflow.com/questions/279561/what-is-the-python-equivalent-of-static-variables-inside-a-function
    def _id(node, _static={"seq":0}):
        if node: return id(node)
        _static["seq"] += 1
        return "_%d" % _static["seq"]

    def graphviz_customize(node):
        return {
            "label": node.val if node else "#",
            "shape": "box" if node else "oval",
            "color": "blue", # if node else "black",
            "fontsize": 8,
            "width": 0.05 if node else 0.02, # in inches
            "height": 0.02 if node else 0.02,
        }

    # mimic the serialiation
    if not root:
        id_root = _id(root)
        G.add_node(id_root, **graphviz_customize(root))
        return G

    wq = deque([(root, _id(root), "", 0)])
    count = 1
    while count and wq:
        node, id_node, id_parent, right_child = wq.popleft()

        G.add_node(id_node, **graphviz_customize(node))
        if id_parent:
            if right_child:
                G.add_edge(id_parent, id_node, color='black', style='dashed')
            else:
                G.add_edge(id_parent, id_node, color='red', style='dashed')

        if not node: continue

        count -= 1
        for idx, nd in enumerate((node.left, node.right)):
            if nd:
                count += 1
            wq.append((nd, _id(nd), id_node, idx))

    return G

from io import BytesIO
from IPython.display import Image, display

def display_graph(G):
    # https://github.com/chebee7i/nxpd/blob/master/nxpd/ipythonsupport.py
    imgbuf = BytesIO()
    G.draw(imgbuf, format='png', prog='dot')
    img = Image(imgbuf.getvalue())
    display(img)

## main ##
root = deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]')
G = build_graph(root)
display_graph(G)

