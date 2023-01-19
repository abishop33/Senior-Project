import os
import winreg
from tkinter import *

# gather the network info and store it in a list called ipconfig
ipconfig = os.popen("ipconfig").readlines()  # stores the command output in an array
ipconfig.pop(0)
ipconfig.pop(2)
ipconfig.pop(3)

# gather the installed apps and store them in an array turned list called appArray
installed_apps = []
try:
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")
    i = 0
    while True:
        subkey = winreg.EnumKey(key, i)
        subkey_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall" + "\\" + subkey
        app_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkey_path)
        try:
            display_name, _ = winreg.QueryValueEx(app_key, "DisplayName")
            installed_apps.append(display_name)
        except OSError:
            pass
        i += 1
except OSError:
    pass

installed_apps = list(set(installed_apps))
installed_apps.sort()
# print(len(installed_apps))

# initial window config and dynamic variable initialization:
root = Tk()
root.title("D.A.M.N. Agent")
root.geometry("800x750")
getEndpointName = os.popen("hostname").readlines()
endpointName = "Overview of " + str(getEndpointName[0])
info = ipconfig
apps = installed_apps

# textbox setup
T = Text(root, height=18, width=86)
T2 = Text(root, height=18, width=89)

# Create label
l1 = Label(text="Network Details:")
l2 = Label(root, text=endpointName)
l2.config(font=("Courier", 14))
l3 = Label(text="Apps Installed:")

# Create an Exit button. and add the elements in order to the Frame
b1 = Button(root, text="Exit", command=root.destroy)
l2.pack()
l1.pack()
T.pack()
l3.pack()
T2.pack()
b1.pack()

# Insert The network details into Textbox 1. and load apps installed into text box 2
T.insert(END, info)
for i in apps:
    T2.insert(END, i + "\n")

T2.delete('end-1c')

# execute pop up
mainloop()
