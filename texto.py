from gtts import gTTS
import os
mytext = 'Utilizando uma API onde digito na parte de "mytext" e o próprio python transforma em áudio!'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=True)
myobj.save("Wellcome.mp3")
os.system("mpg321 welcome.mp3")

