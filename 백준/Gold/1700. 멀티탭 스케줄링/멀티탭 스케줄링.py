n, k = map(int, input().split())
lst = list(map(int, input().split()))

plug = []

cnt = 0
for idx in range(k):
    i = lst[idx]
    later = -1
    res = lst[idx+1:]
    id = 0
    if i in plug:
        continue
    
    while len(plug) == n and id < n and idx != k:
        p = plug[id]
        if p not in res:
            plug.remove(p)
            cnt += 1
            continue
        
        else:
            later = max(later, res.index(p))
        id += 1
    
    if later != -1 and idx < k and len(plug) == n:
        plug.remove(res[later])
        cnt += 1
  
    if i not in plug and len(plug) < n:
        plug.append(i)
        continue
    
print(cnt)