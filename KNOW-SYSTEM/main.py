from tkinter import *
from tkinter import filedialog
from datetime import datetime
import psutil
import platform


root = Tk()

root.title("PC information")

root.geometry("800x600")

root.config(bg="black")

uname = platform.uname()

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


Label(root,text="BASIC INFORMATION", bg ="black", fg="lightgreen", font=("Verdana",24)).pack()


Label(root,text=f"System: {uname.system}" , bg ="black", fg="lightgreen", font=("Verdana",10)).pack()
Label(root,text=f"Node Name: {uname.node}" , bg ="black", fg="lightgreen", font=("Verdana",10)).pack()
Label(root,text=f"Release: {uname.release}" , bg ="black", fg="lightgreen", font=("Verdana",10)).pack()
Label(root,text=f"Machine: {uname.machine}" , bg ="black", fg="lightgreen", font=("Verdana",10)).pack()
Label(root,text=f"Processor: {uname.processor}" , bg ="black", fg="lightgreen", font=("Verdana",10)).pack()

Label(root,text="CPU INFORMATION", bg ="black", fg="lightblue", font=("Verdana",18),pady=20).pack(anchor="w")

cpufreq = psutil.cpu_freq()


Label(root, text=f"Max Frequency: {cpufreq.max:.2f}Mhz", bg="black", fg="lightgreen", font=("Verdana", 10)).pack(anchor="w")
Label(root, text=f"Min Frequency: {cpufreq.min:.2f}Mhz", bg="black", fg="lightgreen", font=("Verdana", 10)).pack(anchor="w")
Label(root, text=f"Current Frequency: {cpufreq.current:.2f}Mhz", bg="black", fg="lightgreen", font=("Verdana", 10)).pack(anchor="w")
Label(root, text=f"Physical cores: { psutil.cpu_count(logical=False)} ", bg="black", fg="lightgreen", font=("Verdana", 10)).pack(anchor="w")
Label(root, text=f"Total cores: {psutil.cpu_count(logical=True)}", bg="black", fg="lightgreen", font=("Verdana", 10)).pack(anchor="w")
Label(root, text="CPU Usage Per Core:", bg="black", fg="lightgreen", font=("Verdana", 10)).pack(anchor="w")

for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
    Label(root, text=f"Core {i}: {percentage}%", bg="black", fg="lightgreen", font=("Verdana", 10)).pack(anchor="w")
Label(root, text=f"Total CPU Usage: {psutil.cpu_percent()}%", bg="black", fg="lightgreen", font=("Verdana", 10)).pack(anchor="w")

Label(root,text="MEMORY INFORMATION", bg ="black", fg="lightblue", font=("Verdana",18),pady=20).pack(anchor="w")
#MEMORIA
svmem = psutil.virtual_memory()
swap = psutil.swap_memory()

Label(root, text=f"Total: {get_size(svmem.total)}", bg="black", fg="lightgreen", font=("Verdana", 10)).pack(anchor="w")
Label(root, text=f"Available: {get_size(svmem.available)}", bg="black", fg="lightgreen", font=("Verdana", 10)).pack(anchor="w")
Label(root, text=f"Used: {get_size(svmem.used)}", bg="black", fg="lightgreen", font=("Verdana", 10)).pack(anchor="w")
Label(root, text=f"Percentage: {svmem.percent}%", bg="black", fg="lightgreen", font=("Verdana", 10)).pack(anchor="w")
Label(root, text=f"Total: {get_size(swap.total)}", bg="black", fg="lightgreen", font=("Verdana", 10)).pack(anchor="w")
Label(root, text=f"Free: {get_size(swap.free)}", bg="black", fg="lightgreen", font=("Verdana", 10)).pack(anchor="w")
Label(root, text=f"Used: {get_size(swap.used)}", bg="black", fg="lightgreen", font=("Verdana", 10)).pack(anchor="w")
Label(root, text=f"Percentage: {swap.percent}%", bg="black", fg="lightgreen", font=("Verdana", 10)).pack(anchor="w")


Label(root,text="DISK INFORMATION", bg ="black", fg="lightblue", font=("Verdana",18),pady=20).pack(anchor="w")
#INFORMACIÓN DEL DISCO DURO
Label(root, text="Partitions and Usage:", bg="black", fg="lightgreen", font=("Verdana", 10)).pack(anchor="w")

partitions = psutil.disk_partitions()

for partition in partitions:
    Label(root, text=f"=== Device: {partition.device} ===", bg="black", fg="lightgreen", font=("Verdana", 10)).pack(anchor="w")
    Label(root, text=f"Mountpoint: {partition.mountpoint}", bg="black", fg="lightgreen", font=("Verdana", 10)).pack(anchor="w")
    Label(root, text=f"  File system type: {partition.fstype}", bg="black", fg="lightgreen", font=("Verdana", 10)).pack(anchor="w")
    

    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        continue
    print(f"  Total Size: {get_size(partition_usage.total)}")
    print(f"  Used: {get_size(partition_usage.used)}")
    print(f"  Free: {get_size(partition_usage.free)}")
    print(f"  Percentage: {partition_usage.percent}%")
disk_io = psutil.disk_io_counters()
print(f"Total read: {get_size(disk_io.read_bytes)}")
print(f"Total write: {get_size(disk_io.write_bytes)}")




root.mainloop()