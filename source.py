from tkinter import*
import math


print("Apogee(km):")
ap = int(input())

while True:
    print("Perigee(km):")
    pr = int(input())
    if pr > ap:
        print("Incorrect value")
    else:
        break
while True:
	print("Altitude(km):")
	alt = int(input())
	if alt > ap or alt < pr:
		print("Incorrect value")
	else:
		break

tk = Tk()
tk.title("ORBIT SIMULATOR")
r1 = ap+6378#до центра земли
r2 = pr+6378
#вычесления
a = (r1+r2)/2#большая полуось
u = 398600.4415888
velkm2 = u*((2/(alt+6378))-(1/a))#квадрат скорости в м/c
velkm = math.sqrt(velkm2)#корень
c = Canvas(tk, height=500, width=500, bg='black')
c.pack()
c.create_line(0, 250, 500, 250, fill='white')
c.create_oval(200, 200, 300, 300, fill='white')

vel_label = c.create_text(250, 10, text=(velkm, 'km/s'), fill = 'white')
alt_label = c.create_text(250, 30, text=('alt:', alt, 'km'), fill = 'white')

def update_labs():
	global velkm
	global velkm2
	global alt
	global a
	global u
	global v
	global ap
	global pr
	global r1
	global r2
	#система обновления переменных
	vel_label.config(text=(velkm, 'km/s'))
	alt_label.config(text=('alt:', alt, 'km'))
	a = (r1+r2)/2
	velm2 = u*((2/(alt+6378))-(1/a))
	velm = sqrt = math.sqrt(velkm2)
	r1 = ap+6378
	r2 = pr+6378
	a = (r1+r2)/2




while True:
	#обнова высоты
	print("New altitude(km):")
	alt = int(input())
	if alt > ap or alt < pr:
		print("Incorrect value")
	else:
		break
	update_labs()

tk.mainloop()
