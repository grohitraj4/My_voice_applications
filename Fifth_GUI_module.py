Tkinter is the only framework that’s built into the Python standard library. Tkinter has several strengths. It is cross-platform, so the same code works on Windows, macOS, and Linux. Visual elements are rendered using native operating system elements, so applications built with Tkinter look like they belong on the platform where they’re run.

Things to do:
Get started with Tkinter with a “Hello, World!” application
Work with widgets, such as buttons and text boxes
Control your application layout with geometry managers
Make your applications interactive by associating button clicks to Python functions

You can install the latest version of Python with the correct Tcl/Tk version from the Universe repository with the following command:

sudo apt-get install python3-tk


With your Python interpreter shell open(type python3 in the terminal and hit enter), the first thing you need to do is import the Python GUI Tkinter module:

>>> import tkinter as tk


A window is an instance of Tkinter’s Tk class. Go ahead and create a new window and assign it to the variable window:

>>> window = tk.Tk() 

Adding a Widget
Now that you have a window, you can add a widget. Use the tk.Label class to add some text to a window. Create a Label widget with the text "Hello, Tkinter" and assign it to a variable called greeting:

>>> greeting = tk.Label(text="Hello, Tkinter")
 

The window you created earlier doesn’t change. You just created a Label widget, but you haven’t added it to the window yet. There are several ways to add widgets to a window. Right now, you can use the Label widget’s .pack() method:

>>> greeting.pack()


When you .pack() a widget into a window, Tkinter sizes the window as small as it can while still fully encompassing the widget. Now execute the following:

>>> window.mainloop()
 

Nothing seems to happen, but notice that a new prompt does not appear in the shell.

window.mainloop() tells Python to run the Tkinter event loop. This method listens for events, such as button clicks or keypresses, and blocks any code that comes after it from running until the window it’s called on is closed. Go ahead and close the window you’ve created, and you’ll see a new prompt displayed in the shell.

Displaying Text and Images With Label Widgets

Label widgets are used to display text or images. The text displayed by a Label widget can’t be edited by the user. It’s for display purposes only.

You can also control the width and height of a label with the width and height parameters.

label = tk.Label(
    text="Hello, World!",
    fg="white",
    bg="black",
    width=10,
    height=10
)
label.pack()

It may seem strange that the label in the window isn’t square even though the width and height are both set to 10. This is because the width and height are measured in text units. One horizontal text unit is determined by the width of the character "0", or the number zero, in the default system font. Similarly, one vertical text unit is determined by the height of the character "0".

Displaying Clickable Buttons With Button Widgets

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
button.pack()

Getting User Input With Entry Widgets

entry = tk.Entry(fg="yellow", bg="blue", width=50)


First, import tkinter and create a new window:

>>> import tkinter as tk
>>> window = tk.Tk()
 

Now create a Label and an Entry widget:

>>> label = tk.Label(text="Name")
>>> entry = tk.Entry()

The Label describes what sort of text should go in the Entry widget. It doesn’t enforce any sort of requirements on the Entry, but it tells the user what your program expects them to put there. You need to .pack() the widgets into the window so that they’re visible: 

>>> label.pack()
>>> entry.pack()

Now you’ve got some text entered into the Entry widget, but that text hasn’t been sent to your program yet. You can use .get() to retrieve the text and assign it to a variable called name:

>>> name = entry.get()
>>> name
'Voice Apps Training'


On the opposite end of the spectrum, you can also .insert() text into an Entry widget. But before that let us clear the text we entered inside the entry. Either you can clear the text manually in the GUI using the backspace or you can use the following command:

>>> entry.delete(0, tk.END)


The first argument determines the starting index(that is 0), and the deletion continues up to but not including the index passed as the second argument(that is special constant tk.END to remove all text in an Entry



Now we can insert text from code using the insert method by running the following command:

>>> entry.insert(0, "Rohit")

>>> entry.insert(tk.END, "Raj")


Now Let’s add a text at the beginning:

>>> entry.insert(0, "Mr. ")

Assigning Widgets to Frames With Frame Widgets

To get a feel for how this works, write a script that creates two Frame widgets called frame_a and frame_b. In this script, frame_a contains a label with the text "I'm in Frame A", and frame_b contains the label "I'm in Frame B". Here’s one way to do this. Open a new file frames.py by type nano frames.py and add the following code in it:

import tkinter as tk

window = tk.Tk()
frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(master=frame_a, text="I'm in Frame A")
label_a.pack()
label_b = tk.Label(master=frame_b, text="I'm in Frame B")
label_b.pack()

frame_a.pack()
frame_b.pack()
window.mainloop()
Note that frame_a is packed into the window before frame_b. The window that opens shows the label in frame_a above the label in frame_b:

Now see what happens when you swap the order of frame_a.pack() and frame_b.pack() in the above code:

import tkinter as tk

window = tk.Tk()
frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(master=frame_a, text="I'm in Frame A")
label_a.pack()
label_b = tk.Label(master=frame_b, text="I'm in Frame B")
label_b.pack()

# Swap the order of `frame_a` and `frame_b`
frame_b.pack()
frame_a.pack()
window.mainloop()

.grid() works by splitting a window or Frame into rows and columns. You specify the location of a widget by calling .grid() and passing the row and column indices to the row and column keyword arguments, respectively. Both row and column indices start at 0, so a row index of 1 and a column index of 2 tells .grid() to place a widget in the third column of the second row.

 

Let us write a code for creating a window asks users to enter the First Name and Last Name. To do that open a new python file by typing nano gridLayout.py and type the following code in it:

import tkinter as tk

window = tk.Tk()
frame1 = tk.Frame()
frame2 = tk.Frame()


#This will place label1 and label2 in frame1
label1 = tk.Label(master=frame1, text=”First Name”)
label2 = tk.Label(master=frame1, text=”Last Name”)
label1.pack()
label2.pack()

#This will place entry1 and entry2 in frame2
entry1 = tk.Entry(master=frame2)
entry2 = tk.Entry(master=frame2)
entry1.pack()
entry2.pack()

#Now using the grid() geometry manager we will place the frame1
#and frame2 on the window
frame1.grid(row=0, column=0)
frame2.grid(row=0, column=1)
window.mainloop()


Then, save the file and run it by typing python3 gridLayout.py. You will see a window like this:g












