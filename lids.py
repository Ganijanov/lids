from django.shortcuts import render, redirect
import telebot
import datetime


bot = telebot.TeleBot("7103426824:AAHYGRa3bfg3oID7mZVDW09ny_LaPo7Lszg", parse_mode=None)
def sender(text):
    bot.send_message('-1001752114157', text)


def botforlid(request):
    kurs = "Foundation" if request.POST.get('type') == '1' else  "Frontend" if request.POST.get('type') == '2' else "Backend"
    txt = f"Ism : {request.POST.get('name')}\nRaqam : {request.POST.get('email')}\nKurs : {kurs}\n"
    print(txt)
    # sender(txt)
    return render( request, 'index.html')