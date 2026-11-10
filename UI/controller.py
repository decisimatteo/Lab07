import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def popola_dropdown(self):
        try:
            biblioteche = self._model.get_biblioteche()
            generi = self._model.get_generi()
        except Exception as errore:
            self._view.show_alert(f"Errore durante il caricamento dei filtri: {errore}")
            self._view.update()
            return

        if biblioteche is None or generi is None:
            self._view.show_alert("Connessione non riuscita. Controlla MySQL e il database biblioteche_torino.")
            self._view.update()
            return

        self._view.dropdown_biblioteca.options.clear()
        self._view.dropdown_biblioteca.options.append(ft.dropdown.Option("Nessun filtro"))
        for biblioteca in biblioteche:
            # Mostro il nome, ma salvo l'id per distinguere le biblioteche
            self._view.dropdown_biblioteca.options.append(
                ft.dropdown.Option(key=str(biblioteca.id), text=biblioteca.nome)
            )

        self._view.dropdown_genere.options.clear()
        self._view.dropdown_genere.options.append(ft.dropdown.Option("Nessun filtro"))
        for genere in generi:
            self._view.dropdown_genere.options.append(ft.dropdown.Option(genere))

        self._view.dropdown_biblioteca.value = "Nessun filtro"
        self._view.dropdown_genere.value = "Nessun filtro"
        self.biblioteca_selezionata = None
        self.genere_selezionato = None
        self._view.update()

    # CALLBACKS DROPDOWN
    def seleziona_biblioteca(self, e):
        scelta = self._view.dropdown_biblioteca.value
        if scelta == "Nessun filtro":
            self.biblioteca_selezionata = None
        else:
            self.biblioteca_selezionata = scelta

    def seleziona_genere(self, e):
        scelta = self._view.dropdown_genere.value
        if scelta == "Nessun filtro":
            self.genere_selezionato = None
        else:
            self.genere_selezionato = scelta

    # AZIONE: MOSTRA LIBRI
    def mostra_libri(self, e):
        # Svuoto i risultati precedenti prima di eseguire una nuova ricerca
        self._view.lista_libri.controls.clear()

        try:
            libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)
        except Exception as errore:
            self._view.show_alert(f"Errore durante la lettura dei libri: {errore}")
            self._view.update()
            return

        if libri is None:
            self._view.show_alert("Connessione non riuscita. Controlla MySQL e il database biblioteche_torino.")
        elif len(libri) == 0:
            self._view.show_alert("Nessun libro trovato con i filtri selezionati.")
        else:
            for libro in libri:
                self._view.lista_libri.controls.append(ft.Text(str(libro)))

        self._view.update()
