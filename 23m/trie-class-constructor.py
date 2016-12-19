'''
Create a Trie Class to see if there's genes (TCGA) that shares a same prefix
'''


class node:
    def __init__(self, val=None):
        self.val = val
        self.kids = {'t': None, 'c': None, 'g': None, 'a': None}

class tree:
    def __init__(self):
        self.root = node()
        self.deg_of_freedom = {'t','c','g','a'}
    '''
        Insert string to the tree 
        (must be either 't','c','g', or 'a')
        Input: String
        Output: bool (True if success)
        
    '''
    def insert(self, tcga):
        if any([i not in self.deg_of_freedom for i in tcga]):
            return False
        else:
            current = self.root
            for char in tcga:
                if not current.kids[char]:
                    current.kids[char] = node(char)
                current = current.kids[char]
            return True
        
    '''
        Check if the entire string found in the tree
        Input: String 
        Output: bool
    '''
    def search(self, tcga):
        current = self.root
        for char in tcga:
            if not current.kids[char]: return False
            current = current.kids[char]
        return True
    '''
        Get the first matching prefix
        Input: String
        Output: The matching prefix (or all string)
    '''
    def prefix(self, tcga):
        current, index = self.root, 0
        for char in tcga:
            if current.kids[char]:                 
                current = current.kids[char]
                index += 1
        return tcga[:index]
            
            
