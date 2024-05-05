
from django.contrib import messages
from datetime import datetime
from .models import Contact
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.http import Http404


# def index(request):
#     return render(request, "home.html")

def login(request):
    return render(request, "login.html")

def signup(request):
    return render(request, "signup.html")

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        date = datetime.today()
        
        contact = Contact(name=name, email=email, phone=phone, message=message, date=date)
        contact.save()
        
        messages.success(request, "Your message has been sent successfully!")
    return render(request, 'home.html')

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# Show question and choices
def detail(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request, 'polls/detail.html', 
                    {'question': question})

#Get question and display results
def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/results.html',                  
                    {'question':question})

# Vote for a qerstion choice
def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', 
                      { 'question': question,
                        'error_message': 'You did not select a choice.'})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args = (question.id,)))
    