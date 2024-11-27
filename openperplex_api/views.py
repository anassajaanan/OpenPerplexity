from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import StreamingHttpResponse
from .utils import client

@api_view(['POST'])
def search(request):
    try:
        query = request.data.get('query')
        options = request.data.get('options', {})
        
        result = client.search(
            query=query,
            location='ae',  # Set to UAE
            pro_mode=True,
            response_language='en',
            answer_type='text',
            search_type='general',
            return_citations=True,
            return_sources=True,
            return_images=True,
            recency_filter='anytime'
        )
        
        return Response(result)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['POST'])
def custom_search(request):
    try:
        system_prompt = request.data.get('system_prompt')
        user_prompt = request.data.get('user_prompt')
        options = request.data.get('options', {})
        
        result = client.custom_search(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            location=options.get('location', 'us'),
            temperature=options.get('temperature', 0.2),
            top_p=options.get('top_p', 0.9),
            return_images=options.get('return_images', False),
            return_sources=options.get('return_sources', False)
        )
        
        return Response(result)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['POST'])
def get_website_text(request):
    try:
        url = request.data.get('url')
        result = client.get_website_text(url)
        return Response({'text': result})
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['POST'])
def get_website_markdown(request):
    try:
        url = request.data.get('url')
        result = client.get_website_markdown(url)
        return Response({'markdown': result})
    except Exception as e:
        return Response({'error': str(e)}, status=500)