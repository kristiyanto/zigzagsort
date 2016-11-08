# zigzagsort


# zigzagsort


An algorithm to sort an array of distinct integer in a zig-zag manner such that `a < b > c < d > e <`

e.g
```python
input = [4,3,7,8,6,2,1]
output = [1,3,2,6,4,8,7]
```

## Summary
This can be performed by first sorting the list, and then swap the next 2 items after current index. The iteration stops at the `(length of the array-2)`.

The complexity of the algorithm:  
Sorting: `nlogn`  
Iterate trrough the list: `n`  
Total= `n + nlogn`   
or `(O) nlogn`  




Codes:  

```python
###########################################
# Sort a list of distinct integers
# such that: a < b > c < d > e <
#
# e.g input: [4,3,7,8,6,2,1]
# e.g result: [1,3,2,6,4,8,7]
# 
# Daniel Kristiyanto
###########################################




def zigzag(a):
    a.sort()
    if not a or len(a) < 3: return a
    for i in range(0,len(a)-2,2):
        a[i+1], a[i+2] = a[i+2], a[i+1]
    return a

s = [4,2,90,1]
zigzag(s)

```