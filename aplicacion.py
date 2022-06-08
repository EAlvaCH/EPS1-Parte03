def leerArchivo(nombre):
    archivo = open(nombre, "rt", encoding = "utf8")
    contenido = archivo.read()
    contenido = contenido.split('\n')
    return contenido

def listar_personas():
    print("\n--- DNI   --   NOMBRE   --   APELLIDO ---\n")
    
    dnis = leerArchivo("dni.txt")
    nombres = leerArchivo("nombre.txt")
    apellidos = leerArchivo("apellido.txt")
    
    for i in range(0, len(dnis)):
        print (f"--- {dnis[i]} -- {nombres[i]} -- {apellidos[i]} \n")
    

def agregar_personas():
    contenido1 = input("Dni: ")
    archivo1 = open("dni.txt","at")
    archivo1.write("\n"+ contenido1)
    
    contenido2 = input("Nombre: ")
    archivo2 = open("nombre.txt","at")
    archivo2.write("\n"+ contenido2)
    
    contenido3 = input("Apellido: ")
    archivo3 = open("apellido.txt","at")
    archivo3.write("\n"+ contenido3)
    
    archivo1.close()
    archivo2.close()
    archivo3.close()

def salir():
    print("Vuelva pronto...")





def menu():
    opcion = 0
    while opcion!=3:
        print("\n\n*************MENU************\n"+
              "1. Listar\n"+
              "2. Agregar \n"+
              "3. Salir\n")
        opcion = int(input("\n Ingrese una opcion: "))
   
        if opcion == 1:
            listar_personas()
            
        if opcion == 2:
            agregar_personas()
            
        if opcion == 3:
            opcion = 3
        if opcion<1 or opcion>3:
            print("opcion incorrecta, intente de nuevo")




userResponse = leerArchivo('login.txt')
passwordResponse = leerArchivo('clave.txt')

bandera = True
contador = 0

while bandera == True:
    usuario = input('\nIngresa el usuario: ')
    clave = input('Ingresa la clave: ')


    
    
    for usuarioItem in userResponse:
        if usuario == usuarioItem:
            for claveoItem in passwordResponse:
                if clave == claveoItem:
                    bandera = False
                    menu()

    


    if bandera == True:
        print('Usuario o contraseña incorrectas \n')
        contador = contador + 1 
        
        if contador == 2: 
            print('\n2 intentos fallidos, se le denegó el acceso')
            bandera = False
    
    print('\n ')