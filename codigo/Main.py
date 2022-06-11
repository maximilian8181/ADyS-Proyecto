import tkinter
import spaceinvader_max
import Tetris
import Snake
import pong

ventana = tkinter.Tk()
ventana.geometry("500x700")

nombre = tkinter.Label(ventana,text="ArcaEscom",font="arial 15")
fondo= tkinter.Label(ventana, bg="grey")
marca = tkinter.Label(ventana,text="Derechos reservados",font="arial 15")
espacio = tkinter.Label(ventana,text="",height=10,bg="grey")


juego_1= tkinter.Button(ventana, text="Space Invader",command= spaceinvader_max.Run , width=25 , height=5,justify="center")
juego_3= tkinter.Button(ventana, text="Snake",command= Snake.Run                    , width=25 , height=5,justify="center")
juego_4= tkinter.Button(ventana, text="Pong",command= pong.Run                      , width=25 , height=5,justify="center")
#juego_2= tkinter.Button(ventana, text="Tetris",command= Tetris.Run)

nombre.pack(side=tkinter.TOP)
fondo.pack(fill= tkinter.BOTH, expand=True)

juego_1.pack(fill=tkinter.X)
juego_3.pack(fill=tkinter.X)
juego_4.pack(fill=tkinter.X)
#juego_2.pack()
espacio.pack( fill=tkinter.X)
marca.pack(side=tkinter.BOTTOM)

ventana.mainloop()

