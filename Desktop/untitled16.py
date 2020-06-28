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
 
    #range methord
    #we only need to know the different appear in printmode
    #we need to know the tree is empty or not
    def frontsize(self,root):
        if root == None:
            return 'the tree is empty'
        #we get the root first, then we need to know the left then,the right 
        print (root.newNode, end = '')
        self.frontsize(root.lchild)
        self.frontsize(root.rchild)
        
    def middlesize(self, root):
        if root == None:
            return
        self.middlesize(root.lchild)
        print(root.newNode, end = '')
        self.middlesize(root.rchild)
        
    def latersize(self, root):
        if root == None:
            return
        self.latersize(root.lchild)
        self.latersize(root.rchild)
        print(root.newNode, end = '')
        
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
    





        