from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.template.loader import render_to_string
# Create your views here.


challenges = {
    'january': "Eat no meat",
    'february': "Cycle for 15 minutes every day",
    'march': "Read a book",
    'april': "Take a 30-minute walk",
    'may': "Drink 8 cups of water daily",
    'june': "Meditate for 10 minutes",
    'july': "Practice yoga",
    'august': "Write in a journal",
    'september': "Learn a new skill",
    'october': "Cook a new recipe",
    'november': "Volunteer for a day",
    'december': "Practice gratitude daily",
}


def index(request):
    list_items = ''
    months = list(challenges.keys())
    return render(request, "challenges/index.html",
                  {'months':months
                   })


def monthly_challenge_by_number(request, month):
    try:
        months = list(challenges.keys())
        redirect_month = months[month-1]
        redirect_path = reverse('month-challenge', args=[redirect_month])
        if month <= 0:
            return HttpResponse("<h1>This month is not supported!</h1>")
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponse("<h1>This month is not supported!</h1>")


def monthly_challenge(request, month):
    if month.lower() not in challenges.keys():
        return HttpResponse("<h1>This month is not supported!</h1>")
    challenge_text = challenges[month.lower()]
    return render(request, 'challenges/challenge.html', {
        "text": challenge_text,
        "month_name": month,
    })
