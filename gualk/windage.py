import os

def create_file(name, content):
    with open(name) as _file:
        _file.write(content)

def delete_file(path_file):
    try:
        # Controlla se il file esiste
        if os.path.exists(path_file):
            os.remove(path_file)  # Elimina il file
            print(f"Il file '{path_file}' è stato eliminato con successo.")
        else:
            print(f"Il file '{path_file}' non esiste.")
    except Exception as e:
        print(f"Si è verificato un errore durante l'eliminazione del file: {e}")

class Windage:
    def __init__(self, name, content, path_file):
        self.create_file = create_file(name=name, content=content)
        self.delete_file = delete_file(path_file=path_file)
    def create_file(create_file, name, content):
        create_file(name, content)
    def delete_file(delete_file, path_file):
        delete_file(path_file)