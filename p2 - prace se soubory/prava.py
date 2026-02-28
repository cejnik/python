from pathlib import Path
file_path = Path(__file__).resolve().parent / "text.txt"

with open (file_path, mode="r+", encoding="utf-8") as my_file:
    print(my_file.readlines())

from pathlib import Path
base_dir = Path(__file__).resolve().parent
file_path = base_dir / "text.txt"
print(file_path)
with open (file_path, mode= "r", encoding="utf-8") as my_file:
    print(my_file.readlines())