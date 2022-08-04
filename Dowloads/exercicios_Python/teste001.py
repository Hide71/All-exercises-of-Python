from playsound import playsound
import gtts
texto = 'hideraldo '
fala = gtts.gTTS(texto, lang='pt-br')
fala.save('audio.mp3')
playsound('audio.mp3')