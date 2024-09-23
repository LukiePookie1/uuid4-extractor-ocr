import pytest
import os
from src.controller import Controller
from src.media_processor import MediaProcessor
from src.uuid4_finder import UUID4Finder
from src.validator import Validator

IMAGE_DIR = os.path.join(os.path.dirname(__file__), 'data', 'test_images')
VIDEO_DIR = os.path.join(os.path.dirname(__file__), 'data', 'test_videos')

TEST_FILES = [
    {
        'path': os.path.join(IMAGE_DIR, 'test.jpg'),
        'expected_uuid4s': ['800155a4-3eaa-499c-8333-8095ab5b32ec'] 
    },
    {
        'path': os.path.join(IMAGE_DIR, 'test2.png'),
        'expected_uuid4s': ['086209ed-ce71-42a7-80dd-f5b73bc83083']  
    },

  
    {
        'path': os.path.join(VIDEO_DIR, 'test.mp4'),
        'expected_uuid4s': ['0cfaec30-4ce8-47fd-9826-86805a27775e']  
    },
    {
        'path': os.path.join(VIDEO_DIR, 'test2.mp4'),
        'expected_uuid4s': ['735cafd5-776d-4d11-894d-f463f6dcc5a9']  
    },
]

def test_controller():
    assert Controller is not None

@pytest.mark.parametrize("test_case", TEST_FILES)
def test_extract_uuid4s(test_case):
    controller = Controller()
    path = test_case['path']
    expected_uuid4s = test_case['expected_uuid4s']
    
    extracted_uuid4s = controller.extract_uuid4s(path)
    
    assert extracted_uuid4s == expected_uuid4s, f"Failed for file: {path}"

def test_media_processor():
    assert MediaProcessor is not None

def test_uuid4_finder():
    assert UUID4Finder is not None

def test_validator():
    assert Validator is not None