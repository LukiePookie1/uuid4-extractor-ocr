# OCR UUID4 Extractor

Python script that uses EasyOCR to extract UUID4(s) from image or video files. It is designed to be used in a video game match ID validation system.

## Dependencies

- Python 3.12
- EasyOCR

## Installation

1. Clone the repository:

```bash
git clone https://github.com/luke-rappa/ocr-uuid4-extractor.git
```

2. Install the required packages:

```bash
brew install python
```

```bash
brew install ffmpeg
```

```bash
pip install -r requirements.txt
```

3. Configure the API endpoint:
   - Create a `.env` file in the project root directory
   - Add your base URL and API key to the `.env` file:
     ```
     BASE_URL=your_base_url_here
     API_KEY=your_api_key_here
     ```

## Usage

### Extract UUID4(s) from an image or video

To extract UUID4(s) from an image or video, run the following command:

```bash
python src/cli.py <path> [fps] [validation]
```

- `<path>` (`str`): Path to the input file. Supports .png, .jpg, .jpeg, and .mp4 files.
- `[--fps]` (`int`, Optional): Frames per second to extract from video. Defaults to 1 if not provided. This argument is ignored for image files. If the UUID4 isn't detected in videos where it appears briefly, I recommend increasing the frame rate to 5 FPS.
- `[--validation]` (Flag, Optional): Include this option to enable validation of the extracted UUID4(s) against the API. Defaults to `False` if not included. 
