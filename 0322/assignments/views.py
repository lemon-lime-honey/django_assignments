from django.shortcuts import render
import random

def today_dinner(request):
    foods = ['피자', '햄버거', '닭갈비', '타코', '난과 커리', '회덮밥', '닭칼국수', '묵은지찜']
    content = {
        'food': random.choice(foods)
    }
    return render(request, 'assignments/today_dinner.html', content)

def throw(request):
    return render(request, 'assignments/throw.html')

def catch(request):
    word = request.GET.get('word')
    content = {
        'word': word,
    }
    return render(request, 'assignments/catch.html', content)

def lotto_create(request):
    return render(request, 'assignments/lotto_create.html')

def lotto(request):
    number = int(request.GET.get('set_number'))
    send = list()
    
    for i in range(number):
        temp = random.sample(range(1, 46), k = 6)
        send.append(temp)
    
    content = {
        'send': send,
    }

    return render(request, 'assignments/lotto.html', content)