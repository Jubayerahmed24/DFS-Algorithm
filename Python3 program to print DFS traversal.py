def non_recursive_dfs(graph, source): 
    if source is None or source not in graph:  
        return "Please Enter Valid input"  
    path = []  
    stack_val = [source]  	  
    stack = []  	  
    while(len(stack_val) != 0):  	  
        s = stack_val.pop()  
        stack.append(s)  
        if s not in path:  
            path.append(s)  
        if s not in graph:  
            #leaf node  
            continue  	  
        for neighbor_node in graph[s]:  
            stack_val.append(neighbor_node)  
    return " ".join(path)