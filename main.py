import tkinter as tk

window = tk.Tk()
window.title('Wifi Device scanner')

header = tk.Label(text="Devices on your network")
# creating the rows
for i in range(1,6):
    window.columnconfigure(0, weight=1, minsize=50)

    frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=2)
    frame.grid(row=i, column=0, padx=3, pady=3, sticky="ew")

    lbl = tk.Label(master=frame, text=f"Device {i}", bg="white")
    lbl.pack(fill=tk.X)

header.grid(row=0, sticky="ew")

window.mainloop()