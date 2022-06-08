
def leerArchivo(nombre):
    archivo = open(nombre, "rt", encoding = "utf8")
    contenido = archivo.read()
    contenido = contenido.split('\n')
    return contenido

def menu():
    print("\n\n*************MENU************\n"+
          "1. Listar\n"+
          "2. Agregar \n"+
          "3. Salir\n")

    opcion = int(input("\n Ingrese una opcion: "))




userResponse = leerArchivo('login.txt')
passwordResponse = leerArchivo('clave.txt')

bandera = True
contador = 0

while bandera == True:
    usuario = input('\nIngresa el usuario: ')
    clave = input('Ingresa la clave: ')

    if contador == 2: 
        print('\n3 intentos fallidos, se le denegó el acceso')
        bandera = False
    
    opcion=1

    for usuarioItem in userResponse:
        if usuario == usuarioItem:
            for claveoItem in passwordResponse:
                if clave == claveoItem:
                    bandera = False
                    menu()


    if bandera == True:
        print('Usuario o contraseña incorrectas \n')
        contador = contador + 1 
    
    print('\n ')