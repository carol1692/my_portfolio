from django.shortcuts import render
from django.utils.html import strip_tags
from .forms.translate_form import MorseForm
import unidecode, re


MORSE_CODE = {
                'a': '.-',
                'b': '-...',
                'c': '-.-.',
                'd': '-..',
                'e': '.',
                'f': '..-.',
                'g': '--.',
                'h': '....',
                'i': '..',
                'j': '.---',
                'k': '-.-',
                'l': '.-..',
                'm': '--',
                'n': '-.',
                'o': '---',
                'p': '.--.',
                'q': '--.-',
                'r': '.-.',
                's': '...',
                't': '-',
                'u': '..-',
                'v': '...-',
                'w': '.--',
                'x': '-..-',
                'y': '-.--',
                'z': '--..',
                '1': '.----',
                '2': '..---',
                '3': '...--',
                '4': '....-',
                '5': '.....',
                '6': '-....',
                '7': '--...',
                '8': '---..',
                '9': '----.',
                '0': '-----',
                '/': '/',
              }

def index_morse(request):
    if request.method == 'POST':
        form = MorseForm(request.POST)
        if form.is_valid():
            try: 
                text_content = strip_tags(form.cleaned_data["input_text"])
                message = unidecode.unidecode(text_content)
                cleaned = re.sub(r'[^a-zA-Z0-9]',' ', message)
                message_normalized = [cleaned.replace(" ", "/").lower()] 
                morse = [MORSE_CODE[letter] for letter in message_normalized[0] if MORSE_CODE[letter]]
                converted_list = map(str, morse)
                result = ''.join(converted_list)
                return render(request,"morse_translator\index.html", {"morse_form":form, "message":message, "result": result})
            except KeyError:
                error = ("Please insert a valid message... ")
                return render(request,"morse_translator\index.html", {"morse_form":form, "message":message, "error": error})
    else:
        form = MorseForm()
    return render(request,"morse_translator\index.html", {"morse_form":form})
   