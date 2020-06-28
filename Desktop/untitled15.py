# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 11:19:17 2020

@author: 13988
"""

class Binaytree:
    
    #def the root object and an empty tree
    def __init__(self, rootObj):
        self.root = rootObj
        self.lchild = None
        self.rchild = None
    
    #insert the left childtree of root Node
    def insertLchildtree(self, newNode): 
        #two different situations, the tree is empty or not 
        if self.lchild == None:
            self.lchild = Binaytree(newNode)
        else:
            l = self.lchild
            self.lchild = Binaytree(newNode)
            self.lchild = l
    
    #so the same as the right tree
    def insertRchildtree(self, newNode):
        if self.rchild == None:
            self.rchild = Binaytree(newNode)
        else:
            r = self.rchild
            self.rchild = newNode
            self.rchild = r
 
    '''
    #they are some new function to get the value of chlid tree and root node        
    def getlchild(self):
        return self.lchild
    
    def getrchlid(self):
        return self.rchild
    
    def setrootnode(self, obj):
        self.key = obj
        
    def getrootnode(self):
        return self.key
    '''
    
a = Binaytree(1)
b = a.insertLchildtree(4)
c = a.insertRchildtree(6)
d = a.insertLchildtree(2)
e = a.insertRchildtree(3)

m = Binaytree(d)
n = m.insertRchildtree(5)





'''
d = b.insertLchildtree(4)
e = b.insertRchlidtree(5)
f = c.insertRchlidtree(6)
'''

        
        
        
    






        