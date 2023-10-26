import pypokedex
import PIL.Image, PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO

#main window
window = tk.Tk()
window.geometry('600x700')
window.title('My Pokedex')
window.config(padx=10,pady=10)

#title label
title_label = tk.Label(window, text="Pokedex")
title_label.config(font=("Arial",32))
title_label.pack(padx=10,pady=10)

#image space
pokemon_image1 = tk.Label(window)
pokemon_image1.pack(padx=10,pady=10)
pokemon_image2 = tk.Label(window)
pokemon_image2.pack(padx=10,pady=10)

#pokemon info
pokemon_information = tk.Label(window)
pokemon_information.config(font=('Arial',20))
pokemon_information.pack(padx=10,pady=10)

#pokemon types
pokemon_types = tk.Label(window)
pokemon_types.config(font=('Arial',20))
pokemon_types.pack(padx=10,pady=10)

#function request from pokeapi
def load_pokemon():
    pokemon = pypokedex.get(name=text_id_name.get(1.0, 'end-1c'))

    http = urllib3.PoolManager()
    response1 =http.request('GET',pokemon.sprites.front.get('default'))
    image1 = PIL.Image.open(BytesIO(response1.data))
    #response2 =http.request('GET',pokemon.sprites.front.get('shiny'))
    #image2 = PIL.Image.open(BytesIO(response2.data))
   
    img1 = PIL.ImageTk.PhotoImage(image1)
    pokemon_image1.config(image=img1)
    pokemon_image1.image = img1
    #img2 = PIL.ImageTk.PhotoImage(image2)
    #pokemon_image2.config(image=img2)
    #pokemon_image2.image = img2

    #dex number, name and types from the requests
    pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}".title())
    pokemon_types.config(text=' - '.join([t for  t in pokemon.types]).title())

label_id_name = tk.Label(window,text='Dex number or Name')
label_id_name.config(font=('Arial',20))
label_id_name.pack(padx=10,pady=10)

text_id_name = tk.Text(window,height=1)
text_id_name.config(font=('Arial',20))
text_id_name.pack(padx=10,pady=10)

#button that enables the function
btn_load = tk.Button(window,text='Load Pokemon', command=load_pokemon)
btn_load.config(font=('Arial',20))
btn_load.pack(padx=10,pady=10)

window.mainloop()