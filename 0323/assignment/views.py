from django.shortcuts import render


def main(request):
    return render(request, 'assignment/main.html')


def throw(request):
    return render(request, 'assignment/throw.html')


def catch(request):
    target = request.GET.get('target')
    content = {
        'target': target,
    }
    return render(request, 'assignment/catch.html', content)


def number_print(request, number):
    context = {
        'number': number,
    }
    return render(request, 'assignment/number_print.html', context)


def calculate(request, number1, number2):
    context = {
        'plus': number1,
        'minus': number2,
        'times': number1 * number2, 
        'quotient': number1 // number2,
    }
    return render(request, 'assignment/calculate.html', context)