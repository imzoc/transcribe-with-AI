# Transcribe with AI
## Purpose
I used OpenAI's Whisper model to transcribe a long interview recording I took for my honors assignment. It saved me a lot of time. Instead of transcribing the entire thing by hand, I just had to go through and make some quick fixes to the imperfect (but pretty decent) AI transcription. This tutorial will help you do that, and hopefully you can pick up some computer science concepts along the way :)

If you have recommendations, please open an [issue](https://github.com/imzoc/transcribe-with-AI/issues) or email me (my netid is zachk).

## Requirements
Transcribing an audio file with transcribe.py requires:
1. Having Python and PIP on your computer.
2. Editing some variables in transcribe.py (just so that Python knows where your files are, nothing crazy :) )
3. Running some basic UNIX-style commands from a command-line interface (aka CLI).

This README document will walk you through the process. If you know what you're doing, download the Python script from [releases](https://github.com/imzoc/transcribe-with-AI/releases).

## Step-by-step
1. Open a CLI:
	* On MacOS, you want to open Terminal.app. Open finder, go to your Applications folder, open the Utilities sub-folder, and you should see it. Alternatively, you can be cool and use Spotlight Search (press `⌘`+`space`, type whatever application you want--in this case, terminal.app, and press enter :) )
	* On Windows, open cmd.exe. Press the Windows key and type "cmd.exe". 
2. Make sure you have Python on your computer.
	* From the CLI you just opened, run `python --version`. If it any version above 3.8, like `Python 3.9.7`, you're probably good to go. If it says something like "python not found", try "python3" instead of "python".
		* If you're using macOS, also try running "/usr/bin/python3" or "/usr/local/bin/python3" instead of "python". This is called using an *absolute path* and should almost always work if you have Python on your computer. This is because Python is actually just a binary file, and it's almost always located in /usr/bin or /usr/local/bin. Again, only on UNIX-like operating systems like macOS; I have no idea how the heck Window does this, so consult the honorific ChatGPT for help if you need it.
	* If your computer can't find Python (or if it's on out-of-date version, like Python 2.x.x), [download the most up-to-date version of Python](https://www.python.org/downloads/).
3. Make sure you have all of the packages we will use. This requires a tool called "pip".
	* From the CLI, run `python3 -m ensurepip --upgrade`.
	* Then run `pip install pydub whisper os`. If the CLI doesn't recognize "pip", try "pip3". This should download those packages, we will import into our own program.
4. Get your files in order.
	* Download the latest zipped [release](https://github.com/imzoc/transcribe-with-AI/releases) file to your Downloads folder and unzip it.
	* Use your file explorer (Finder, for example, on macOS) to move any audio files you want to transcribe into the folder you just unzipped.
5. Open transcribe.py __in a text editor__ and make some quick changes.
	* The easiest way to do open a script like this is by right clicking on transcribe.py and selecting "Open with Notepad/TextEdit". Just make sure it renders the file as text and doesn't run it just yet :)
	* Replace the the "file_name" and "audio_format" variables (located just under the "USING PYDUB" comment) as appropriate for *your* audio files.
6. Go back to your CLI and navigate to the "target" directory. To do that, you need these UNIX commands:
	* Run `pwd` to print the directory you're currently in.
	* Run `ls` to list the files and folders in the directory you're currently in.
	* Run `cd [folder]` to navigate to a target folder. Capitalization matters.
	* Run `cd ..` to backtrack to the directory above the current directory.

	There are loads of useful guides out there on filesystem navigation. If you're having trouble, consult ChatGPT (unironically, it will probably be able to help you :) ) Here's an example from my macOS (all of my commands are after the "%" symbol):


	`(base) zachary@Lizard-3 ~ % pwd`<br>
	`/Users/zachary`

	`(base) zachary@Lizard-3 ~ % ls`<br>
	`7zz	                Documents		Passwords.kdbx  	libraries`<br>
	`Applications		Downloads		Pictures		Library`

	`(base) zachary@Lizard-3 ~ % cd Downloads/transcribe-with-AI-1.0.0`

	`(base) zachary@Lizard-3 transcribe-with-AI-1.0.0 % pwd`<br>
	`/Users/zachary/Downloads/transcribe-with-AI-1.0.0`

	`(base) zachary@Lizard-3 transcribe-with-AI % ls`<br>
	`README.md		interiew.m4a		transcribe.py`


7. Run the script:
	* From the CLI window that's already in the directory with all of our files, run `python3 transcribe.py`. If it looks like the window froze, it's working. It can take a while... don't mess with it.

8. Find the transcribed .txt file in the same directory!
9. Star this repository on GitHub for +ratio (please :) ).
