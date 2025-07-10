import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import json
import subprocess
import os


# Nombre del archivo de configuración
ARCHIVO_EMPRESAS = "empresas.json"


# Cargar lista de empresas desde el archivo JSON
def cargar_empresas():
    try:
        with open(ARCHIVO_EMPRESAS, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        messagebox.showerror("Error", f"No se encontró el archivo '{ARCHIVO_EMPRESAS}'")
        return []
    except json.JSONDecodeError:
        messagebox.showerror("Error", f"El archivo '{ARCHIVO_EMPRESAS}' no tiene un formato válido.")
        return []


# Acción al hacer clic en "Iniciar"
def iniciar_modulo():
    empresa_seleccionada = var_empresa.get()
    modulo_seleccionado = var_modulo.get()

    if empresa_seleccionada == "Seleccione una empresa":
        messagebox.showwarning("Advertencia", "Debe seleccionar una empresa antes de continuar.")
        return
    if modulo_seleccionado == "Seleccione un módulo":
        messagebox.showwarning("Advertencia", "Debe seleccionar un módulo antes de continuar.")
        return

    for empresa in empresas:
        if empresa["nombre"] == empresa_seleccionada:
            ruta = empresa["modulos"].get(modulo_seleccionado)
            if ruta and os.path.exists(ruta):
                directorio = os.path.dirname(ruta)
                subprocess.Popen(ruta, cwd=directorio)  # ✅ Ahora sí encuentra el .ini
                root.destroy()
            else:
                messagebox.showerror("Error", f"No se encontró la ruta para el módulo:\n{modulo_seleccionado}")
            return


# Acción al cambiar de empresa
def on_empresa_cambia(*args):
    empresa_seleccionada = var_empresa.get()
    if empresa_seleccionada == "Seleccione una empresa":
        menu_modulos['menu'].delete(0, 'end')
        var_modulo.set("Seleccione un módulo")
        return

    for empresa in empresas:
        if empresa["nombre"] == empresa_seleccionada:
            modulos = list(empresa["modulos"].keys())
            var_modulo.set("Seleccione un módulo")

            menu_modulos['menu'].delete(0, 'end')
            for m in modulos:
                menu_modulos['menu'].add_command(label=m, command=tk._setit(var_modulo, m))
            return


def centrar_ventana(ventana, ancho, alto):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")


# Iniciar aplicación
root = tk.Tk()
root.title("MultiLanzadorHB - HybridLite v1.00.01")
centrar_ventana(root, 500, 350)
root.resizable(False, False)

# Icono de la aplicación
try:
    root.iconbitmap("icon.ico")
except:
    print("Icono no encontrado")

# Frame principal
frame_principal = ttk.Frame(root)
frame_principal.pack(expand=True, padx=10, pady=10)

# Logo
try:
    img = Image.open("hybrid_logo.png")
    img = img.resize((100, 100), Image.LANCZOS)
    logo = ImageTk.PhotoImage(img)
    label_logo = ttk.Label(frame_principal, image=logo)
    label_logo.image = logo  # Mantener referencia
    label_logo.grid(row=0, column=0, padx=(0, 10), pady=10, sticky="nsew")
except Exception as e:
    ttk.Label(frame_principal, text="Logo no disponible", foreground="red").grid(
        row=0, column=0, padx=(0, 10), pady=10, sticky="nsew"
    )
    print("No se pudo cargar el logo:", e)

# Frame para formularios (empresa y módulo)
frame_form = ttk.Frame(frame_principal)
frame_form.grid(row=0, column=1, sticky="nsew")

# Cargar empresas
empresas = cargar_empresas()

if empresas:
    nombres_empresas = [e["nombre"] for e in empresas]

    # Variable para selección de empresa
    var_empresa = tk.StringVar(root)
    var_empresa.set("Seleccione una empresa")

    # Etiqueta y menú de empresas
    ttk.Label(frame_form, text="Empresa:", font=("Arial", 10)).grid(
        row=0, column=0, sticky="e", padx=5, pady=10
    )
    opciones_empresas = ["Seleccione una empresa"] + nombres_empresas
    menu_empresas = ttk.OptionMenu(frame_form, var_empresa, *opciones_empresas)
    menu_empresas.config(width=25)
    menu_empresas.grid(row=0, column=1, padx=5, pady=10, sticky="w")

    # Variable para selección de módulo
    var_modulo = tk.StringVar(root)
    var_modulo.set("Seleccione un módulo")

    # Etiqueta y menú de módulos
    ttk.Label(frame_form, text="Módulo:", font=("Arial", 10)).grid(
        row=1, column=0, sticky="e", padx=5, pady=10
    )
    menu_modulos = ttk.OptionMenu(frame_form, var_modulo, "Seleccione un módulo")
    menu_modulos.config(width=25)
    menu_modulos.grid(row=1, column=1, padx=5, pady=10, sticky="w")

    # Asociar evento de cambio de empresa
    var_empresa.trace_add("write", on_empresa_cambia)

else:
    ttk.Label(
        frame_principal,
        text="No hay empresas configuradas.",
        foreground="red",
        font=("Arial", 10)
    ).pack(pady=10)

# Botón de inicio
btn_iniciar = ttk.Button(
    frame_principal,
    text="Iniciar Sistema",
    width=20,
    command=iniciar_modulo
)
btn_iniciar.grid(row=1, column=0, columnspan=2, pady=20)

# Panel de estado (footer)
footer_frame = ttk.Frame(root)
footer_frame.pack(side="bottom", fill="x")

footer_texto = (
    "© 2025 Arksoft Integradores de Sistemas, C.A. RIF: J310994692 - Todos los derechos reservados\n"
    "Contacto: +58 424-3672111 | arksoft.sistemas@gmail.com"
)

ttk.Label(
    footer_frame,
    text=footer_texto,
    font=("Arial", 8),
    justify="center",
    wraplength=480
).pack(pady=5)

# Iniciar la aplicación
root.mainloop()