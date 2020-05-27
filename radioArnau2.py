import requests
import time
import datetime
print(datetime.datetime.now())
import re


url = 'http://prem1.rockradio.com:80/bluesrock?9555ae7caa92404c73cade1d'
encoding = 'latin1'
info = ''

radio_session = requests.Session()

while True:

    radio = radio_session.get(url, headers={'Icy-MetaData': '1'}, stream=True)

    metaint = int(radio.headers['icy-metaint'])

    stream = radio.raw

    audio_data = stream.read(metaint)
    meta_byte = stream.read(1)

    if (meta_byte):
        meta_length = ord(meta_byte) * 16

        meta_data = stream.read(meta_length).rstrip(b'\0')

        stream_title = re.search(br"StreamTitle='([^']*)';", meta_data)


        if stream_title:

            stream_title = stream_title.group(1).decode(encoding, errors='replace')

            if info != stream_title:
                print('Now playing: ', stream_title)
                info = stream_title
            else:
                pass

        else:
            print('No StreamTitle!')

    time.sleep(1)