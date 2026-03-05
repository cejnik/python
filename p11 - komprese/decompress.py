import base64
import zlib


# Načtení
with open('compressed.txt', 'r') as file:
    compressed_data_base64 = file.read()

# Dekódování z base64 na byte

compressed_data = base64.b64decode(compressed_data_base64)

# Dekomprese dat zpět na původní formát byte
decompressed_data_byte = zlib.decompress(compressed_data)

# Převod dekomprimovaných bytových dat zpět na řetězec
decompressed_data = decompressed_data_byte.decode('utf-8')

with open ('after_text.txt', 'w') as new_file:
    new_file.write(decompressed_data)