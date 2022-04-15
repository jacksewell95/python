import tkinter as tk
import tkinter.ttk as ttk

# Create a new window using tk.Tk() and assign to 'window'
window = tk.Tk()
# Add a widget - use tk.Label() to add text
# Width and height are measured in text units, so will naturally be taller than it is wide 
message = tk.Label(text="Python is cool! :D",
                   fg="#00ff00",
                   bg="black",
                   width=20,
                   height=10)
# Add the Label widget to the window using its .pack() method
message.pack()
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
