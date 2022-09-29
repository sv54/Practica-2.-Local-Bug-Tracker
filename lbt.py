


from ast import List


class Usuario:
    def __init__(self, name, password, admin):
        self.nombre = name
        self.password = password
        self.admin = admin

    


class Respuesta:
    def __init__(self, nombre, resp):
        self.nombreUser=nombre
        self.respuesta = resp

class Issue:
    def __init__(self,nombre, titulo, descripcion):
        self.nombre=nombre
        self.titulo=titulo
        self.descripcion=descripcion
        self.comentarios=[]
        abierto=True


        

    def cerrarIssue(self, user: Usuario, usuarios: List):
        i = usuarios.index(user)
        if usuarios[i].admin:
            Issue.abierto=False
            resp = Respuesta(user.nombre, "Issue cerrado por admin")
            Issue.addResponse(resp)

    def reabrirIssue(self, user: Usuario, usuarios: List):
        i = usuarios.index(user)
        if usuarios[i].admin:
            Issue.abierto=True
            resp = Respuesta(user.nombre, "Issue reabierto por admin")
            Issue.addResponse(resp)
        

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


    issue1= Issue("The Frog","Error en la version 1.0.0","Hay error en la version 1.0.0 que hace que no se impirma Hello World")
    respuesta1 = Respuesta("Serhii","Vale, lo intentare corregir hoy mismo")
    issue1.addResponse(respuesta1)
    respuesta2 = Respuesta("Serhii","Corregido, version 1.0.1 ya disponible!")
    issue1.addResponse(respuesta2)
    issue1.cerrarIssue(user1, usuarios)
    issue1.reabrirIssue(user1, usuarios)
    respuesta3 = Respuesta("Serhii","Todo se ha complicado demasiado, avisad si encontrais un bug por aqui")
    issue1.addResponse(respuesta3)


    issue2= Issue("Pepe","Error en la version 1.3.1","Me es imposible sacar como resultado -- I dont belive you! Try Again!. He intentado con todos numeros posibles")
    issues.append(issue1)
    issues.append(issue2)


def registrarse():
    pass

if __name__ == "__main__":
    issues=[Issue]
    usuarios=[Usuario]
    BD(issues,usuarios)
    for i in issues[0].comentarios:
        print(i.respuesta)
    for i in issues[1].comentarios:
        print(i.respuesta)










