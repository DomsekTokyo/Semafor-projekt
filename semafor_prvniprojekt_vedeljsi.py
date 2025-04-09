from tkinter import *

okno = Tk()
okno.geometry("500x1000+1200+0")
okno.config(bg = "black")
frame = None
frame2 = None
frame3 = None
frame4 = None
frame5 = None




obrazek = PhotoImage(file = "C:\\Users\\mikul\\OneDrive\\Plocha\\python\\Projekt_Kalkulačka\\Python_calc\\logo2.png")

def Semafor():
    global frame , frame2, frame3, frame4, frame5, frame6
   
    
    
    but.config(font= ("Arial", 10))
    but1.config(font= ("Arial", 10))

    destroy_frame(frame=frame6)
    destroy_frame(frame=frame)
    destroy_frame(frame=frame2)
    destroy_frame(frame=frame3)
    destroy_frame(frame=frame4)
    destroy_frame(frame=frame5)
    
    
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
    import random
    global frame, frame2, frame3, x, barva, name_label, tmave_pismo, frame4, frame5, frame6
   
    names = [
    "Adéla", "Alena", "Andrea", "Aneta", "Barbora", "Blanka", "Diana", "Dominika", "Eva", "Hana", 
    "Helena", "Ilona", "Jana", "Karolína", "Kristýna", "Lucie", "Martina", "Monika", "Nikol", 
    "Petra", "Radka", "Renáta", "Simona", "Tereza", "Veronika", "Zuzana", "Anežka", "Beáta", "Bohuslava", 
    "Cecílie", "Dana", "Dita", "Ema", "Ester", "Fanny", "Gabriela", "Hana", "Iva", "Ivana", "Jitka", 
    "Julie", "Karla", "Klára", "Lenka", "Liana", "Lucie", "Marcela", "Michaela", "Milan", "Monika", 
    "Nina", "Olga", "Pavla", "Renáta", "Růžena", "Sandra", "Silvie", "Tatiana", "Věra", "Viktorie", 
    "Vladimíra", "Zdenka", "Zlata", "Alice", "Berta", "Blanka", "Božena", "Dita", "Dominika", "Edita", 
    "Emílie", "Johana", "Julie", "Kamila", "Květoslava", "Ladislava", "Laura", "Ludmila", "Margarita", 
    "Milada", "Naděžda", "Nikola", "Oľga", "Petra", "Radoslava", "Sára", "Veronika", "Vladislava", 
    "Xenie", "Yveta", "Zuzana", "Marcela", "Magdalena", "Bohumila", "Kateřina", "Zora", "Marta", 
    "Ilona", "Gita", "Petra", "Sylvie", "Irena", "Lucie", "Denisa", "Alžběta", "Monika", "Jana", "Radmila",
    "Milena", "Drahomíra", "Karla", "Lenka", "Adéla", "Kamila", "Mariana", "Michaela", "Tatjana", 
    "Zuzana", "Lívia", "Tereza", "Ivana", "Věra", "Erika", "Rita", "Renáta", "Veronika", "Martina", 
    "Dagmar", "Olga", "Irena", "Klára", "Marta", "Marcela", "Monika", "Petra", "Karolína", "Eva"
]
    name = None
    
    
    
    
    but.config(font= ("Arial", 10))
    but1.config(font= ("Arial", 10))

    destroy_frame(frame=frame)
    destroy_frame(frame=frame2)
    destroy_frame(frame=frame3)
    destroy_frame(frame=frame4)
    destroy_frame(frame=frame5)
        
    
    
    
    if frame3 is not None:  # Ujistíme se, že frame3 zničíme pouze, pokud není None
        frame3.destroy()
        frame3 = None
        
    okno.config(background="black")
    frame3 = Frame(okno, background="black")
    frame3.pack()


    canvas = Canvas(frame3, width=400, height=400, bg="black")
    canvas.pack()

    import random
    vlastnosti = [
    "milá", 
    "loajální", 
    "laskavá", 
    "upřímná", 
    "vstřícná", 
    "pozitivní", 
    "inteligentní", 
    "kreativní", 
    "tolerantní", 
    "empatická", 
    "přátelská", 
    "spolehlivá", 
    "usměvavá", 
    "odvážná", 
    "čestná", 
    "oddaná", 
    "trpělivá", 
    "šarmantní", 
    "nápomocná", 
    "zodpovědná"
]
    # Tvar srdce složený ze dvou oblouků a trojúhelníku
    canvas.create_oval(100, 50, 200, 150, fill="red", outline="red")  # Levý kruh
    canvas.create_oval(205, 50, 305, 150, fill="red", outline="red")  # Pravý kruh
    canvas.create_oval(150, 100, 250, 150, fill="red", outline="red")
    canvas.create_polygon(301,120,104,120, 200, 280,  fill="red" )
    name_label = canvas.create_text(200, 150, text= name, font=("Arial", 20), fill="white")
    tmave_pismo = None
    def Red():
        global barva, name_label, tmave_pismo
        tmave_pismo = False
        barva = "červená"
        canvas.create_oval(100, 50, 200, 150, fill="red", outline="red")  # Levý kruh
        canvas.create_oval(205, 50, 305, 150, fill="red", outline="red")  # Pravý kruh
        canvas.create_oval(150, 100, 250, 150, fill="red", outline="red")
        canvas.create_polygon(301,120,104,120, 200, 280,  fill="red" )
        name_label = canvas.create_text(200, 150, text= name, font=("Arial", 20), fill="white")
    def Blue():
        global barva, name_label, tmave_pismo
        tmave_pismo = False
        barva = "modrá"
        canvas.create_oval(100, 50, 200, 150, fill="blue", outline="blue")  # Levý kruh
        canvas.create_oval(205, 50, 305, 150, fill="blue", outline="blue")  # Pravý kruh
        canvas.create_oval(150, 100, 250, 150, fill="blue", outline="blue")
        canvas.create_polygon(301,120,104,120, 200, 280,  fill="blue" )
        name_label = canvas.create_text(200, 150, text= name, font=("Arial", 20), fill="white")
    def Pink():
        global barva, name_label, tmave_pismo
        tmave_pismo = True
        barva = "růžová"
        canvas.create_oval(100, 50, 200, 150, fill="pink", outline="pink")  # Levý kruh
        canvas.create_oval(205, 50, 305, 150, fill="pink", outline="pink")  # Pravý kruh
        canvas.create_oval(150, 100, 250, 150, fill="pink", outline="pink")
        canvas.create_polygon(301,120,104,120, 200, 280,  fill="pink" )
        name_label = canvas.create_text(200, 150, text= name, font=("Arial", 20), fill="black")
    def Yellow():
        global barva, name_label, tmave_pismo
        tmave_pismo = True
        barva = "žlutá"
        canvas.create_oval(100, 50, 200, 150, fill="yellow", outline="yellow")  # Levý kruh
        canvas.create_oval(205, 50, 305, 150, fill="yellow", outline="yellow")  # Pravý kruh
        canvas.create_oval(150, 100, 250, 150, fill="yellow", outline="yellow")
        canvas.create_polygon(301,120,104,120, 200, 280,  fill="yellow")
        name_label = canvas.create_text(200, 150, text= name, font=("Arial", 20), fill="black")
    x = None
    barva = "červená"

    def Flirt():
        global x, barva
        if x is not None:
            canvas.delete(x)
        if barva == "žlutá" or barva == "růžová":
            x = canvas.create_text(200, 170, text=random.choice(vlastnosti), font=("Arial", 15), fill="black")
        else:
            x = canvas.create_text(200, 170, text=random.choice(vlastnosti), font=("Arial", 15), fill="white")
    frame4 = Frame(okno, bg= "black",  width=360, height=50)
    frame4.place(x =80, y = 350)

    frame5 = Frame(okno, bg= "black",  width=340, height=150)
    frame5.place(x =100, y = 500)
    flirt = Button(frame5,text="Flirt", fg = "white", bg = "black", relief="sunken", bd = 5, font = ("Arial", 30), command=Flirt)
    flirt.place(x = 0, y = 0)
    
    def zadej_jmeno():
        global name_label , tmave_pismo
        
        
        
        
        if name_label is not None:
            canvas.delete(name_label)

        

        
        name = random.choice(names)
        
        if(tmave_pismo):
            name_label = canvas.create_text(200, 150, text=name, font=("Arial", 20), fill="black")
        else:
            name_label = canvas.create_text(200, 150, text=name, font=("Arial", 20), fill="white")


    jmeno = Button(frame5,text="Jméno", fg = "white", bg = "black", relief="sunken", bd = 5, font = ("Arial", 30), command=zadej_jmeno)
    jmeno.place(x = 140, y = 0)

    button = Button(frame4,text="Žlutá", fg = "white", bg = "black", relief="sunken", bd = 5, font = (20), command = Yellow)
    button.place(x =0, y = 0)
    button2 = Button(frame4,text="Modrá", fg = "white", bg = "black", relief="sunken", bd = 5, font = (20), command = Blue)
    button2.place(x =75, y = 0)
    button2 = Button(frame4,text="Růžová", fg = "white", bg = "black", relief="sunken", bd = 5, font = (20), command = Pink)
    button2.place(x =160, y = 0)
    button2 = Button(frame4,text="Červená", fg = "white", bg = "black", relief="sunken", bd = 5, font = (20), command = Red)
    button2.place(x =255, y = 0)


    
def destroy_frame(frame):
    if frame is not None:
        frame.destroy()
        return None
    return frame




frame_buttons = Frame(okno, bg="black")  # Vytvoříme frame pro tlačítka
frame_buttons.pack(side=TOP, padx=10, pady=10)  # Tento frame umístíme nahoře

but = Button(frame_buttons, text="Semafor", command=Semafor, font=('arial', 30), bg = "black", fg = "white")
but.pack(side=LEFT, padx=10)  # Tlačítko Semafor

but1 = Button(frame_buttons, text="Srdce", command=Texttt, font=('arial', 30), bg = "black", fg = "white")
but1.pack(side=LEFT, padx=10)  # Tlačítko Zkouška

frame6 = Frame(okno, bg = "black")
frame6.pack(side= TOP)


info = Label(frame6, text = "Zvolte si aplikaci", font = ("Arial", 30), bg = "black", fg = "white")
info.pack(side = TOP, anchor="center")
okno.mainloop()
