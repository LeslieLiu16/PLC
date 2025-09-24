from aip import AipSpeech
import wave
import time
from pyaudio import PyAudio, paInt16
import controller

framerate = 16000  # 采样率
num_samples = 2000  # 采样点
channels = 1  # 声道
sampwidth = 2  # 采样宽度2bytes
FILEPATH = 'speech.wav'

""" 你的 APPID AK SK """
APP_ID = '7082803'
API_KEY = 'Yks9eZcnc3o53q77KkCXUoyS'
SECRET_KEY = 'M02vHIUG2SZLLuyDPqrDmnJaTETauczq'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def save_wave_file(filepath, data):
    wf = wave.open(filepath, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes(b''.join(data))
    wf.close()

def my_record():
    pa = PyAudio()
    stream = pa.open(format=paInt16, channels=channels,
                     rate=framerate, input=True, frames_per_buffer=num_samples)
    my_buf = []
    # count = 0
    t = time.time()
    print('正在录音...')
    while time.time() < t + 4:  # 秒
        string_audio_data = stream.read(num_samples)
        my_buf.append(string_audio_data)
    print('录音结束.')
    save_wave_file(FILEPATH, my_buf)
    stream.close()

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

if __name__ == '__main__':
    my_record()
    res = client.asr(get_file_content('speech.wav'), 'wav', 16000, {'dev_pid': 1537,}).get('result')[0]
    
    if '左转' in res:
        controller.left_run()

    else:
        print("无法识别")