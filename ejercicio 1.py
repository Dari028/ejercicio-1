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
    
   
    def buscar_paciente_ced(self, clave):
        encontrado = False
        if clave in self.__dict_pacientes_ced:
            encontrado = True
        return encontrado

    def buscar_paciente_nom(self, clave):
        encontrado = False
        if clave in self.__dict_pacientes_nom:
            encontrado = True
        return encontrado

    def ingresarPaciente(self,pac):
        id_ = pac.verCedula()
        name_ = pac.verNombre()

        if id_ in self.__dict_pacientes_ced or name_ in self.__dict_pacientes_nom:
            return False
            
        self.__dict_pacientes_ced[id_] = pac
        self.__dict_pacientes_nom[name_] = pac
        return True


    def verDatosPaciente(self, c):
        if c  in self.__dict_pacientes_ced:
            return  self.__dict_pacientes_ced[c]
        
        if c  in self.__dict_pacientes_nom:
            return self.__dict_pacientes_nom[c]
        else:
            return None

    def verNumeroPacientes(self):
        return len(self.__dict_pacientes_ced)
        
def main():
    sis = Sistema()
    while True:
        opcion = int(input("Ingrese 0 para volver al menu, 1 para ingresar nuevo paciente, 2 ver paciente: , 3 - ver cantidad de pacientes, 4 - salir "))
        if opcion == 1:
            print("A continuacion se solicitaran los siguientes datos:")
            nombre = input("Ingrese el nombre: ")
            cedula = int(input("Ingrese la cedula: "))    
            genero = input("Ingrese el genero: ")
            servicio = input("Ingrese el servicio: ")
            pac = Paciente()
            pac.asignarNombre(nombre)
            pac.asignarCedula(cedula)
            pac.asignarGenero(genero)
            pac.asignarServicio(servicio)
            r = sis.ingresarPaciente(pac)

            if r == True:
                print("Paciente ingresado")
            else:
                print("Paciente ya existe en el sistema")

        elif opcion == 2:
            cn = input("Ingrese la cedula o el nombre del paciente a buscar: ")
            try:
                cn = int(cn)
            except ValueError:
                pass

            if sis.buscar_paciente_ced(cn):
                p = sis.verDatosPaciente(cn)
                print("Nombre: " + p.verNombre())
                print("Cedula: " + str(p.verCedula()))
                print("Genero: " + p.verGenero())
                print("Servicio: " + p.verServicio())
            elif sis.buscar_paciente_nom(cn):
                p = sis.verDatosPaciente(cn)
                print("Nombre: " + p.verNombre())
                print("Cedula: " + str(p.verCedula()))
                print("Genero: " + p.verGenero())
                print("Servicio: " + p.verServicio())
            else:
                print("El paciente no se encontró")
        
        elif opcion == 3:
            print(f"La cantidad de pacientes en el sistema es: {sis.verNumeroPacientes()}")
                    
        
        if opcion==4 :
            break

if __name__ == '__main__':
    main()