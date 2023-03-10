from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

URL = "https://www.billboard.com/charts/hot-100/"
YOUR_CLIENT_ID = os.environ["CLIENT_ID"]
YOUR_CLIENT_SECRET = os.environ["CLIENT_SECRET"]
YOUR_APP_REDIRECT_URI = os.environ["APP_REDIRECT_URI"]

travel_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# Scraping Billboard 100

response = requests.get(URL + travel_date)
top_songs_html = response.text
soup = BeautifulSoup(top_songs_html, "html.parser")

top_100_songs = soup.find_all("h3", class_="a-no-trucate")
top_100_songs_list = [songs.getText().strip("\n") for songs in top_100_songs]

# Spotify Authentication

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=YOUR_CLIENT_ID,
                                               client_secret=YOUR_CLIENT_SECRET,
                                               redirect_uri=YOUR_APP_REDIRECT_URI,
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt"))
user_id = sp.current_user()["id"]
# print(user_id)

# Search Spotify for songs by title and artist

song_uri = []
year = travel_date.split("-")[0]
for song in top_100_songs_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uri.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating new private playlist in Spotify
new_playlist = sp.user_playlist_create(user_id, name=f"{travel_date} Billboard 100", public=False)
print(new_playlist)

# Adding the songs to the playlist
sp.playlist_add_items(playlist_id=new_playlist['id'], items=song_uri)
