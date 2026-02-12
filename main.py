import Fabio.domain_models as dm
import Gabriele.ticket_system as ts
import Marco.workshop_service as ws

print("--- AVVIO SISTEMA GESTIONALE 'GliBOH' ---")
# creo l'oggetto dell'officina
###############################
while True:
    print("\n" + "="*30) #Fortissimo
    print(f"MENU PRINCIPALE") #- {officina.nome}
    print("="*30) #questo  è più HARD
    print("1. Inserisci nuovo Elettrodomestico (Apre Ticket)")
    print("2. Visualizza Ticket Aperti")
    print("3. Calcola Preventivo (Test Metodo Variadico)")
    print("4. Statistiche per Tipo (Test Type/Isinstance)")
    print("5. Chiudi Ticket")
    print("0. Esci")
    break