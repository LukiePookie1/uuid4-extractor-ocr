from typing import List
import re

UUID4_PATTERN: str = r'[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}'

class UUID4Finder:
    def find_uuid4(self, text: str) -> List[str]:
        return
    
    def clean_uuid(self, uuid_candidate: str) -> str:
        return