


from ast import List


class Usuario:
    def __init__(self, name, password, admin):
        self.nombre = name
        self.password = password
        self.admin = admin


class Respuesta:
    def __init__(self, nombre, resp):
        self.nombre=nombre
        self.respuesta = resp

class Issue:
    def __init__(self,nombre, titulo, descripcion, tags):
        self.nombre=nombre
        self.titulo=titulo
        self.descripcion=descripcion
        self.comentarios=[]
        self.tags=tags
        self.abierto=True


    def cerrarIssue(self, user: Usuario):

        if user.admin:
            self.abierto=False
            resp = Respuesta(user.nombre, "Issue cerrado por admin")
            self.addResponse(resp)

    def reabrirIssue(self, user: Usuario):
        if user.admin:
            self.abierto=True
            resp = Respuesta(user.nombre, "Issue reabierto por admin")
            self.addResponse(resp)
        

    def addResponse(self, resp: Respuesta):
        self.comentarios.append(resp)
        
        

#Inicializamos la base de datos.
def BD(issues, usuarios):
    
    
    user1= Usuario("Serhii", "123", True)
    user2= Usuario("Pepe", "123", False)
    user3= Usuario("The Frog", "123", False)
    usuarios.append(user1)
    usuarios.append(user2)
    usuarios.append(user3)


    issue1= Issue("The Frog","Error en la primera version","Hay error en la version 1.0.0 que hace que no se impirma Hello World", ['1.0.0', 'help!'])
    respuesta1 = Respuesta("Serhii","Vale, lo intentare corregir hoy mismo")
    issue1.addResponse(respuesta1)
    respuesta2 = Respuesta("Serhii","Corregido, version 1.0.1 ya disponible!")
    issue1.addResponse(respuesta2)
    issue1.cerrarIssue(user1)
    issue1.reabrirIssue(user1)
    respuesta3 = Respuesta("Serhii","Todo se ha complicado demasiado, avisad si encontrais un bug por aqui")
    issue1.addResponse(respuesta3)


    issue2= Issue("Pepe","Error en la version 1.3.1","Me es imposible sacar como resultado -- I dont belive you! Try Again!. He intentado con todos numeros posibles", [])
    issues.append(issue1)
    issues.append(issue2)


def register():
    nombre= input("Inserte su nombre de usuario: \n")
    password= input("Inserte su constrasenya de usuario: \n")
    password2= input("Inserte su constrasenya de usuario: \n")

    if password== password2:
        user= Usuario(nombre, password, False)
        usuarios.append(user)
    else:
        print("las contrasenyas no coinciden")

def login():
    nombre = input("Username: ")
    password = input("Password: ")
    password = str(password)
    logeado = False
    encontrado = False

    for i in usuarios:
        if i.nombre == nombre:
            encontrado = True
            if i.password == password:
                logeado = True
                print("Logeado correctamente!")
                topics(i)
            else:
                break
        

def verTopic(user:Usuario, issue: Issue):
    while True:
        print('========================')
        print('Publicado por: ' + issue.nombre)
        print(issue.titulo)
        for y in issue.tags:
            print(y + '|')


        for y in issue.comentarios:
            print(y.nombre + ' ha respondido:')
            print(y.respuesta)
        if issue.abierto:
            print("Quiere anyadir repuesta? ")
            print("1. Si")
            print("2. No")
            if user.admin:
                print("3. Cerrar topic")
            i = input()
            if i == "1":
                i= input("Su respuesta: ")
                resp = Respuesta(user.nombre, i)
                issue.addResponse(resp)
            if i == "2":
                break
            if i == "3" and user.admin:
                issue.cerrarIssue(user)
                break

        else:
            if user.admin:
                print("Quiere reabrir topic? ")
                print("1. Si")
                print("2. No")
                i = input()
                if i == "1":
                    issue.reabrirIssue(user)
                if i == "2":
                    break
            else:
                print("1. Salir")
                i = input()
                if i == "1":
                    break

def nuevoTopic(user: Usuario):
    print("Titulo: ")
    titulo = input()
    print("Descripcion de problema: ")
    descripcion = input()


    tags = []
    i = 0
    while i != "no":
        i = input("Quiere anyadir tags? ('no' para dejar de anyadir)")
        tags.append(i)

    issue= Issue(user.nombre, titulo, descripcion, tags)
    issues.append(issue)



def topics(usuario: Usuario):
    while True:
        contador = 0
        topic=0
        for i in issues:
            contador=contador+1
            print(str(contador) + '. ' +i.titulo)
            if len(i.tags) == 0:
                print("Sin tags")
            else:
                print("Tags: ", end='')
                for y in i.tags:
                    print(y + '|', end='')
                print()
            print('-----')

        contador=contador+1
        print(str(contador)+'. Reportar nuevo error')
        contador=contador+1
        print(str(contador)+'. Cerrar Sesion')
        topic = input("Eliga opcion: ")
        if topic == str(contador):
            break
        elif topic == str(contador-1):
            nuevoTopic(usuario)
        elif int(topic) < contador and int(topic) > 0: 
            verTopic(usuario,issues[int(topic)-1])
        


def menu():
    while True:
        print("1. Iniciar sesion")
        print("2. Registrarse")
        #print("3. Listar Topics")
        i = input("Eliga una opcion:")
        if i == '1':
            login()
        if i == '2':
            register()


if __name__ == "__main__":
    issues=[]
    usuarios=[]
    BD(issues,usuarios)

    menu()
    













