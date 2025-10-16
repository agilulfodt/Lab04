import csv

from cabina import Cabina, CabinaAnimali


class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self._nome = nome
        self._lista_cabine = []

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
                        else:
                            if riga[5].isdigit():
                                id_cabina, n_letti, ponte, prezzo_base, animali = riga
                                cabina = CabinaAnimali(id_cabina, n_letti, ponte, prezzo_base, animali)
                                self._lista_cabine.append(cabina)
                                # todo
        except FileNotFoundError:
            raise FileNotFoundError("File non trovato")

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO

