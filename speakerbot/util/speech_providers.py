import os
import subprocess
from urllib import quote_plus

from text_manipulators import split_text
from sounds import SoundPlayer

class GoogleTextToSpeech(object):

    def __init__(self, url_string=None):

        self.url_string = url_string
        if not url_string:
            self.url_string = u"http://translate.google.com/translate_tts?tl=en_gb&ie=UTF-8&q=%s"

    def say(self, text):

        if len(text) > 100:
            phrases = split_text(text, 100)
            for phrase in phrases:
                self.say(phrase)

            return

        text = quote_plus(text.encode("utf-8"))

        filename = "speech/%s.mp3" % text

        self.get_file(filename, self.url_string % (text))

        s = SoundPlayer()
        s.play_sound(filename)

    def get_file(self, filename, url, retries=3):

        if not os.path.isfile(filename) or os.path.getsize(filename) == 0:
            f = open(filename, "w")
            subprocess.call(
                    ['curl','-A Mozilla', url], 
                    stdout=f)
        if os.path.getsize(filename) == 0 and retries > 0:
            self.get_file(filename, url, retries=retries-1)

class EspeakTextToSpeech(object):

    def __init__(self, speak_path="espeak", wpm=150):

        self.speak_path = speak_path
        self.wpm_string = "-s %s" % wpm 

    def say(self, text): 

        subprocess.call([self.speak_path, text, self.wpm_string])