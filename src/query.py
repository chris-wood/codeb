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


