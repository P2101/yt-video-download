import pytube # pip install pytube

url = input('Enter video url: ')

# the storage PATH of the video
path = "C:/Users/NAME/Desktop/folder" 

pytube.YouTube(url).streams.get_highest_resolution().download(path) 
