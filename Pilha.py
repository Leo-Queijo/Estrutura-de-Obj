class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """ Verifica se a pilha esta vazia"""
        return len(self.items) == 0

    def push(self,item):
        """Adiciona um item no topo da pilha"""
        self.items.append(item)
    def pop(self):
        """Remove e retorna o item do topo da pilha"""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()
    def peek (self):
        """Retorna o item do topo da pilha sem remove-la"""
        if self.is_empty():
            raise IndexError ("peek from empty stack")
        return self.items[-1]
    def size(self):
        """Retorna o número de itens na pilha"""
        return len(self.items)
    def __str__(self):
        """Retorna uma representação em string da pilha"""
        
        return str(self.items)
    
    def __repr__(self):
        """Retorna uma representação em string da pilha"""
        
        result = ''
        for item in reversed(self.items):
            result += f'\n|{item}'
        return result
    
    
        
