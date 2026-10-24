import json

MAX_LENGTH = 50

FIELDS_TO_TRUNCATE = ['title', 'seller', 'color', 'description']

input_path = 'src/ecommerce/fixtures/ecommerce/ProductModel.json'
output_path = 'src/ecommerce/fixtures/ecommerce/ProductModel_truncated.json'

with open(input_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    fields = item.get('fields', {})
    for field in FIELDS_TO_TRUNCATE:
        if field in fields and fields[field] is not None:
            value = str(fields[field])
            if len(value) > MAX_LENGTH:
                fields[field] = value[:MAX_LENGTH]
                print(f"Truncado pk={item['pk']} campo={field}: '{value[:MAX_LENGTH]}...'")

with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"\nArchivo guardado en: {output_path}")