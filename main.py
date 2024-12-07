from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
import yt_dlp
import time
import os

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Video Downloader</title>
    </head>
    <body>
        <h1>Video Downloader</h1>
        <form action="/download" method="post">
            <label for="url">Enter Video URL:</label><br>
            <input type="text" id="url" name="url" required><br><br>
            <button type="submit">Download Video</button>
        </form>
    </body>
    </html>
    """


@app.post("/download")
async def download_video(url: str = Form(...)):
    output_filename = None
    try:
        timestamp = int(time.time())
        output_filename = f"vid_{timestamp}.mp4"

        ydl_opts = {
            'format': 'best',
            'outtmpl': output_filename,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        if os.path.exists(output_filename):
            return FileResponse(
                output_filename,
                media_type="video/mp4",
                filename=output_filename,
                background=lambda: os.remove(
                    output_filename)  # Cleanup after response
            )
        else:
            raise HTTPException(
                status_code=500, detail="Failed to download video.")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
