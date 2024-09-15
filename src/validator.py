import os
from typing import List, Tuple
from dotenv import load_dotenv

load_dotenv()
BASE_URL: str = os.getenv('BASE_URL', '')
API_KEY: str = os.getenv('API_KEY', '')

class Validator:
    def validate_match_ids(self, potential_ids: List[str]) -> List[Tuple[str, bool]]:
        return
    
    def substitute_common_errors(self, potential_id: str) -> str:
        return
