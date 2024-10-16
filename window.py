from tkinter import *


animes = [['Kaguya-sama', 'Comédia', 'Seinen', 'Curta'],
          ['Nana', 'Drama', 'Shoujo', 'Média'],
          ['Darling in the Franxx', 'Ação', 'Shounen', 'Curta']]

def btn_clicked():
    display_selected()


window = Tk()

window.title("Anime Chooser")

estilos = [
    'Ação',
    'Comédia',
    'Drama',
    'Romance',
    'Suspense',
]

demografia = [
    'Shounen',
    'Shoujo',
    'Seinen',
    'Josei',
    'Kodomomuke',
]

duracao = [
    'Curta',
    'Média',
    'Longa',
]


window.geometry("1000x600")
window.configure(bg = "#f7c7ff")
canvas = Canvas(
    window,
    bg = "#f7c7ff",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    534.0, 300.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    264.0, 187.5,
    image = entry0_img)

entry0 = Entry(
    font= ('Helvetica', 13),
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = 90.0, y = 161,
    width = 348.0,
    height = 51)

clicked0 = StringVar(window)

dropEstilos = OptionMenu(window, clicked0, *estilos)

dropEstilos.place(
    x=90.0, y=161,
    width=348.0,
    height=51)

dropEstilos.config(font=('Helvetica', 12), bg="WHITE")

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    264.0, 300.0,
    image = entry1_img)

entry1 = Entry(
    font= ('Helvetica', 13),
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry1.place(
    x = 90.0, y = 273,
    width = 348.0,
    height = 52)

clicked1 = StringVar(window)

dropDemografia = OptionMenu(window, clicked1, *demografia)

dropDemografia.place(
    x=90.0, y=273,
    width=348.0,
    height=51)

dropDemografia.config(font=('Helvetica', 12), bg="WHITE")

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    766.5, 324.5,
    image = entry2_img)

entry2 = Label(
    font= ('Helvetica', 17),
    bd = 0,
    bg = "#f4fcff",
    highlightthickness = 0,
    text = "Resultado aqui")

entry2.place(
    x = 613.0, y = 161,
    width = 307.0,
    height = 325)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    266.0, 412.0,
    image = entry3_img)

entry3 = Entry(
    font= ('Helvetica', 13),
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry3.place(
    x = 92.0, y = 385,
    width = 348.0,
    height = 52)

clicked3 = StringVar(window)

dropDuracao = OptionMenu(window, clicked3, *duracao)

dropDuracao.place(
    x=90.0, y=385,
    width=348.0,
    height=51)

dropDuracao.config(font=('Helvetica', 12), bg="WHITE")

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 141, y = 474,
    width = 261,
    height = 60)


def display_selected():
    flag = False
    estilo = clicked0.get()
    demografia = clicked1.get()
    duracao = clicked3.get()
    animeresults = []
    for items in animes:
        if (items[1] == estilo) and (items[2] == demografia) and (items[3] == duracao):
            animechoice = items[0]
            animeresults.append(animechoice)
            flag = True

    if flag==True:
        entry2.config(text=str(animeresults))
    else:
        entry2.config(text="Nenhuma correspondência\nfoi encontrada.")




window.resizable(False, False)
window.mainloop()
