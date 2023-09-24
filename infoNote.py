import tkinter as tk
from tkinter import ttk
from modifyNote import modifyNote
from deleteNote import deleteNote

def windowInfoNote(note, refreshTable, store):
    window = tk.Toplevel()
    window.title('Información de la nota')
    window.geometry('500x400')

    _, title, desc, date_c, date_m = note

    title_label = ttk.Label(window, text='Titulo: ')
    title_label.grid(column=0, row=0, pady=20)

    title_note_label = ttk.Label(window, text=title)
    title_note_label.grid(column=1, row=0)

    description_label = ttk.Label(window, text='Descripción: ')
    description_label.grid(column=0, row=1, pady=20)
    
    description_note_label = ttk.Label(window, text=desc)
    description_note_label.grid(column=1, row=1)

    dc_label = ttk.Label(window, text='Fecha Creación: ')
    dc_label.grid(column=0, row=2, pady=20)
    
    dc_note_label = ttk.Label(window, text=date_c)
    dc_note_label.grid(column=1, row=2)

    dm_label = ttk.Label(window, text='Fecha Modificación: ')
    dm_label.grid(column=0, row=3, pady=20)
    
    dm_note_label = ttk.Label(window, text=date_m)
    dm_note_label.grid(column=1, row=3)

    delete = ttk.Button(window, text='Eliminar', command=lambda: deleteNote(window, note, refreshTable, store))
    delete.grid(column=0, row=5)

    modify = ttk.Button(window, text='Modificar', command=lambda: modifyNote(window, note, refreshTable, store))
    modify.grid(column=1, row=5)

    close = ttk.Button(window, text='Cerrar', command=window.destroy)
    close.grid(column=2, row=5)
