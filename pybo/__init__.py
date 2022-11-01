from flask import Flask, render_template, request, send_file,make_response
app = Flask(__name__)
import matplotlib.pyplot as plt
import librosa, soundfile
import librosa.display
from werkzeug.utils import secure_filename
from datetime import datetime
import os
import io
from pydub import AudioSegment

global save_location
global return_data
plt.style.use('seaborn-white')

@app.route('/')
def hello_pybo():
    return render_template('main.html')

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        audio_data = request.files["lc"]  # 그냥 받아온거 같은대
        if audio_data:
            filename = secure_filename(audio_data.filename)
            src = f"pybo/static/sound/{filename}"
            audio_data.save(src) #src가 sound 폴더에 있는 파일
            stem,fileExtension = os.path.splitext(filename)
            if fileExtension == '.mp3':
                audSeg = AudioSegment.from_mp3(src)
                ##
                os.remove(src)
                src = f"pybo/static/sound/{stem}" + '.wav'
                audSeg.export(src, format="wav")

            sr = librosa.get_samplerate(src)
            audio_data, sr = librosa.load(src, sr=sr // 5)
            new_filename = f'{filename.split(".")[0]}_{str(datetime.now())}.wav'
            new_filename = new_filename.replace(':',"_")
            os.remove(src)


            save_location = f'C:\projects\mysite\pybo\static\output\{new_filename}'
            # scaled = np.int16(audio_data / np.max(np.abs(audio_data)) * 32767)
            # write(save_location,sr,scaled)
            # #절취선 ======

            soundfile.write(save_location,audio_data,sr,format='WAV')

            #return render_template('downloaded.html', save_location=save_location)

            return_data = io.BytesIO()
            with open(save_location, 'rb') as fo:
                return_data.write(fo.read())
            # (after writing, cursor will be at last byte, so move it to start)
            return_data.seek(0)

            os.remove(save_location)

            response = make_response(send_file(return_data, as_attachment=True,download_name='transform.wav'))


            return send_file(return_data, as_attachment=True,download_name='converted_file.wav')








