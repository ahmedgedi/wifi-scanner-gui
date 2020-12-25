import tkinter as tk
import tkinter.messagebox
import sys, socket

window = tk.Tk()
window.title('Wifi Device scanner')

header = tk.Label(text="Open ports on your network")
router_ip= tk.Entry(master=window, width=50)

devices_found = []


def list_devices(devices_found):
    for i in devices_found:
        for j in range(1, len(devices_found) + 1):
            window.columnconfigure(0, weight=1, minsize=50)

            frame = tk.Frame(master=window, relief=tk.GROOVE, highlightbackground="black", highlightcolor="black", highlightthickness=1 )
            frame.grid(row=j+2, column=0, padx=3, sticky="ew")

            lbl = tk.Label(master=frame, text=i, bg="white")
            lbl.pack(fill=tk.X)


def pingsweep(ip):
    tkinter.messagebox.showinfo(title=None, message="Scanning your local network...")
    try:
        for port in range(1, 1024):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((ip, port))

            if result == 0:
                devices_found.append(f"Port {port} is open!")
            s.close()

    except socket.gaierror:
        print("\n Hostname could not be resolved. Exiting program...")
        sys.exit()

    except socket.error:
        print("\n Couldn't connect to server. Exiting program...")
        sys.exit()


def start_scan(event):
    # TODO: simple check for now, need to add more stringent IP checking rules
    if len(router_ip.get()) < 4: 
        return print('invalid router IP')

    pingsweep(router_ip.get())
    list_devices(devices_found)


scan_btn = tk.Button(master=window, text="Scan your network")
scan_btn.bind("<Button-1>", start_scan)

header.grid(row=2, sticky="ew")
scan_btn.grid(row=1, column=0, sticky="ew", pady=2)
router_ip.grid(row=0, column=0, sticky="ew", pady=1)

window.mainloop()