from model.ticket import Ticket
from controller.ticketController import TicketController

def add_queue(ticket: Ticket, ticketTypes: dict) -> None:
    """
    Add a ticket to the queue, using the TicketController class to manage the queue.
    you need order the tickets by type and priority. (dudas, asesor, caja, otros)
    """

    queue_options = { "duda","caja","asesor","otros"}

    if ticket.type not in queue_options:
        print ( "Tipo de tiquete no valido")
        return
    
    if ticket.type not in ticketTypes:
        ticketTypes[ticket.type] = TicketController()

    ticketTypes[ticket.type].enqueue(ticket)    
    print(f"Ticket de tipo '{ticket.type}' Añadido a la cola")

    #print("Añadir ticket a la cola")
    #turno = input("Turno: ")
    #prioridad = input("Prioridad: ")
    #ticket = Ticket(turno, prioridad)
    #TicketController.enqueue(Ticket)
    #print("Ticket añadido a la cola")