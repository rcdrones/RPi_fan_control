
import time
import tkinter as tk



def reflash_data():
	tmpFile = open( '/sys/class/thermal/thermal_zone0/temp' )
	cpu_temp_raw = tmpFile.read()
	tmpFile.close()
	cpu_temp = round(float(cpu_temp_raw)/1000, 1)
	cpu_temp_var.set(str(cpu_temp)) 

	window.after(1000,reflash_data)


window = tk.Tk()
window.title("Fan Control Program")
window.geometry("400x200")

cpu_temp_var = tk.StringVar()




temp_lable = tk.Label( window,
          textvariable = cpu_temp_var,
          bg = "green",
          font = ("Arial",12),
          width = 20,height = 2)

temp_lable.place(x=100, y=100, anchor='nw')


window.after(100,reflash_data)

window.mainloop()
