import csv
from cabina import Cabina, CabinaAnimali, CabinaDeluxe
from passeggero import Passeggero


class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self._nome = nome
        self._lista_cabine = []
        self._lista_passeggeri = []

    """Aggiungere setter e getter se necessari"""
    # TODO
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        # TODO
        try:
            with open(file_path,'r') as csv_file:
                reader = csv.reader(csv_file)
                for riga in reader:
                    if len(riga) > 3:
                        if len(riga) == 4:
                            id_cabina, n_letti, ponte, prezzo_base = riga
                            cabina = Cabina(id_cabina, n_letti, ponte, prezzo_base)
                            self._lista_cabine.append(cabina)
                        elif riga[4].isdigit():
                            id_cabina, n_letti, ponte, prezzo_base, animali = riga
                            cabina = CabinaAnimali(id_cabina, n_letti, ponte, prezzo_base, animali)
                            self._lista_cabine.append(cabina)
                        else:
                            id_cabina, n_letti, ponte, prezzo_base, stile = riga
                            cabina = CabinaDeluxe(id_cabina, n_letti, ponte, prezzo_base, stile)
                            self._lista_cabine.append(cabina)
                    else:
                        id_passeggerio, nome, cognome = riga
                        passeggero = Passeggero(id_passeggerio, nome, cognome)
                        self._lista_passeggeri.append(passeggero)
            for c in self._lista_cabine:
                print(c)
            for p in self._lista_passeggeri:
                print(p)
        except FileNotFoundError:
            raise FileNotFoundError("File non trovato")

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO
        passeggero = None
        for p in self._lista_passeggeri:
            if p.id_passeggero == codice_passeggero:
                passeggero = p
                break
        if passeggero == None:
            raise Exception(f"passeggero non trovato")
        cabina = None
        for c in self._lista_cabine:
            if c.id_cabina == codice_cabina:
                cabina = c
                break
        if cabina == None:
            raise Exception(f"cabina non trovata")
        if cabina.disponibile == False:
            raise Exception(f"{cabina} non disponibile")
        if passeggero.cabina_assegnata != None:
            raise Exception(f"{passeggero} è già assegnato alla {passeggero.cabina_assegnata}")

        passeggero.cabina_assegnata = cabina
        try:
            cabina.add_passeggero(passeggero)
        except Exception as e:
            print(e)

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO
        return sorted(self._lista_cabine)


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO
        for p in self._lista_passeggeri:
            print(f"{p} {p.cabina_assegnata}")