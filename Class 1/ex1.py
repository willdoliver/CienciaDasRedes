import networkx as nx
import matplotlib.pyplot as plt

def main():
    G=nx.Graph()

    G.add_node("Albuquerque")
    G.add_node("Atlanta")
    G.add_node("Chicago")
    G.add_node("New York")
    G.add_node("Pinhais")
    G.add_node("Curitiba")
    G.add_node("Miami")
    G.add_node("Sao Paulo")
    G.add_node("Londrina")
    G.add_node("Foz")
    G.add_node("Maringa")
    G.add_node("Cleveland")
    G.add_node("Denver")
    G.add_node("Philadelphia")
    G.add_node("Minneapolis")
    G.add_node("Phoenix")
    G.add_node("Ponta Grossa")
    G.add_node("Boston")
    G.add_node("Tulsa")

    G.add_edge("Albuquerque","Atlanta")
    G.add_edge("Chicago","New York")
    G.add_edge("Chicago","Pinhais")
    G.add_edge("Curitiba","Atlanta")
    G.add_edge("Curitiba","Chicago")
    G.add_edge("Curitiba","Miami")
    G.add_edge("Curitiba","New York")
    G.add_edge("Curitiba","Sao Paulo")
    G.add_edge("Londrina","Foz")
    G.add_edge("Maringa","Albuquerque")
    G.add_edge("Maringa","Cleveland")
    G.add_edge("Miami","Denver")
    G.add_edge("Miami","New York")
    G.add_edge("Miami","Philadelphia")
    G.add_edge("Minneapolis","Foz")
    G.add_edge("New York","Cleveland")
    G.add_edge("New York","Minneapolis")
    G.add_edge("Philadelphia","Atlanta")
    G.add_edge("Phoenix","Cleveland")
    G.add_edge("Phoenix","Maringa")
    G.add_edge("Pinhais","Londrina")
    G.add_edge("Ponta Grossa","Cleveland")
    G.add_edge("Ponta Grossa","Foz")
    G.add_edge("Ponta Grossa","Londrina")
    G.add_edge("Sao Paulo","Boston")
    G.add_edge("Sao Paulo","Chicago")
    G.add_edge("Sao Paulo","Foz")
    G.add_edge("Sao Paulo","Londrina")
    G.add_edge("Sao Paulo","Minneapolis")
    G.add_edge("Sao Paulo","Ponta Grossa")
    G.add_edge("Tulsa","Maringa")
    G.add_edge("Tulsa","New York")

    # print(G.nodes())
    # print(G.edges())

    nx.draw(G,with_labels=True)
    plt.savefig("dreamAirlines.png")
    plt.show()


    originCities = G.nodes()
    destinationCities = G.nodes()
    origin = ''
    destination = ''

    size = 0
    for originCity in originCities:
        for destinationCity in destinationCities:
            for path in nx.all_simple_paths(G, originCity, destinationCity):
                if size < len(path):
                    size = len(path)
                    biggerPath = path
                    origin = originCity
                    destination = destinationCity

    print("Largest Path between two cities: ")
    print("\tOrigin: "+origin)
    print("\tDestination: "+destination)
    print("\tSize: "+ str(size))
    print("\tBigger Path: "+ str(biggerPath))


    # 2-b Coeficiente de clusterizacao de Curitiba? e Geral?
    print("Curitiba clustering coeficient: "+ str(nx.average_clustering(G,nodes=["Curitiba"])))
    print("General clustering coeficient: "+ str(round(nx.average_clustering(G),5)))
    
    nx.set_node_attributes(G, {"Albuquerque": {"Country": "United States"}})
    nx.set_node_attributes(G, {"Atlanta": {"Country": "United States"}})
    nx.set_node_attributes(G, {"Chicago": {"Country": "United States"}})
    nx.set_node_attributes(G, {"New York": {"Country": "United States"}})
    nx.set_node_attributes(G, {"Miami": {"Country": "United States"}})
    nx.set_node_attributes(G, {"Cleveland": {"Country": "United States"}})
    nx.set_node_attributes(G, {"Denver": {"Country": "United States"}})
    nx.set_node_attributes(G, {"Philadelphia": {"Country": "United States"}})
    nx.set_node_attributes(G, {"Minneapolis": {"Country": "United States"}})
    nx.set_node_attributes(G, {"Phoenix": {"Country": "United States"}})
    nx.set_node_attributes(G, {"Boston": {"Country": "United States"}})
    nx.set_node_attributes(G, {"Tulsa": {"Country": "United States"}})
    nx.set_node_attributes(G, {"Pinhais": {"Country": "Brazil"}})
    nx.set_node_attributes(G, {"Curitiba": {"Country": "Brazil"}})
    nx.set_node_attributes(G, {"Sao Paulo": {"Country": "Brazil"}})
    nx.set_node_attributes(G, {"Londrina": {"Country": "Brazil"}})
    nx.set_node_attributes(G, {"Foz": {"Country": "Brazil"}})
    nx.set_node_attributes(G, {"Maringa": {"Country": "Brazil"}})
    nx.set_node_attributes(G, {"Ponta Grossa": {"Country": "Brazil"}})

    edgeAttrs = {
        ("Albuquerque", "Atlanta"): {"Cost": 1},
        ("Chicago","New York"): {"Cost": 1},
        ("Chicago","Pinhais"): {"Cost": 5},
        ("Curitiba","Atlanta"): {"Cost": 5},
        ("Curitiba","Chicago"): {"Cost": 5},
        ("Curitiba","Miami"): {"Cost": 5},
        ("Curitiba","New York"): {"Cost": 5},
        ("Curitiba","Sao Paulo"): {"Cost": 1},
        ("Londrina","Foz"): {"Cost": 1},
        ("Maringa","Albuquerque"): {"Cost": 5},
        ("Maringa","Cleveland"): {"Cost": 5},
        ("Miami","Denver"): {"Cost": 1},
        ("Miami","New York"): {"Cost": 1},
        ("Miami","Philadelphia"): {"Cost": 1},
        ("Minneapolis","Foz"): {"Cost": 5},
        ("New York","Cleveland"): {"Cost": 1},
        ("New York","Minneapolis"): {"Cost": 1},
        ("Philadelphia","Atlanta"): {"Cost": 1},
        ("Phoenix","Cleveland"): {"Cost": 1},
        ("Phoenix","Maringa"): {"Cost": 5},
        ("Pinhais","Londrina"): {"Cost": 1},
        ("Ponta Grossa","Cleveland"): {"Cost": 5},
        ("Ponta Grossa","Foz"): {"Cost": 1},
        ("Ponta Grossa","Londrina"): {"Cost": 1},
        ("Sao Paulo","Boston"): {"Cost": 5},
        ("Sao Paulo","Chicago"): {"Cost": 5},
        ("Sao Paulo","Foz"): {"Cost": 1},
        ("Sao Paulo","Londrina"): {"Cost": 1},
        ("Sao Paulo","Minneapolis"): {"Cost": 5},
        ("Sao Paulo","Ponta Grossa"): {"Cost": 1},
        ("Tulsa","Maringa"): {"Cost": 5},
        ("Tulsa","New York"): {"Cost": 1}
    }
    nx.set_edge_attributes(G, edgeAttrs)

    # print(G.nodes(data=True))
    # print(G.edges(data=True))

    nx.draw(G,with_labels=True)

    plt.savefig("dreamAirlinesV2.png")
    plt.show()

    nx.write_gml(G, "dreamAirlinesV2.gml")


if __name__ == "__main__":
    main()