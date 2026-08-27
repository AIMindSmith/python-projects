# Smart Alarm Clock

A small browser-based alarm clock built with Flask, HTML, CSS, and JavaScript. It displays the current time, lets you set an alarm, plays a local sound when the alarm triggers, and supports stopping, snoozing for five minutes, and resetting the alarm.

## Features

- Live 24-hour clock display
- Alarm time selection in hours and minutes
- Browser sound notification when the alarm rings
- Stop, five-minute snooze, and new-alarm controls
- Responsive dark-themed interface
- Flask server for serving the application assets

## Requirements

- Python 3.8 or newer
- Flask
- Flask-CORS
- A browser with audio playback enabled

## Setup

1. Open a terminal in this project directory:

   ```powershell
   cd "c:\Users\atulb\Downloads\projects that complete\python_with_flask"
   ```

2. Install the Python dependencies:

   ```powershell
   python -m pip install flask flask-cors
   ```

3. Start the Flask server:

   ```powershell
   python backend.py
   ```

4. Open [http://localhost:5000](http://localhost:5000) in a browser.

To stop the server, press `Ctrl+C` in the terminal.

## Project Structure

```text
python_with_flask/
├── backend.py       # Flask application and asset routes
├── index.html       # Alarm clock interface and client-side logic
├── style.css        # Application styling
├── sound.mp3        # Alarm sound played by the browser
└── Python_learning/ # Additional learning material
```

## Routes

| Route | Purpose |
| --- | --- |
| `GET /` | Serves the alarm clock page |
| `GET /style.css` | Serves the stylesheet |
| `GET /sound.mp3` | Serves the alarm sound |

## Current Layout Note

Flask's `render_template('index.html')` expects the HTML file in a `templates` directory, but this project currently keeps `index.html` in the project root. If `/` returns `TemplateNotFound: index.html`, either move the file to `templates/index.html` or update `backend.py` to serve the root-level file with `send_from_directory`.

The alarm itself runs in the browser, so it is reset when the page is refreshed or closed. Audio playback may also require an initial interaction with the page depending on browser autoplay policies.
