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


class Libreta:
    def __init__(self):
        self.head = None
        self.tail = None
        self.apellidos = []
        self.contacto = []

    def empty(self):
        return self.head == None


    def insert(self, contacto):
        if self.empty():
            self.head = Node(contacto)
            self.tail = self.head
            self.contacto.append(self.head)
            self.apellidos.append(self.head.contacto.apellido)
        else:
            node = Node(contacto)
            node.next_node = self.head
            self.head = node
            self.contacto.append(self.head)
            self.apellidos.append(node.contacto.apellido)

    def print_list(self):
        if self.empty():
            print("Lista vacia")
        else:
            self.apellidos.sort()
            for apellidos in self.apellidos:
             for contacto in self.contacto:
                if apellidos == contacto.contacto.apellido:
                    print(contacto.contacto.nombre," ", contacto.contacto.apellido," - " , contacto.contacto.mail," - ",contacto.contacto.telefono )


if __name__ == '__main__':
    L = Libreta()
    a = Contacto('Elza', 'Pato', +56954627651, 'Elza.pato@mail.udp.cl')
    b = Contacto('Alan', 'Turing', +569133132123, 'ElchoroAlan@yahoorespuestas.net')
    c = Contacto('Homero', 'Chino', +56998746571, 'amantedelacomida83@aol.com')
    L.insert(a)
    L.insert(b)
    L.insert(c)
    L.print_list()
