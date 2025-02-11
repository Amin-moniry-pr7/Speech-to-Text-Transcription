from pydub import AudioSegment
from pydub.silence import split_on_silence
import os



def remove_silence(input_path, min_silence_len, silence_thresh):
    sound = AudioSegment.from_file(input_path)
    audio_chunks = split_on_silence(sound, min_silence_len=min_silence_len, silence_thresh=silence_thresh)
    combined = AudioSegment.empty()
    for chunk in audio_chunks:
        combined += chunk
    output_path = os.path.splitext(input_path)[0] + "_no_silence.wav"
    combined.export(output_path, format="wav")
    return output_path

def measure_audio_duration(audio_path):
    audio = AudioSegment.from_file(audio_path)
    return len(audio) / 1000
