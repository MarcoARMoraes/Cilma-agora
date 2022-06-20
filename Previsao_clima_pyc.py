import requests
from tkinter import *

#CRIAÇÃO DA JANELA
janela_principal = Tk()
janela_principal.title("CLIMA AGORA")
janela_principal.geometry("340x360")
janela_principal.resizable(False, False)


def previsao_clima():
    api_key = "997a0917ca53d680598b7e189411de9e"
    cidade = entrada_procura_cidade.get()
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br"

    requisicao = requests.get(link)
    requisicao_dic = (requisicao.json())
    descricao = requisicao_dic['weather'][0]['description']
    temperatura = requisicao_dic['main']['temp'] - 273.15
    sensacao_termica = requisicao_dic['main']['feels_like'] - 273.15
    lbl_resultado['text'] = (f'Temperatura no momento em {cidade.title()}: \n{temperatura:.2f}Cº. '
                             f'\nSensação térmica: {sensacao_termica:.2f}Cº'
                             f'\nCondições: {descricao}.')

    if descricao == "céu limpo":
        lbl_imagem_vazia.grid_forget()
        lbl_imagem_sol.grid(row=3, column=0)
    elif descricao == "nublado":
        lbl_imagem_vazia.grid_forget()
        lbl_imagem_nublado.grid(row=3, column=0)
    elif descricao == "chuva":
        lbl_imagem_vazia.grid_forget()
        lbl_imagem_chuva.grid(row=3, column=0)
    elif descricao == "chuva leve":
        lbl_imagem_vazia.grid_forget()
        lbl_imagem_chuva.grid(row=3, column=0)

def limpa_resultado():
    lbl_resultado['text'] = ""
    lbl_imagem_nublado.grid_forget()
    lbl_imagem_sol.grid_forget()
    lbl_imagem_chuva.grid_forget()
    lbl_imagem_vazia.grid(row=3, column=0)

frame_titulo = Frame(janela_principal)
frame_titulo.grid(row=0, columnspan=2)
lbl_titulo = Label(frame_titulo, width=20, bg="light blue", text="CLIMA AGORA",
                   font="Arial 20 bold", fg="white")
lbl_titulo.grid(row=0, column=0)
lbl_vazia_1 = Label(frame_titulo, text="")
lbl_vazia_1.grid(row=1, column=0)

#ESCOLHA DA CIDADE
frame_cidade = Frame(janela_principal)
frame_cidade.grid(row=1, column=0)
lbl_cidade = Label(frame_cidade, text="Cidade: ", font="Arial 10 bold")
lbl_cidade.grid(row=0, column=0)
entrada_procura_cidade = Entry(frame_cidade)
entrada_procura_cidade.grid(row=0, column=1)
lbl_vazia_2 = Label(frame_cidade, text="")
lbl_vazia_2.grid(row=1, column=0)
btn_procura_cidade = Button(frame_cidade, text="OK", font="Arial 10 bold", fg="white",
                            bg="gray", width=10, relief="raised", command=previsao_clima)
btn_procura_cidade.grid(row=2, column=0)
btn_limpa_resultado = Button(frame_cidade, text="Limpar", font="Arial 10 bold", fg="white",
                             bg="gray", width=10, relief="raised", command=limpa_resultado)
btn_limpa_resultado.grid(row=2, column=1)
lbl_vazia_3 = Label(frame_cidade, text="")
lbl_vazia_3.grid(row=3, column=0)

#RESULTADO
lbl_resultado = Label(janela_principal, text="", font="Arial 10 bold", anchor=N,
                      width=40, height=4)
lbl_resultado.grid(row=2, column=0)

img_sol = PhotoImage(file="sol.png")
img_nublado = PhotoImage(file="nublado.png")
img_chuva = PhotoImage(file="chuva.png")


lbl_imagem_vazia = Label(janela_principal, width=46, height=5)
lbl_imagem_vazia.grid(row=3, column=0)
lbl_imagem_sol = Label(janela_principal, width=322, image=img_sol)
#lbl_imagem_sol.grid(row=3, column=0)
lbl_imagem_nublado = Label(janela_principal, width=322, image=img_nublado)
#lbl_imagem_nublado.grid(row=3, column=0)
lbl_imagem_chuva = Label(janela_principal, width=322, image=img_chuva)
#lbl_imagem_chuva.grid(row=3, column=0)

#ASSINATURA
lbl_assinatura = Label(janela_principal, text="Desenvolvido por Marco Moraes", font="Arial 10 italic", bd=10)
lbl_assinatura.grid(row=4, columnspan=2)

#UTILIZAÇÃO DO API DE CLIMA
"""api_key = "997a0917ca53d680598b7e189411de9e"
cidade = str(input('Digite a cidade: '))
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br"

requisicao = requests.get(link)
requisicao_dic = (requisicao.json())
descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp'] - 273.15
print(f'Temperatura no momento em {cidade.title()}: {temperatura:.2f}Cº. \nCondições: céu {descricao}.')"""

janela_principal.mainloop()