'''
Author: Zachary Keyes

This script uses OpenAI Whisper's API (https://github.com/openai/whisper/blob/main/README.md#python-usage)
to transcribe the audio file from prep_audio.py. It also puts it into a .txt file.
'''
# make sure whisper is installed; if not, install it with: pip install whisper
import whisper # see https://github.com/openai/whisper for documentation


# use the location of the *prepped* audio file you want to use.
input_file_name = "/Users/zachary/Desktop/FSHD/interiew_prepped.mp3"

# this loads the language model (we want to use "base", so don't change that!) that will
# transcribe the audio file. This is the "AI" part.
model = whisper.load_model("base") # load model

# this transcribes the audio file with the loaded language model.
RESULT = model.transcribe(input_file_name) # transcribe audio file

# RESULT now stores the transcribed text. We're going to put it into a file.

# this creates and opens a file to write onto. Use the location and name of the .txt file you want.
# Don't touch the "w", that just tells open() to use write mode instead of read mode or something.
t_file = open("/Users/zachary/Desktop/FSHD/transcription.txt", "w") # create a .txt file

# now we write the transcribed text. 
t_file.write(RESULT["text"]) # write transcribed text to file

# it's good practice to close files when you're done with them.
t_file.close() # close file

''' A little bit of extra explanation...

RESULT here is actually a python dictionary object. To access anything stored in a dictionary,
you have to use a "key", which then returns a "value". model.transcribe(input_file_name) stores
the transcribed text that we want under the "text" key. 
'''