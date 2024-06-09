import os

def list_txt_files(directory='.'):
    """Retorna uma lista de arquivos .txt no diretório especificado."""
    return [f for f in os.listdir(directory) if f.endswith('.txt')]