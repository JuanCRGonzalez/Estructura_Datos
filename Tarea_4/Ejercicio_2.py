class TareaEstudiante:
    def __init__(self, descripcion_tarea, prioridad_tarea, fecha_vencimiento_tarea):
        self.descripcion_tarea = descripcion_tarea
        self.prioridad_tarea = prioridad_tarea
        self.fecha_vencimiento_tarea = fecha_vencimiento_tarea
    
    def __str__(self):
        return f"Descripción: {self.descripcion_tarea}, Prioridad: {self.prioridad_tarea}, Fecha de Vencimiento: {self.fecha_vencimiento_tarea}"
    
    def tarea_completada(self):
        try:
            return self.completado  
        except AttributeError:
            return False

    def completar_tarea(self):
        self.completado = True


class Nodo:
    def __init__(self, tarea):
        self.tarea = tarea
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_tarea(self, tarea):
        nuevo_nodo = Nodo(tarea)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo

    def eliminar_tarea(self, descripcion=None, posicion=None):
        if descripcion:
            nodo_actual = self.cabeza
            previo = None
            while nodo_actual:
                if nodo_actual.tarea.descripcion == descripcion:
                    if previo:
                        previo.siguiente = nodo_actual.siguiente
                    else:
                        self.cabeza = nodo_actual.siguiente
                    print(f"Tarea eliminada: {nodo_actual.tarea}")
                    return
                previo = nodo_actual
                nodo_actual = nodo_actual.siguiente
            print("No se encontró la tarea con esa descripción.")
        elif posicion is not None:
            nodo_actual = self.cabeza
            previo = None
            contador = 0
            while nodo_actual:
                if contador == posicion:
                    if previo:
                        previo.siguiente = nodo_actual.siguiente
                    else:
                        self.cabeza = nodo_actual.siguiente
                    print(f"Tarea eliminada en la posición {posicion}: {nodo_actual.tarea}")
                    return
                previo = nodo_actual
                nodo_actual = nodo_actual.siguiente
                contador += 1
            print("No se encontró una tarea en esa posición.")

    def mostrar_tareas(self):
        # Mostrar todas las tareas
        nodo_actual = self.cabeza
        if nodo_actual is None:
            print("No hay tareas para mostrar.")
            return
        
        while nodo_actual:
            print(nodo_actual.tarea)
            nodo_actual = nodo_actual.siguiente

    def buscar_tarea(self, descripcion):
        nodo_actual = self.cabeza
        while nodo_actual:
            if nodo_actual.tarea.descripcion == descripcion:
                print(f"Tarea encontrada: {nodo_actual.tarea}")
                return
            nodo_actual = nodo_actual.siguiente
        print("Tarea no encontrada.")

    def completar_tarea(self, descripcion):
        nodo_actual = self.cabeza
        while nodo_actual:
            if nodo_actual.tarea.descripcion == descripcion:
                nodo_actual.tarea.completar_tarea()
                self.eliminar_tarea(descripcion=descripcion)
                print(f"Tarea completada y eliminada: {nodo_actual.tarea}")
                return
            nodo_actual = nodo_actual.siguiente
        print("No se encontró la tarea para completar.")



lista_tareas = ListaEnlazada()

tarea1 = TareaEstudiante("Tarea urgente", 1, "2025-03-20")

lista_tareas.agregar_tarea(tarea1)

print("Tareas antes de ordenar y mostrar:")
lista_tareas.mostrar_tareas()