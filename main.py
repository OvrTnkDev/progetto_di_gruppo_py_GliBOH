from unittest import case
import Fabio.domain_models as dm
import Gabriele.ticket_system as ts
import Marco.workshop_service as ws
import time

print("--- AVVIO SISTEMA GESTIONALE 'GliBOH' ---")
# creo l'oggetto dell'officina
officina = ws.Officina("GliBOH")
###############################
while True:
    print("\n" + "="*30) #Fortissimo
    print(f"MENU PRINCIPALE - {officina.nome}")
    print("="*30) #questo  è più HARD
    print("1. Inserisci nuovo Elettrodomestico (Apre Ticket)")
    print("2. Visualizza Ticket Aperti")
    print("3. Calcola Preventivo (Test Metodo Variadico)")
    print("4. Statistiche per Tipo (Test Type/Isinstance)")
    print("5. Chiudi Ticket")
    print("0. Esci")
    
    scelta = input("Seleziona un'opzione: ")
    match scelta:
        case "0":
            print("Uscita in corso... Arrivederci!")
            break
        
        case "1":
            print("\n--- INSERIMENTO NUOVO ELETTRODOMESTICO ---")
            tipo = input("Tipo (Lavatrice/Frigorifero/Forno): ")
            marca = input("Marca: ")
            modello = input("Modello: ")
            anno = int(input("Anno di Acquisto: "))
            if anno > 2025 or anno < 1900:
                print("Errore: Anno non valido. Riprova.")
                continue
            guasto = input("Descrizione del Guasto: ")
            id_ticket = input("ID Ticket: ")
            if tipo.lower() == "lavatrice":
                capacita = float(input("Capacità (kg): "))
                giri = int(input("Giri Centrifuga: "))
                elettrodomestico = dm.Lavatrice(marca, modello, anno, guasto, capacita, giri)
                
            elif tipo.lower() == "frigorifero":
                volume = float(input("Volume (litri): "))
                freez = input("Ha Freezer? (sì/no): ").lower() == "sì"
                elettrodomestico = dm.Frigorifero(marca, modello, anno, guasto, volume, freez)
                
            elif tipo.lower() == "forno":
                potenza = int(input("Potenza (W): "))
                ventilato = input("Ha Ventilazione? (sì/no): ").lower() == "sì"
                elettrodomestico = dm.Forno(marca, modello, anno, guasto, potenza, ventilato)
                
            else:
                print("Tipo non valido.")
                continue
            nuovo_ticket = ts.Ticket_system(id_ticket, elettrodomestico)
            officina.aggiungi_ticket(nuovo_ticket.get_id(), nuovo_ticket.get_elettrodomestico())
            print(f"Ticket {id_ticket} aperto con successo.")
        
        case "2":
            print("\n--- TICKET APERTI ---")
            officina.stampa_ticket_aperti()
        
        case "3":
            print("\n--- CALCOLO PREVENTIVO ---")
            id_ticket = input("ID Ticket: ")
            # Verifico se il ticket esiste
            if id_ticket not in officina.ticket_list:
                print(f"Ticket ID {id_ticket} non trovato.")
                continue
            
            voci_extra = input("Voci Extra (separate da ':'): ")
            
            # Converto la stringa di voci extra in un dizionario
            voci_extra = {k: float(v) for k, v in (item.split(':') for item in voci_extra.split(','))} if voci_extra.strip() else None
            #print(f"Voci Extra: {voci_extra}")
            #time.sleep(4)
            preventivo = officina.totale_preventivi(voci_extra)
            if preventivo is not None:
                print(f"Preventivo Totale: {preventivo:.2f}€")
        
        case "4":
            print("\n--- STATISTICHE PER TIPO ---")
            stats = officina.statistiche_per_tipo()
            print("Numero di Riparazioni per Tipo di Elettrodomestico: ", stats)
            
        case "5":
            print("\n--- CHIUSURA TICKET ---")
            id_ticket = input("ID Ticket da chiudere: ")
            if officina.chiudi_ticket(id_ticket):
                print(f"Ticket {id_ticket} chiuso con successo.")
            else:
                print(f"Impossibile chiudere il Ticket {id_ticket}. Verifica l'ID e riprova.")
        
        case _:
            print("Opzione non valida. Riprova.")
            continue