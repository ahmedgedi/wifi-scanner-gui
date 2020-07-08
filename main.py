import tkinter as tk

window = tk.Tk()
window.title('Wifi Device scanner')

def start_scan():
    return print('Scanning.....')


header = tk.Label(text="Devices on your network")
scan_btn = tk.Button(master=window, text="Scan your network", command=start_scan)

devices_found = ['No devices found']


for i in devices_found:
    for j in range(1, len(devices_found) + 1):
        window.columnconfigure(0, weight=1, minsize=50)

        frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=2)
        frame.grid(row=j, column=0, padx=3, pady=3, sticky="ew")

        lbl = tk.Label(master=frame, text=i, bg="white")
        lbl.pack(fill=tk.X)

header.grid(row=1, sticky="ew")
scan_btn.grid(row=0, column=0, sticky="ew", pady=2)


window.mainloop()