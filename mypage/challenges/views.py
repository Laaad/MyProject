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


def monthly_challenge_by_number(request, month):
    try:
        months = list(challenges.keys())
        redirect_month = months[month-1]
        redirect_path = reverse('month-challenge', args=[redirect_month])
        if month <= 0:
            return HttpResponse("This month is not supported!")
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponse("This month is not supported!")


def monthly_challenge(request, month):
    if month.lower() not in challenges.keys():
        return HttpResponse("This month is not supported!")
    challenge_text = challenges[month.lower()]
    return HttpResponse(challenge_text)
