import yt_dlp

def download_video(url):
    ydl_opts = {
        'outtmpl': 'downloads/%(title)s.%(ext)s',  # Set download folder
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Example usage
download_video('https://www.youtube.com/watch?v=LCwrRLJFqM4&list=RDLCwrRLJFqM4&start_radio=1')
