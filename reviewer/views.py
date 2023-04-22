from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import JsonResponse

def get_sentiment(request):

    if request.method == 'POST':
        # Access the data from the POST request
        data = request.POST.dict()
        print(data)
    
        response = {}
        response['test'] = 'success'
        return JsonResponse(data, status=200, safe=False)
    
    response_data = {
        'status': 'error',
        'message': 'Invalid HTTP method',
        'data': None
    }
    return JsonResponse(response_data,status=400)