import yt_dlp # py -m pip install pytube

url = input("Enter video url: ")

path = r"C:\Users\Name\Downloads"

ydl_opts = {
    'outtmpl': path + '/%(title)s.%(ext)s',
    'format': 'best'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Video descargado correctamente")
