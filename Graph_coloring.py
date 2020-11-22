import networkx as nx
import matplotlib.pyplot as plt

colors_hash = {'red':[],'blue':[],'green':[],'black':[],'orange':[],'yellow':[],'pink':[],'purple':[]}
#make a dictionnary representation from adj matrix
def create_dicc(matrix):
    dict={}
    
    for x in range(0, len(matrix)):
        list = []
        idx = 0
        for l in matrix[x]:
        
            if l ==1:
                list.append(idx)
            idx +=1
        dict[x] = list
        

    return dict

#if a node val is in the neighbors of another node key
def isNeighbour(dict, key,val ):
    for x in dict[key]:
        if x == val:
            return True
    else:
        return False

#do the coloring
def graph_coloring(adj_matrix, R):

    tab_nodes_input = [0]*(R)
    tab_nodes_sorted_input=[0]*(R)
    colored = [0]*R

    
    #get the degrees of each node
    n=0
    for l in adj_matrix:
    
        sum1= 0
        for s in l:
            sum1 += s
       
        tab_nodes_input[n] = sum1
        n+=1
    itn = 0



    #sort nodes by the degree Desc
    for l in range(0,len( tab_nodes_input)):
    #gt max
        max=tab_nodes_input[0]
        for i in range(0,len(tab_nodes_input)):
            if tab_nodes_input[i] >= max:
                max = tab_nodes_input[i]
           
                idx = i
        tab_nodes_input[idx] =0
    
        tab_nodes_sorted_input[l]=idx
    

        

    nodes = create_dicc(adj_matrix)
    G = nx.Graph()

    for i in range(0,len(adj_matrix)):
        G.add_node(i,node_color = 'white')
        for j in range(0, len(adj_matrix)):
            if adj_matrix[i][j] == 1:
                G.add_edge(i,j)

    numNodes = 0
    i = 0

    colors_draw={}
    while(numNodes < len(tab_nodes_sorted_input)-1 and i<len(tab_nodes_sorted_input)-1  ):
        for color in colors_hash:
            
            #pick a node in the array
            node = tab_nodes_sorted_input[i]
        
        # print(color)
            
            if (colored[node] == 0):
                #if its not colored add it to that color
                colors_hash[color].append(node)
                colors_draw[node] = color
                #set it as colored
                colored[node] = 1
                #print(node)
                #color his non adjacent neighbors
                j = 0
                numNodes += 1
                nodeNext = tab_nodes_sorted_input[j]
            # print(nodeNext)
                #iterate on nodes array
                while(j< len(tab_nodes_sorted_input)):
                    nodeNext = tab_nodes_sorted_input[j]
                    #print("next") 
                    #print(nodeNext)
                    nonAdjacentToColor = True
                    #if its not colored and not adjacent to the current node
                    if(colored[nodeNext] == 0 and isNeighbour(nodes,node,nodeNext) == False):
                        for l in colors_hash[color]:
                    #if its not adjacent to the current color
                            if isNeighbour(nodes,l,nodeNext) == True:
                                nonAdjacentToColor = False
                        if nonAdjacentToColor == True:
                        #set as colored and assign it currentcolor
                            #print("next colored")
                            #print(nodeNext)
                            colored[nodeNext] = 1
                            colors_hash[color].append(nodeNext)
                            colors_draw[nodeNext] = color
                            numNodes += 1
                        # print("numnodes")
                            #print(numNodes)
                            if(numNodes == len(tab_nodes_sorted_input)):
                                break
                    
                    j += 1 
            i += 1
            
            if(numNodes == len(tab_nodes_sorted_input)):
                break
    labels = {}
    for key in nodes:
        labels[key] = key
    pos= nx.spring_layout(G)
    for key in colors_hash:
        
        nx.draw_networkx_nodes(G,pos, nodelist=colors_hash[key],node_size=600, node_color=key,edgecolors='black')
        nx.draw_networkx_labels(G,pos,labels,font_size=14,font_color='white',font_weight=200,font_family='arial')
    nx.draw_networkx_edges(G,pos)
    plt.show()
    for key in colors_hash:
        if(len(colors_hash[key]) != 0):
            print (key,' -> ', colors_hash[key])

def main():
    

    #read matrix
    #get size
    R = int(input("Enter the number of nodes"))
    matrix = []
    #get matrix
    print("Enter the adjacency matrix by rows with one space between numbers: ")
    for i in range(R):
        a=list(map(int,input().split()))
        
        matrix.append(a)
    print(matrix)
    graph_coloring(matrix, R)


main()