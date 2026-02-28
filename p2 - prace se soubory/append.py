from pathlib import Path
base_dir = Path(__file__).resolve().parent
file_path = base_dir / "text.txt"

with open (file_path) as my_file:
    all_names = my_file.readlines()
    for name in all_names:
        name = name.strip()
        with open(f"output/guest_{name}", mode= "w") as guest_name:
            guest_name.write("Ahoj, tohle je test.") 