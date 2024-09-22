from typing import List, Tuple
import os
from src.media_processor import MediaProcessor
from src.uuid4_finder import UUID4Finder
from src.validator import Validator

class Controller:
    def extract_uuid4s(self, path: str, fps: int = 1) -> List[str]:
        processor = MediaProcessor()
        
        if os.path.isfile(path):
            if path.lower().endswith(('.png', '.jpg', '.jpeg')):
                text = processor.uuid4_image(path) 
            elif path.lower().endswith(('.mp4', '.avi', '.mov')):
                text = processor.uuid4_video(path, fps)
            else:
                raise ValueError("Unsupported file format. Please provide an image or video file.")
        else:
            raise ValueError("Provided path is not a valid file.")
        
        finder = UUID4Finder()
        uuid4s = finder.find_uuid4(text)
        
        return uuid4s

    def extract_verify_uuid4s(self, path: str, fps: int = 1) -> List[Tuple[str, bool]]:
        uuid4s = self.extract_uuid4s(path, fps)
        validator = Validator()
        validated_uuid4s = validator.validate_match_ids(uuid4s)
        
        return validated_uuid4s