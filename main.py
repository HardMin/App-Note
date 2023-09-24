from tkinter import ttk
import tkinter as tk
from createNote import createNote

from infoNote import windowInfoNote
# Esto se quita y sera reemplazado por la base de dato
store = [
    ('Holacj', 'asdaf', '123', ''),
    ('La bda', 'Easdl', '123', ''),
    ('La boda', 'Elasd', '123', ''),
    ('La boasdda', 'asdEl', '123', ''),
    ('La basdoda', 'Easdl', '123', ''),
    ('La boda', 'El', '123asd', ''),
    ('La asdboda', 'El', '123asd', ''),
    ('Laasd boda', 'El', 'asd123', ''),
    ('La boda', 'El', '1asd23', ''),
    ('asdLa boda', 'El', '12asd3', ''),
    ('La basdoda', 'El', '12asd3', ''),
]

class App():
    def __init__(self):
        self.raiz = tk.Tk()
        self.raiz.title('App Note')
        self.raiz.geometry('800x300')
        self.raiz.grid_propagate(False)

        self.Table()
        self.button = ttk.Button(self.raiz, text='Nueva nota', command=lambda: createNote(self.refreshTable, store))
        self.button.pack()
        self.raiz.mainloop()

    # Interfaz de la tabla
    def Table(self):
        self.table = ttk.Treeview(self.raiz)
        scroll_table = ttk.Scrollbar(orient='vertical', command=self.table.yview)
        self.table.configure(yscrollcommand=scroll_table.set)

        self.table['columns'] = ('id', 'title', 'description', 'date_create', 'date_modify')

        self.table.column('#0', width=0,  stretch=False)
        self.table.column('id', width=5, anchor='center')
        self.table.column('title', width=90, anchor='center')
        self.table.column('description', width=90, anchor='center')
        self.table.column('date_create', width=90, anchor='center')
        self.table.column('date_modify', width=90, anchor='center')

        self.table.heading('#0', text='', anchor='center')
        self.table.heading('id', text='id', anchor='center')
        self.table.heading('title', text='Titulo', anchor='center')
        self.table.heading('description', text='Descripción', anchor='center')
        self.table.heading('date_create', text='Fecha Creación', anchor='center')
        self.table.heading('date_modify', text='Fecha Modificación', anchor='center')

        self.table.bind('<<TreeviewSelect>>', self.getNoteFocus)

        self.load()

    # Captura la nota que se hizo click
    def getNoteFocus(self, event): # obtener nota al hacerle click
        for selection_item in self.table.selection():
            item = self.table.item(selection_item)
            value = item['values']
            windowInfoNote(value, self.refreshTable, store)

    # Cargar tabla
    def load(self):
        # Empaquetar tabla
        self.table.pack(fill='both', expand=1)

        # Genera cada nota en la lista
        for id, value in enumerate(store):
            item = (id+1, value[0], value[1], value[2], value[3])
            self.table.insert(parent='', index='end', iid=item[0], text='', values=item)

    # Refresca la tabla
    def refreshTable(self):
        self.table.delete(*self.table.get_children())
        self.load()


App()
