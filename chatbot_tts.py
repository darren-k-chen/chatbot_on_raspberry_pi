from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

import time
from gtts import gTTS
import os

def chat_en():
    cb = ChatBot('en_bot')
    trainer = ChatterBotCorpusTrainer(cb)
    trainer.train("chatterbot.corpus.english")

    while 1:
        say = input('Please say something >>')

        rep = str(cb.get_response(say))
        tts = gTTS(text = rep, lang = 'en')

        time_now = time.asctime(time.localtime(time.time()))
        filename = 'Response on ' + time_now + '.mp3'

        tts.save(filename)
        os.system("mpg321 " + filename)

def chat_hant():
    cb = ChatBot('hant_bot')
    trainer = ChatterBotCorpusTrainer(cb)
    trainer.train("chatterbot.corpus.traditionalchinese")

    while 1:
        say = input('Please say something >>')

        rep = str(cb.get_response(say))
        tts = gTTS(text = rep, lang = 'zh')

        time_now = time.asctime(time.localtime(time.time()))
        filename = 'Response on ' + time_now + '.mp3'

        tts.save(filename)
        os.system("mpg321 " + filename)

def main():
    lan_en = ["en", "EN", "English", "english", "ENGLISH"]
    lan_hant = ["hant", "zh-tw", "zh", "cn", "traditional-chinese", "chinese", "Chinese", "CHINESE"]

    tmp = input('Please Enter Your Language >>')

    try:
        chat_en() if tmp in lan_en
        chat_hant() if tmp in lan_hant

        print("=====END=====") else
    except:
        main()

if __name__ == '__main__':
    main()
