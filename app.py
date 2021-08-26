# Calvin Kwong
from floyd import load_graph, DP_floyd, shortest_path

class Application:
    def __init__(self, nodes, edges):
        self.nodes_filename = nodes
        self.edges_filename = edges
        self.adjacency_matrix = load_graph(self.nodes_filename, self.edges_filename)
        self.D, self.P = DP_floyd(self.adjacency_matrix)

    def get_airport_id(self, airport_name):
        '''
        Returns the airport id of an airport. If the airport is not
        found within the adjacency matrix, returns 0. The term 'inf'
        will also return 0.
        '''
        try:
            return self.adjacency_matrix[0].index(airport_name)
        except ValueError:
            return 0

    def find_route(self):
        s = input("Starting aiport abbreviation: ")
        start = self.get_airport_id(s)
        if start == 0:
            print("Invalid airport.")
        else:
            d = input("Destination airport abbreviation: ")
            end = self.get_airport_id(d)
            if end == 0:
                print("Invalid airport.")
            else:
                shortest_path(self.D, self.P, start, end)
        self.main()

    def list_airports(self):
        airports = self.adjacency_matrix[0]
        for i in range(1, len(airports)):
            print('{0}. {1}'.format(i, airports[i]))
        print('---')
        self.main()

    def execute(self, choice):
        if choice.strip() == '1':
            self.find_route()
        elif choice.strip() == '2':
            self.list_airports()
        elif choice.strip() == '3' or choice.strip().lower() == 'quit':
            pass
        else:
            print("Invalid input.")
            self.main()

    def main(self):
        print("1. Find Route")
        print("2. List Airports")
        print("3. Quit")
        choice = input(">> ")
        self.execute(choice)
        

if __name__ == "__main__":
    app = Application('test_nodes.csv', 'test_edges.csv')
    app.main()
