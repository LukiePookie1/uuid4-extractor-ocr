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
        'path': os.path.join(IMAGE_DIR, 'test3.png'),
        'expected_uuid4s': ['9c3fe9f2-34ea-4a5c-b530-fd10c6ce8f4c']  
    },
    {
        'path': os.path.join(IMAGE_DIR, 'test4.jpg'),
        'expected_uuid4s': ['95b1ba9a-73dc-49f1-a6cd-ec6ce03855ec']  
    },
    {
        'path': os.path.join(IMAGE_DIR, 'test5.png'),
        'expected_uuid4s': ['9951d48e-651a-4be4-97bb-57b9a6177f9d']  
    },
    {
        'path': os.path.join(IMAGE_DIR, 'test6.png'),
        'expected_uuid4s': ['5ec13461-fe54-4d3a-90fc-1e560d35c2fb']  
    },
    {
        'path': os.path.join(IMAGE_DIR, 'test7.png'),
        'expected_uuid4s': ['66cf1db1-c2f1-428c-b426-2a2105405f00']  
    },
    {
        'path': os.path.join(IMAGE_DIR, 'test8.jpg'),
        'expected_uuid4s': ['cfc25231-a074-4204-87e5-a6c01e524bcb']  
    },
    {
        'path': os.path.join(IMAGE_DIR, 'test9.jpg'),
        'expected_uuid4s': ['02be6975-2f51-465b-af13-f35cd89c7bf8']  
    },
    {
        'path': os.path.join(IMAGE_DIR, 'test10.jpg'),
        'expected_uuid4s': ['25e395bc-56e4-4bed-b5f6-b3e17a15627b']  
    },
    {
        'path': os.path.join(IMAGE_DIR, 'test11.png'),
        'expected_uuid4s': ['9c3fe9f2-34ea-4a5c-b530-fd10c6ce8f4c']  
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

@pytest.mark.parametrize("test_case", TEST_FILES)
def test_extract_uuid4s(test_case):
    controller = Controller()
    path = test_case['path']
    expected_uuid4s = test_case['expected_uuid4s']
    
    extracted_uuid4s = controller.extract_uuid4s(path)
    
    missing_uuid4s = [uuid for uuid in expected_uuid4s if uuid not in extracted_uuid4s]
    assert not missing_uuid4s, f"Missing UUID4s {missing_uuid4s} in file: {path}"
