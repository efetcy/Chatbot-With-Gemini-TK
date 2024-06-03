import google.generativeai as genai  # Google Generative AI içeriye aktarımı                               
import os  # İşletim sistemi ile ilgili işlemler için os modülünü içe aktarın
from playsound import playsound  # Ses dosyalarını çalmak için playsound modülünü içe aktarın               
from gtts import gTTS  # Google Text-to-Speech modülünü içe aktarın                                         
import random  # Rastgele sayı üretimi için random modülünü içe aktarın 
import tkinter # Tkinter modülünü içe aktarın

# Google Generative AI API anahtarını tanımlama
api = 'api-key'

# Metni sesli okuyan bir fonksiyon tanımlama
def speak(text):  # speak adlı bir fonksiyon tanımlama
    tts = gTTS(text, lang="tr")  # Metni sese dönüştür
    rand = random.randint(1, 10000)  # Rastgele bir sayı oluştur
    file = "audio" + str(rand) + ".mp3"  # Rastgele sayı ile ses dosyası oluştur.
    tts.save(file)  # Ses dosyasını kaydet
    playsound(file)  # Ses dosyasını oynat
    os.remove(file)  # Ses dosyasını sil

genai.configure(api_key=api)    # Google Generative AI API'sini yapılandırın

model = genai.GenerativeModel('gemini-pro')

chat = model.start_chat(history=[])


prompt = "Birlikte 9. sınıf öğrencileri gibi konuşacağız, önce ben başlayacağım senin ismin TUNÇ anlaşıldı mı?" #Yapay zekanın yapılandırılması için ilk messaj(promptu) giriyoruz.
cevap = chat.send_message(prompt)  # Prompt'u chatbot'a gönderin ve cevabı alın

# Create a window
window = tkinter.Tk()
window.title("GUI")
window.geometry("600x300")


previous_label = None  # Önceki etiketi saklamak için bir değişken oluşturun

def print_entry():
    global previous_label  # Önceki etiketi global olarak tanımlayın
    alınan = Entry.get()
    user_input = alınan
    response = chat.send_message(user_input)  # Chatbot'tan cevap al
    if previous_label:  # Eğer önceki etiket varsa
        previous_label.destroy()  # Önceki etiketi sil
    label = tkinter.Label(window, text="ChatBot: " + response.text)
    label.pack()
    previous_label = label  # Yeni etiketi önceki etiket
    speak(response.text)  # Chatbot cevabını sesli oku


Entry = tkinter.Entry(window, width=200)
Entry.pack()

button = tkinter.Button(window, text="Gönder", command=print_entry)
button.pack()



tkinter.mainloop()