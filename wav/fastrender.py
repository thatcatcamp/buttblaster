import urllib.parse
import uuid

import requests


with open("prompts.txt") as fh:
    lines = fh.readlines()
for line in lines:
    fixed = urllib.parse.quote(line)
    req = f"http://localhost:5002/api/tts?voice=en-us%2Fharvard-glow_tts&text={fixed}&vocoder=hifi_gan%2Funiversal_large&denoiserStrength=0.002&noiseScale=0.667&lengthScale=0.85&ssml=false"
    print(req)
    back = requests.get(req)
    with open(uuid.uuid4().hex + ".wav", "wb") as oh:
        oh.write(back.content)

