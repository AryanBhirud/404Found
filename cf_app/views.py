from django.http import HttpRequest
from django.shortcuts import redirect, render

from .models import Answer


def home(request):
    context = {}
    return render(request, 'cf_app/homepage.html', context)

def themes(request):
    context = {}
    if request.method == 'POST':
        q1 = request.POST.get('q1')
        q2 = request.POST.get('q2')
        q3 = request.POST.get('q3')
        q4 = request.POST.get('q4')
        q5 = request.POST.get('q5')
        q6 = request.POST.get('q6')
        q7 = request.POST.get('q7')
        q8 = request.POST.get('q8')
        q9 = request.POST.get('q9')
        q10 = request.POST.get('q10')
        answer = Answer(q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6, q7=q7, q8=q8, q9=q9, q10=q10)
        answer.save()
        return redirect('success_page')

        

    return render(request, 'cf_app/themes.html', context)
