import tkinter as tk
from tkinter import ttk
from datetime import datetime

# Crea la nueva nota
def createNote(refreshTable, store):

    # Levanta una nueva ventana encima de la raiz
    window = tk.Toplevel()
    window.title('Información de la nota')

    # Capturar el valor del entry o entrada de datos
    value_title = tk.StringVar()
    value_description = tk.StringVar()

    # Guardar los cambios
    def save():
        # Obtener la fecha actual
        date = datetime.now()
        # Creando nueva tupla para la nueva nota
        newNote = (
            value_title.get(), 
            value_description.get(), 
            f'{date.day}/{date.month}/{date.year}',
            ''
        )
        # ++++++++++++++ Aqui tienes que agregar la funcionalidad para crear una nueva nota +++++++++++++++
        # Llama la funcion del modulo o archivo store.py que pueda crear la nota
        store.append(newNote)

        # Esto cierra la ventana
        window.destroy()
        # Refrescar nota
        refreshTable()

    ttk.Label(window, text='Titulo').grid(column=0, row=0)
    entry_title = ttk.Entry(window, textvariable=value_title)
    entry_title.grid(column=1, row=0)

    ttk.Label(window, text='Descripción').grid(column=0, row=1)
    entry_description = ttk.Entry(window, textvariable=value_description)
    entry_description.grid(column=1, row=1)

    ttk.Button(window, text='Guardar', command=save).grid(column=1, row=2)
    ttk.Button(window, text='Cancelar', command=window.destroy).grid(column=0, row=2)

    window.bind('<Return>', lambda x: save())
    window.bind('<Escape>', lambda x: window.destroy())
    
    window.mainloop()
