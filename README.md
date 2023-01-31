# Transcribe with AI
## Purpose
The transcribe.py script in this repository can transcribe a file that contains audio and output a text file with the transcription.
## Requirements
Transcribing an audio file with my transcribe.py script requires having Python on your computer, editing one line of code in the transcribe.py file itself,
and running a few commands via the command-line. See "Usage" for detailed instructions.
## Usage
1. Open a command-line interface
* On MacOS, it's called Terminal.app. It is located in the ~/Applications/Utilities/ folder, or you can press `⌘`+`space` and type "terminal.app" in the search bar. 
* On Windows, it's called cmd.exe. You can search for it by pressing the Windows key and typing "cmd.exe".
2. Make sure you have Python installed on your computer. You can
check by running `python3 --version` or `python --version` on the
command-line interface you just opened. If it looks something like:<br><br>
`(base) zachary@Lizard-3 ~ % python3 --version`<br>
`Python 3.9.7`<br><br>
Then you're good to go. If it says something like "python3 not
found" or if the version is much lower than 3.9.7 (like if it's
Python 2.X.X or something), you can download an up-to-date version
of Python from https://www.python.org/downloads/.
3. On the command-line, run `python3 -m ensurepip --upgrade` to make
sure that "pip", which is Python's package manager, is installed.
Then, also on the command-line run `pip install pydub whisper os`. This will download the
packages that we want to use.
4. Put this script ("transcribe.py") in the same folder/directory
as the file you want to transcribe. This can be in your Documents
folder, Downloads folder, or wherever, but make sure they're in the
same one!
5. On the command-line interface, navigate to the folder/directory
that this script and the file you want to transcribe is in.
* Running "pwd" (which stands for "print working directory") will
  tell you which directory your command-line interface is
  currently in.
* Running "ls" will list the files and folders in that directory
* Running "cd [path to target folder]" will navigate the
  command-line to the target folder. Double-pressing tab at any
  point while you type the path will show you which paths you can choose 
  and may even auto-complete it for you if there's only one path.
For example, on MacOS (I have already moved my recording, "interview.m4a", to the target directory):<br><br>
	`(base) zachary@Lizard-3 ~ % pwd`<br>
	`/Users/zachary`<br>
	`(base) zachary@Lizard-3 ~ % ls`<br>
	`7zz	                Documents		Passwords.kdbx  	libraries`<br>
	`Applications		Downloads		Pictures		Library`<br>
	`(base) zachary@Lizard-3 ~ % cd Documents/github/transcribe-with-AI/`<br>
	`(base) zachary@Lizard-3 transcribe-with-AI % ls`<br>
	`README.md		interiew.m4a		transcribe.py`<br><br>
6. You need to change one line of code so that the script uses your
file, because right now it's configured to use mine! Read the code
and the in-line comments I made, but don't worry about
understanding it.
9. Run the script! Make sure the command-line interface is still
in the correct folder and run `python3 transcribe.py`. It can take
a few minutes on some computers so be patient.

## A little extra explanation
When we make the objects "stream", "model", and "transcription" from
modules that we imported, those objects inherit a bunch of properties
and methods from code that other people wrote. The great thing about this
is that we don't need to know how exactly that code works; we just need to know
how to use those methods and attributes. All I did here was
read the appropriate documentation (which I provided links to in-line in the code)
and figure out how to use those methods and attributes.
This simplifies the programming process immensely and
allows programmers to easily and efficiently use other programmers'
code, as can be seen here!
