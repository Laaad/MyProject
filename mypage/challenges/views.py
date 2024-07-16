from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
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
    for month in months:
        capitalised_month = month.capitalize()
        month_path = reverse("month-challenge",args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalised_month}</a></li>"

    response_data = f"<ul>{list_items}"
    return HttpResponse(response_data)


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
    response_data = f"<h1>{challenge_text}</h1>"
    return HttpResponse(response_data)
