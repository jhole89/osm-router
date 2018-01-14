from main.parser import AppParser
from main.graph import Graph


def run():
    """
    Main function for running application

    :return: None
    """
    parser = AppParser().register_args()
    args = parser.parse_args()

    with open(args.file_path, mode='r') as f:
        route_graph = Graph()

        for line in f.read().splitlines():
            record = line.split()

            if len(record) == 3:
                route_graph.add_node(record[0])
                route_graph.add_node(record[1])
                route_graph.add_edge(record, directional=False)

    print(route_graph.get_shortest_path(args.start_node, args.end_node))


if __name__ == '__main__':
    run()
