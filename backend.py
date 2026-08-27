#https://www.fesliyanstudios.com/royalty-free-sound-effects-download/alarm-203
# -*- coding: utf-8 -*-
from flask import Flask, render_template, send_from_directory
from flask_cors import CORS
import os
import sys
import io

# Set UTF-8 encoding for output
if sys.stdout.encoding is None:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

# Get the directory of this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    """Serve the main alarm clock page"""
    return render_template('index.html')

@app.route('/style.css')
def get_style():
    """Serve the CSS file"""
    return send_from_directory(BASE_DIR, 'style.css')

@app.route('/sound.mp3')
def get_sound():
    """Serve the alarm sound file"""
    return send_from_directory(BASE_DIR, 'sound.mp3')

if __name__ == '__main__':
    try:
        print("=" * 60)
        print("SMART ALARM CLOCK")
        print("=" * 60)
        print("\nWeb server starting...")
        print("Open your browser and go to: http://localhost:5000")
        print("\nTip: You can also access from other devices on your network")
        print("by using your computer's IP address (e.g., http://192.168.x.x:5000)")
        print("\nTo stop the server, press Ctrl+C")
        print("=" * 60 + "\n")
        
        # Run the Flask app
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n\nServer stopped!")
    except Exception as e:
        print(f"Error: {e}")