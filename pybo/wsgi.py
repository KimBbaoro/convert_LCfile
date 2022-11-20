

def hello(name):
    print(f"Hi, {name}")

# def get_sr(path): #sr 받기
#     sr = librosa.get_samplerate(path)
#     return sr
#
# def y_8k(audio_data,sr):
#     audio_np = audio_data.numpy()
#     y_8k = librosa.resample(audio_np,sr,8000)
#     return y_8k


if __name__ == '__main__':

    print("hello")

    # audio_data = request.files["lc"]
    # #print(type(audio_data))
    # sr = librosa.get_samplerate(audio_data)
    # print('flag2')
    # print(sr)
    #
    # audio_data, sr = librosa.load(audio_data, sr=sr // 3)
    # print('flag3')
    # print(sr)
    # ipd.Audio(audio_data, rate=sr)
    # print('flag4')

    # sr = get_sr(audio_data)
    # audio_data = librosa.load(audio_data, sr = 8000)
    # ipd.Audio(audio_data)

