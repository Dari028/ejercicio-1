class Paciente: # se crea la clase paciente
    def __init__(self):   # se inicia el constructor
        self.__nombre = ""  # de la linea 3 a la 6 se definen los atributos de la clase paciente y todos estan privatizados
        self.__cedula = 0
        self.__genero = ""
        self.__servicio = ""
        
    def verNombre(self): #  linea 8-15 se establece el metodo para observar los atributos (nombre,cedula,genero,servicio) de la clase
        return self.__nombre
    def verServicio(self):
        return self.__servicio
    def verGenero(self):
        return self.__genero
    def verCedula(self):
        return self.__cedula
    
    def asignarNombre(self,n): #  linea 17-24 se establece el metodo para asignar los atributos (nombre,cedula,genero,servicio) de la clase
        self.__nombre = n
    def asignarServicio(self,s):
        self.__servicio = s
    def asignarGenero(self,g):
        self.__genero = g
    def asignarCedula(self,c):
        self.__cedula = c

class Sistema: # se crea la clase sistema
    def __init__(self): # se inicializa el constructor
        self.__dict_pacientes_ced = {} #lines 28-29 se crean los diccionarios de caracter privado que albergaran a los pacientes lo que indica que los pacientes componen al sistema
        self.__dict_pacientes_nom = {}
    
   
    def buscar_paciente_ced(self, clave):  #lines 32-36 se verifica si el paciente esta en el diccionari que tiene como clave la cedula mediante un ciclo
        encontrado = False
        if clave in self.__dict_pacientes_ced:
            encontrado = True
        return encontrado

    def buscar_paciente_nom(self, clave): #linea 38-42 se verifica si el paciente esta en el diccionario que tiene como clave el nombre mediante un ciclo 
        encontrado = False
        if clave in self.__dict_pacientes_nom:
            encontrado = True
        return encontrado

    def ingresarPaciente(self,pac):# linea 44-53 se ingresa el paciente a los dos diccionarios con la clave respectiva
        id_ = pac.verCedula()
        name_ = pac.verNombre()

        if id_ in self.__dict_pacientes_ced or name_ in self.__dict_pacientes_nom:
            return False
            
        self.__dict_pacientes_ced[id_] = pac
        self.__dict_pacientes_nom[name_] = pac
        return True


    def verDatosPaciente(self, c): # linea 56-63 se busca la clave (nombre o cedula) en cada diccionario 
        if c  in self.__dict_pacientes_ced:
            return  self.__dict_pacientes_ced[c]
        
        if c  in self.__dict_pacientes_nom:
            return self.__dict_pacientes_nom[c]
        else:
            return None

    def verNumeroPacientes(self): # # linea 65-66 indica el numero de pacientes
        return len(self.__dict_pacientes_ced)
        
def main(): # se crea la funcion main que alvergara las funciones principales del algoritmo
    sis = Sistema() # se crea una instancia de la clase sistema
    while True: # linea 70-117 esta el ciclo
        opcion = int(input("Ingrese 0 para volver al menu, 1 para ingresar nuevo paciente, 2 ver paciente: , 3 - ver cantidad de pacientes, 4 - salir ")) # linea 71 se crea el menu
        if opcion == 1: # linea 72-77 si la opcion es uno se pidira informacion del paciente
            print("A continuacion se solicitaran los siguientes datos:")
            nombre = input("Ingrese el nombre: ")
            cedula = int(input("Ingrese la cedula: "))    
            genero = input("Ingrese el genero: ")
            servicio = input("Ingrese el servicio: ")
            pac = Paciente()  # se crea una instancia de la clase paciente
            pac.asignarNombre(nombre) # linea 79-82 mediante los metodos de asignar se le asignan los datos al objeto paciente 
            pac.asignarCedula(cedula)
            pac.asignarGenero(genero)
            pac.asignarServicio(servicio)
            r = sis.ingresarPaciente(pac) # mediante el metodo de ingresar paciente se guarda el objeto en los diccionarios del sistema

            if r == True:   # linea 85-88 se informa si el proceso fue exitos o no
                print("Paciente ingresado")
            else:
                print("Paciente ya existe en el sistema")

        elif opcion == 2:  ## si la opcion es 2 
            cn = input("Ingrese la cedula o el nombre del paciente a buscar: ") # linea 91-95 se pide la clave del paciente y se verifica el tipo de variable de la clave
            try:
                cn = int(cn)
            except ValueError:
                pass

            if sis.buscar_paciente_ced(cn): # linea 97-102 buscamos al paciente con la cedula y extraemos e imprimimos la informacion del objeto tipo paciente
                p = sis.verDatosPaciente(cn)
                print("Nombre: " + p.verNombre())
                print("Cedula: " + str(p.verCedula()))
                print("Genero: " + p.verGenero())
                print("Servicio: " + p.verServicio())
            elif sis.buscar_paciente_nom(cn):# linea 103-1028 buscamos al paciente con el nombre y extraemos e imprimimos la informacion del objeto tipo paciente
                p = sis.verDatosPaciente(cn)
                print("Nombre: " + p.verNombre())
                print("Cedula: " + str(p.verCedula()))
                print("Genero: " + p.verGenero())
                print("Servicio: " + p.verServicio())
            else: # linea  109-110 en dado caso de que el pacinete no este en el sistema se muestra el mensaje
                print("El paciente no se encontró")
        
        elif opcion == 3: # linea se imprime el numero de pacientes
            print(f"La cantidad de pacientes en el sistema es: {sis.verNumeroPacientes()}")
                    
        
        if opcion==4 : #linea se para el ciclo (cerramos el sistema)
            print(":)")
            break

if __name__ == '__main__': #linea 120-121 verificamos si el script esta siendo ejecutado o es importado
    main()
