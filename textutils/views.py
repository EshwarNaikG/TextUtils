# I have created this file - Eshwar
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def ex1(request):
    s='''<h2>Navigation Bar <br> </h2>
        <a href= "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9" > Django Code With Harry Bhai </a><br>
        <a href="https://www.facebook.com/"> Facebook </a> <br>
        <a href="https://www.flipkart.com/"> Flipkart </a> <br>
        <a href="https://www.hindustantimes.com/"> News </a> <br>
        <a href="https://www.google.com/"> Google </a> <br>'''
    return HttpResponse(s)
      
def analyze(request):
    # Get the text from the form
    djtext = request.POST.get('text', 'default')  # Default to empty string

    # Check which checkboxes are selected
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    # check which checkbox is on
    if removepunc == "on":
        analyzed = ''
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': 'Removed Punctuation', 'analyzed_text': analyzed}
        djtext = analyzed  # Update djtext for further processing

        # return render(request, 'analyze.html', params )
        #  Return the analyzed text

    if (fullcaps == "on"):
        analyzed = ''
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'Changed to UPPERCASE', 'analyzed_text': analyzed}
        #  Return the analyzed text
        djtext = analyzed  # Update djtext for further processing

        # return render(request, 'analyze.html', params)
    
    if(newlineremover == "on"):
        analyzed = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed += char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed  # Update djtext for further processing

        # return render(request, 'analyze.html', params)
    
    if(extraspaceremover == "on"):
        analyzed = ''
        for index, char in enumerate(djtext):
            if not (djtext[index] == ' ' and djtext[index + 1] == ' '):
                analyzed += char
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    
    if(charcount == "on"):
        analyzed = len(djtext)
        params = {'purpose': 'Character Count', 'analyzed_text': analyzed}
        
    if(removepunc == "off" and fullcaps == "off" and newlineremover == "off" and extraspaceremover == "off"):

        return HttpResponse("Error: No valid operation selected.")
           
    return render(request, 'analyze.html', params)
  
    

    