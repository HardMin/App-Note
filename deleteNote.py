
def deleteNote(raiz, note, refreshTable, store):
    store.pop(note[0] - 1)
    raiz.destroy()
    refreshTable()
