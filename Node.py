# -*- coding: utf-8 -*-
"""
Created and Modified by: Matthew Iglesias
80591632
Dr. Diego Aguirre
T.A. Anitha Nath
"""
class Node(object):
    password = ""
    count = -1
    next = None
    
    def _init_(self, password,count,next):
        self.password = password
        self.count = count
        self.next = next