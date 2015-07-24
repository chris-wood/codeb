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
    ''' TODO: sql grammar parser
    '''
    pass

class VisitorContext():
    def __init__(self):
        self.names = []
        pass

    def addName(self, name):
        self.names.append(name)

    def __str__(self):
        return str(self.names)

class SimpleVisitor(ast.NodeVisitor):
    def generic_visit(self, node):
        print type(node).__name__ # print object's class name
        ast.NodeVisitor.generic_visit(self, node) # call parent's visit to traverse to children

    def visit_Module(self, node):
        self.context = VisitorContext()
        self.generic_visit(node)

        print self.context

    def visit_Load(self, node):
        print "Cutting tree at the LOAD"
        pass

    def visit_Name(self, node):
        print "Name:", node.id
        self.context.addName(node.id)

# query -> query plan (visitor logic) -> executor
visitor = SimpleVisitor()
visitor.visit(helloTree)
