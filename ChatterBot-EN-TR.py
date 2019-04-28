import speech_recognition as sr
import os
from translate_api.translate_api import api
from google.cloud import texttospeech
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import datetime
import feedparser
import serial

chatbot=ChatBot('Ron Obvious',
                   logic_adapters=[
                           'chatterbot.logic.BestMatch'])
#conversation = []


os.environ['GOOGLE_APPLICATION_CREDENTIALS']='My-First-Project-f012fb137d0b.json'
#print('Program başlıyor...')
#print (os.getcwd())
#os.chdir("/home/corradeo/Desktop")
#print (os.getcwd())
#os.system('export GOOGLE_APPLICATION_CREDENTIALS="/home/corradeo/Desktop/My-First-Project-f012fb137d0b.json"') 
#os.system('set | grep GOOGLE_APPLICATION_CREDENTIALS ') 

ser = serial.Serial(
    port='/dev/ttyACM2',\
    baudrate=19200,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

def bluetoothVeriAl():
    print('bluetootha girildi')
    giris=True
    while giris : 
        a=False
        giris=False
        for c in ser.read():
            if c == 71:
                a=True
                konusma('merhaba sevgili belediye başkanı adayımız')
        while a :
            for c in ser.read():
                if c== 101 :
                    konusma('Evet')
                elif c==104:
                    konusma('hayır')

                elif c==49:
                    konusma('bana kendinizden bahseder misiniz')
                elif c==50:
                    konusma('aday olma düşünceniz nasıl gelişti')                  
                elif c==51:
                    konusma('adaylığınızı açıkladıktan sonra ne tür tepkiler aldınız')                
                elif c==52:
                    konusma('seçmenler neden size oy vermelidir')                  
                elif c==53:
                    konusma('seçim çalışmanız sırasında yaşadığınız ilginç bir anınız var mı') 
                elif c==54:
                    konusma('türkiye ve ısparta adına bir hayaliniz var mı')                  
                elif c==55:
                    konusma('türkiyenin 2023 vizyonunda ıspartanın yeri nedir') 
                elif c==56:
                    konusma('ısparta size ne anlam ifade ediyor')                  
                elif c==57:
                    konusma('hayalinizdeki ısparta nasıl bir şehir') 
                elif c==48:
                    konusma('yaptığınız seyahatlerde gittiğiniz şehirleri belediyecilik açısından değerlendir misiniz')                  
                elif c==97:
                    konusma('belediyecilik açısından beğendiğiniz il veya ilçeler var mı var ise bu il ve ilçeler nelerdir') 
                elif c==98:
                    konusma('ıspartanın sorunları nelerdir')                  
                elif c==99:
                    konusma('bu sorunları nasıl çözebiliriz') 
                elif c==100:
                    konusma('projeleriniz nelerdir')                  
                elif c==102:
                    konusma('başka bir projeniz var mı')   
                elif c==103:
                    konusma('ulaşım ile ilgili bir projeniz var mı')                  
                elif c==105:
                    konusma('trambüs hattı projeniz hakkında bilgi verir misiniz')                
                elif c==106:
                    konusma('trambüs hattı ücretleri halkı memnun edecek mi')                  
                elif c==107:
                    konusma('trambüs hattı nerelerden geçecektir') 
                elif c==108:
                    konusma('akıllı trafik projeniz hakkında bilgi verir misiniz')                  
                elif c==109:
                    konusma('akıllı trafik projeniz hangi noktalarda uygulanacak') 
                elif c==110:
                    konusma('akıllı trafik projesi ve trambüs projesi ıspartanın trafik sorununu çözebilecek mi')                  
                elif c==111:
                    konusma('ıspartanın tarihi kültürel ve doğal güzellikleri nelerdir') 
                elif c==112:
                    konusma('izleyicilere ıspartada gitmelerini önerdiğiniz yerler nelerdir')                  
                elif c==113:
                    konusma('ıspartada turizm hangi seviyededir') 
                elif c==114:
                    konusma('turizm ile ilgili projeleriniz nelerdir bu projeler hakkında bilgi verir misiniz')                   
                elif c==116:
                    konusma('ıspartada nüfusun önemli bir kısmı öğrencilerden oluşmaktadır öğrenci arkadaşlara neler söylemek istersiniz')                  
                elif c==117:
                    konusma('öğrenci iken karşılaştığınız zorluklar nelerdir') 
                elif c==118:
                    konusma('ıspartadaki öğrenciler için maddiyat önemli bir sorun bu sorun için bir projeniz var  mı')                  
                elif c==120:
                    konusma('şehir merkezindeki kütüphane yetersiz bu konuda bir projeniz var mı')                
                elif c==121:
                    konusma('kütüphane projeniz hakkında bilgi verir misiniz')                  
                elif c==122:
                    konusma('kütüphane nerede bulunacaktır') 
                elif c==65:
                    konusma('kütüphane 7 24 açık olabilecek mi')                  
                elif c==66:
                    konusma('öğrenciler ile ilgili projelerde öğrenci arkadaşlarımız ile fikir alış verişi yapacak mısınız') 
                elif c==67:
                    konusma('öğrenci arkadaşlarımız projeniz hakkında ne düşünüyorlar')                  
                elif c==68:
                    konusma('ülkemizin geleceği gençlerimiz hakkında neler düşünüyorsunuz') 
                elif c==69:
                    konusma('ıspartadaki kadınlara yönelik projeleriniz nelerdir')                  
                elif c==70:
                    konusma('kadınlara yönelik projeniz hakkında bilgi verir misiniz') 
                elif c==72:
                    konusma('kadınlara yönelik projeniz ile toplumda kadının etkisi artacak mı')                  
                elif c==73:
                    konusma('kadınlar ile ilgili proje ile birlikte yaşamlarında neler değişecek') 
                elif c==74:
                    konusma('yaşlılara yönelik bir projeniz var mı')                  
                elif c==75:
                    konusma('yaşlılar ile ilgili proje ile birlikte yaşamlarında neler değişecektir')   
                elif c==76:
                    konusma('gençlere kadınlara ve yaşlılara yönelik projeleriniz ıspartaya neler kazandıracaktır')                  
                elif c==77:
                    konusma('sivil toplum kuruluşlarının ıspartadaki önemi nedir')                
                elif c==78:
                    konusma('sivil toplum kuruluşları ile ilgili bir projeniz var mı')                  
                elif c==79:
                    konusma('sivil toplum kuruluşları ile ilgili projeniz hakkında bilgi verir misiniz') 
                elif c==80:
                    konusma('halkın sivil toplum kuruluşlarına katılması yönende neler söylemek istersiniz')                  
                elif c==82:
                    konusma('şehirdeki otobüs durakları iklime uygun değil bu konu hakkında projeniz var mı') 
                elif c==83:
                    konusma('kapalı otobüs durakları hakkında bilgi verir misiniz')                  
                elif c==84:
                    konusma('kapalı otobüs durağında televizyon olacak mı ') 
                elif c==85:
                    konusma('kapalı otobüs durakları hangi noktalarda bulunacak')                  
                elif c==86:
                    konusma('kapalı otobüs durağında klima olacak mı ') 
                elif c==87:
                    konusma('teknoloji hakkında ne düşünüyorsunuz')                  
                elif c==88:
                    konusma('teknolojinin yararları nelerdir') 
                elif c==89:
                    konusma('teknolojinin zararları nelerdir')                  
                elif c==90:
                    konusma('teknoloji sektöründe çalışmayı düşünen öğrencilere tavsiyeleriniz nelerdir')
                elif c==64:
                    konusma('bu projeniz hakkında bilgi verir misiniz')                  
                elif c==63:
                    konusma('kitap okumayı seviyor musunuz')                
                elif c==61:
                    konusma('ne tür kitaplar okuyorsunuz')                  
               
                    
                elif c==81:
                    a=False
                    giris=False

                break
        print('çıkılıyor')


def hava():
    parse = feedparser.parse("http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode=EUR|TR|32100|ISPARTA|")
    parse = parse["entries"][0]["summary"]
    parse = parse.split()
    aa=("Bugün"+" "+str(parse[2])+" "+str(parse[4])+" "+"Derece"+" "+"ve"+" "+str(trTranslate(parse[7]))+" "+"bekleniyor")
    return(str(aa))
def konusma(metin):
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.types.SynthesisInput(text=metin)
    
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='tr-TR',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE)
    
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)
    
    response = client.synthesize_speech(synthesis_input, voice, audio_config)
    
    with open('output.mp3', 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')
    os.system('mpg321 output.mp3')
def trTranslate(text):
    sonuc =api(str(text),'en','tr')
    return sonuc

def enTranslate(text):
    sonuc =api(str(text),'tr','en')
    return sonuc

def anlama():
    with sr.Microphone() as kaynak:
         ses = r.listen(kaynak,timeout = None)
         text = r.recognize_google(ses,language="tr-TR")
         print(text)
         return text
     
def tarih ():
    an= datetime.datetime.today()
    tam=str(an.day)+" "+trTranslate(str(datetime.datetime.strftime(an, '%B')))+" "+str(an.year)+" "+trTranslate(str(datetime.datetime.strftime(an, '%A')))
    print(str(tam))
    return(str(tam))
def saat():
    an= datetime.datetime.today()
    hr="saat"+" "+str(an.hour)+" "+str(an.minute)
    print(hr)
    return(str(hr))


r= sr.Recognizer()   
with sr.Microphone() as kaynak:   
     print("Please wait. Calibrating microphone...")   
     # listen for 5 seconds and calculate the ambient noise energy level   
     r.adjust_for_ambient_noise(kaynak, duration=5)
     konusma('kalibrasyon tamamlandi')

def wakeword():     
    print('konuşmak için bana seslenin')
    konusma('konuşmak için bana seslenin')
    trueOrFalse= True
    while trueOrFalse:
        try:
            ses = anlama()
            if str(ses)=="Aytek":
                trueOrFalse= False
            elif str(ses)=="Hey Aytek":
                trueOrFalse= False
            elif str(ses)=="Merhaba Aytek":
                trueOrFalse= False
            elif str(ses)=="Selamünaleyküm Aytek":
                trueOrFalse= False
        except sr.UnknownValueError:
                 print("Anlamadim.")
    
        except sr.RequestError:
                 print("Bad Request")
        
def dongu() :
            try:
                 print('dinliyorum')
                 sorgu= anlama()  
                 if (str(sorgu))=="Bugünün tarihi ne":
                     konusma(tarih())
                 elif (str(sorgu))=="güle güle":
                     wakeword()
                 elif (str(sorgu))=="görüşürüz":
                     wakeword()
                 elif (str(sorgu))=="saat kaç":
                     konusma(saat())
                 elif (str(sorgu))== "hava nasıl":
                     konusma(hava())
                 elif (str(sorgu))=='soru eklemek istiyorum':
                     ekleme()
#                 elif (str(sorgu))=='Müslüm Baba çal':
#                     muslum()
                 else:
                     response = str(chatbot.get_response(str(sorgu)))
                     if response==('bu sorunun cevabı henüz eklenmedi eklemek ister misiniz'):
                         cevap=anlama()
                         if cevap == 'evet ':
                             ekleme()
                         else :
                             dongu()
                     print(str(response))
                     konusma(str(response))                   
            except sr.UnknownValueError:
                 print("Anlamadim.")
            except sr.RequestError:
                 print("Bad Request")
def ekleme():
    pswd='No 25'
    konusma('Yönetici şifresini söyleyiniz')
    sifre = anlama()
    print(sifre)
    if sifre == pswd:
        konusma('eklemek istediğiniz soruyu söyleyiniz')
        soru = anlama()
        konusma(str('sorunuz ' + soru))
        konusma('sorunun cevabını söyleyiniz')
        cevap=anlama()
        konusma(str('cevabınız '+ cevap))
        konusma('onaylıyor musunuz')
        onaylama= anlama()
        if onaylama=='Evet':
           with open("chats.txt", "a") as f:
               f.write('\n')
               f.write("'"+str(soru)+"',"+'\n')
               f.write("'"+str(cevap)+"',")
           i=0
           while i  < 100:
               trainer= ListTrainer(chatbot)
               conversation = open('chats.txt','r').readlines()
               trainer.train(conversation)
               i += 1
        else:
            konusma('işlem tekrar ediliyor')
            ekleme()
    elif sifre==('iptal et'):
        wakeword()
    else:
        konusma('sifre yanlış')
        ekleme()
#def muslum():
#    os.system("mpg321 muslum.mp3")
wakeword()
konusma('Sizi dinliyorum')        

while True:
    
    bluetoothVeriAl()
    dongu()
ser.close()
