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
            url: str = f"{BASE_URL}{match_id}"
            headers: dict = {
                'x-api-key': API_KEY
            }

            try:
                response: requests.Response = requests.get(url, headers=headers)

                if response.status_code == 200:
                    validated_ids.append((match_id, True))
                else:
                    validated_ids.append((match_id, False))
            
            except requests.RequestException:
                validated_ids.append((match_id, False))
        return validated_ids
    
    def substitute_common_errors(self, potential_id: str) -> str:
        return
