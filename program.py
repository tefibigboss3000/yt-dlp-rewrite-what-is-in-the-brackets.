import os
import re


print("==========================")
print("yt-dlp remove the '[]' ")
ruta_del_usuario = input("Enter the path to the folder containing your MP3, WAV, or FLAC files here. ") #<--- for the gringos: here you need to enter the path to the folder where your songs are located


RUTA_CARPETA = ruta_del_usuario.strip().strip('"').strip("'")


def limpiar_nombres_mp3(ruta):
    if not os.path.exists(ruta):
        print("error, the path does not exist")
        return
    # para avisar cuando no se encuentre la ruta

    patron = r"\s*\[.*?\]"

    # ahora se lista la ruta
    archivos = os.listdir(ruta)
    
    contador = 0

    for archivo in archivos:
        if archivo.lower().endswith(('.mp3','.wav', '.flac')):
            nombre_base, extension = os.path.splitext(archivo)
            
            nuevo_nombre_base = re.sub(patron, "", nombre_base).strip()
            
            nuevo_archivo = nuevo_nombre_base + extension

            if archivo != nuevo_archivo:
                ruta_antigua = os.path.join(ruta, archivo)
                ruta_nueva = os.path.join(ruta, nuevo_archivo)
                
                try:
                    os.rename(ruta_antigua, ruta_nueva)
                    print(f"Renaming the song: '{archivo}' ➔ '{nuevo_archivo}'")
                    contador += 1
                except Exception as e:
                    print(f"Error renaming {archivo}: {e}, Please check if your file is in MP3, WAV or FLAC format.")

    print(f"\nThe process finished: you renamed it. {contador} files.")




limpiar_nombres_mp3(RUTA_CARPETA)