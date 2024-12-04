class Pelicula:
    
    def __init__(self,titulo,genero,duracion,clasificacion):
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion
        self.clasificacion = clasificacion

    def mostrar_detalle(self):
        return print(f"Título: {self.titulo}\nGénero: {self.genero}\nDuración: {self.duracion} min\nClasificacion: {self.clasificacion}")
#############################################################################################
class Sala:
    
    def __init__(self,numero,capacidad,pelicula,reservas):
        self.numero = numero
        self.capacidad = capacidad
        self.pelicula = pelicula
        self.reservas = reservas

    def asignar_pelicula(self,pelicula):
        self.pelicula = pelicula
        
#--------------------------------------------------------------------------------------------
    def mostrar_disponibilidad(self):
        contador_asientos_libres = 0 
        
        for asiento in range(1,self.capacidad+1):
            
            if asiento not in self.reservas:
                contador_asientos_libres = contador_asientos_libres + 1 #conteo de los asientos libres en la sala
                print(f"Asiento {asiento}: Libre")
            else:
                print(f"Asiento {asiento}: (Reservado)")

        print(f"AGOTADOS" if contador_asientos_libres == 0 else f"Disponibilidad: {contador_asientos_libres}")
#--------------------------------------------------------------------------------------------
    def realizar_reserva(self,nombre,asiento):
        self.reservas[asiento] = nombre 
        return print("Reserva realizada")
#--------------------------------------------------------------------------------------------
    def cancelar_reserva(self,asiento):
        del self.reservas[asiento]
        return print("Reserva cancelada")
#--------------------------------------------------------------------------------------------
    def mostrar_reservas(self):
        for asiento,reserva in self.reservas.items():
            print(f"Asiento{asiento} : {reserva}")
#--------------------------------------------------------------------------------------------
class Cine(Sala):
    def __init__(nombre,Sala):
        self.nombre = nombre
