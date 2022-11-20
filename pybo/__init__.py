from flask import Flask, render_template, request, send_file



import librosa, soundfile
import librosa.display
from werkzeug.utils import secure_filename
from datetime import datetime
import os
import io
from pydub import AudioSegment

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_pybo():
        return render_template('main.html')


    @app.route('/upload', methods=['POST', 'GET'])
    def upload():
        if request.method == 'POST':
            audio_data = request.files["lc"]
            if audio_data:
                filename = secure_filename(audio_data.filename)
                src = f"pybo/sound/{filename}"
                audio_data.save(src)
                stem, fileExtension = os.path.splitext(filename)
                if fileExtension == '.mp3':
                    audSeg = AudioSegment.from_mp3(src)
                    ##
                    os.remove(src)
                    src = f"pybo/sound/{stem}" + '.wav'
                    audSeg.export(src, format="wav")

                sr = librosa.get_samplerate(src)
                audio_data, sr = librosa.load(src, sr=sr // 6)
                new_filename = f'{filename.split(".")[0]}_{str(datetime.now())}.wav'
                new_filename = new_filename.replace(':', "_")
                os.remove(src)

                save_location = f'pybo/output/{new_filename}'

                soundfile.write(save_location, audio_data, sr, format='WAV')

                return render_template("download.html", save_location=save_location)


    @app.route('/download', methods=['POST', 'GET'])
    def download():
        save_location = request.form["save_location"]
        with open(save_location, 'rb') as fo:
            return_data = io.BytesIO()

            return_data.write(fo.read())
        # (after writing, cursor will be at last byte, so move it to start)
        return_data.seek(0)

        os.remove(save_location)
        return send_file(return_data, as_attachment=True, download_name='converted_file.wav')
    return app