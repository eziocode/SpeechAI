import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()


def get_info():
    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source)
        print('listening...')
        voice = listener.listen(source)
        info = listener.recognize_google(voice)
        print(info)
        return info.lower()


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login('your mailID', 'password of your mailID')
    email = EmailMessage()
    email['From'] = 'Sender_Email'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'friend': 'email_id of your friend',
    'bro': '--email here--',
    'sister': '--email here--'
    #      can make more emails
}

talk('Hi Sir I am your email assistant for today ')


def get_email_info():
    try:
        talk('To Whom you want to send email')
        name = get_info()
        if name in email_list:
            receiver = email_list[name]
            print(receiver)
            talk('What is the subject of your email')
            subject = get_info()
            talk('What is the message of your email')
            message = get_info()
            send_email(email_list[name], subject, message)
            talk('Email sent successfully')
            talk('Do you want to send more email?')
            send_more = get_info()
            if 'yes' in send_more:
                get_email_info()
            elif 'no' in send_more:
                talk('Thank you for using my email assistant')
    except sr.UnknownValueError:
        talk('Sorry sir, I did not get that')
        get_email_info()
    else:
        talk('Sorry sir, I don\'t know you')
        talk('Do you want to send email to someone else?')
        send_more = get_info()
        if 'yes' in send_more:
            get_email_info()
        elif 'no' in send_more:
            talk('Thank you for using my email assistant')
        else:
            get_email_info()


get_email_info()
