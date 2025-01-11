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
    songs_dir = os.path.join('playlists', folder_name)
    
    # Clean the song name to be filesystem-friendly
    safe_song_name = "".join(x for x in song if x.isalnum() or x in (' ', '-', '_')).strip()
    output_path = os.path.join(songs_dir, f'{safe_song_name}.mp3')
    
    options = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(songs_dir, f'{safe_song_name}.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'quiet': True,
        'ffmpeg_location': r'C:\ffmpeg\bin'
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        try:
            ydl.download([f"ytsearch1:{query}"])
            print(f"Downloaded: {song}")
            return output_path
        except Exception as e:
            print(f"Failed to download {song}: {e}")
            return None

def save_to_csv(songs, playlist_name):
    """Save the playlist details to a CSV file."""
    csv_dir = 'csv'
    if not os.path.exists(csv_dir):
        os.makedirs(csv_dir)
    
    df = pd.DataFrame(songs)
    csv_path = os.path.join(csv_dir, f"{playlist_name}.csv")
    df.to_csv(csv_path, index=False)
    print(f"Saved playlist to {csv_path}")

def main():
    # Create base directories if they don't exist
    for dir_name in ['songs', 'csv']:
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

    playlist_url = input("Enter Spotify Playlist URL: ")
    songs, playlist_name = get_playlist_songs(playlist_url)

    # Create a folder for the playlist inside songs directory
    songs_playlist_dir = os.path.join('songs', playlist_name)
    if not os.path.exists(songs_playlist_dir):
        os.makedirs(songs_playlist_dir)

    # Save playlist details to CSV
    save_to_csv(songs, playlist_name)

    # Download songs
    for song in songs:
        search_and_download(song['name'], song['artist'], playlist_name)

    print(f"All songs downloaded in folder: {songs_playlist_dir}")

if __name__ == "__main__":
    main()