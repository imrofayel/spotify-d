from flask import Flask, render_template, request, jsonify
import os
from main import get_playlist_songs, search_and_download, save_to_csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_playlist():
    playlist_url = request.form.get('playlist_url')
    
    try:
        # Get playlist songs
        songs, playlist_name = get_playlist_songs(playlist_url)
        
        # Create necessary directories
        songs_playlist_dir = os.path.join('playlists', playlist_name)
        if not os.path.exists(songs_playlist_dir):
            os.makedirs(songs_playlist_dir)
            
        # Save playlist to CSV
        save_to_csv(songs, playlist_name)
        
        # Download each song
        for song in songs:
            search_and_download(song['name'], song['artist'], playlist_name)
            
        return jsonify({
            'status': 'success',
            'message': f'Successfully downloaded playlist: {playlist_name}',
            'playlist_name': playlist_name,
            'song_count': len(songs)
        })
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True)
