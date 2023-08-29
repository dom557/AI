import tkinter as tk
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import datetime
import wikipedia
import pyjokes

translator = Translator()
listener = sr.Recognizer()

def talk(text):
    response_label.configure(text=text)
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        translated_text = translator.translate(text, dest='ar').text
        tts = gTTS(text=translated_text, lang='ar')
        tts.save(fp.name)

        playsound(fp.name)

# Rest of the code remains the same
# ...


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='ar-EG')
            command = command.lower()
            print(command)
    except:
        pass
    return command

def run_alexa():
    try:
        command = take_command()
        print(command)

        if 'تشغيل' in command:
            song = command.replace('تشغيل', '')
            talk('حسنًا سيدي، جاري تشغيل ' + song)
            pywhatkit.playonyt(song)
        elif 'الوقت' in command:
            time = datetime.datetime.now().strftime('%H:%M %p')
            talk('الوقت الحالي هو ' + time)
        elif 'ويكيبيديا' in command:
            person = command.replace('من هو', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)

        elif 'نكتة' in command:
            talk(pyjokes.get_joke())
            print(pyjokes.get_joke())
        elif 'رمسيس' in command:
            talk('مرحبًا يا سيد أبا حازم، كيف يمكنني مساعدتك؟')
        elif 'ما هو المشكلة' in command:
            talk('لا يوجد مشكلة أبا حازم، أعتقد أنها مشكلة في الاتصال بالإنترنت')
        elif 'هل يمكنك مساعدتي' in command:
            talk('نعم بالتأكيد')
        elif 'كيف حالك' in command:
            talk('أنا بخير، شكرًا لك. كيف حالك؟')
        elif 'بخير' in command or 'جيد' in command:
            talk('من الجيد أن تكون بخير')
        elif 'من صنعك' in command:
            talk('تم صنعي من قبل العبقري السيد أبا حازم')
        elif 'من أنا' in command:
            talk('إذا كنت تتحدث إلي في الوقت الحالي، فأنت بالتأكيد إنسان')

        elif 'ما هو أفضل فصل' in command:
            talk('أخبرني السيد أبا حازم أن أفضل فصل هو قسم 102')
        elif 'شكرًا' in command:
            talk('على الرحب والسعة')
        elif 'شيخ' in command:
            talk('الشيخ علي أبا حازم هو عمك وهو معك الآن')

    except:
        pass

def start_Ramssis():

     run_alexa()

def stop_Ramssis():
    engine.stop()

root = tk.Tk()
root.geometry("700x400")
root.title("Abahazem Assistant")


# Create label
label1 = tk.Label(root, text="Welcome to Ramssis Assistant", font=("Arial", 24))
label1.pack(pady=20)

# Create button to start Alexa
start_button = tk.Button(root, text="Start Ramssis", command=start_Ramssis, font=("Arial", 16))
start_button.pack(pady=20)

# Create button to stop Alexa
stop_button = tk.Button(root, text="Stop Ramssis", command=stop_Ramssis, font=("Arial", 16))
stop_button.pack(pady=20)
# Create a label for displaying Alexa's responses
response_label = tk.Label(root, text="", font=("Italic", 10))
response_label.pack(pady=20)
root.mainloop()
