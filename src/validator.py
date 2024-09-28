import os
from typing import List, Tuple
from dotenv import load_dotenv
import requests

load_dotenv()
BASE_URL: str = os.getenv('BASE_URL', '')
API_KEY: str = os.getenv('API_KEY', '')

class Validator:
    def validate_match_ids(self, potential_ids: List[str]) -> List[Tuple[str, bool]]:
        validated_ids: List[Tuple[str, bool]] = []
        for match_id in potential_ids:
            if self.is_valid_match_id(match_id):
                validated_ids.append((match_id, True))
            else:
                found_valid = False
                for corrected_id in self.substitute_common_errors(match_id):
                    if self.is_valid_match_id(corrected_id):
                        validated_ids.append((corrected_id, True))
                        found_valid = True
                        break  
                if not found_valid:
                    validated_ids.append((match_id, False))
        return validated_ids

    def is_valid_match_id(self, match_id: str) -> bool:
        url: str = f"{BASE_URL}{match_id}"
        headers: dict = {
            'x-api-key': API_KEY
        }
        try:
            response: requests.Response = requests.get(url, headers=headers)
            return response.status_code == 200
        except requests.RequestException:
            return False

    #There is a non-zero chance that a valid UUID4 is detected, but it is not a valid match ID.
    #Mistakes: 6 for b, b for 6, e for 0, c for 0, c for d, 8 for 3, 4 for a, etc
    def substitute_common_errors(self, potential_id: str):
        substitutions = {
            '6': ['b'],
            'b': ['6'],
            'e': ['0'],
            '0': ['e'],
            'c': ['0', 'd'],
            'd': ['c'],
            '8': ['3'],
            '3': ['8'],
            '4': ['a'],
            'a': ['4'],
        }

        for i, char in enumerate(potential_id):
            if char in substitutions:
                for sub_char in substitutions[char]:
                    corrected_id = potential_id[:i] + sub_char + potential_id[i+1:]
                    yield corrected_id
