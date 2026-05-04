import json
from pathlib import Path
from typing import List, Dict

class LaborLinkRepository:
    def __init__(self, filename="storage.json"):
        self.filename = Path(filename)
        self.data = self._load()

    def _load(self) -> Dict:
        if self.filename.exists():
            try:
                with open(self.filename, "r", encoding="utf-8") as f:
                    return json.load(f)
            except:
                return self._default_data()
        return self._default_data()

    def _default_data(self) -> Dict:
        return {
            "employers": [],
            "candidates": [],
            "vacancies": [],
            "deals": []
        }

    def _save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2, default=str)

    def add(self, entity_type: str, entity_dict: Dict):
        if entity_type not in self.data:
            self.data[entity_type] = []
        self.data[entity_type].append(entity_dict)
        self._save()

    def get_all(self, entity_type: str) -> List[Dict]:
        return self.data.get(entity_type, [])