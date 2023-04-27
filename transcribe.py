"""
    Author: Zachary Keyes
    Class: FSHD 150B1
    Description: This Python script uses OpenAI Whisper and PyDub to
    transcribe a file that contains audio. It outputs to a .txt file.
    
    Note: most input file formats will work as long as they have audio
    in them somewhere. See Pydub's documentation for more deets :)
    Note: make sure to run this script from the shell in the same
    directory as your file (or you can use an absolute path).
"""

import os

import pydub
import whisper

### USING PYDUB (https://github.com/jiaaro/pydub#quickstart)
file_name = "interiew.m4a"  # Change this to your file name!
audio_format = "m4a"  # Modify this (if needed)!
stream = pydub.AudioSegment.from_file(file_name, audio_format)
stream.set_channels(1)
stream.set_frame_rate(16000)
stream.export("prepped_audio.mp3", format="mp3")

### USING WHISPER (https://github.com/openai/whisper#python-usage)
model = whisper.load_model("base")
transcribed_audio = model.transcribe("prepped_audio.mp3")
transcription = open("transcription.txt", "w")
transcription.write(transcribed_audio["text"])
transcription.close()

os.remove("prepped_audio.mp3")
