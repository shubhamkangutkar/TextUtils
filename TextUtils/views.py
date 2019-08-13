# Dev created file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext =request.POST.get('text', 'default')

    removepunc =request.POST.get('remove punc', 'off')
    fullcaps =request.POST.get('ALL UPPERCASE', 'off')
    spacermv =request.POST.get('space remover', 'off')
    exspacermv =request.POST.get('extraspace remover', 'off')
    charcnt =request.POST.get('character counter', 'off')
    newline =request.POST.get('new line remover', 'off')

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=''
        for c in djtext:
            if c not in punctuations:
                analyzed = analyzed + c
        params = {'purpose': 'Remove Punctuation', 'analyzed_text': analyzed}
        djtext = analyzed

    if newline == 'on':
        analyzed =''
        p='\n'
        for c in djtext:
            if c != "\n" and c!= "\r":
                analyzed = analyzed + c
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if spacermv == 'on':
        analyzed =''
        for c in djtext:
            if c != ' ':
                analyzed = analyzed + c
        params = {'purpose': 'Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == 'on':
        analyzed = djtext.upper()
        params = {'purpose': 'ALL UPPERCASE', 'analyzed_text': analyzed}
        djtext = analyzed

    if exspacermv =='on':
        analyzed=" "
        for index,c in enumerate(djtext):
            if djtext[index] == ' ' and djtext[index+1] == ' ':
                pass
            else:
                analyzed = analyzed +c
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if charcnt == 'on':
        analyzed = 'Total Character are : '+str(len(djtext))
        params = {'purpose': 'Character Counter', 'analyzed_text': analyzed}
        djtext = analyzed
    return render(request, 'analyze.html', params)

def about(request):
    return render(request, 'about.html')
