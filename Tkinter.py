import tkinter as tk
import tkinter.ttk as ttk

# Create a new window using tk.Tk() and assign to 'window'
window = tk.Tk()
# Add a widget - use tk.Label() to add text
# Width and height are measured in text units, so will naturally be taller than it is wide
message = tk.Label(text = "Enter name:",
                   fg = "#00ff00",
                   bg = "black",
                   width = 40,
                   height = 2)
# Add the Label widget to the window using its .pack() method
message.pack()

# Entry gives small text box that user can enter text into
# Takes similar parameters to Label and Button (bot not height)
entry = tk.Entry(fg = "#00ff00",
                 bg = "black",
                 width = 40)

entry.pack()

entry.insert(0, "Jack")
name = entry.get()
print(f"Name: {name}")

# Button can be configured to call function when clicked
# Takes similar parameters to label
button = tk.Button(text = "Next",
                   fg="black",
                   bg = "#00ff00",
                   width = 40,
                   height = 5)

# Button needs packing to appear in window
button.pack()

# Tkinter sizes the window as small as it can
# Tell Python to run the Tkinter event loop
# This listens for events (button clicks / keypresses) and blocks any following code until the window is closed
window.mainloop()

# Repeat using the themed widgets ttk.Label()
new_window = tk.Tk()
new_message = ttk.Label(text="Themed widgets aren't so good. The new parameters don't work :'(",
                        foreground="white",
                        background="black",)
new_message.pack()
new_window.mainloop()
