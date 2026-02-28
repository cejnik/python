import os
from tkinter import Tk, filedialog
from PIL import Image
import pillow_heif

# Registrace HEIC formátu
pillow_heif.register_heif_opener()

def convert_heic_to_jpeg(files):
    for file in files:
        try:
            image = Image.open(file)
            output_file = os.path.splitext(file)[0] + ".jpg"
            image.convert("RGB").save(output_file, "JPEG", quality=95)
            print(f"Převedeno: {output_file}")
        except Exception as e:
            print(f"Chyba u {file}: {e}")

def main():
    root = Tk()
    root.withdraw()  # schová hlavní okno

    files = filedialog.askopenfilenames(
        title="Vyber HEIC fotografie",
        filetypes=[("HEIC files", "*.heic")]
    )

    if files:
        convert_heic_to_jpeg(files)
        print("Hotovo!")
    else:
        print("Nebyl vybrán žádný soubor.")

if __name__ == "__main__":
    main()
