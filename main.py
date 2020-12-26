import tkinter as tk
import tkinter.messagebox
import sys, socket, time
import re

window = tk.Tk()
window.title('Wifi Device scanner')

header = tk.Label(text="Open ports on your device")
router_ip= tk.Entry(master=window, width=50)

devices_found = []

def list_devices(devices_found):
    for i, j in enumerate(devices_found):
        window.columnconfigure(0, weight=1, minsize=50)

        frame = tk.Frame(master=window, relief=tk.GROOVE, highlightbackground="black", highlightthickness=1 )
        frame.grid(row=i+2, column=0, padx=5, sticky="ew")

        lbl = tk.Label(master=frame, text=j, bg="white", pady=2)
        lbl.pack(fill=tk.X)


def pingsweep(ip):
    try:
        for port in range(1, 1024):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((ip, port))

            if result == 0:
                devices_found.append(f"Port {port} is open!")
            s.close()

    except socket.gaierror:
        tk.messagebox.showerror("ERROR", "Hostname could not be resolved. Exiting program...")
        window.destroy()

    except socket.error:
        tk.messagebox.showerror("ERROR",  "Couldn't connect to server. Exiting program...")
        window.destroy()


def start_scan(event):
    pat = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    if pat.match(router_ip.get()):
        continue
    else:
        tk.messagebox.showerror("ERROR", "Invalid IP address provided. Closing..")
        window.destroy()
    
    pingsweep(router_ip.get())
    list_devices(devices_found)


scan_btn = tk.Button(master=window, text="Scan your network")
scan_btn.bind("<Button-1>", start_scan)

header.grid(row=2, sticky="ew")
scan_btn.grid(row=1, column=0, sticky="ew", pady=2)
router_ip.grid(row=0, column=0, sticky="ew", pady=1)

window.mainloop()