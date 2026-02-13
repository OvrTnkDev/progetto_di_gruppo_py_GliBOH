"""FABIO: Il "Domain Master" (File: domain_models.py)
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
    def __init__(self, marca, modello, anno_acquisto, guasto):
        # Attributi privati
        self.__marca = marca
        self.__modello = modello
        self.__anno_acquisto = anno_acquisto
        self.__guasto = guasto
    
    # Getters e Setters Espliciti
    def get_marca(self):
        return self.__marca
    
    def get_modello(self):
        return self.__modello
    
    def get_anno_acquisto(self):
        return self.__anno_acquisto
    
    def set_anno_acquisto(self, anno):
        # controllo
        if anno > 2025: 
            print("Errore: Anno nel futuro non valido")
            return None
        else:
            self.__anno_acquisto = anno

    def get_guasto(self):
        return self.__guasto

    def descrizione(self):
        return f"Marca: {self.__marca}\nModello: {self.__modello}\nAnno: {self.__anno_acquisto}\nGuasto: {self.__guasto}\n"
    
    def stima_costo_base(self):
        return 49.99


# creazione classe Lavatrice
class Lavatrice(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto, capacita_kg, giri_centrifuga):
        # Chiamata al costruttore del padre
        super().__init__(marca, modello, self.set_anno_acquisto(anno_acquisto), guasto)
        self.__capacita_kg = capacita_kg
        self.__giri_centrifuga = giri_centrifuga
    
    # Polimorfismo: Override del metodo base
    def stima_costo_base(self):
        costo = super().stima_costo_base()
        if self.__capacita_kg > 10:
            costo += 19.99
        return costo

# creazione classe Frigorifero
class Frigorifero(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto, litri, ha_freezer):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.__litri = litri
        self.__ha_freezer = ha_freezer
        
        # Polimorfismo: Override del metodo base
    def stima_costo_base(self):
        costo = super().stima_costo_base()
        if self.__ha_freezer:
            costo += 39.99
        return costo

# creazione classe Forno
class Forno(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto, tipo_alimentazione, ha_ventilato):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.__tipo_alimentazione = tipo_alimentazione
        self.__ha_ventilato = ha_ventilato
        
        # Polimorfismo: Override del metodo base
    def stima_costo_base(self):
        costo = super().stima_costo_base()
        if self.__tipo_alimentazione == "gas":
            costo += 49.99
        return costo


"""# prove
l = Lavatrice("Samsung", "EcoBubble", 2020, "Non scarica", 12, 1200)
print(l.descrizione())
print(f"Preventivo base: {l.stima_costo_base()}€")"""