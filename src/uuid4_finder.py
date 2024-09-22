import re
from typing import List

UUID4_PATTERN = r'[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}'
UUID4_PATTERN_FORGIVING = r'[0-9a-f]{8}-?[0-9a-f]{4}-?4[0-9a-f]{3}-?[89ab][0-9a-f]{3}-?[0-9a-f]{12}'

class UUID4Finder:
    def find_uuid4(self, text: str) -> List[str]:
        normalized_text = re.sub(r'\s', '', text).lower()
        potential_uuid4s = re.findall(UUID4_PATTERN, normalized_text)
        
        if not potential_uuid4s:
            substitution_map = {'g': '9', 'o': '0', 'i': '1', 's': '5', 't': 'f', 'l': '1', 'S': '5', '_': '-', ']': '1', '[': '1', 'z': '2'}
            
            fixed_text = normalized_text
            for wrong_char, correct_char in substitution_map.items():
                fixed_text = fixed_text.replace(wrong_char, correct_char)
            
            potential_uuid4s = re.findall(UUID4_PATTERN_FORGIVING, fixed_text)

            reconstructed_uuid4s = []
            for uuid in potential_uuid4s:
                if '-' not in uuid or len(uuid) != 36:
                    reconstructed_uuid4s.append(self.reconstruct_uuid4(uuid))
                else:
                    reconstructed_uuid4s.append(uuid)
            
            potential_uuid4s = reconstructed_uuid4s
            
        return potential_uuid4s

    def reconstruct_uuid4(self, potential_uuid4: str) -> str:
        clean_uuid = potential_uuid4.replace('-', '')
    
        reconstructed_uuid4 = (
            clean_uuid[:8] + '-' +
            clean_uuid[8:12] + '-' +
            clean_uuid[12:16] + '-' +
            clean_uuid[16:20] + '-' +
            clean_uuid[20:]
        )
        
        return reconstructed_uuid4