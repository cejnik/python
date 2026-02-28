# Když nevíš kde hledat soubor a potřebuješ o složku výš
from pathlib import Path
file_path = Path(__file__).parent.parent / "text.txt" 


with open(file_path) as my_file:
    print(my_file.readlines())