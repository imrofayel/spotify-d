## Spotify Downloader :trollface:

just another spotify downloader.

<img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white">

Bro, its just a `python (flask)` app. You just need `Python` and `ffmpeg` to start.

1. Install **[Python 3.x](https://www.python.org/downloads/) & pip** *(comes with Python installer)*.

2. Download [`ffmpeg-git-essentials.7z`](https://www.gyan.dev/ffmpeg/builds/) and extract the downloaded file in `C:\` and rename the extracted folder to `ffmpeg`. Add `C:\ffmpeg\bin` to your system's **PATH** (User variables) environment variable.
   
3. **Clone** the repository, open the folder in `VSCode` and create a **virtual environment** (recommended) using
   ```bash
   python -m venv venv
   ```
   activate the **virtual environment** by running
     ```bash
     .\venv\Scripts\activate.bat
     ```
     and install **dependencies** if any dependency isn't there, dont worry python 🐍 gonna tell you.
   ```bash
   pip install -r requirements.txt
   ```
   
4. Rename `.env.example` to `.env` and add [Spotify credentials](https://developer.spotify.com/dashboard/).

5. **そうそう** you good to go. Run `python app.py` and listen without limits.

⚠️ Dependencies could be outdated in `requirements.txt` so update these manually.

It's open-source under **MIT**.

*Here's the screenshot btw.*

<img src="https://github.com/user-attachments/assets/1d4ea66e-ddb3-4d50-9441-09eb0a866421" width="700px">


