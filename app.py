import speech_recognition as sr
import os
import logging
from pydub import AudioSegment

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')


def convert_to_wav(audio_file):
    """
    Convert non-WAV audio files to WAV format using pydub.

    Args:
        audio_file (str): Path to the audio file.

    Returns:
        str: Path to the converted WAV file.
    """
    try:
        # Load the audio file
        audio = AudioSegment.from_file(audio_file)

        # Export the audio as WAV
        wav_file = os.path.splitext(audio_file)[0] + '.wav'
        audio.export(wav_file, format='wav')

        return wav_file
    except Exception as e:
        logging.error(f"Error converting audio: {e}")
        return None


def transcribe_audio(audio_file):
    """
    Transcribe audio from a given file using Google's Speech Recognition API.

    Args:
        audio_file (str): Path to the audio file.

    Returns:
        str: Transcribed text from the audio file or error message.
    """
    recognizer = sr.Recognizer()

    # Check if the audio file exists
    if not os.path.exists(audio_file):
        logging.error("Audio file not found!")
        return "Error: Audio file not found."

    # Convert non-WAV audio files to WAV format
    if not audio_file.endswith(".wav"):
        logging.info("Converting audio to WAV format for compatibility...")
        audio_file = convert_to_wav(audio_file)
        if audio_file is None:
            return "Error: Failed to convert audio file."

    try:
        # Load the audio file
        with sr.AudioFile(audio_file) as source:
            logging.info("Listening to audio...")
            audio_data = recognizer.record(source)  # Read the entire audio file

        # Recognize and transcribe the audio using Google's API
        logging.info("Transcribing audio...")
        text = recognizer.recognize_google(audio_data)
        logging.info("Transcription complete!")
        return text

    except sr.UnknownValueError:
        logging.error("Audio could not be understood.")
        return "Error: Audio could not be understood."
    except sr.RequestError as e:
        logging.error(f"API error: {e}")
        return f"API error: {e}"
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return f"Unexpected error: {e}"


# Example usage
if __name__ == "__main__":
    audio_path = "sample.mp3"  # Can be MP3 or any other supported format
    transcription = transcribe_audio(audio_path)
    print("Transcribed Text:", transcription)