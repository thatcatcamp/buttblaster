#!/bin/bash
# create fresh copies of the wav files
# pip3 install -f 'https://synesthesiam.github.io/prebuilt-apps/' -f 'https://download.pytorch.org/whl/cpu/torch_stable.html' larynx
larynx --voice harvard '{body}' > {file_name}"
