import tkinter as tk
import tkinter.ttk as ttk

# Create a new window using tk.Tk() and assign to 'window'
window = tk.Tk()
# Add a widget - use tk.Label() to add text
message = tk.Label(text="Python is cool! :D")
# Add the Label widget to the window using its .pack() method
message.pack()
# Tkinter sizes the window as small as it can
# Tell Python to run the Tkinter event loop
# This listens for events (button clicks / keypresses) and blocks any following code until the window is closed
window.mainloop()

# Repeat using the themed widgets ttk.Label()
new_window = tk.Tk()
new_message = ttk.Label(text="Themed widgets are cooler!! :D")
new_message.pack()
new_window.mainloop()
