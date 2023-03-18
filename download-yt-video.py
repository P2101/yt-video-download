import pytube # pip install pytube

url = input('Enter video url: ')

path = "C:/Users/Pau Pons/OneDrive/Escritorio/Pau/youtube" # the storage path of the video

pytube.YouTube(url).streams.get_highest_resolution().download(path) # download the video
