# Task: Devi implementare la Classe Officina.

# Gestione Lista: Una lista self.tickets per contenere gli oggetti creati da Dev 2.

# CRUD base: aggiungi_ticket(ticket), chiudi_ticket(id).

# Metodo statistiche_per_tipo(self) (Il requisito del type):

# Itera sulla lista dei ticket.

# Estrai l'elettrodomestico da ogni ticket.

# Usa type(obj) is Lavatrice (o isinstance) per incrementare dei contatori separati.

# Stampa il report finale.

# Metodo totale_preventivi: Chiama i preventivi di tutti i ticket e fai la somma totale.

# Output atteso: La classe che governa l'intero processo e genera le statistiche.

from Gabriele.ticket_system import Ticket_system
# from domain_models import Lavatrice, Frigorifero, Forno
class Officina:
    def __init__(self, nome: str):
        self.nome = nome
        self.ticket_list = {} #(lista di oggetti TicketRiparazione) uso il dizionario perche migliora l'accesso tramite k
        
    # aggiungi_ticket(self, ticket)
    # chiudi_ticket(self, id_ticket)
    # stampa_ticket_aperti(self): mostra ID, tipo di elettrodomestico e stato.
    # totale_preventivi(self): somma i preventivi di tutti i ticket. 
    
        
    def aggiungi_ticket(self, id_ticket: str, elettrodomestico:str): #id_ticket str perche input utente
        if id_ticket in  self.ticket_list.keys:
            print(f"Ticket {self.ticket_list} già esistente ")
            return None
        
        ticket_OBJ = Ticket_system(id_ticket, elettrodomestico )
        
        self.ticket_list[str(ticket_OBJ.id_ticket)] = ticket_OBJ
        return True

    def chiudi_ticket(self, id_ticket: str):
        if not id_ticket in self.ticket_list.keys:
            print(f"Ticket {self.ticket_list} non esiste")
            return None
        
        ticket_da_chiudere = ""
        
        for k , v in self.ticket_list.items():
            if k == id_ticket:
                ticket_da_chiudere = v
        
        ticket_da_chiudere.cambia_stato("chiuso")
        return True
            
    
    def stampa_ticket_aperti(self):
        if self.ticket_list >= 0:
            print("nessun Ticket Aperto") # TODO: check se almeno un ticket aperto in dict
            return False
        
        ticket_aperti = [k for k in self.ticket_list.items() if k.get_stato == "aperto"] # Che Eleganza!! AAHAH
        print(ticket_aperti) 
            
    
    def totale_preventivi(self, voci_extra: list): #TODO : controllare e capire cazzo fa voci_extra
        if self.ticket_list >= 0:
            print("nessun Ticket Aperto")
            return False
        
        totale = []
    
        for k in self.ticket_list.items():
            totale.append(k.calcola_preventivo(voci_extra))
        
        return sum(totale)
            
        
        
        
    
        
        