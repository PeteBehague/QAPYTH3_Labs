import wmi
import subprocess

processes = {}
i = 0
def getfirstproc():
    return processes[0]

def getnextproc():
    global i
    i += 1
    if (i < len(processes)):
        return processes[i]
    else:
        return None

# Mainline
f = wmi.WMI()

try:

    j = 0
    for process in f.Win32_Process():
        processes[j] = (process.ProcessId, process.ParentProcessId, process.Name)
        j += 1
except IndexError as e:
    print("Something bad heappened")
    exit(0)
print("List Created")
