from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def get_sentiment(request):

    if request.method == 'POST':
        
        data = request.POST.dict()
        print(data)
    
        response = {}
        response['test'] = 'success'
        return JsonResponse(response, status=200, safe=False)
    
    response_data = {
        'status': 'error',
        'message': 'Invalid HTTP method',
        'data': None
    }
    return JsonResponse(response_data,status=400)




@csrf_exempt
def get_reviews(request):

    if request.method == 'POST':
       
        data = request.POST.dict()
        print(data)
    
        response = {}
        response['test'] = 'all good'
        return JsonResponse(response, status=200, safe=False)
    
    response_data = {
        'status': 'error',
        'message': 'Invalid HTTP method',
        'data': None
    }
    return JsonResponse(response_data,status=400)



