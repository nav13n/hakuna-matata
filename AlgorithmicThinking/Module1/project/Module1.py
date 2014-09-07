"""
Code for project portion of Module 1

"""

EX_GRAPH0={0:set([1,2]),1:set([]),2:set([])}
EX_GRAPH1={0:set([1,4,5]),1:set([2,6]),2:set([3]),3:set([0]),4:set([1]),5:set([2]),6:set([])}
EX_GRAPH2={0:set([1,4,5]),1:set([2,6]),2:set([3,7]),3:set([7]),4:set([1]),5:set([2]),6:set([]),7:set([3]),8:set([1,2]),9:set([0,4,5,6,7,3])}


def make_complete_graph(num_nodes):
     """
     Function that creates a complete directed graph
     Returns a dictionary corresponding to a complete directed graph with the specified number of nodes"""
     answer_graph={}
     if(num_nodes>0):
         for node in range(num_nodes):
             answer_graph[node]=set(range(num_nodes))-set([node])
     return answer_graph


def compute_in_degrees(digraph):
    """ Returns a dictionary whose keys correspond to in-degrees of nodes in the graph."""
    in_degree_dict={}
    for node,node_neighbours in digraph.iteritems():
        if not node in in_degree_dict:
            in_degree_dict[node]=0

        for neighbour in node_neighbours:
            if neighbour in in_degree_dict:
                in_degree_dict[neighbour]=in_degree_dict[neighbour]+1
            else:
                in_degree_dict[neighbour]=1

    return in_degree_dict



def in_degree_distribution(digraph):
    """ Returns a dictionary whose keys correspond to in-degrees of nodes in the graph.  """
    in_degree_distribution_dict={}
    in_degree_dict=compute_in_degrees(digraph)
    for in_degree in in_degree_dict.values():
        if(in_degree in in_degree_distribution_dict.keys()):
            in_degree_distribution_dict[in_degree]=in_degree_distribution_dict[in_degree]+1
        else:
            in_degree_distribution_dict[in_degree]=1
    return in_degree_distribution_dict


def main():
    """
    Driver Function
    """
    print EX_GRAPH0
    print compute_in_degrees(EX_GRAPH0)
    print in_degree_distribution(EX_GRAPH0)
    print make_complete_graph(4)


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
