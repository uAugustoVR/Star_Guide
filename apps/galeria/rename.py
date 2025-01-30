import os
import uuid
from datetime import datetime

def rename_photo(instance, filename):
    ext = filename.split('.')[-1]  # Obtém a extensão do arquivo
    new_filename = f"{uuid.uuid4().hex}.{ext}"  # Gera um nome único
    date_path = datetime.now().strftime("%Y/%m/%d")  # Gera o caminho com a data
    return os.path.join(f"photos/{date_path}/", new_filename)  # Mantém a estrutura
