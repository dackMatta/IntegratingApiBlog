from django.shortcuts import render
import requests
from django.http import JsonResponse
from faker import Faker

def random_quote(request):
    fake = Faker()
    quote = fake.sentence()
    return JsonResponse({'quote': quote})

def index(request):
  r1 = requests.get('https://api.github.com/events')
  data = r1.json()
  events = data[0]['repo']
  
  r2 = requests.get('https://www.boredapi.com/api/activity')
  data = r2.json()
  activity  = data['activity']

  r3 = requests.get('https://dog.ceo/api/breeds/image/random')
  res3 = r3.json()
  dog = res3['message']

  return render(request, 'templates/index.html', {'events': events, 'activity': activity, 'dog': dog})