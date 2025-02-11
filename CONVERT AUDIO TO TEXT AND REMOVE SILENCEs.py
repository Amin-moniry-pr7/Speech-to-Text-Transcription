from Database_And_prepare_audio import initialize_database
from Speech_and_transcribe import speech_to_text
import time
import os



if __name__ == '__main__':

    db_path = 'PODCAST.db'
    initialize_database(db_path)

    input_path = input('Enter the path to an audio file (WAV, MP3, M4A, OGG, or FLAC): ').strip()
    if not os.path.isfile(input_path):
        print('Error: File not found.')
        exit(1)

    output_path = input('Enter the path to save the transcription (e.g., output.txt): ').strip()
    language = input('Enter the language code (e.g., en-US): ').strip()

    while True:
        try:
            min_silence_len = int(input('Minimum silence length in milliseconds (e.g., 1000): '))
            silence_thresh = float(input('Silence threshold in dB (e.g., -40.0): '))
            assert min_silence_len > 0 and silence_thresh < 0
            break
        except:
            print('Invalid input. Please try again.')

    try:
        start_time = time.time()
        speech_to_text(input_path, output_path, language, min_silence_len, silence_thresh, db_path)
        end_time = time.time()
        print(f"Processing completed in {end_time - start_time:.2f} seconds.")
    except Exception as e:
        print('Error:', e)
        exit(1)
