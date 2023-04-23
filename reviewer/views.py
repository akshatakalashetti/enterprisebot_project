from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .helper import sentiment_analyser
from .models import Reviews
import json

@csrf_exempt
def get_sentiment(request):

    if request.method == 'POST':
        data= json.loads(request.body)
        print(data)
        statement = data.get('statement',None)
        if not statement:
            response_data = {
                'status': 'error',
                'message': 'missing review statement',
                'data': None
                }
            return JsonResponse(response_data,status=400)

        sentiment, avg_score = sentiment_analyser(statement)
        response_data = {
            'status': 'success',
            'message': 'Got sentiment analysis results',
            'data': {
                'statement' : statement,
                'sentiment': sentiment,
                'avg_polarity_score': avg_score,
            }
            }
        return JsonResponse(response_data,status=200)


    
    response_data = {
        'status': 'error',
        'message': 'Invalid HTTP method',
        'data': None
    }
    return JsonResponse(response_data,status=400)




@csrf_exempt
def get_reviews(request):
    # sentiments= best, good, neutral, bad, worst
    # colors= red, green, white, purple
    # sizes= 64, 256
    if request.method == 'POST':
        data= json.loads(request.body)
        print(data)
        sentiment = data.get('sentiment',None)
        color = data.get('color',None)
        size = data.get('size',None)
        reviews = Reviews.objects.all()
        if sentiment:
            reviews = reviews.filter(sentiment__icontains=sentiment)
        if color:
            reviews = reviews.filter(color__icontains=color)
        if size:
            reviews = reviews.filter(size__icontains=size)

        review_list = []
        for i in reviews:
            review_list.append({
                'title': i.title,
                'review_body': i.review_body,
                'color': i.color,
                'size': i.size,
                'sentiment': i.sentiment,
            })

        response_data = {
        'status': 'success',
        'message': 'Filtered reviews',
        'data': review_list,
        }
        return JsonResponse(response_data,status=200)

    response_data = {
        'status': 'error',
        'message': 'Invalid HTTP method',
        'data': None
    }
    return JsonResponse(response_data,status=400)



