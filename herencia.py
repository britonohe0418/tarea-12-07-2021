class Persona:
    _siguiente = 0

    def __init__(self, nombre='Invitado', activo=True):
        self._codigo = self.siguiente()
        self.__nombre = self.__nombre_mayuscula(nombre)
        self.activo = activo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nom):
        self.__nombre = nom

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, cod):
        self._codigo = cod

    def siguiente(self):
        Persona._siguiente = Persona._siguiente+1
        return Persona._siguiente

    def __nombre_mayuscula(self, nombre):
        return nombre.upper()
    
    def mostrar_datos(self):
        return 'Código: {} - Nombre: {} - Activo: {}'.format(self.codigo, self.nombre, self.activo)


class Empleado(Persona):
    def __init__(self, nom='Invitado', act=True, sal=400):
        Persona.__init__(self, nom, act)
        self.salario = sal
    
    def mostrar_datos(self):
        return Persona.mostrar_datos(self) + ' - Sueldo: ' + str(self.salario)


p1 = Persona()
print(p1.mostrar_datos())
p2 = Persona('Daniel', False)
print(p2.mostrar_datos())
print(Empleado().mostrar_datos())