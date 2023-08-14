import pyvis.network, random
import file_utils

colors = [
  "#FF5733",
  "#33FF57",
  "#5733FF",
  "#FF33A6",
  "#33FFB5",
  "#B533FF",
  "#FFC133",
  "#33C1FF",
  "#E833FF",
  "#FF33B8",
  "#33FF85",
  "#8533FF",
  "#FF3374",
  "#33FFD0",
  "#4CFF33",
  "#FFD933",
  "#3357FF",
  "#FF337E",
  "#33FFEB",
  "#8B33FF",
  "#FF3344",
  "#33FF4E",
  "#5733FF",
  "#FF7E33",
  "#33FF62",
  "#A633FF",
  "#FF335B",
  "#33FFC7",
  "#5733FF",
  "#FFA533",
  "#33E2FF",
  "#DB33FF"
]

def render_graph(data):
    net = pyvis.network.Network()
    net.show_buttons(filter_=['physics']) 

    key_count = 0
    value_count = 0 # gets reset every new key

    for key in data.keys():
        if len(data[key]) > 0:
            color = random.choice(colors)
            net.add_node(key_count, label=key, color=color)
    
            for item in data[key]:
                net.add_node(value_count, label=item, color=color)
                net.add_edge(key_count, value_count)
                value_count += 1

        key_count += 1

    net.show('nodes.html', notebook=False)