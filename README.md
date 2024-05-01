# Depth First Search (DFS) Algorithm

The DFS algorithm is a recursive algorithm that uses the idea of backtracking. It involves exhaustive searches of all the nodes by going ahead, if possible, else by backtracking.
Here, the word backtrack means that when you are moving forward and there are no more nodes along the current path, you move backwards on the same path to find nodes to traverse. All the nodes will be visited on the current path till all the unvisited nodes have been traversed after which the next path will be selected.
This recursive nature of DFS can be implemented using stacks. The basic idea is as follows:
Pick a starting node and push all its adjacent nodes into a stack.
Pop a node from stack to select the next node to visit and push all its adjacent nodes into a stack.
Repeat this process until the stack is empty. However, ensure that the nodes that are visited are marked. This will prevent you from visiting the same node more than once. If you do not mark the nodes that are visited and you visit the same node more than once, you may end up in an infinite loop.

<h2>How does DFS work?</h2>
Depth-first search is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.

Let us understand the working of Depth First Search with the help of the following illustration:

Step 1: Initially stack and visited arrays are empty.
<center><img src="https://s9.gifyu.com/images/SaNaN.png" alt="1" border="0"></center>
Stack and visited arrays are empty initially.

Step 2: Visit 0 and put its adjacent nodes which are not visited yet into the stack.
<center><img src="https://s9.gifyu.com/images/SaNaK.png" alt="2" border="0"></center>
Visit node 0 and put its adjacent nodes (1, 2, 3) into the stack

Step 3: Now, Node 1 at the top of the stack, so visit node 1 and pop it from the stack and put all of its adjacent nodes which are not visited in the stack.
<center><img src="https://s12.gifyu.com/images/SaNap.png" alt="3" border="0"></center>
Visit node 1

Step 4: Now, Node 2 at the top of the stack, so visit node 2 and pop it from the stack and put all of its adjacent nodes which are not visited (i.e, 3, 4) in the stack.
<center><img src="https://s12.gifyu.com/images/SaNax.png" alt="4" border="0"></center>
Visit node 2 and put its unvisited adjacent nodes (3, 4) into the stack

Step 5: Now, Node 4 at the top of the stack, so visit node 4 and pop it from the stack and put all of its adjacent nodes which are not visited in the stack.
<center><img src="https://s12.gifyu.com/images/SaNas.png" alt="5" border="0"></center>
Visit node 4

Step 6: Now, Node 3 at the top of the stack, so visit node 3 and pop it from the stack and put all of its adjacent nodes which are not visited in the stack.
<center><img src="https://s12.gifyu.com/images/SaNaH.png" alt="6" border="0"></center>
Visit node 3

Below is the implementation of the above approach <a href="https://github.com/Jubayerahmed24/DFS-Algorithm/blob/main/Python3%20program%20to%20print%20DFS%20traversal.py">Python3 program to print DFS traversal.py</a>

Output:
Following is Depth First Traversal (starting from vertex 2) 
  2 0 1 3 

# Implementing Depth First Search (A non-recursive approach)

Let's consider the following graph for the DFS implementation.

<img src="https://s12.gifyu.com/images/SaNaL.png" alt="7" border="0">

Let's define the graph as an adjacency list using the Python Dictionary.

1.	   graph = {"A":["B","C","D"],  
2.	   "B":["E"],  
3.	   "C":["G","F"],  
4.	   "D":["H"],  
5.	   "E":["I"],  
6.	   "F":["J"],  
7.	   "G":["K"]}  

We can implement the DFS both recursion technique and non-recursion technique, iterative approach.
In this section, we will understand the iterative approach.

We will use a stack and a list to keep track of the visited nodes.
o	First, we will visit to the root node and mark it as visited. Then, we will move towards all of its neighbors to the stack.
o	At each step, we will pop out an item from the stack and check if it has been visited.
o	If the node is not visited, it will be added to the path and all of its neighbors to the stack.

# DFS Pseudocode
Below is the Pseudocode of the DFS. In the init() function, we run the DFS function on every node because most of the times, a graph may contain two different disconnect part. So it makes sure that we cover every vertex, can also run DFS algorithm on every node.

1.	    DFS(G, u)  
2.	    u.visited = true  
3.	    for each v ∈ G.Adj[u]  
4.	        if v.visited == false  
5.	            DFS(G,v)        
6.	    init() {  
7.	    For each u ∈ G  
8.	        u.visited = false  
9.	     For each u ∈ G  
10.	       DFS(G, u)  12.	}  

Let's implement the DFS using the Python code. <a href="https://github.com/Jubayerahmed24/DFS-Algorithm/blob/main/Example%201.py">lExample -1</a>

Output:
A D H C F J G K B E I

The order of the traversal of the graph is in the 'Depth First' manner.

# DFS using a Recursive Method

The recursive is a popular problem solving approach in which the same problem is divided into smaller instances. We will define the base case inside our program. Let's understand the below example.<a href="https://github.com/Jubayerahmed24/DFS-Algorithm/blob/main/Example%202.py">Example -2</a>

Output:
['A', 'B', 'E', 'I', 'C', 'G', 'K', 'F', 'J', 'D', 'H']

The order of traversal is again in the Depth-first manner.

# Complexity

The time complexity of the DFS is represented as O(V+E), where V shows the number of nodes and E is the number of edges. The space complexity is 0(V).
Application of Algorithm

The following are the real-life application of DFS.
o	It is used to find the path.
o	It is used to test if graph is bipartite.
o	It is used to finding the strongly connected components of a graph.
o	It is used for detecting cycle in a graph.
o	It is used for scheduling the problem.
o	It is used in topological sorting.

# Conclusion

This tutorial includes the concept of Depth-First Search in Python which is used to traverse the graph or tree. We have discussed both recursive and non-recursive methods to implement DFS in Python. We have also defined how to represent graph in Python.




Done!

<h2>Thanks, everyone for reading:)

