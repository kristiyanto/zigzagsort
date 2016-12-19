'''
Find all possible permutations

e.g: input: 'abc'
     output: ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']

'''

def permutations(string):
    if len(string) < 2: return string
    
    result, recursion = [], permutations(string[1:])
    for i in recursion:
        for j in range(len(recursion)+1):
            result.append(i[:j] + string[0] + i[j:])
    return result