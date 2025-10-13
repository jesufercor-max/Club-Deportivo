import json

input_file = "app_club/fixtures/datos.json"
output_file = "app_club/fixtures/datos_fixed.json"

# Abrimos en modo binario y decodificamos ignorando caracteres problemáticos
with open(input_file, "rb") as f:
    content = f.read().decode("utf-8", errors="ignore")
    data = json.loads(content)

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("✔ Fixture recodificado correctamente en UTF-8 puro -> datos_fixed.json")
