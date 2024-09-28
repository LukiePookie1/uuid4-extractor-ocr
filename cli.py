import argparse
import json
from src.controller import Controller

def main():
    parser = argparse.ArgumentParser(description="Extract UUID4(s) from image or video files.")
    parser.add_argument("path", type=str, help="Path to the input file. Supports .png, .jpg, .jpeg, .mp4, .mov, and .avi files.")
    parser.add_argument("--fps", type=int, default=1, help="Frames per second to extract from video. Defaults to 1 if not provided. Ignored for image files.")
    parser.add_argument("--validation", action="store_true", help="Enable validation of the extracted UUID4(s) against the API.")

    args = parser.parse_args()

    controller = Controller()

    if args.validation:
        result = controller.extract_verify_uuid4s(args.path, args.fps)
        if result:
            output = [{'uuid4': uuid4, 'is_valid': is_valid} for uuid4, is_valid in result]
        else:
            output = {'message': 'No UUID4 Found'}
    else:
        result = controller.extract_uuid4s(args.path, args.fps)
        if result:
            output = result
        else:
            output = {'message': 'No UUID4 Found'}

    print(json.dumps(output))

if __name__ == "__main__":
    main() 
