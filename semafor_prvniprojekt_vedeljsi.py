from tkinter import *

okno = Tk()
okno.geometry("400x800+1200+100")
def aktivni(val):
    global rychlost
    rychlost = int(val)
okno.config(bg="black")
okno.title("Semafor")
rychlost = 2000
frame = Frame(okno, background = "black")
frame.pack(side=RIGHT)
scale = Scale(frame,from_=100, to=5000, length=400, orient=VERTICAL, tickinterval=500, showvalue=0, troughcolor="green", command=aktivni, bg="black", fg="green", font=("arial", 20))
scale.pack()
scale.set(rychlost)
def vychozi():
    global rychlost
    rychlost = 2000
    scale.set(rychlost)
    

#damne tlačitko na vychozi hodnotu
tlačitko = Button(frame, text = "výchozí", command = vychozi, bg = "black", fg="green", font=("arial", 20))
tlačitko.pack()



obrazek = PhotoImage(file = "C:\\Users\\mikul\\OneDrive\\Plocha\\python\\Projekt_Kalkulačka\\Python_calc\\logo2.png")
text = Label(text = "Semafor", bg = "black", fg="green",font=('arial',30), justify=CENTER, relief=SUNKEN,borderwidth=10, image = obrazek,
             compound=TOP)
text.pack(side=TOP)
canva = Canvas(okno, width=170, height=380, background="black")
canva.pack()
cervena = canva.create_oval(30, 10, 150, 130, fill="red")
zluta = canva.create_oval(30, 130, 150, 250, fill="yellow")
zelena = canva.create_oval(30, 250, 150, 370, fill="green")





# cervena = Label(ramecek,text = "", background="red", height=5, width=10 )
# cervena.pack(pady= 14)

# zluta = Label(ramecek,text = "", background="yellow", height=5, width=10 )
# zluta.pack(pady= 14)

# zelena = Label(ramecek,text = "", background="green", height=5, width=10)
# zelena.pack(pady=14)

smer = "cervena"
prechod = None
def cerveny():
    global smer, prechod, rychlost
    
    canva.itemconfig(cervena, fill = "red")
    canva.itemconfig(zelena, fill = "gray")
    canva.itemconfig(zluta, fill = "gray")
    prechod = okno.after(rychlost, zluty) 
    smer = "cervena"
   


def zluty():
    global smer, prechod
    if smer == "cervena":
         
        canva.itemconfig(cervena, fill = "gray")
        canva.itemconfig(zelena, fill = "gray")
        canva.itemconfig(zluta, fill = "yellow")
        prechod = okno.after(rychlost, zeleny) 
    else:
        canva.itemconfig(cervena, fill = "gray")
        canva.itemconfig(zelena, fill = "gray")
        canva.itemconfig(zluta, fill = "yellow")
        prechod = okno.after(rychlost, cerveny) 

def zeleny():
    global smer, prechod
    
    canva.itemconfig(cervena, fill = "gray")
    canva.itemconfig(zelena, fill = "green")
    canva.itemconfig(zluta, fill = "gray")
    prechod = okno.after(rychlost,zluty)
    smer = "zelena" 


x = IntVar()

def zapnout():
    global prechod
    if(x.get() == 1):
        cerveny()
    else:

        okno.after_cancel(prechod)
        canva.itemconfig(cervena, fill = "red")
        canva.itemconfig(zelena, fill = "green")
        canva.itemconfig(zluta, fill = "yellow")
        

def vyber():
    if x.get() == 0:
        if(y.get()==0):
        
            canva.itemconfig(cervena, fill = "red")
            canva.itemconfig(zelena, fill = "gray")
            canva.itemconfig(zluta, fill = "gray")
        elif(y.get()==1):
            canva.itemconfig(cervena, fill = "gray")
            canva.itemconfig(zelena, fill = "gray")
            canva.itemconfig(zluta, fill = "yellow")
        elif(y.get()==2):
            canva.itemconfig(cervena, fill = "gray")
            canva.itemconfig(zelena, fill = "green")
            canva.itemconfig(zluta, fill = "gray")
        else:
            canva.itemconfig(cervena, fill = "red")
            canva.itemconfig(zelena, fill = "green")
            canva.itemconfig(zluta, fill = "yellow")


y = IntVar()
moznosti = ["červena","žluta","zelena", "reset"]
for a in range(len(moznosti)):
    radio = Radiobutton(okno,text = moznosti[a], variable=y, value=a, command = vyber, font =("Arial",20), indicatoron=1, padx = 40, bg = "black", fg = "green"
                       ,activebackground="black", activeforeground="green", relief= RIDGE, bd=3)
    radio.pack()


potrvzeno = Checkbutton(okno, text="rozsvítit semafor", variable=x, offvalue = 0, onvalue=1, command = zapnout, font =("Arial",20), bg="black", foreground="green"
                        ,activebackground="black", activeforeground="green")
potrvzeno.pack()



okno.mainloop()

