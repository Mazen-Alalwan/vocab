from django.http import HttpResponse
from django.shortcuts import render
from googletrans import Translator
translator = Translator()

dictionary = {}



def home(request):
    return render(request, 'home.html')


def translating(request):
    word = request.GET['word']
    translation = translator.translate(word, dest='ar')
    dictionary[word] = translation.text

    return render(request, 'trasnlating.html', {'translation': translation.text, 'dictionary': dictionary.items()})

