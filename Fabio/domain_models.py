"""📦 FABIO: Il "Domain Master" (File: domain_models.py)
Responsabilità:
Definire le entità fisiche. Non deve importare nulla. È la base del sistema.
Task:
Devi implementare la gerarchia degli elettrodomestici.
Classe Base Elettrodomestico:
Attributi rigorosamente privati (marca, modello, ecc.).
getters e setters per tutto.
Metodo stima_costo_base(self) (ritorna un fisso, es. 30€).
Sottoclassi (Lavatrice, Frigorifero, Forno):
Usa super().init nel costruttore.
Override di stima_costo_base(self) implementando la logica condizionale (es. se la lavatrice ha >10kg, costa di più).
Output atteso: Un file pulito con solo le classi dei prodotti."""

# creazione classe base
class Elettrodomestico():
    
    # costruttore
    def __init__(self, marca, modello, anno_acquisto, guasto, costo_base_diagnosi = 50):
        self.__marca = marca
        self.__modello = modello
        self.__anno_acquisto = anno_acquisto
        self.__guasto = guasto
        self.__costo_base_diagnosi = costo_base_diagnosi
    
    def getter(self, tipo):
        tipo = tipo.lower()
        
        if tipo == "mc":
            return self.__marca
        elif tipo == "mo":
            return self.__modello
        elif tipo == "aa":
            return self.__anno_acquisto
        elif tipo == "gs":
            return self.__guasto
        elif tipo == "cbd":
            return self.__costo_base_diagnosi
        else:
            print("Errore di richiesta!")
    
    def descrizione(self):
        return f"marca: {self.__marca}\nmodello: {self.__modello}\nanno_acquisto: {self.__anno_acquisto}\nguasto: {self.__guasto}"
    
    def stima_costo_base(self):
        return f"\ncosto base riparazione: {self.getter("cbd")}"


# creazione classe Lavatrice
class Lavatrice(Elettrodomestico):
    pass

# creazione classe Frigorifero
class Frigorifero(Elettrodomestico):
    pass

# creazione classe Forno
class Forno(Elettrodomestico):
    pass


# prove
ele = Elettrodomestico("samsung", "sess1234", 1998, "rotore")
print(ele.descrizione())
print(ele.stima_costo_base())