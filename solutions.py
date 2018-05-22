"""
Question 1
Given two strings s and t, determine whether some anagram of t is a substring
of s. For example: if s = "udacity" and t = "ad", then the function returns
True. Your function definition should look like: question1(s, t) and return a
boolean True or False.
"""

# Helper function to check if two strings are anagram of each other
def anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def question1(s, t):
    t_len = len(t)
    s_len = len(s)
    t_sort = sorted(t)
    for i in range(s_len - t_len + 1):
        if anagram(s[i: i + t_len], t_sort):
            return True
    return False


# Case 1: ("udacity", "ad") 
#print question1("udacity","ad")
# True

# Case 2: ("udacity", "")
#print question1("udacity","")
# True

# Case 3: ("ad", "udacity" ) 
#print question1("ad","udacity")
# False

# Case 4 : ("1987652034","10")
#print question1("1987651034","10")
# True

"""
Question 2
Given a string a, find the longest palindromic substring contained in a. Your function definition should look like question2(a), and return a string.
"""
def question2(a):
    max_length = 1
    length = len(a)
    beginIndex = 0
    table = [[False for x in range(length)] for y in range(length)]
    for i in range(length):
        table[i][i] = True
    for i in range(length-1):
        if a[i] == a[i+1]:
            table[i][i+1] = True
            max_length = 2
            beginIndex = i

    curr_len = 3
    while curr_len <= length:
        for i in range(length-curr_len+1):
            j = i+curr_len-1
            if (table[i+1][j-1] and a[i] == a[j]):
                table[i][j] = True
                max_length = curr_len
                beginIndex = i
        curr_len+=1

    return a[beginIndex:beginIndex+max_length]

# Case 1:  
#print question2("bananas")
# anana

# Case 2:
#print question2("")
#

# Case 3: 
#print question2("babad")
# aba

"""
Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured like this:

{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}
Vertices are represented as unique strings. The function definition should be question3(G)

"""
# A utility function to find set of an element i


def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])
 
    # A function that does union of two sets of x and y
def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
 
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
 
        # If ranks are same, then make one as root 
        # and increment its rank by one
    else :
        parent[yroot] = xroot
        rank[xroot] += 1

def Kruskal(graph, V, key_dict):
    result = [] # to store the resultant spanning tree

    # edge case when the graph is empty 
    if len(graph) < 2:
        return "Graph does not have enough vertices to form edges"

    # sort the graph in order of the weights
    graph =  sorted(graph,key=lambda item: item[2])
   
    parent = []
    rank = []

    # Create V subsets of vertices and assign rank 0 to all the vertices
    for node in range(V):
        parent.append(node)
        rank.append(0)

    edges = 0
    i = 0

    while edges < V-1:
        u,v,w =  graph[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent ,v)
        # If including this edge does't cause cycle, include it in result and increment the index of result for next edge
        if x != y:
            edges = edges + 1    
            result.append([u,v,w])
            union(parent, rank, x, y)            
            # Else discard the edge

    output = []
    final_result = {}
    for u,v,weight  in result:
        output = [(key_dict[v],weight)]
        if key_dict[u] not in final_result:
            final_result[key_dict[u]] = output
        else:
            final_result[key_dict[u]].append(output)
            
    return final_result

def question3(g):
    dict1 = {}
    count = 0
    graph = []
    key_dict = {}
    u,v,w = None,None,None

    for i in g:
        dict1[i] = count
        key_dict[count] = i
        count += 1
    for i in g:
        for j in g[i]:
            u = dict1[i]
            v = dict1[j[0]]
            w = j[1]
            graph.append([u,v,w])

    return Kruskal(graph,count,key_dict)

# Case 1:
g = {'A': [('B', 10),('C', 5),('D', 6)],'B': [('A', 10), ('C', 15)],'C': [('A', 5), ('B', 15),('D', 4)],'D': [('A', 6),('C', 4)]}
print (question3(g))
# {'C': [('D', 4)], 'A': [('C', 5), [('B', 10)]]}

# Case 2: 
g = {}
print (question3(g))
# Graph does not have enough vertices to form edges

# Case 3:
g = {'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}
print (question3(g))
# {'A': [('B', 2)], 'B': [('C', 5)]}



"""
Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. The function definition should look like question5(ll, m), where ll is the first node of a linked list and m is the "mth number from the end". You should copy/paste the Node class below to use as a representation of a node in the linked list. Return the value of the node at that position.

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None
"""

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None


def getLength(ll):
    temp=ll
    count=0
    while(temp):
        count+=1
        temp=temp.next
    return count

def question5(ll,m):

    if type(ll) != Node:
        return "ll is not a linked list"

    length = getLength(ll)

    if length < m :
        return "m is greater than the length of the linked list"

    current = ll

    for i in range(length-m):
        current = current.next

    return current.data


n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)
n4.next = n5
n3.next = n4
n2.next = n3
n1.next = n2

# Case 1:
print(question5(n1,8))
# m is greater than the length of the linked list

# Case 2:
print(question5(123,4))
# ll is not a linked list

# Case 3:
print(question5(n1,3))
# 3




