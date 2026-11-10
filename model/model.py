from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        libri = self._libro_dao.get_libri()
        if libri is None:
            return None

        libri_filtrati = []
        for libro in libri:
            # Se il filtro è None non escludo nessun libro per quella scelta
            if biblioteca is not None and str(libro.id_biblioteca) != biblioteca:
                continue
            if genere is not None and libro.genere != genere:
                continue

            libri_filtrati.append(libro)

        return libri_filtrati

    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        return self._libro_dao.get_generi()

    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        return self._biblioteca_dao.get_biblioteche()
