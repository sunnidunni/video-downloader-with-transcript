# google colab link:

https://colab.research.google.com/drive/14q-q10T9q_aXGjRA1o3glyJhz_e_ZRvB?usp=sharing#scrollTo=M1UARqrb7ysm

## FastAPI Video Downloader Documentation

Welcome to the API documentation for the **Video Downloader API**. This FastAPI service allows users to download videos from various platforms by providing a URL. Below is a step-by-step guide to help you use the API effectively.

---

## Step 1: Set Up the API

### Base URL
- **Development**: `http://127.0.0.1:8000`
- **Production**: Replace with your deployed server URL.

Ensure the API is running by starting the FastAPI server. You can do this with the following command in the directory containing your FastAPI code:

```bash
uvicorn main:app --reload
```

---

## Step 2: Understand the Endpoint

### Video Download Endpoint
**URL**: `/download`

**Method**: `POST`

**Description**: This endpoint accepts a video URL and downloads the corresponding video file. Upon success, the video file is returned as a downloadable response.

#### Parameters
- **`url`** (required):
  - Type: `string`
  - Description: The URL of the video to download.

---

## Step 3: Example Usage

### Using `curl`
You can make a request to the API using the `curl` command-line tool. Replace `<VIDEO_URL>` with the actual video URL.

```bash
curl -X POST -F "url=<VIDEO_URL>" http://127.0.0.1:8000/download --output downloaded_video.mp4
```

### Using Python
The following Python script demonstrates how to interact with the API programmatically:

```python
import requests

# API Endpoint
api_url = "http://127.0.0.1:8000/download"

# Video URL to download
video_url = "<VIDEO_URL>"

# Sending the POST request
response = requests.post(api_url, data={"url": video_url})

if response.status_code == 200:
    # Save the downloaded video
    with open("downloaded_video.mp4", "wb") as f:
        f.write(response.content)
    print("Video downloaded successfully as 'downloaded_video.mp4'.")
else:
    print(f"Failed to download video. Error: {response.text}")
```

### API Response
#### Success
- **HTTP Status Code**: `200`
- **Response**: The downloaded video file.

#### Failure
- **HTTP Status Code**: `4xx` or `5xx`
- **Response**: An error message describing the issue.

---

## Step 4: Handle Errors

### Common Errors
1. **400 Bad Request**:
   - Cause: Missing or invalid `url` parameter.
   - Solution: Ensure the `url` parameter is provided and is a valid video URL.

2. **500 Internal Server Error**:
   - Cause: Issues during the download process (e.g., unsupported URL or server error).
   - Solution: Verify the video URL or check the server logs for more details.

---

## Step 5: Notes and Best Practices

1. **Supported Platforms**: The API supports all linkedin post urls.
2. **Temporary Storage**: Downloaded files are temporarily stored on the server and cleaned up after being served.
3. **API Integration**: Use the `/download` endpoint in your applications for seamless video downloading.

---

## Step 6: Integration Guide

If you want to integrate this API into your existing layout or application, follow these steps:

### **Frontend Integration**
1. Create a form or input field where users can enter the video URL.
2. On submission, send a `POST` request to the `/download` endpoint with the video URL.
3. Handle the response:
   - If the request succeeds, save the returned file or trigger a download for users.
   - For errors, display an appropriate error message.

Example using JavaScript `fetch`:

```javascript
const form = document.getElementById('download-form');
form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const url = document.getElementById('video-url').value;
    
    const response = await fetch('http://127.0.0.1:8000/download', {
        method: 'POST',
        body: new URLSearchParams({ url: url }),
    });
    
    if (response.ok) {
        const blob = await response.blob();
        const downloadUrl = window.URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = downloadUrl;
        link.download = 'downloaded_video.mp4';
        document.body.appendChild(link);
        link.click();
        link.remove();
    } else {
        alert('Failed to download video: ' + await response.text());
    }
});
```
