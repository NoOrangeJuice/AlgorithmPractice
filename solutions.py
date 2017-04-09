### Import necessary modules.
# Import defaultdict for Question 3.
from collections import defaultdict
import random
import itertools

### Question 1 main function and helper functions.
print """Given two strings s and t, determine whether some anagram of t is a
substring of s. For example: if s = "udacity" and t = "ad", then the
function returns True. Your function definition should look like:
question1(s, t) and return a boolean True or False."""
# Define an anagram.
def anagram(s1, s2):
    return sorted(s1) == sorted(s2)

# Main function.
def Question1(t, s):
    # use built in any function to check any anagram of t is substring of s
    return any(anagram(s[i: i+len(t)], t)
                 for i in range(len(s)-len(t)+ 1))
# Simple test case.
print Question1("app", "paple")
# True

# Test case with a space character.
print Question1("", "a space")
# True

# Test case with numbers.
print Question1("15", "4732890793878894351")
# True

# Test case with punctuation.
print Question1("$ %", "100% $Expensive")
# True

# Test case that returns false.
print Question1("music", "muscle")
# False

# End question 1.
print """---End Question 1---
"""


### Question 2 main function and helper functions.
print """Given a string a, find the longest palindromic substring contained in a.
Your function definition should look like question2(a), and return a string."""
# Gives substrings of s in decending order.
def substrings(s):

    # Declare local variable for the length of s.
    l = len(s)

    # Here I chose range over xrange for python version compatibility.
    for end in range(l, 0, -1):
        for i in range(l-end+1):
            yield s[i: i+end]

# Define palindrome.
def palindrome(s):
    return s == s[::-1]

# Main function.
def Question2(a):
    for l in substrings(a):
        if palindrome(l):
            return l

# Simple test case.
print Question2("stresseddesserts")
# stresseddesserts

# Test case using numbers.
print Question2("987654321123456789")
# 987654321123456789

# Complex test case.
print Question2("""whatisapalindromebutareflectionofthdualityoflife,forever
callingustowardstheeventuallydissolutionofindividualidentityandpersonal
senseofbelonging.whenstressedasadessertsisthepalindromemycodewillrender.""")
# stressedasadesserts

# Null.
print Question2("")
# None.

# End Question 2.
print """---End Question 2---
"""


### Question 3 main function and helper functions.
print """Given an undirected graph G, find the minimum spanning tree within G.
A minimum spanning tree connects all vertices in a graph with the smallest
possible total weight of edges. Your function should take in and return an
adjacency list structured like this:

{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)],
 'C': [('B', 5)]}
 """
# Within code v = vertice, r = root, e = edge, u = union, m = make, f = find.
# Global Variables for simplifying code.
parent = dict()
rank = dict()

# Find vertices.
def f(v):
    if parent[v] != v:
        return f(parent[v])
    else:
        return v
# Make vertices.
def m(v):
    parent[v] = v
    rank[v] = 0

# Define union between vertices.
def u(v1, v2):
    r1 = f(v1)
    r2 = f(v2)
    if r1 != r2:
        if rank[r1] > rank[r2]:
            parent[r2] = r1
        else:
            parent[r1] = r2
            if rank[r1] == rank[r2]: rank[r2] += 1

# Main Function.
def Question3(G):
    for v in G['vertices']:
        m(v)

    # Set Edges as list and MST as set within list.
    edges = list(G['edges'])
    edges.sort
    MST = set()

    # For each edge define two vertices and weight, create union
    # if v1 != v2 and add to MST.
    for e in edges:
        weight, v1, v2 = e
        if f(v1) != f(v2):
            u(v1, v2)
            MST.add(e)
    return sorted(MST)

G = {'vertices': ['A', 'B', 'C'],
'edges': set([
(2, 'A', 'B'),
(2, 'B', 'A'),
(5, 'B', 'A'),
(5, 'B', 'C')
])
}


#{'A': [('B', 2)],
# 'B': [('A', 2), ('C', 5)],
# 'C': [('B', 5)]}

print "Minimum Spanning Tree of G:"
print Question3(G)
# Minimum Spanning Tree of G:
# [(2, 'A', 'B'), (5, 'B', 'C')]


# Expected Output.
# Minimum Spanning Tree of G:
# set([(1, 6, 5), (2, 4, 9), (2, 5, 4), (2, 1, 7), (2, 3, 6), (0, 2, 1)])
print """---End Question 3---
"""

### Question 4 Main function and helper functions.
print """Find the least common ancestor between two nodes on a binary search tree.
The least common ancestor is the farthest node from the root that is an
ancestor of both nodes. For example, the root is a common ancestor of all nodes
on the tree, but if both nodes are descendents of the root's left child, then
that left child might be the lowest common ancestor. You can assume that both
nodes are in the tree, and the tree itself adheres to all BST properties.
The function definition should look like question4(T, r, n1, n2), where T is
the tree represented as a matrix, where the index of the list is equal to the
integer stored in that node and a 1 represents a child node, r is a
non-negative integer representing the root, and n1 and n2 are non-negative
integers representing the two nodes in no particular order. For example, one
test case might be:

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
"""
# Main Function.
def Question4(tree, root, n1, n2):
    # set nodes as list
    n = [n1, n2]

    # Since we have not found LCA yet set as False
    lcafound = False

    # Loop until lcafound is True
    while lcafound is False:

        # Use enumerate to represent each node as tuple (index, value)
        for index, n in enumerate(tree):
            #print tree

            # if node is not already the root continue
            if n1 != root:
                if n[n1] == 1:
                    #print n
                    n1 = index

                    # Check if both nodes have same index value
                    if index in n:
                        lcafound = True

                        #print index
                        return index
                    else:
                        n.append(index)

            # if node is not already the root continue
            if n2 != root:
                if n[n2] == 1:
                    #print n
                    n2 = index

                    # Check if both nodes have same value
                    if index in n:
                        lcafound = True

                        #print index
                        return index
                    else:
                        n.append(index)


# Test Cases.
print ("Least Common Ancestor is:", Question4([[0, 1, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[1, 0, 0, 0, 1],
[0, 0, 0, 0, 0]],
3,
1,
4))
# Least Common Ancestor:
# 3
print ("Least Common Ancestor is:", Question4([[0, 0, 0, 0, 0],
[1, 0, 1, 0, 0],
[0, 0, 0, 0, 0],
[0, 1, 0, 0, 1],
[0, 0, 0, 0, 0]],
3,
1,
2))
# Least Common Ancestor:
# 1
print ("Least Common Ancestor is:", Question4([[0, 1, 0, 0, 0],
[0, 1, 0, 0, 0],
[0, 1, 1, 1, 0],
[1, 1, 0, 1, 1],
[0, 0, 0, 1, 0]],
3,
1,
4))
# Least Common Ancestor:
# 3
print """---End Question 4---
"""


### Question 5 Main function and helper functions.
print """Find the element in a singly linked list that's m elements from the end.
For example, if a linked list has 5 elements, the 3rd element from the end is
the 3rd element. The function definition should look like question5(ll, m),
where ll is the first node of a linked list and m is the "mth number from
the end". You should copy/paste the Node class below to use as a representation
of a node in the linked list. Return the value of the node at that position.

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None
"""
global ll
ll = None

# Provided Node Class.
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

# Function for adding values to list.
def add(new_data):
    global ll
    node = Node(new_data)
    node.next = ll
    ll = node

def Question5(ll, m):
    # Nodes already traversed
    element1 = ll
    # Nodes from beginning
    element2 = ll
    # Node count.
    c = 0

    # Traverse list until c = m
    if(ll is not None):
        while(c < m):
            element2 = element2.next
            c += 1

    # Loop until the linked list reaches its end.
    while(element2 is not None):
        #print ("This is element 1:", element1.data)
        #print ("This is element 2:", element2.data)
        element1 = element1.next
        element2 = element2.next

    # return of the current node m positions from the end
    return element1.data

# List meant to represent a telephone with 0 being the end.
add("0")
add("9 WXYZ")
add("8 TUV")
add("7 PQRS")
add("6 MNO")
add("5 JKL")
add("4 GHI")
add("3 DEF")
add("2 ABC")
add("1")
# Singly Linked List:
# 1 - 2 ABC - 3 DEF - 4 GHI - 5 JKL - 6 MNO - 7 PQRS - 8 TUV - 9 WXYZ - 0
print ("node at position m in relation to the end of ll is: ", Question5(ll, 4))
# ('node at position m in relation to the end of ll is: ', '7 PQRS')
print ("node at position m in relation to the end of ll is: ", Question5(ll, 8))
# ('node at position m in relation to the end of ll is: ', '3 DEF')
print ("node at position m in relation to the end of ll is: ", Question5(ll, 1))
# ('node at position m in relation to the end of ll is: ', '0')
print """---End Question 5---
"""
print """---End Solutions---
"""
