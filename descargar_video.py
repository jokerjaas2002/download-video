import yt_dlp
import tkinter as tk
from tkinter import messagebox, ttk

def obtener_formatos(url):
    ydl_opts = {'format': 'best'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info_dict = ydl.extract_info(url, download=False)
            formats = info_dict.get('formats', [])
            return [(f['format_id'], f['ext'], f['height']) for f in formats if 'height' in f]
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al obtener formatos: {e}")
            return []

def descargar_video(url, formato):
    ydl_opts = {'format': formato}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            messagebox.showinfo("Éxito", "Video descargado exitosamente!")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

def iniciar_descarga():
    url = url_entry.get()
    formato_seleccionado = formato_combobox.get()
    if url and formato_seleccionado:
        descargar_video(url, formato_seleccionado)
    else:
        messagebox.showwarning("Advertencia", "Por favor, introduce una URL válida y selecciona un formato.")

def cargar_formatos():
    url = url_entry.get()
    if url:
        formatos = obtener_formatos(url)
        formato_combobox['values'] = [f"{f[0]} ({f[1]}, {f[2]}p)" for f in formatos]
        if formatos:
            formato_combobox.current(0)  # Seleccionar el primer formato por defecto

# Configuración de la ventana principal
root = tk.Tk()
root.title("Descargador de Videos de YouTube")

# Etiqueta y campo de entrada para la URL
url_label = tk.Label(root, text="Introduce la URL del video de YouTube:")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Botón para cargar formatos
load_button = tk.Button(root, text="Cargar Formatos", command=cargar_formatos)
load_button.pack(pady=5)

# Menú desplegable para seleccionar el formato
formato_combobox = ttk.Combobox(root, width=50)
formato_combobox.pack(pady=5)

# Botón para iniciar la descarga
download_button = tk.Button(root, text="Descargar Video", command=iniciar_descarga)
download_button.pack(pady=20)

# Ejecutar la aplicación
root.mainloop()