import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Pour redimensionner et utiliser les images
import socket

# Adresse IP de la STM32
IP_STM32 = "192.168.1.113"  # ou celle que tu as configurée
PORT = 6454             # même port que dans udp_bind()


# Création de la fenêtre principale
root = tk.Tk()
root.title("Interface LED STM32")
root.geometry("400x300")

# Variables pour les Checkbuttons R, G, B
r_var = tk.BooleanVar()
g_var = tk.BooleanVar()
b_var = tk.BooleanVar()


# Variables pour image sélectionnée
selected_image = tk.StringVar(value="Aucune")

# === Fonctions ===

def select_image(name):
    selected_image.set(name)
    print(f"Image sélectionnée : {name}")
    update_image_buttons()

def update_image_buttons():
    if selected_image.get() == "Image1":
        btn_img1.config(bg="lightblue")
        btn_img2.config(bg="SystemButtonFace")
    elif selected_image.get() == "Image2":
        btn_img2.config(bg="lightblue")
        btn_img1.config(bg="SystemButtonFace")

def send_info():
    rgb = []
    if r_var.get(): rgb.append("R")
    if g_var.get(): rgb.append("G")
    if b_var.get(): rgb.append("B")
    info = f"Image : {selected_image.get()} RGB : {rgb})"

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(info.encode(), (IP_STM32, PORT))
    print(f"{info} envoyé à {IP_STM32}:{PORT}")

    messagebox.showinfo("Envoi", f"{info} envoyé à {IP_STM32}:{PORT}")


# === Chargement des images ===

# On charge et redimensionne les icônes
img1_raw = Image.open("interface_graphique/icone_coeur.png").resize((80, 80))
img2_raw = Image.open("interface_graphique/icone_etoile.png").resize((80, 80))
img1_icon = ImageTk.PhotoImage(img1_raw)
img2_icon = ImageTk.PhotoImage(img2_raw)

# === Layout ===

# Cadre à gauche pour les boutons image
frame_left = tk.Frame(root)
frame_left.pack(side=tk.LEFT, padx=10, pady=10)

tk.Label(frame_left, text="Choix image :").pack()

btn_img1 = tk.Button(frame_left, image=img1_icon, command=lambda: select_image("Image1"))
btn_img1.pack(pady=5)

btn_img2 = tk.Button(frame_left, image=img2_icon, command=lambda: select_image("Image2"))
btn_img2.pack(pady=5)

# Cadre à droite pour les canaux RGB
frame_right = tk.Frame(root)
frame_right.pack(side=tk.RIGHT, padx=10, pady=10)

tk.Label(frame_right, text="Canaux RGB :").pack()
tk.Checkbutton(frame_right, text="R", variable=r_var).pack()
tk.Checkbutton(frame_right, text="G", variable=g_var).pack()
tk.Checkbutton(frame_right, text="B", variable=b_var).pack()

# Bouton central pour "envoyer"
tk.Button(root, text="Envoyer", command=send_info).pack(pady=20)

# Boucle principale
root.mainloop()
