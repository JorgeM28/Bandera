from tkinter import *

bandera = Tk()
bandera.title("Noruega")
bandera.geometry("700x450")
bandera.resizable(0,0)

bandera.config(bg="white")


frame_azul = Frame(bandera)
frame_azul.config(bg="blue", width=70, height=450)
frame_azul.place(x=223, y=0)


#Frame practica
frame_azul2 = Frame(bandera)
frame_azul2.config(bg="blue", width=700, height=70)
frame_azul2.place(x=0, y=197)


# frame operaciones
frame_rojo1 = Frame(bandera)
frame_rojo1.config(bg="red", width=191, height=167)
frame_rojo1.place(x=0, y=0)

# frame resultados
frame_rojo2 = Frame(bandera)
frame_rojo2.config(bg="red", width=382, height=167)
frame_rojo2.place(x=325, y=0)

frame_rojo3 = Frame(bandera)
frame_rojo3.config(bg="red", width=191, height=167)
frame_rojo3.place(x=0, y=299)

frame_rojo4 = Frame(bandera)
frame_rojo4.config(bg="red", width=382, height=167)
frame_rojo4.place(x=325, y=299)


bandera.mainloop()