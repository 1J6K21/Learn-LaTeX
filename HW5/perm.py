def perm(a):
    # Base Case: if list has 0 or 1 element, it's already a "permutation"
    if len(a) <= 1:
        return [a]

    res = []
    for i in range(len(a)):
        # 1. Pick the current element
        current = a[i]
        
        # 2. Get the remaining elements (everything except index i)
        remaining = a[:i] + a[i+1:]
        
        # 3. Recursively find permutations of the remaining elements
        for p in perm(remaining):
            # 4. Add the current element to the front of each sub-permutation
            res.append([current] + p)
            
    return res

b = ['a', 'b', 'c']
print(perm(b))
