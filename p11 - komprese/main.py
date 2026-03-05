import base64
import zlib

with open ('text.txt', 'r') as file:
    data = file.read()

# převod textu na byte
data_bytes = bytes(data, encoding='utf-8')

# Komprese data - výsledná data jsou bytes
compressed_data = zlib.compress(data_bytes)

# Zakódování komprimovaných dat do formátu base64
compressed_data_base64 = base64.b64encode(compressed_data)

# 1. možnost - zapsat data compressed_data_base64 do souboru
with open('compressed.txt', 'wb') as com_file:
    com_file.write(compressed_data_base64)

# Doporučeno -------------------------------------------------------
# 2. možnost - zapsat data compresed_data_base64 do souboru jako text
decoded_data = compressed_data_base64.decode('utf-8')
with open ('compressed.txt', 'w') as file:
    file.write(decoded_data)



