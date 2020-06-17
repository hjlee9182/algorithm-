from collections import deque

class Node:
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage):
        self.now = Node(homepage)
    def visit(self, url):
        nod = Node(url,prev=self.now)
        self.now.next = nod
        self.now = nod

    def back(self, steps):
        while steps>0 and self.now.prev:
            self.now = self.now.prev
            steps = steps-1
        return self.now.data

    def forward(self, steps):
        while steps>0 and self.now.next:
            self.now = self.now.next
            steps = steps-1
        return self.now.data