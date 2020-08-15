import os
import pathlib

from pocketsphinx import LiveSpeech, get_model_path


model_path = get_model_path()
my_keywords_dir_path = pathlib.Path(__file__).parent.absolute()

speech = LiveSpeech(
    verbose=False,
    sampling_rate=16000,
    buffer_size=2048,
    no_search=False,
    full_utt=False,
    hmm=os.path.join(model_path, "en-us"),
    lm=os.path.join(model_path, "en-us.lm.bin"),
    dic=os.path.join(my_keywords_dir_path, "tello_keywords.dict")
)

for phrase in speech:
    print(phrase)
