Execute the command below so that the packages on Ubuntu are updated to the latest version. If you skip this step, you may encounter an error while installing python packages.

You can create a new folder and enter it using the following command.

sudo apt-get -y update

Step 2: Install python3 pip3
sudo apt install python3-pip

Step 3: Install Speech Recognition module
You can install SpeechRecognition from a terminal with pip:
pip3 install SpeechRecognition

Verify in terminal
>>> import speech_recognition as sr
>>> sr.__version__
'3.8.1'

Create a recognizer class
>>> r = sr.Recognizer()

type the following in the terminal: to see the methods
>>> r = sr.Recognizer()
>>> dir(r)

You will see a list of methods. Out of this, we will widely be using the recognize_google() method, which is the Googles Web Speech API service.

Now lets get into the meat of the topic. Till now, we have only initialised Now let's get into the meat of the topic. Till now, we have only initialised the Recognizer. We haven’t fed it any audio input to see how it works. So let's get into it.

Now there are 2 ways to give audio input to the Recognizer:

Using an Audio File
Using the Microphone

First try running the following command in the terminal(make sure you have exited from the python interpreter by typing exit() or pressing the keys Ctrl+d or control+d)

python3 -m speech_recognition

You will get an ModuleNotFoundError message informing you that pyaudio is not present on your system.

Install Pyaudio module
sudo apt-get install python3-pyaudio
Once you’ve got PyAudio installed, you can test the installation from the console.
python3 -m speech_recognition

Make sure your default microphone is ON and unmuted. If the installation worked, you should see something like this:

A moment of silence, please…
Set minimum energy threshold to 600.4452854381937
Say something!

Now, open up another interpreter session(by typing python3 in the terminal) and create an instance of the recognizer class. 

>>> import speech_recognition as sr
>>> r = sr.Recognizer()
 

Now, let's use the microphone as the source, you will use the default system microphone. You can access this by creating an instance of the Microphone class.

>>> mic = sr.Microphone()

Using listen() to Capture Microphone Input:

Now that you’ve got a Microphone instance ready to go, it’s time to capture some input. You can capture input from the microphone using the listen() method of the Recognizer class inside of the with block. This method takes an audio source as its first argument and records input from the source until silence is detected.

>>> with mic as source:
...    audio = r.listen(source)
...
 

Once you execute the with block(hit enter after typing the above code), try speaking “hello” into your microphone. Wait a moment for the interpreter prompt to display again. Once the “>>>” prompt returns, you’re ready to recognize the speech.

>>> r.recognize_google(audio)
'hello'
 

If the prompt never returns, your microphone is most likely picking up too much ambient noise. You can interrupt the process with Ctrl+c or control+c to get your prompt back.

To handle ambient noise, you’ll need to use the adjust_for_ambient_noise() method of the Recognizer class. Since input from a microphone is far less predictable than input from an audio file, it is a good idea to do this anytime you listen for microphone input.

>>> with mic as source:
...    r.adjust_for_ambient_noise(source)
...    audio = r.listen(source)
...
 

After running the above code, wait a second for adjust_for_ambient_noise() to do its thing, then try speaking “hello” into the microphone. Again, you will have to wait a moment for the interpreter prompt to return before trying to recognize the speech.

Recall that adjust_for_ambient_noise() analyzes the audio source for one second. If this seems too long to you, feel free to adjust this with the duration keyword argument.

The SpeechRecognition documentation recommends using a duration no less than 0.5 seconds. In some cases, you may find that durations longer than the default of one second generate better results. The minimum value you need depends on the microphone’s ambient environment. Unfortunately, this information is typically unknown during development. In my experience, the default duration of one second is adequate for most applications.
