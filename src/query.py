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

# query -> query plan (visitor logic) -> executor

