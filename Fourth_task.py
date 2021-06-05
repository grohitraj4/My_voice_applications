pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline.

Installation: To install pyttsx3 library, type the following command in the terminal

pip3 install pyttsx3

nstall libespeak1 which is a software speech synthesizer for English and some other languages. It is needed to avoid errors while initializing the pyttsx3 engine.e

sudo apt-get install libespeak1


To get started with this library, open up a new Python file, let’s name is tts.py(type nano tts.py to create and open the file) and then import it:

import pyttsx3


Pyttsx3 Engine Initialization: Now we need to initialize the TTS engine.

engine = pyttsx3.init()

The above code initializes the pyttsx3 package. The Instance of the initialized pyttsx3 package is stored in the engine variable. We are calling the variable engine as it works as the engine and converts Text-To-Speech whenever execute the functions from the package.



Now to convert some text, we need to use say() and runAndWait() methods:

# convert this text to speech

text = "This is my first Voice message"
engine.say(text)
 

say() method adds an utterance to speak to the event queue.

# play the speech

engine.runAndWait()


The runAndWait() method runs the actual event loop until all the queued up commands. So you can call the say() method multiple times and run a single runAndWait() method in the end, to hear the synthesis, try it out!

Another important thing regarding the runAndWait() method is that it synchronizes the engine process.



After all the processes are over, we shut down the engine by calling the stop() function.

engine.stop()


Next, exit the nano text editor by click Ctrl+x and then press y.

This is the final code that should be present in the tts.py file:

import pyttsx3

engine = pyttsx3.init()
text = "This is my first Voice message"
engine.say(text)
engine.runAndWait()
engine.stop()


Note: You can type cat tts.py to view the file contents.

Now, run the file by typing python3 tts.py in the terminal and you will be able to hear the Voice output of the text.

This library provides us with some properties that we can tweak based on our needs. For instance, let's get the details of speaking rate:

# get details of speaking rate

rate = engine.getProperty("rate")
print(rate)

Output:

200

Alright, let's change this to 300 (make the speaking rate much faster):

# setting new voice rate (faster)

engine.setProperty("rate", 300)
engine.say(text)
engine.runAndWait()


Or slower:

# slower

engine.setProperty("rate", 100)
engine.say(text)
engine.runAndWait()


Another useful property is voices, which allow us to get details of all voices available on your machine:

# get details of all voices available

voices = engine.getProperty("voices")
print(voices)


Here is the output in my case:

[<pyttsx3.voice.Voice object at 0x000002D617F00A20>, <pyttsx3.voice.Voice object at 0x000002D617D7F898>, <pyttsx3.voice.Voice object at 0x000002D6182F8D30>]

As you can see, my machine has three voice speakers, let's use the second, for example:

# set another voice

engine.setProperty("voice", voices[1].id)
engine.say(text)
engine.runAndWait()
Try this for yourself to get a proper idea of this property.

