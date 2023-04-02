from pytube import YouTube, Playlist

link = "https://youtube.com/shorts/QOMidWm_VUQ?feature=share"
youtube = YouTube(link)

# print(youtube.title)
# print(youtube.thumbnail_url)

# Download only audios
# audios = youtube.streams.filter(only_audio=True)

# Download both audio and video
videos = youtube.streams

vid = list(enumerate(videos))
for i in vid:
    print(i)

streaming = int(input("Enter: "))
videos[streaming].download()
print('Successfully Download.')


# Download full playlist

url = "https://youtube.com/playlist?list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3"
py = Playlist(url)
print(f"Downloading: {py.title}")

for video in py.videos:
    video.streams.first().download()
