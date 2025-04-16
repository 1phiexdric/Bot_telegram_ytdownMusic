import os

import yt_dlp


def descargar_musica(url, carpeta="Descargas"):

    """
    Descarga la música de un video de YouTube en formato MP3.

    Args:
        url (str): La URL del video de YouTube.
        carpeta (str): La carpeta donde se guardará la música descargada. Por defecto es "musica".

    Returns:
        None
    """

    try:
        os.makedirs(carpeta, exist_ok=True)
        salida = os.path.join(carpeta, '%(title)s.%(ext)s')
        opciones = {
            'format': 'bestaudio/best',
            'outtmpl': f'{carpeta}/%(title)s.%(ext)s', 
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '160',
        }],
            'ffmpeg_location': '/usr/bin/ffmpeg',
            'cookiefile': './cookies.txt',  # Ruta al archivo de cookies
        }
        with yt_dlp.YoutubeDL(opciones) as ydl:
            #ydl.download([url])
            info = ydl.extract_info(url, download=True)
            salida = ydl.prepare_filename(info)  # Obtener la ruta del archivo generado
            salida = os.path.splitext(salida)[0] + ".mp3"  # Cambiar extensión a .mp3
            return salida
    except yt_dlp.utils.DownloadError as e:
        print(f"ocurrio un error: {e}")
    

if __name__ == "__main__":
    music_url = input("Ingresa la url del video: ")
    descargar_musica(music_url)


