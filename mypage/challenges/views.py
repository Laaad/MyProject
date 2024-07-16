from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def january(request):
    return HttpResponse("Eat no meat!")


def february(request):
    return HttpResponse("Run for 15 minutes everyday!")


def monthly_challenge(request, month):
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
    if month.lower() not in challenges.keys():
        return HttpResponse("This month is not supported!")
    challenge_text = challenges[month.lower()]
    return HttpResponse(challenge_text)
