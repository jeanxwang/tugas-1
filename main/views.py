from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Aliyah Faza Qinthara',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)