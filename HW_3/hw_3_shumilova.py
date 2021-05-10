#!/usr/bin/env python
# coding: utf-8

# In[22]:


from pathlib import Path #to indicate the path to our file

path = Path('/home/maria/Documents/Python/02_semester/04_json_format_hw_4/data.JSON')

file = open(path,)
fname = json.load(file)


# In[23]:


tree = dict()
nodes = set()
for el in fname:
    nodes.add(el['name'])
    for p in el['parents']:
        if p in tree:
            tree[p].append(el['name'])
        else:
            tree[p] = [el['name']]
print(tree)
print(nodes)


# In[24]:


def get_descendants(tree, node):

    visited = []
    queue = []
    def bfs(visited, graph, node):
      visited.append(node)
      queue.append(node)

      while queue:
        s = queue.pop(0)
        res.append(s)

        if s in graph:
            for neighbour in graph[s]:
              if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    bfs(visited, tree, node)

for el in sorted(nodes):
    res = []
    get_descendants(tree, el)
    print(el, len(res))


# In[ ]:




