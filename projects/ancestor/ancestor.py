from graph import Graph


def earliest_ancestor(ancestors, starting_node):
	tree = Graph()                          
	for (node_1, node_2) in ancestors:      
		tree.add_vertex(node_1)             
		tree.add_vertex(node_2)             

	for (node_1, node_2) in ancestors:      
		tree.add_edge(node_1, node_2)       

	target_node = None                      
	longest_path = 1                        

	for node in tree.vertices:                  
		path = tree.dfs(node, starting_node)    
												
		if path:                                
			if len(path) > longest_path:        
				longest_path = len(path)        
				target_node = node              
		elif not path and longest_path == 1:    
			target_node = -1                    
	return target_node                          
