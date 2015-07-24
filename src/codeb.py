import os
import sys
import ast

helloProgram = """
def helloWorld():
    print("Hello world")
helloWorld()
"""

sqlInjectionProgram = """
def find_question(request):
    question_text = request.POST.get('question_text', None)

    if question_text is None:
        return HttpResponseRedirect(reverse('polls:index'))

    qry = "SELECT * FROM polls_question WHERE question_text='%s'" % question_text
    try:
        question = Question.objects.raw(qry)[:1][0]
    except Question.DoesNotExist as e:
        raise Http404('Question does not exist!')

    print question

    return render(request, 'polls/detail.html', {'question': question})
"""

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
        print "Cutting tree at the LOAD, i.e., not recursing"
        pass

    # def visit_FunctionDef(self, node):
    #     print node

    def visit_Name(self, node):
        print "Name:", node.id
        self.context.addName(node.id)

helloTree = ast.parse(helloProgram)
sqlTree = ast.parse(sqlInjectionProgram)
# exec(compile(helloTree, filename="<ast>", mode="exec"))

# query -> query plan (visitor logic) -> executor
visitor = SimpleVisitor()
visitor.visit(helloTree)
visitor.visit(sqlTree)
