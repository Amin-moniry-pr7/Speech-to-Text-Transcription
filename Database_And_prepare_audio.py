from pydub import AudioSegment
import sqlite3
import os

def initialize_database(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS PODCAST (id INTEGER PRIMARY KEY AUTOINCREMENT,input_path TEXT,
            output_path TEXT,language TEXT,original_duration REAL,processed_duration REAL,transcription TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

def save_to_database(db_path, data):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO PODCAST (input_path, output_path, language, original_duration, processed_duration, transcription)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (data['input_path'], data['output_path'], data['language'], data['original_duration'], data['processed_duration'], data['transcription']))
    conn.commit()
    conn.close()

def prepare_voice_file(path):
    ext = os.path.splitext(path)[1]
    if ext == '.wav':
        return path
    if ext in ('.mp3', '.m4a', '.ogg', '.flac'):
        wav_file = os.path.splitext(path)[0] + '.wav'
        AudioSegment.from_file(path).export(wav_file, format='wav')
        return wav_file
    raise ValueError(f'Unsupported format: {ext}')
