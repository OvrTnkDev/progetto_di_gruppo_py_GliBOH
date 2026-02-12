'''GAB: Il "Transaction Manager" (File: ticket_system.py)
Responsabilità: Gestire l'oggetto che collega il lavoro al prodotto. Dipendenze: Deve importare da Dev 1. from domain_models import Elettrodomestico

Task: Devi implementare la Classe TicketRiparazione.

Attributi: id, stato, note (lista), e un oggetto elettrodomestico (che ti arriva dal costruttore).

Metodo Variadico (Cruciale):

Firma: calcola_preventivo(self, voci_extra)

Logica: Recupera il costo base dall'oggetto elettrodomestico (self.__elettrodomestico.stima_costo_base()) e sommalo alla somma divoci_extra.

Metodi di gestione: Aggiungi nota, cambio stato.

Output atteso: La classe che gestisce la singola riparazione, capace di accettare un numero variabile di costi extra.'''




class Ticket_system():
    def __init__(self, id_ticket:int, elettrodomestico:str):
        
        self.__id_ticket = id_ticket
        self.__elettrodomestico = elettrodomestico  # Dipendenza da classe Elettrodomestico
        self.__stato = "aperto"
        self.__note = []
        
        
  #Metodi di gestione: Aggiungi nota, cambio stato.      
    def aggiungi_nota(self, testo):
        """Aggiunge una nota descrittiva alla lista delle lavorazioni."""
        if testo:
            self.__note.append(testo)
            
            
    def cambia_stato(self, nuovo_stato):
        
        stati_validi = ["aperto", "in lavorazione", "chiuso"]
        if nuovo_stato.lower() in stati_validi:
            self.__stato = nuovo_stato.lower()
        else:
            print(f"Stato '{nuovo_stato}' non valido.")
        
        
    
    
    
    
    
    
    
    
    
#get set
    def get_id(self):
        return self.__id_ticket

    def get_stato(self):
        return self.__stato

    def get_elettrodomestico(self):
        return self.__elettrodomestico    