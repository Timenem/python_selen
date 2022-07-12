"""
example graph 
"""

def check_connection(network, first, second):
    nods = [i.split(sep='-') for i in network]
    nodesList = [i.strip() for i in (list(str(nods).replace('[', '').replace(']', '').replace("'", '').split(sep=',')))]
    g = nx.Graph()
    g.add_nodes_from(set(nodesList))
    for i in nods:
        g.add_edge(i[0], i[1])
    nx.draw(g, node_color='red', with_labels=True, node_size=1300)
    plt.show()


check_connection(("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
                  "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
                 "scout3", "scout4")
