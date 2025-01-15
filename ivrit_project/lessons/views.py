from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def layout(request):
    return render(request, 'lessons/layout.html')

def lessons(request):
    return render(request, 'lessons/lesson1.html')


#@csrf_exempt
def GetInputValue(request):
  input_value = request.POST['quantity']
  return HttpResponse(input_value)




