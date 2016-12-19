'''
    Design all possible text combination on a phone
    e.g: input  = 223
         out    = ['aa']
'''

def phone(a):
    dic = {2:['a','b', 'c'], 3:['d','e','f'],
           4: ['g','h','i'], 5: ['j','k','l'], 6:['m','n','o'],
           7: ['p','q','r','s'], 8:['t','u','v'], 9:['w','x','y','z']}
    return reduce(lambda accum, digit: [x+y for x in accum for y in dic.get(int(digit), '')], a, [''])

print phone('29394848')