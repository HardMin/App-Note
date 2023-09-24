import tkinter as tk
from tkinter import ttk
from datetime import datetime 


def modifyNote(raiz, note, refreshTable, store):
    # Cierra la ventana de la informacion de la nota
    raiz.destroy()
    
    # Ventana de modificar
    window = tk.Toplevel()
    window.title('Modificar Nota')

    # Captura el valor de la entrada de dato
    value_title = tk.StringVar()
    value_description = tk.StringVar()

    # Captura el valor de la nota actual y agregarlo a la entrada de dato
    value_title.set(note[1])
    value_description.set(note[2])

    # Guardar cambios
    def save():
        # Capturar la fecha actual, para la fecha de la modificacion
        date = datetime.now()

        # Este bloque desde aqui
        # +++++++++++++++++++++++++++++++++++++++++
        item = list(store[note[0]-1])

        # El value_variable.get() captura el valor actual de la entradad de dato

        item[0] = value_title.get() 
        item[1] = value_description.get()
        item[3] = f'{date.day}/{date.month}/{date.year}'
        tuple(item)

        store.pop(note[0]-1)
        store.insert(note[0]-1, item)

        # +++++++++++++++++++++++++++++++++++++++++
        # Hasta aqui, se elimina. Aqui debes conectar con la base de datos para actualizar los valores

        window.destroy()
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
