from __future__ import annotations
import json
from pathlib import Path
from typing import Any

KNOWLEDGE_DIR = Path(__file__).resolve().parent.parent / "knowledge"
INTENTS_FILE = KNOWLEDGE_DIR / "intents.json"
ALIASES_FILE = KNOWLEDGE_DIR / "aliases.json"

class IntentEngine:
    def __init__(self)-> None:
        self.intents = self.__load__json(INTENTS_FILE)
        self.aliases = self.__load__json(ALIASES_FILE)
    
    @staticmethod
    def _load_json(path: Path) -> dict[str,Any]:
        if not path.exists():
            return{}
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    
    def resolve(self, query:str) -> dict[str, Any]:
        query = query.strip().lower()
        canonical = self.aliases.get(query,query)

        if canonical in self.intents:
            return{
                "intent": canonical,
                "data": self.intents[canonical],
            }
        return{
            "intent": canonical,
            "data": {},
        }

intent_engine = IntentEngine()