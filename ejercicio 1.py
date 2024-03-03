class Paciente:
    def __init__(self):
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""
        self.__servicio = ""
        
    def verNombre(self):
        return self.__nombre
    def verServicio(self):
        return self.__servicio
    def verGenero(self):
        return self.__genero
    def verCedula(self):
        return self.__cedula
    
    def asignarNombre(self,n):
        self.__nombre = n
    def asignarServicio(self,s):
        self.__servicio = s
    def asignarGenero(self,g):
        self.__genero = g
    def asignarCedula(self,c):
        self.__cedula = c

class Sistema:
    def __init__(self):
        self.__dict_pacientes_ced = {}
        self.__dict_pacientes_nom = {}
        self.__NumeroPacientes=len(self.__dict_pacientes_nom)
         
    def buscar_paciente_ced(self, c):
        
        if c in self.__dict_pacientes_ced:
            return True
        else:  
            return False
    def buscar_paciente_nom(self, c):
        
        if c in self.__dict_pacientes_nom:
            return True
        else:  
            return False

    


    def ingresarPaciente(self,pac):
       
        id_ = pac.verCedula()
        name_ = pac.verNombre()

        if id_ in self.__dict_pacientes_ced:
            return False
        elif name_ in self.__dict_pacientes_nom:
            return False
            
        self.__dict_pacientes_ced[id_] = pac
        self.__dict_pacientes_nom[name_] = pac
        return True


    
    def verDatosPaciente(self, c):
        if c in self.__dict_pacientes_ced:
            return self.__dict_pacientes_ced[c]
        elif c in self.__dict_pacientes_nom:
            return self.__dict_pacientes_nom[c]
        else:
            return None


    def verNumeroPacientes(self):
        # print("Enel sistema hay: " + str(len(self.__lista_pacientes)) + " pacientes")
        return self.__NumeroPacientes
    def imprimir_diccionarios(self):
        print("Diccionario de pacientes por cedula:")
        print(self.__dict_pacientes_ced)
        print("Diccionario de pacientes por nombre:")
        print(self.__dict_pacientes_nom)
sis = Sistema()
sis1 = Sistema()
sis2 = Sistema()
def main():
    
    while True:
        print(sis2.imprimir_diccionarios())
        opcion = int(input("Ingrese 0 para volver al menu, 1 para ingresar nuevo paciente, 2 ver paciente: , 3 - ver cantidad de pacientes "))
        if opcion == 1:
            print("A continuacion se solicitaran los seguientes datos:")
            # 1 Se solicitaran los datos
            nombre = input("Ingrese el nombre: ")
            cedula = int(input("Ingrese la cedula: "))    
            genero = input("Ingrese el genero: ")
            servicio = input("Ingrese el servicio: ")
            # 2 se crea un objeto Paciente
            pac = Paciente()
            # como es paciente esta vacio debo ingresarle la informacion
            pac.asignarNombre(nombre)
            pac.asignarCedula(cedula)
            pac.asignarGenero(genero)
            pac.asignarServicio(servicio)
            r = sis2.ingresarPaciente(pac)
            # 3 se almacena en el diccionario que esta dentro de la clase sistema

            if r == True:
                print("paciente ingresado")
                print(sis2.imprimir_diccionarios())
            else:
                print("paciente ya existe en el sistema")

        elif opcion == 2:
        
            cn = input("Ingrese la cedula o el nombre del paciente a buscar: ")
            if sis2.buscar_paciente_ced(cn)==True:
                p = sis2.verDatosPaciente(cn)
                print("Nombre: " + p.verNombre())
                print("Cedula: " + str(p.verCedula()))
                print("Genero: " + p.verGenero())
                print("Servicio: " + p.verServicio())
            elif sis2.buscar_paciente_nom(cn)== True:
                p = sis2.verDatosPaciente(cn)
                print("Nombre: " + p.verNombre())
                print("Cedula: " + str(p.verCedula()))
                print("Genero: " + p.verGenero())
                print("Servicio: " + p.verServicio())
            else:
                print("El paciente no se encontró")
                print(cn)
                print(sis.buscar_paciente_nom(cn))
                print(sis.buscar_paciente_ced(cn))
        
        elif opcion == 3:
            print(f"la cantidad de pacientes en el sistema es: {sis.verNumeroPacientes()}")
                    
        elif opcion != 0:
            continue
        else:
            break

if __name__ == '__main__':
    main()
    
