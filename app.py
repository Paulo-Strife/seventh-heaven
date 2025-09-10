import cartesianas_para_cilindricas as cpc
import cartesianas_para_esféricas as cpe
import cilindricas_cartesianas as cc
import cilindricas_para_esféricas as cpe2
import esfericas_cartesiana as es
import esféricas_cilindricas as ec
import tkinter as tk
from tkinter import ttk

def converter():
    try:
        x = float(entry_x.get())
        y = float(entry_y.get())
        z = float(entry_z.get())
        escolha = tipo.get()

        if escolha == "Cartesiana para Cilíndricas":
            rho, theta, z_cil = cpc.cartesianas_para_cilindricas(x, y, z)
            resultado.set(f"Coordenadas Cilíndricas:\nρ = {rho:.2f}\nθ = {theta:.2f}\nz = {z_cil:.2f}")

        elif escolha == "Cartesianas paraEsféricas":
            r, theta, phi = cpe.cartesianas_para_esfericas(x, y, z)
            resultado.set(f"Coordenadas Esféricas:\nr = {r:.2f}\nθ = {theta:.2f}\nφ = {phi:.2f}")

        elif escolha == "Cilíndricas para Cartesianas":
            rho = x
            theta = y
            z_cil = z
            x_cart, y_cart, z_cart = cc.cilindricas_para_cartesianas(rho, theta, z_cil)
            resultado.set(f"Coordenadas Cartesianas:\nx = {x_cart:.2f}\ny = {y_cart:.2f}\nz = {z_cart:.2f}")

        elif escolha == "Cilíndricas para Esféricas":
            rho = x
            theta = y
            z_cil = z
            r, theta_esf, phi = cpe2.cilindricas_para_esféricas(rho, theta, z_cil)
            resultado.set(f"Coordenadas Esféricas:\nr = {r:.2f}\nθ = {theta_esf:.2f}\nφ = {phi:.2f}")

        elif escolha == "Esféricas para Cartesianas":
            r = x
            theta = y
            phi = z
            x_cart, y_cart, z_cart = es.esfericas_para_cartesianas(r, theta, phi)
            resultado.set(f"Coordenadas Cartesianas:\nx = {x_cart:.2f}\ny = {y_cart:.2f}\nz = {z_cart:.2f}")

        elif escolha == "Esféricas para Cilíndricas":
            r = x
            theta = y
            phi = z
            rho, theta_cil, z_cil = ec.esfericas_para_cilindricas(r, theta, phi)
            resultado.set(f"Coordenadas Cilíndricas:\nρ = {rho:.2f}\nθ = {theta_cil:.2f}\nz = {z_cil:.2f}")

        else:
            resultado.set("Selecione o tipo de conversão que deseja")
    except ValueError:
        resultado.set("Valor inválido, tente novamente")

def atualizar_labels(event=None):
    escolha = tipo.get()
    if "Cartesianas" in escolha:
        label_x.config(text="x:")
        label_y.config(text="y:")
        label_z.config(text="z:")
    elif "Cilíndricas" in escolha:
        label_x.config(text="ρ:")
        label_y.config(text="θ:")
        label_z.config(text="z:")
    elif "Esféricas" in escolha:
        label_x.config(text="r:")
        label_y.config(text="θ:")
        label_z.config(text="φ:")

# Janela principal
janela = tk.Tk()
janela.title("Conversor de coordenadas")
janela.geometry("500x500")

ttk.Label(janela, text="Conversor de Coordenadas", font=("Arial", 16)).pack(pady=10)

# Menu de seleção
tipo = tk.StringVar()
tipo.set("Cartesianas para Cilíndricas")
ttk.Label(janela, text="Escolha o tipo de conversão:").pack()

opcoes = [
    "Cartesianas para Cilíndricas",
    "Cartesianas para Esféricas",
    "Cilíndricas para Cartesianas",
    "Cilíndricas para Esféricas",
    "Esféricas para Cartesianas",
    "Esféricas para Cilíndricas"
]

combo_tipo = ttk.Combobox(janela, textvariable=tipo, values=opcoes, state="readonly")
combo_tipo.pack()
combo_tipo.bind("<<ComboboxSelected>>", atualizar_labels)

# Entradas
frame_imports = ttk.Frame(janela)
frame_imports.pack(pady=10)

label_x = ttk.Label(frame_imports, text="x:")
label_x.grid(row=0, column=0)
entry_x = ttk.Entry(frame_imports)
entry_x.grid(row=0, column=1)

label_y = ttk.Label(frame_imports, text="y:")
label_y.grid(row=1, column=0)
entry_y = ttk.Entry(frame_imports)
entry_y.grid(row=1, column=1)

label_z = ttk.Label(frame_imports, text="z:")
label_z.grid(row=2, column=0)
entry_z = ttk.Entry(frame_imports)
entry_z.grid(row=2, column=1)

# Botão
ttk.Button(janela, text="Converter", command=converter).pack(pady=10)

# Resultado
resultado = tk.StringVar()
ttk.Label(janela, textvariable=resultado, font=("Arial", 13), foreground="black").pack(pady=10)

janela.mainloop()