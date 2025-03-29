from typing import Union
from fastapi import FastAPI
from model import Ticket
from controller import TicketController
from functions import add_queue

app = FastAPI()

#Se crea los tipos de datos de TicketController para cada tipo de ticket"
ticketTypes = {
    "dudas": TicketController(),
    "asesor": TicketController(),
    "caja": TicketController(),
    "otros": TicketController()
}

# Endpoint para crear un turno

@app.post("/ticketCreate")
def crear_turno(turno: Ticket):

    # Aquí podrías agregar la lógica para guardar el turno en una base de datos---------------
    if turno.service_type not in ticketTypes:
        return{"error":"Ticket no valido"}

    #add_queue(turno, ticketTypes) CORREGIDO
    #return {"mensaje": "Turno creado correctamente", "datos_turno": turno}

    # Asignar prioridad de tickets por edad
    if turno.age > 60 and not turno.priority_attention:
        turno.priority_attention = True

    add_queue(turno, ticketTypes)
    return {"mensaje": "Turno creado correctamente", "datos_turno": turno}

# Endpoint para obtener el siguiente turno
@app.get("/ticketNext")
def obtener_siguiente_turno(tipo: str):
    if tipo not in ticketTypes:
        return {"error": "Tipo de ticket no valido"}
    #Si el tipo de tiquetes escogido no esta dentro de "ticketTypes, no lo valida"

    next_ticket=ticketTypes[tipo].dequeue()
    if next_ticket is None:
        return {"mensaje":"No hay turnos en la cola"}
    #Si el "tipo" de tickets en valido y está vacio, entonces no hay turnos pendientes

    return {"mensaje": "El siguiente turno es", "datos_turno": next_ticket}

# Endpoint para listar los turnos en cola por el tipo de turno
@app.get("/ticketList")
def listar_turnos_cola(tipo: str):
    
    if tipo not in ticketTypes:
        return {"error": "Tipo de ticket no válido"}

    turnos = []
    current = ticketTypes[tipo].head
    while current:
        turnos.append({
            "turno": current.data.name,
            "prioridad": current.priority
        })
        current = current.next

    return {"mensaje": "Lista de turnos en cola", "datos_turnos": ""}

# Otros endpoints existentes
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
