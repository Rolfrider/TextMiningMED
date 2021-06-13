from graphviz import Digraph

colors = ['green','red', 'pink', 'yellow', 'orange', 'brown', 'purple'] #edge colors

class Visualise:

    def _generate_dot_nodes(self, dot):
        unique_nodes = set()
        for dependency in self.data:
        	for itemset in dependency.itemsets:
        		itemset_str = ''
        		for i in range(len(itemset)):
        			itemset_str+=str(itemset[i])
        			if i != len(itemset)-1:
        				itemset_str+=','
        		unique_nodes.add(itemset_str)

        for id, val in enumerate(unique_nodes):
            attr_num = self._get_number_of_elements_in_set(val)
            with dot.subgraph(name='cluster' + str(attr_num)) as c:
                c.attr(fillcolor='blue:cyan', label='acluster', fontcolor='white',style='filled', gradientangle='270')
                c.attr('node', shape='box', fillcolor='red:yellow',style='filled', gradientangle='90')
                c.node(val, val)
                c.attr(label='Zbiory elementów o liczności ' + str(attr_num))

    def _get_number_of_elements_in_set(self, attr_set):
        return attr_set.count(',') + 1 if attr_set else 0

    def _add_dot_edges(self, dot):
    	itemsets_str = {}
    	it = 0
    	for dependency in self.data:
    		itemsets_str[it] = []
    		for itemset in dependency.itemsets:
    			itemset_str = ''
    			for i in range(len(itemset)):
    				itemset_str+=str(itemset[i])
    				if i != len(itemset)-1:
    					itemset_str+=','
    			itemsets_str[it].append(itemset_str)
    		it+=1

    	for idx in range(len(itemsets_str)):
    		for j in range(len(itemsets_str[idx])):
    			if j!= len(itemsets_str[idx])-1:
    				try:
    					dot.edge(itemsets_str[idx][j], itemsets_str[idx][j+1], color=colors[idx])
    				except:
    					dot.edge(itemsets_str[idx][j], itemsets_str[idx][j+1], color=colors[0])
    
    def draw(self):
        dot = Digraph(comment='Wizualizacja zbiorów częstych')
        dot.attr(label=r'\n\nCzęste sekwencje odnalezione za pomocą algorytmu GSP')
        dot.attr(fontsize='20')
        itemset_str = self._generate_dot_nodes(dot)
        self._add_dot_edges(dot)
        dot.render('experiments/visualisation.gv', view=True)

    def __init__(self, data):
        self.data = data