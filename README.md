<div align="center">
  <img src="./Fabio/imm.png" width="100%" alt="D" />
</div>

# 🔧 Progetto Gestionale Officina "GliBOH"

Software gestionale modulare in Python per un'officina di riparazione elettrodomestici. Il progetto implementa i paradigmi fondamentali della Programmazione Orientata agli Oggetti (OOP).

## 📋 Obiettivi Didattici
Il progetto dimostra l'applicazione pratica di:
* **Incapsulamento**: Uso di attributi privati (`__attr`) e getter/setter.
* **Ereditarietà**: Gerarchia di classi (Elettrodomestico -> Lavatrice, Frigorifero, Forno).
* **Polimorfismo**: Override del metodo `stima_costo_base()` nelle sottoclassi.
* **Introspection**: Uso di `type()` o `isinstance()` per la reportistica.
* **Metodi Variadici**: Gestione di argomenti variabili (`*args`) per il calcolo dei preventivi.

---

## 📂 Architettura dei File
**ATTENZIONE**: Rispettare rigorosamente i nomi dei file qui sotto per garantire il funzionamento degli `import` tra i moduli.

| File | Ruolo | Dipendenze |
| :--- | :--- | :--- |
| `domain_models.py` | Definisce le entità fisiche (Prodotti). | *Nessuna* |
| `ticket_system.py` | Gestisce la logica del ticket di riparazione. | Importa da `domain_models` |
| `workshop_service.py` | Gestisce l'officina e le statistiche. | Importa da `ticket_system` e `domain_models` |
| `main.py` | Entry point per l'esecuzione e l'integrazione. | Importa tutto |

---

## 👥 Divisione Compiti (Team DEV)

### 📦 DEV Fabio: Domain Master
**File di lavoro:** `domain_models.py`
**Obiettivo:** Creare la gerarchia delle classi prodotto (Entity Layer).

* [ ] **Classe Base `Elettrodomestico`**
    * Attributi privati: `__marca`, `__modello`, `__anno_acquisto`, `__guasto`.
    * Metodi: Getter/Setter per tutti gli attributi.
    * Metodo `stima_costo_base(self)`: deve ritornare un valore `float` (es. 50.0), **NON** una stringa.
* [ ] **Sottoclassi (Lavatrice, Frigorifero, Forno)**
    * Tutte devono usare `super().__init__(...)`.
    * **Lavatrice**: Attributi `capacita_kg`, `giri_centrifuga`. Override costo (+20€ se >10kg).
    * **Frigorifero**: Attributi `litri`, `ha_freezer`. Override costo (+30€ se ha freezer).
    * **Forno**: Attributi `tipo_alimentazione`, `ha_ventilato`. Override costo (+15€ se a gas).

### 🎫 DEV Gabriele: Transaction Manager
**File di lavoro:** `ticket_system.py`
**Obiettivo:** Logica di business del singolo intervento.

* [ ] **Import**: `from domain_models import Elettrodomestico`
* [ ] **Classe `TicketRiparazione`**
    * Attributi privati: `__id_ticket`, `__elettrodomestico` (oggetto), `__stato`, `__note` (lista).
    * Metodi: `aggiungi_nota(testo)`, getter/setter per stato.
    * **Metodo Variadico**: `calcola_preventivo(self, *voci_extra)`
        * Logica: Chiama `self.__elettrodomestico.stima_costo_base()` + la somma di `*voci_extra`.
        * Return: Un valore `float`.

### 🏭 DEV Marco: Operations Manager
**File di lavoro:** `workshop_service.py`
**Obiettivo:** Gestione globale e Reporting.

* [ ] **Import**: `from ticket_system import TicketRiparazione` e classi da `domain_models`.
* [ ] **Classe `Officina`**
    * Attributi: `nome`, `tickets` (lista vuota inizialmente).
    * Metodi: `aggiungi_ticket(ticket)`, `chiudi_ticket(id)`.
    * Report: `stampa_ticket_aperti()`, `totale_preventivi()`.
    * **Statistiche per Tipo**: `statistiche_per_tipo(self)`
        * Logica: Itera sui ticket.
        * Usa `isinstance(ticket.get_elettrodomestico(), Lavatrice)` (o `type()`) per contare quanti oggetti di ogni tipo sono in riparazione.
        * Stampa il conteggio finale.

### 🚀 TEAM: Integration (Tutti insieme)
**File di lavoro:** `main.py`
**Obiettivo:** Testare il flusso completo.

1.  Istanziare 1 Lavatrice, 1 Frigo, 1 Forno.
2.  Creare l'Officina.
3.  Creare 3 Ticket e aggiungerli all'officina.
4.  Testare `calcola_preventivo(10, 20, 5)` con argomenti variabili.
5.  Lanciare `statistiche_per_tipo()` e verificare l'output.

---

## ⚠️ Linee Guida (Team Leader Rules)
1.  **Return Types**: I metodi di calcolo devono ritornare numeri, non stringhe. La formattazione valuta ("€") si fa solo nel `print` finale.
2.  **Incapsulamento**: Mai accedere a `obj.variabile`. Usare sempre `obj.get_variabile()`.
3.  **Pulizia**: Commentare il codice dove la logica non è immediata.
4.  **Naming**: Classi in `PascalCase` (es. `TicketRiparazione`), metodi e variabili in `snake_case` (es. `calcola_preventivo`).