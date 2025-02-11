from Remove_silence_and_mesuere import measure_audio_duration, remove_silence
from Database_And_prepare_audio import save_to_database, prepare_voice_file
import speech_recognition as sr




def transcribe_audio(audio_data, language):
    return sr.Recognizer().recognize_google(audio_data, language=language)

def speech_to_text(input_path, output_path, language, min_silence_len, silence_thresh, db_path):
    wav_file = prepare_voice_file(input_path)
    original_duration = measure_audio_duration(wav_file)
    print(f"Original duration: {original_duration:.2f} seconds")

    processed_file = remove_silence(wav_file, min_silence_len, silence_thresh)
    processed_duration = measure_audio_duration(processed_file)
    print(f"Duration without silence: {processed_duration:.2f} seconds")

    with sr.AudioFile(processed_file) as source:
        text = transcribe_audio(sr.Recognizer().record(source), language)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Transcription saved to: {output_path}")

    data = {
        'input_path': input_path,
        'output_path': output_path,
        'language': language,
        'original_duration': original_duration,
        'processed_duration': processed_duration,
        'transcription': text
    }
    save_to_database(db_path, data)