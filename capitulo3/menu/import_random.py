class Pila(object):
    def __init__(self):
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()
    
    def esta_vacia(self):
        return len(self.items) == 0

    def ver_tope(self):
        return self.items[-1]
    







