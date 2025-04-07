from django.shortcuts import render
#not working now
def return_home(request):
    context = {'message': 'Welcome to the return page!'}
    return render(request, 'return_home/return.html', context)
# Create your views here.
