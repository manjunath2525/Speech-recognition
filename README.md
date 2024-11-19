# Audio Transcription Application

This Python application transcribes audio from various file formats into text using the Google Speech Recognition API. It supports audio file conversion to WAV format for compatibility and provides detailed logging for easy troubleshooting.

## Features

- Convert non-WAV audio files (e.g., MP3, FLAC) to WAV format using `pydub`.
- Transcribe audio to text using Google's Speech Recognition API (`speech_recognition`).
- Logging support for easy debugging and progress tracking.
- Error handling for file not found, conversion failure, and API issues.

## Requirements

- Python 3.x
- `speech_recognition` library
- `pydub` library
- `pyaudio` (for microphone support, optional)
- `ffmpeg` or `libav` (for audio file format conversion)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/your-repository-name.git
cd your-repository-name
```

### 2. Install the dependencies

You can install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist, you can manually install the necessary packages:

```bash
pip install SpeechRecognition pydub
```

### 3. Install FFmpeg

`pydub` relies on `ffmpeg` for audio format conversion. Install it by following the instructions for your system:

- **Windows**: Download FFmpeg from [FFmpeg.org](https://ffmpeg.org/download.html), then add the bin directory to your system's PATH.
- **macOS**: Use Homebrew:

  ```bash
  brew install ffmpeg
  ```

- **Linux**: Install via your package manager:

  ```bash
  sudo apt install ffmpeg
  ```

## Usage

1. Place your audio file in the project directory or specify the full path.
2. Run the script:

   ```bash
   python audio_transcription.py
   ```

   The script will convert the audio to WAV (if necessary), transcribe it using Google's Speech Recognition API, and print the transcription to the console.

### Example:

```bash
python audio_transcription.py
```

The transcription will be displayed in the terminal as:

```
Transcribed Text: [Your transcribed text here]
```

## Functions

### `convert_to_wav(audio_file)`

Converts any non-WAV audio file to WAV format.

#### Args:
- `audio_file (str)`: Path to the audio file.

#### Returns:
- `str`: Path to the converted WAV file, or `None` if the conversion fails.

### `transcribe_audio(audio_file)`

Transcribes audio from the provided file.

#### Args:
- `audio_file (str)`: Path to the audio file.

#### Returns:
- `str`: Transcribed text or an error message.

## Error Handling

- **File Not Found**: If the provided audio file is not found, an error message will be logged.
- **Conversion Failure**: If the audio file cannot be converted to WAV format, an error message will be logged.
- **Speech Recognition Issues**: Any issues with understanding the audio or API requests are logged with detailed error messages.
