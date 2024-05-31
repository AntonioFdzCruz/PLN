import os
from flask import Flask, request, render_template, jsonify, url_for
from gtts import gTTS

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['AUDIO_FOLDER'] = 'static/audio'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file:
        # Guardar el archivo subido
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        
        # Leer el contenido del archivo de texto
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()

        # Convertir el texto a voz
        tts = gTTS(text, lang='es')
        audio_filename = 'audio.mp3'
        audio_path = os.path.join(app.config['AUDIO_FOLDER'], audio_filename)
        tts.save(audio_path)
        
        # Generar la URL del archivo de audio
        audio_url = url_for('static', filename=f'audio/{audio_filename}')
        return jsonify({'audio_url': audio_url})

if __name__ == '__main__':
    # Crear las carpetas si no existen
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    if not os.path.exists(app.config['AUDIO_FOLDER']):
        os.makedirs(app.config['AUDIO_FOLDER'])
    app.run(debug=True)
