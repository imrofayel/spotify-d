from flask import Flask, render_template, request, jsonify, send_file
import os
import zipfile
import io
from main import get_playlist_songs, search_and_download, save_to_csv
import time

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
        
        # Create temporary directory for downloads
        temp_dir = os.path.join('playlists', playlist_name)
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
        
        # Download each song
        downloaded_files = []
        for song in songs:
            file_path = search_and_download(song['name'], song['artist'], playlist_name)
            if file_path and os.path.exists(file_path):
                downloaded_files.append(file_path)
        
        # Create a zip file in memory
        memory_file = io.BytesIO()
        with zipfile.ZipFile(memory_file, 'w', zipfile.ZIP_DEFLATED) as zf:
            # Add each downloaded file to the zip
            for file_path in downloaded_files:
                if os.path.exists(file_path):
                    arcname = os.path.basename(file_path)
                    zf.write(file_path, arcname)
        
        # Move to the beginning of the BytesIO buffer
        memory_file.seek(0)
        
        # Clean up the temporary directory after a short delay
        def cleanup():
            time.sleep(1)  # Wait a bit to ensure file handles are closed
            for file_path in downloaded_files:
                try:
                    if os.path.exists(file_path):
                        os.remove(file_path)
                except:
                    pass
            try:
                if os.path.exists(temp_dir):
                    os.rmdir(temp_dir)
            except:
                pass

        # Return the zip file
        return send_file(
            memory_file,
            mimetype='application/zip',
            as_attachment=True,
            download_name=f'{playlist_name}.zip'
        )
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True)
