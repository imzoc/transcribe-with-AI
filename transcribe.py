'''
    Author: Zachary Keyes
    Class: FSHD 150B1
    Description: This Python script uses OpenAI Whisper and PyDub to
    transcribe a file that contains audio. It outputs to a .txt file.

    If you're a newbie, see README.md
    If you're also curious and want a little extra explanation, also
    see README.md.

'''

from pydub import AudioSegment
import whisper

### USING PYDUB (https://github.com/jiaaro/pydub#quickstart)
### Most file formats will work as long as they have audio in them
### somewhere. This section preps the audio so that whisper will work
### most effectively. Replace "interiew.m4a" with the file you want to
### transcribe and "m4a" with the appropriate file extension.

stream = AudioSegment.from_file("interiew.m4a", "m4a")  # Modify this!
stream.set_channels(1)  # Don't modify this!
stream.set_frame_rate(16000)  # Don't modify this!
stream.export("prepped.mp3", format="mp3")  # Don't modify this!

### USING WHISPER (https://github.com/openai/whisper#python-usage)
model = whisper.load_model("base")  # the "base" model should be sufficient.
transcribed_audio = model.transcribe("prepped.mp3")  # Don't modify this!
transcription = open("transcription.txt", "w")  # This creates the text file
transcription.write(transcribed_audio["text"])  # This writes the text file
transcription.close()  # This closes the text file (good practice)