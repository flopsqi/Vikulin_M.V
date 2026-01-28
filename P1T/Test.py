import json
with open("results.json", "w", encoding="utf-8") as f:
    json.dump([], f, ensure_ascii=False, indent=4)
