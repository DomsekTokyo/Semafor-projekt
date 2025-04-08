from tkinter import *

okno = Tk()
okno.geometry("500x1000+1200+0")
frame1 = None
frame2 = None
frame3 = None
obrazek = PhotoImage(file = "C:\\Users\\mikul\\OneDrive\\Plocha\\python\\Projekt_Kalkulačka\\Python_calc\\logo2.png")

def Semafor():
    global frame , frame2, frame3
    # if frame3:
    #     frame3.destroy()

    if 'frame' in globals() and frame is not None:
        frame.destroy()
        frame = None
    if 'frame2' in globals() and frame2 is not None:
        frame2.destroy()
        frame2 = None
    if 'frame3' in globals() and frame3 is not None:
        frame3.destroy()
        frame3 = None
    
    def aktivni(val):
        global rychlost
        rychlost = int(val)
    
    okno.config(bg="black")
    okno.title("Semafor")
    rychlost = 2000
    frame = Frame(okno, background = "black")
    frame.pack(side = RIGHT)
    
    frame2 = Frame(okno, background="black")
    frame2.pack(side=LEFT)

    scale = Scale(frame, from_=100, to=5000, length=400, orient=VERTICAL, tickinterval=500, showvalue=0, troughcolor="green", command=aktivni, bg="black", fg="green", font=("arial", 20))
    scale.pack()

    scale.set(rychlost)

    def vychozi():
        global rychlost
        rychlost = 2000
        scale.set(rychlost)

    tlačitko = Button(frame, text="výchozí", command=vychozi, bg="black", fg="green", font=("arial", 20))
    tlačitko.pack(pady=10)

    text = Label(frame2, text="Semafor", bg="black", fg="green", font=('arial',30), justify=CENTER, relief=SUNKEN, borderwidth=10, image=obrazek, compound=TOP)
    text.pack(pady=10)
    
    canva = Canvas(frame2, width=170, height=380, background="black")
    canva.pack(pady=10)
    
    cervena = canva.create_oval(30, 10, 150, 130, fill="red")
    zluta = canva.create_oval(30, 130, 150, 250, fill="yellow")
    zelena = canva.create_oval(30, 250, 150, 370, fill="green")

    smer = "cervena"
    prechod = None
    
    def cerveny():
        global smer, prechod, rychlost
        canva.itemconfig(cervena, fill="red")
        canva.itemconfig(zelena, fill="gray")
        canva.itemconfig(zluta, fill="gray")
        prechod = okno.after(rychlost, zluty)
        smer = "cervena"
    
    def zluty():
        global smer, prechod
        if smer == "cervena":
            canva.itemconfig(cervena, fill="gray")
            canva.itemconfig(zelena, fill="gray")
            canva.itemconfig(zluta, fill="yellow")
            prechod = okno.after(rychlost, zeleny)
        else:
            canva.itemconfig(cervena, fill="gray")
            canva.itemconfig(zelena, fill="gray")
            canva.itemconfig(zluta, fill="yellow")
            prechod = okno.after(rychlost, cerveny)

    def zeleny():
        global smer, prechod
        canva.itemconfig(cervena, fill="gray")
        canva.itemconfig(zelena, fill="green")
        canva.itemconfig(zluta, fill="gray")
        prechod = okno.after(rychlost, zluty)
        smer = "zelena"

    x = IntVar()

    def zapnout():
        global prechod
        if x.get() == 1:
            cerveny()
        else:
            okno.after_cancel(prechod)
            canva.itemconfig(cervena, fill="red")
            canva.itemconfig(zelena, fill="green")
            canva.itemconfig(zluta, fill="yellow")
    
    def vyber():
        if x.get() == 0:
            if y.get() == 0:
                canva.itemconfig(cervena, fill="red")
                canva.itemconfig(zelena, fill="gray")
                canva.itemconfig(zluta, fill="gray")
            elif y.get() == 1:
                canva.itemconfig(cervena, fill="gray")
                canva.itemconfig(zelena, fill="gray")
                canva.itemconfig(zluta, fill="yellow")
            elif y.get() == 2:
                canva.itemconfig(cervena, fill="gray")
                canva.itemconfig(zelena, fill="green")
                canva.itemconfig(zluta, fill="gray")
            else:
                canva.itemconfig(cervena, fill="red")
                canva.itemconfig(zelena, fill="green")
                canva.itemconfig(zluta, fill="yellow")

    y = IntVar()
    moznosti = ["červena", "žluta", "zelena", "reset"]
    
    for a in range(len(moznosti)):
        radio = Radiobutton(frame2, text=moznosti[a], variable=y, value=a, command=vyber, font=("Arial", 20), indicatoron=1, padx=40, bg="black", fg="green", activebackground="black", activeforeground="green", relief=RIDGE, bd=3)
        radio.pack(pady=5)

    potrvzeno = Checkbutton(frame2, text="rozsvítit semafor", variable=x, offvalue=0, onvalue=1, command=zapnout, font=("Arial", 20), bg="black", foreground="green", activebackground="black", activeforeground="green")
    potrvzeno.pack(pady=10)

def Texttt():
    global frame, frame2, frame3
    try:
        if frame is not None:
            frame.destroy()
            frame = None
        if frame2 is not None:
            frame2.destroy()
            frame2 = None
    except:
        print("")
    
    if frame3 is not None:  # Ujistíme se, že frame3 zničíme pouze, pokud není None
        frame3.destroy()
        frame3 = None
        
    okno.config(background="black")
    frame3 = Frame(okno, background="black")
    frame3.pack()


    canvas = Canvas(frame3, width=400, height=400, bg="black")
    canvas.pack()

    # Tvar srdce složený ze dvou oblouků a trojúhelníku
    canvas.create_oval(100, 50, 200, 150, fill="red", outline="red")  # Levý kruh
    canvas.create_oval(205, 50, 305, 150, fill="red", outline="red")  # Pravý kruh
    canvas.create_oval(150, 100, 250, 150, fill="red", outline="red")
    canvas.create_polygon(301,120,104,120, 200, 280,  fill="red" )
    canvas.create_text(200, 150, text="Janička", font=("Arial", 20), fill="white")
    


frame_buttons = Frame(okno, bg="black")  # Vytvoříme frame pro tlačítka
frame_buttons.pack(side=TOP, padx=10, pady=10)  # Tento frame umístíme nahoře

but = Button(frame_buttons, text="Semafor", command=Semafor, font=('arial', 10), bg = "black", fg = "white")
but.pack(side=LEFT, padx=10)  # Tlačítko Semafor

but1 = Button(frame_buttons, text="Zkouška", command=Texttt, font=('arial', 10), bg = "black", fg = "white")
but1.pack(side=LEFT, padx=10)  # Tlačítko Zkouška

okno.mainloop()
