print("Jami spotify playlist downloader")

import os
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials
import yt_dlp
import pandas as pd


load_dotenv()  # Load .env file

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")


def get_playlist_songs(playlist_url):
    """Fetch all songs from a Spotify playlist."""
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET
    ))

    playlist_id = playlist_url.split("/")[-1].split("?")[0]
    playlist = sp.playlist(playlist_id)

    songs = []
    for item in playlist['tracks']['items']:
        track = item['track']
        songs.append({
            'name': track['name'],
            'artist': ", ".join(artist['name'] for artist in track['artists']),
            'spotify_url': track['external_urls']['spotify']
        })

    return songs, playlist['name']

def search_and_download(song, artist, folder_name):
    """Search for the song on YouTube and download it as an MP3."""
    query = f"{song} {artist}"
    options = {
        'format': 'bestaudio/best',
        'outtmpl': f'{folder_name}/{song}.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        try:
            ydl.download([f"ytsearch1:{query}"])
            print(f"Downloaded: {song}")
        except Exception as e:
            print(f"Failed to download {song}: {e}")

def save_to_csv(songs, playlist_name):
    """Save the playlist details to a CSV file."""
    df = pd.DataFrame(songs)
    df.to_csv(f"{playlist_name}.csv", index=False)
    print(f"Saved playlist to {playlist_name}.csv")

def main():
    playlist_url = input("Enter Spotify Playlist URL: ")
    songs, playlist_name = get_playlist_songs(playlist_url)

    # Create a folder for the playlist
    if not os.path.exists(playlist_name):
        os.mkdir(playlist_name)

    # Save playlist details to CSV
    save_to_csv(songs, playlist_name)

    # Download songs
    for song in songs:
        search_and_download(song['name'], song['artist'], playlist_name)

    print(f"All songs downloaded in folder: {playlist_name}")

if __name__ == "__main__":
    main()