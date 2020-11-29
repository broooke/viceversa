from django.shortcuts import render

def home(requests):
    return render(requests,"index.html")

def reverse(requests):
    user_text = requests.GET['usertext']
    words = len(user_text.split(" "))
    reverse_text = user_text[::-1]
    return render(requests,"index1.html",{"usertext":user_text,"words":words, "reverse":reverse_text})


