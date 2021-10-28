# Breadth-first search (BFS) is an algorithm for traversing
# or searching tree or graph data structures.
# It starts at the tree root (or some arbitrary node of a graph,
# sometimes referred to as a 'search key'[2]), and explores all of
# the neighbor nodes at the present depth prior to moving on to the
# nodes at the next depth level.
class Node(object):

	def __init__(self, name):
		self.name = name;
		self.adjacencyList = [];
		self.visited = False;
		self.predecessor = None;
		
class BreadthFirstSearch(object):

	def bfs(self, startNode):
	
		queue = [];
		queue.append(startNode);
		startNode.visited = True;
		
		# BFS -> queue      DFS --> stack BUT usually we implement it with recursion !!!
		while queue:
		
			actualNode = queue.pop(0);
			print("%s " % actualNode.name);
			
			for n in actualNode.adjacencyList:
				if not n.visited:
					n.visited = True;
					queue.append(n);
					
node1 = Node("A");
node2 = Node("B");
node3 = Node("C");
node4 = Node("D");
node5 = Node("E");

node1.adjacencyList.append(node2);
node1.adjacencyList.append(node3);
node2.adjacencyList.append(node4);
node4.adjacencyList.append(node5);

bfs = BreadthFirstSearch();
bfs.bfs(node1);