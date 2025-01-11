## Spotify Downloader :trollface:

just another spotify downloader.

<img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white">

Bro, its just a `python (flask)` app. Here's basic guidelines which worked for me but if it these dont work for you then dont panic and fix it. You just need `Python` and `ffmpeg` to start.

1. Install **Python 3.x & pip**.

2. Download [`ffmpeg-git-essentials.7z`](https://www.gyan.dev/ffmpeg/builds/) and extract the downloaded file in `C:\` and rename the extracted folder to `ffmpeg`. Add `C:\ffmpeg\bin` to your system's **PATH** environment variable.
   
3. **Clone** the repository and create a **virtual environment** (recommended)
   ```bash
   python -m venv venv
   ```
   activate the **virtual environment**
     ```bash
     .\venv\Scripts\activate
     ```
     and install **dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
4. Rename `.env.example` to `.env` and add [Spotify credentials](https://developer.spotify.com/dashboard/).

5. **そうそう** you good to go. Run `python app.py` and listen without limits.

It's open-source under **MIT**.

*Here's the screenshot btw.*

<img src="https://github.com/user-attachments/assets/0f2aa83c-e71d-4915-976c-b3de32474c6a" width="700px">


