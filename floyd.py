# Final Exam CUS1188 Calvin Kwong
import math
import copy

def load_graph(node_filename, edge_filename):
    '''
    Loads the two datafiles and returns an adjacency matrix which
    represents a weighed, directed graph that encodes the routes between
    the various airports and the travel distance between each route.
    '''
    with open(node_filename, encoding="utf8") as f:
        nodes = 0
        for line in f:
            nodes += 1
    adjacency_matrix = [[math.inf]*nodes for i in range(nodes)]

    # renames first row and first column to airport abbreviations
    with open(node_filename, encoding="utf8") as fn:
        fn.readline()
        node = fn.readline()
        count = 1
        while node:
            node_info = node.split(',')
            adjacency_matrix[0][count] = node_info[1]
            adjacency_matrix[count][0] = node_info[1]
            adjacency_matrix[count][count] = 0
            node = fn.readline()
            count += 1
    # adds edges
    with open(edge_filename, encoding="utf8") as fe:
        fe.readline()
        edge = fe.readline()
        while edge:
            edge_info = edge.split(',')
            start, end, length = int(edge_info[0]), int(edge_info[1]), int(edge_info[2])
            adjacency_matrix[start][end] = length
            edge = fe.readline()
    return adjacency_matrix

def DP_floyd(D):
    '''
    Outputs the 2D list D_out as a solution to the shortest path
    problem given the adjacency matrix D. Also outputs the matrix P
    which stores the id of the node that has the highest index among
    all intermediate nodes that are in the shortest path.
    '''
    D_out = D
    n = len(D_out)
    P = copy.deepcopy(D)
    # makes the values in P equal to 0
    for x in range(1, n):
        for y in range(1, n):
            P[x][y] = 0
    # finds minimum path
    for k in range(1, n):
        for i in range(1, n):
            for j in range(1, n):
                if D_out[i][k] + D_out[k][j] < D_out[i][j]:
                    P[i][j] = k
                    D_out[i][j] = D_out[i][k] + D_out[k][j]
    return D_out, P

def shortest_path(D_out, P, s, d):
    '''
    Displays the actual shortest path of a starting node s to
    destination node d. Uses the inputs D_out and P.
    '''
    # Recursively obtains all the nodes travelled through
    nodes = [s, ]
    def path(P, s, d, nodes):
        if P[s][d] != 0:
            path(P, s, P[s][d], nodes)
            nodes.append(P[s][d])
            path(P, P[s][d], d, nodes)
    path(P, s, d, nodes)
    nodes.append(d)

    for n in range(len(nodes)-1):
        start = nodes[n]
        destination = nodes[n+1]
        print('{0} -> {1} ({2} miles),'.format(D_out[start][0], D_out[destination][0], D_out[start][destination]))
    print('(Total distance: {0} miles)'.format(D_out[s][d]))


    
