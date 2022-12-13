'''
Author: Zachary Keyes

This script prepares the audio file for the language model we want to use. Specifically,
it just changes the number of channels to 1 if it was recorded in stereo mode or something and sets
the frame rate/frequency to 16000Hz.
'''
# make sure pydub is installed; if not, install it with: pip install pydub
from pydub import AudioSegment # see https://github.com/jiaaro/pydub for thorough documentation


# use the location of your the audio file you want to use.
input_file_name = "/Users/zachary/Desktop/FSHD/interiew.mp3"

# use your own file's file extension (mine was "mp3")
sound = AudioSegment.from_file(input_file_name, format="mp3") # load source


# don't change these, these stay the same!
sound = sound.set_channels(1)
sound = sound.set_frame_rate(16000)

# set desired output file; best if it's not the same as input_file_name.
output_file_name = "/Users/zachary/Desktop/FSHD/interiew_prepped.mp3"

# This will create the file in the desired format (whisper works best with mp3 and wav formats,
# I believe) and put all of the audio data inside of it.
sound.export(output_file_name, format="mp3")

# Now go run my Whisper script!