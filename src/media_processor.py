import os
from typing import List
from ffmpy import FFmpeg
import tempfile
import easyocr

class MediaProcessor: 
    def __init__(self):
        self.temp_dir = tempfile.TemporaryDirectory()

    def uuid4_video(self, video_path: str, fps: int = 1) -> List[str]:
        images = self.slice_video(video_path, fps)
        full_text = ""
        
        for image in images:
            text = self.detect_text(image)
            full_text += text + " "
            
        return full_text.strip()

    def uuid4_image(self, image_path: str) -> List[str]:
        text = self.detect_text(image_path)

        return text

    #Helper functions
    def slice_video(self, video_path: str, fps: int = 1) -> List[str]:
        ff = FFmpeg(
            inputs={video_path: None},
            outputs={os.path.join(self.temp_dir.name, "frame_%03d.png"): f"-vf fps={fps}"}
        )
    
        ff.run()
    
        frame_paths = []
        for file in os.listdir(self.temp_dir.name):
            if file.endswith('.png'):
                frame_paths.append(os.path.join(self.temp_dir.name, file))
        return frame_paths

    
    def detect_text(self, image_path: str) -> str:
        reader = easyocr.Reader(['en'])

        result = reader.readtext(image_path)   

        #Only want text, not bounding boxes or confidence scores
        text = [text for _, text, _ in result]
        
        return "".join(text)        

    def __del__(self):
        self.temp_dir.cleanup()
        