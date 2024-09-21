import re
from typing import List

UUID4_PATTERN = r'[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}'
UUID4_PATTERN_FORGIVING = r'[0-9a-f]{8}-?[0-9a-f]{4}-?4[0-9a-f]{3}-?[89ab][0-9a-f]{3}-?[0-9a-f]{12}'

#Failed: 3, 4, 5

class UUID4Finder:
    def find_uuid4(self, text: str) -> List[str]:
        text_without_whitespace = re.sub(r'\s', '', text)
        potential_uuid4s = re.findall(UUID4_PATTERN_FORGIVING, text_without_whitespace)
        
        if not potential_uuid4s:
            substitution_map = {'g': '9', 'o': '0', 'i': '1', 's': '5', 't': 'f', 'l': '1', 'S': '5', 'O': '0'}
            
            fixed_text = text_without_whitespace
            for wrong_char, correct_char in substitution_map.items():
                fixed_text = fixed_text.replace(wrong_char, correct_char)
            
            potential_uuid4s = re.findall(UUID4_PATTERN_FORGIVING, fixed_text)
            
            return potential_uuid4s
    
    def clean_uuid(self, uuid_candidate: str) -> str:
        return
    