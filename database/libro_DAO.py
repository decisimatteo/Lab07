from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_libri(self):
        connessione = DBConnect.get_connection()
        if connessione is None:
            return None

        cursore = None
        try:
            cursore = connessione.cursor()
            cursore.execute("SELECT * FROM libro ORDER BY titolo, id")

            libri = []
            for riga in cursore.fetchall():
                libro = Libro(riga[0], riga[1], riga[2], riga[3], riga[4], riga[5])
                libri.append(libro)

            return libri
        finally:
            if cursore is not None:
                cursore.close()
            connessione.close()

    def get_generi(self):
        connessione = DBConnect.get_connection()
        if connessione is None:
            return None

        cursore = None
        try:
            cursore = connessione.cursor()
            # DISTINCT evita di inserire più volte lo stesso genere nel menu
            cursore.execute("SELECT DISTINCT genere FROM libro WHERE genere IS NOT NULL ORDER BY genere")

            generi = []
            for riga in cursore.fetchall():
                generi.append(riga[0])

            return generi
        finally:
            if cursore is not None:
                cursore.close()
            connessione.close()
