from PIL import Image

# Ruta del logo PNG
logo_path = "hybrid_logo.png"
# Ruta de salida del icono ICO
icon_path = "icon.ico"

try:
    # Abrir imagen y redimensionarla (opcional)
    img = Image.open(logo_path)

    # Guardar como .ico (con varios tamaños incluidos)
    img.save(icon_path, format="ICO", sizes=[(16, 16), (32, 32), (48, 48), (256, 256)])

    print(f"✅ ¡Icono creado correctamente en '{icon_path}'!")
except FileNotFoundError:
    print(f"❌ No se encontró el archivo '{logo_path}'.")
except Exception as e:
    print(f"⚠️ Ocurrió un error: {e}")