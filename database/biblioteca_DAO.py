from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_biblioteche(self):
        connessione = DBConnect.get_connection()
        if connessione is None:
            return None

        cursore = None
        try:
            cursore = connessione.cursor()
            cursore.execute("SELECT * FROM biblioteca ORDER BY nome")

            biblioteche = []
            for riga in cursore.fetchall():
                biblioteca = Biblioteca(riga[0], riga[1], riga[2])
                biblioteche.append(biblioteca)

            return biblioteche
        finally:
            if cursore is not None:
                cursore.close()
            # Con close() restituisco la connessione al pool per poterla usare di nuovo
            connessione.close()
