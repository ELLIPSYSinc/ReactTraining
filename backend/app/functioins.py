from graphviz import Digraph
def temp(sentences,user_id):
    words = [i.lower() for i in '\n'.join(sentences).split()]
    chain = {i: [] for i in words}
    for i in [[words[i], words[i+1]] for i in range(len(words)-1)]:
        chain[i[0]].append(i[1])
    chain = {i: chain[i] for i in chain if i[-1] != "." and i[-1] != ","}
    edges = {(i, j): str(1/len(list(set(chain[i]))))[:4] if len(
        chain[i]) != 0 else "0" for i in chain for j in chain[i]}
    G = Digraph(format="png")
    G.attr("node", shape="circle")
    for i, j in edges:
        G.edge(str(i), str(j), label=edges[(i, j)])
    text = "".join([str(i) for i in G.source])
    edges_json = [i.replace("\n", '').replace('}', '')
                  for i in text.split('\t')][2:]
    G.render(f"markov{user_id}")
    return edges_json