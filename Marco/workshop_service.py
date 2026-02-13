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
from Fabio.domain_models import Lavatrice, Frigorifero, Forno
from Utilities.utility import log_func


class Officina:
    def __init__(self, nome: str):
        self.nome = nome
        self.ticket_list = {} #(lista di oggetti TicketRiparazione) uso il dizionario perche migliora l'accesso tramite k
    
        
    def aggiungi_ticket(self, id_ticket: str, elettrodomestico:str): #id_ticket str perche input utente
        if id_ticket in  self.ticket_list.keys():
            print(f"Ticket {self.ticket_list} già esistente ")
            return None
        
        ticket_OBJ = Ticket_system(id_ticket, elettrodomestico )
        
        self.ticket_list[str(ticket_OBJ.get_id())] = ticket_OBJ
        return True

    def chiudi_ticket(self, id_ticket: str):
        if not id_ticket in self.ticket_list.keys():
            print(f"Ticket {self.ticket_list} non esiste")
            return None
        
        ticket_da_chiudere = ""
        
        # for k , v in self.ticket_list.items():
        #     if k == id_ticket:
        #         ticket_da_chiudere = v
        
        # ticket_da_chiudere.cambia_stato("chiuso")
        # return True
        
        ticket = self.ticket_list.get(id_ticket)
        if ticket:
            ticket.cambia_stato("chiuso")
            return True
        print(f"Ticket {id_ticket} non trovato.")
        return False
    
    def stampa_ticket_aperti(self):
        if len(self.ticket_list) == 0:
            print("nessun Ticket Aperto")
            return False
        
        almeno_uno_aperto = False
        
        for k in self.ticket_list.items():
            if k.get_stato() == "aperto":
                almeno_uno_aperto = True
                break
        
        ticket_aperti = [k for k in self.ticket_list.items() if k.get_stato == "aperto"] # Che Eleganza!! AAHAH
        print(ticket_aperti) 
            
    
    def totale_preventivi(self, voci_extra=0):
        if voci_extra.strip():
            voci_extra = voci_extra.split("-")
            list(voci_extra)
            
        if self.ticket_list >= 0:
            print("nessun Ticket Aperto")
            return False
        
        totale = []
    
        for k in self.ticket_list.items():
            totale.append(k.calcola_preventivo(voci_extra))
        
        return sum(totale)
    
    def statistiche_per_tipo(self):
        # contatori
        stats = {"Lavatrice": 0, "Frigorifero": 0, "Forno": 0}
        
        for ticket in self.ticket_list.values():
            el = ticket.get_elettrodomestico()
            
            if isinstance(el, Lavatrice):
                stats["Lavatrice"] += 1
            elif isinstance(el, Frigorifero):
                stats["Frigorifero"] += 1
            elif isinstance(el, Forno):
                stats["Forno"] += 1
        
        # stats = {}
        # for ticket in self.ticket_list.values():
        #     tipo = type(ticket.get_elettrodomestico()).__name__
        #     stats[tipo] = stats.get(tipo, 0) + 1
        
        # Stampa del report 
        print(f"\n--- Report Statistiche Officina {self.nome} ---")
        print(f"Numero di lavatrici in riparazione: {stats['Lavatrice']}")
        print(f"Numero di frigoriferi in riparazione: {stats['Frigorifero']}")
        print(f"Numero di forni in riparazione: {stats['Forno']}")
            
        
        
        
