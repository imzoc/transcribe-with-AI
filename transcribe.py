'''
    Author: Zachary Keyes
    Class: FSHD 150B1
    Description: This Python script uses OpenAI Whisper and PyDub to
    transcribe a file that contains audio. It outputs to a .txt file.
    Note: most input file formats will work as long as they have audio
    in them somewhere. 
    Note: on line 20, you must replace "interiew.m4a" with the file you
    want to transcribe and "m4a" with the appropriate file extension.
    Note: if you're a newbie, see README.md
    Note: if you're also curious and want a little extra explanation,
    also see README.md.
'''

import os
import pydub
import whisper

### USING PYDUB (https://github.com/jiaaro/pydub#quickstart)
stream = pydub.AudioSegment.from_file("interiew.m4a", "m4a")  # Modify this!
stream.set_channels(1)
stream.set_frame_rate(16000)
stream.export("prepped.mp3", format="mp3")  # no need to modify, this will be deleted.

### USING WHISPER (https://github.com/openai/whisper#python-usage)
model = whisper.load_model("base")
transcribed_audio = model.transcribe("prepped.mp3")
transcription = open("transcription.txt", "w")
transcription.write(transcribed_audio["text"])
transcription.close()

os.remove("prepped.mp3")  # This just deletes the extra file we had to make
