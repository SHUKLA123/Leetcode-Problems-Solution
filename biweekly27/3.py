from collections import defaultdict
n = 5
prerequisites = [[0,1],[1,2],[2,3],[3,4]]
queries = [[0,4],[4,0],[1,3],[3,0]]
def test(n,prerequisites,queries):
        edges = defaultdict(list)
        for uv in prerequisites:
            u, v = uv
            edges[u].append(v)
        print(edges)
        def search(start, end):
            seen = set([start])
            curr = [start]
            while curr:
                nxt = []
                for node in curr:
                    for nbr in edges[node]:
                        if nbr not in seen:
                            seen.add(nbr)
                            nxt.append(nbr)
                            if nbr == end:
                                return True
                curr = nxt
            
            return False
        
        out = []
        for uv in queries:
            u, v = uv
            out.append(search(u, v))
        
        return out 
print(test(n,prerequisites,queries))
