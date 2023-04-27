# Transcribe with AI
## Purpose
transcribe.py can transcribe an audio file, generate a transcription using AI, and output a text file with the transcription.
## Requirements
Transcribing an audio file with transcribe.py requires:
1. Having Python on your computer
2. Editing some variables in transcribe.py (just so that Python knows where your files are, nothing crazy :) )
3. Running some basic commands from a command-line interface (aka CLI).

This README document will walk you through the process.

## Step-by-step
1. Open a CLI:
	* On MacOS, you want to open Terminal.app. Open finder, go to your Applications folder, open the Utilities sub-folder, and you should see it. Alternatively, you can be cool and use Spotlight Search (press `⌘`+`space`, type whatever application you want--in this case, terminal.app, and press enter :) )
	* On Windows, open cmd.exe. Press the Windows key and type "cmd.exe". 
2. Make sure you have Python on your computer.
	* From the CLI, run `python --version`. If it any version above 3.8, like `Python 3.9.7`, you're probably good to go. If it says something like "python3 not found", try "python3" instead of "python".
		* If you're using macOS, also try "/usr/bin/python3" or "/usr/local/bin/python3" instead of "python". This is called using an *absolute path* and should almost always work if you have Python on your computer. This is because Python is actually just a binary file, and it's almost always located in /usr/bin or /usr/local/bin. Again, only on UNIX-like operating systems like macOS; I have no idea how the heck Window does this, so consult the honorific ChatGPT for help if you need it.
	* If your computer can't find Python (or if it's on out-of-date version, like Python 2.x.x), [download the most up-to-date version of Python](https://www.python.org/downloads/).
3. Make sure you have all of the packages we will use. This requires a tool called "pip".
	* From the CLI, run `python3 -m ensurepip --upgrade`. 
	* Then run `pip install pydub whisper os`. If the CLI doesn't recognize "pip", try "pip3".
4. Get your files in order (important! This program uses *relative paths* to interact with the filesystem, which I will explain later).
	* Download the latest [release](https://github.com/imzoc/transcribe-with-AI/releases) to your Downloads folder and unzip it.
	* Use your file explorer (Finder, for example, on macOS) to move any audio files you want to transcribe into the unzipped folder you just made.
5. Open transcribe.py __in a text editor__ and make some quick changes.
	* The easiest way to do open a script like this is by right clicking on transcribe.py and selecting "Open with Notepad/TextEdit". Just make sure it renders the file as text and doesn't run it just yet :)
	* Edit the the file_name and audio_format variables as appropriate for your audio files.
6. Go back to the CLI and navigate to the "target" directory. From there, we will run our script.
	* Run `pwd` to print the directory you're currently in.
	* Run `ls` to list the files and folders in the directory you're currently in.
	* Run `cd [path to target folder]` to navigate
to a sub-directory.

	There are loads of useful guides out there on filesystem navigation. If you're having trouble, consult ChatGPT (unironically, it will probably be able to help you :) ) Here's an example from my macOS (all of my commands are after the "%" symbol):


	`(base) zachary@Lizard-3 ~ % pwd`<br>
	`/Users/zachary`

	`(base) zachary@Lizard-3 ~ % ls`<br>
	`7zz	                Documents		Passwords.kdbx  	libraries`<br>
	`Applications		Downloads		Pictures		Library`

	`(base) zachary@Lizard-3 ~ % cd Downloads/transcribe-with-AI-1.0.0/`

	`(base) zachary@Lizard-3 transcribe-with-AI-1.0.0 % pwd`<br>
	`/Users/zachary/Downloads/transcribe-with-AI-1.0.0`

	`(base) zachary@Lizard-3 transcribe-with-AI % ls`<br>
	`README.md		interiew.m4a		transcribe.py`


7. Run the script.
	* From the __same__ CLI window (remember relative paths? Everything we do now is *relative* to the directory our CLI is in), run `python3 transcribe.py`. If it looks like the window froze, it's working. It can take a while... don't mess with it.

8. Find the transcribed .txt file in the same directory!