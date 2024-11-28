class node:
    def __init__(self, val, next, prev) -> None:
        self.val = val
        self.next = next
        self.prev = prev

class Node_P:
    def _init_ (self, valor):
        self.prox = None
        self.valor = valor

 
class pilha:
    header = Node_P()
    def _init_ (self):
        self.top = None
        self.size = 0
    
    def inserir (self, elemento):
        if self.top == None:
            self.top = elemento
            self.top.prox = self.header
            self.size += 1
            return
        else:
            self.top.prox = self.top
            self.top = elemento
            self.size += 1
            return
    
    def pop (self):
        elemento = self.top
        self.top = self.top.prox
        return elemento


class ListaDL:

    def __init__(self):
        self.header = node (-1, None, None)
        self.size = 0

    #Pra inserir no LISTADL
    def insert(self, val):
        if(self.header.next == None):
            self.header.next = node(val, None, self.header)
        else:
            node = self.header
            while node.next != None:
                node = node.next
            node.next = node(val, None, node)
        
        self.size += 1

    #Para procurar operador na LISTADL
    def search(list):
        node = list.header
        while node.val.isnumeric() and node.next:
            node = node.next
    
        if not node.val.isnumeric():
            return node
        else: 
            return None

    #Para deletar elemento na LISTADL
    def delete(self, element : node):

        element.prev.next = element.next # sempre
        if(element.next): # caso não seja o último
            element.next.prev = element.prev

        self.size -= 1

    def Operação(self, operator):
        if(operator):
            operator.prev.prev.val = int(operator.prev.prev.va)
            operator.prev.val = int(operator.prev.val)
            if (operator == "+"):
                operator.prev.val = (operator.prev.prev.val + operator.prev.val)

            elif (operator == "-"):
                operator.prev.val = (operator.prev.prev.val - operator.prev.val)

            elif (operator == "/"): 
                operator.prev.val = (operator.prev.prev.val / operator.prev.val)

            elif (operator == "*"):
                operator.prev.val = (operator.prev.prev.val * operator.prev.val)

            elif (operator == "%"):
                operator.prev.val = (operator.prev.prev.val % operator.prev.val)

            else: #POTENCIAÇÃO
                operator.prev.val = (operator.prev.prev.val ** operator.prev.val )               
            
            #Fazer no final quando terminar a operação
            operator.prev.prev.prev.next = operator.prev
            operator.prev.next = operator.next
            operator.prev.prev = operator.prev.prev.prev
            operator.next.prev = operator.prev


def main():
    expr = "(" + input() + ")"

    expr_pol = ListaDL()
    
    pilha_parenteses = pilha()
    pilha_operação = pilha()

    for i in expr:
        if(expr[i].isnumeric()):
            expr_pol.insert(expr[i])

        elif(expr[i] == "("):
            parentese = node_P()
            pilha_parenteses.inserir(parentese)
        
        elif(expr[i] in ops):
            operação = node_P()
            operação.valor = expr[i]
            pilha_operação.inserir(operação)
        else:
            pilha_parenteses.pop()
            op = (pilha_operação.pop()).valor
            expr_pol.insert(op)

    while expr_pol.size > 1:
            expr_pol.Operação(expr_pol.search())
