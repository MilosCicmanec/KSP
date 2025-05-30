from functools import lru_cache
import sys
sys.setrecursionlimit(2000)
def min_partitions(s):
    n = len(s)
    
    @lru_cache(None)
    def dfs(start):
        if start == n:
            return 0
        min_parts = float('inf')
        for end in range(start, n):
            if end == start or s[start] == s[end]:
                min_parts = min(min_parts, 1 + dfs(end + 1))
        return min_parts
    
    return dfs(0)

string = list(input())
print(min_partitions(string))