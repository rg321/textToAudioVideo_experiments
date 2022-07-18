import cv2
import time
import nltk
import phonemes
import time
import pyttsx3
from threading import Thread

#Defines
timePerPhoneme = 0.04
longPhonemeBonus = 0
smallPhonemeBonus = -0.03

# called by each thread
def speak_word(word, time, engine):
    engine.setProperty('rate', time)
    engine.say(word)
    engine.runAndWait()
    return


file_content = open("sample.txt").read()
tokens = nltk.word_tokenize(file_content)

entries = nltk.corpus.cmudict.entries()

start_time = time.time()
TextToSpeech = []
for token in tokens:
    for entry in entries:
        if token.lower() == entry[0]:
            TextToSpeech.append(entry)
            break
end_time = time.time()
#Debug!
print("Pre-processing Done! Time: %s Seconds"%(end_time - start_time))

engine = pyttsx3.init()
engine.setProperty('voice', 'english_rp+f3')

result = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'mp4v'), 15, (300,300), isColor=False)

## For each mouth you should put a refering mouth to show
## do the double check
for word in TextToSpeech:
    # cv2.imshow('window', phonemes.mouths['blair_rest.jpg'])
    # cv2.waitKey(1)

    timeForAWord = 0.0
    timeOfThisPhoneme = 0.0
    MouthsToShow = []
    for ph in word[1]:
        for key, value in phonemes.PhonemeToMouth.items():
            if '1' in ph:
                timeForAWord += timePerPhoneme + longPhonemeBonus
                timeOfThisPhoneme = timePerPhoneme + longPhonemeBonus
            elif '0' in ph:
                timeForAWord += timePerPhoneme + smallPhonemeBonus
                timeOfThisPhoneme = timePerPhoneme + smallPhonemeBonus
            else:
                timeForAWord += timePerPhoneme
                timeOfThisPhoneme = timePerPhoneme
            if key in ph:
                MouthsToShow.append((value, timeOfThisPhoneme))



    t = Thread(target=speak_word, args=(word[0], timeForAWord, engine))
    t.start()

    #Show Mouths
    for mouth in MouthsToShow:
        img = phonemes.mouths[mouth[0]]
        result.write(img)
        cv2.imshow('window', img)
        cv2.waitKey(1)
        time.sleep(mouth[1])

    t.join()

result.release()