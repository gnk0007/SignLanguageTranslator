from flask import Flask, render_template, redirect, url_for, flash, send_file
import os
import subprocess

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

@app.route('/')
def index():
    return render_template('index.html', show_animation=True)

@app.route('/home')
def home():
    return render_template('index.html', show_animation=False)

@app.route('/create_gesture')
def create_gesture():
    try:
        subprocess.run(['python', 'create_gesture.py'])
        flash('Contact us to create new geasture!', 'success')
    except Exception as e:
        flash(f'Error creating gesture: {e}', 'error')
    return redirect(url_for('home'))

@app.route('/scan_gesture')
def scan_gesture():
    return render_template('scan_gesture.html')

@app.route('/scan_gesture_run', methods=['POST'])
def scan_gesture_run():
    try:
        subprocess.run(['python', 'app.py'])
        flash('Gesture scanned successfully!', 'success')
    except Exception as e:
        flash(f'Error scanning gesture: {e}', 'error')
    return redirect(url_for('home'))

@app.route('/show_sentence')
def show_sentence():
    file_path = 'sentence.txt'
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                sentence = file.read()
            return render_template('show_sentence.html', sentence=sentence)
        else:
            flash('Sentence file not found.', 'error')
            return redirect(url_for('home'))
    except Exception as e:
        flash(f'Error showing sentence: {e}', 'error')
        return redirect(url_for('home'))

@app.route('/convert_to_audio')
def convert_to_audio():
    try:
        subprocess.run(['python', 'text_to_speech.py'])
        flash('Converted to audio successfully!', 'success')
        audio_file = 'output.mp3'
        if os.path.exists(audio_file):
            os.system(f'start {audio_file}')  # For Windows
            # os.system(f'afplay {audio_file}')  # For MacOS
            # os.system(f'mpg321 {audio_file}')  # For Linux
        else:
            flash('Audio file not found.', 'error')
    except Exception as e:
        flash(f'Error converting to audio: {e}', 'error')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
