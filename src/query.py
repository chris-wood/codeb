import os
import sys
import ast

helloProgram = """
def helloWorld():
    print("Hello world")
helloWorld()
"""

helloTree = ast.parse(helloProgram)
exec(compile(helloTree, filename="<ast>", mode="exec"))

class CodeDatabase(object):
    def __init__(self, program):
        self.program = program
        self.ast = ast.parse(program)

class CodeQuery(object):
    pass

class SimpleVisitor(ast.NodeVisitor):
    def generic_visit(self, node):
        print type(node).__name__ # print object's class name
        ast.NodeVisitor.generic_visit(self, node) # call parent's visit to traverse to children
    
    def visit_Load(self, node):
        print "Cutting tree at the LOAD"
        pass

    def visit_Name(self, node):
        print "Name:", node.id

# query -> query plan (visitor logic) -> executor
visitor = SimpleVisitor()
visitor.visit(helloTree)

