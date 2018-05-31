class Contacto:
    def __init__(self, nombre, apellido, telefono, mail):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.mail = mail


class Node:
    def __init__(self, contacto):
        self.contacto = contacto
        self.next = None


class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.nombres = []

    def empty(self):
        return self.head == None


    def insert(self, contacto):
        if self.empty():
            self.head = Node(contacto)
            self.tail = self.head
            self.nombres.append(self.head.contacto.nombre)
        else:
            node = Node(contacto)
            node.next_node = self.head
            self.head = node
            self.nombres.append(node.contacto.nombre)

    def print_list(self):
        if self.empty():
            print("Lista vacia")
        else:
            self.nombres.sort()
            for nombres in self.nombres:
             print(nombres)


if __name__ == '__main__':
    L = List()
    a = Contacto('b', 'b', 3245345, 'mail1')
    b = Contacto('c', 'c', 32453345, 'mail2')
    c = Contacto('a', 'a', 32453345, 'mail3')
    L.insert(a)
    L.insert(b)
    L.insert(c)
    L.print_list()
