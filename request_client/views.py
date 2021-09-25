from django.http import HttpResponse
from rest_framework.views import APIView

# from request_client.utils.facebook_request_client import RequestClient
from request_client.models import SearchKeyword, PostComments
from request_client.utils.sentiment_analyzer import main as Sentiment_analyzer
from .serializer import SearchKeywordSerializer

import json



class SearchView(APIView):
    def get(self, request):
        
        response_data = {'suggestions': []}
        keyword_suggestions = SearchKeyword.objects.all()
        if keyword_suggestions:
            keyword_data = SearchKeywordSerializer(
                instance=keyword_suggestions, many=True)
            response_data['suggestions'] = keyword_data.data

        return HttpResponse(json.dumps(response_data),content_type='application/json',status=200)

    def post(self, request, query=''):
        response_data = {}
        status = 200
        
        try:
            if query is not '':
                comments_for_query = '' 
                # RequestClient().main(search_keyword=query)

                if comments_for_query.get('saved') is True:
                    comment_obj = PostComments.objects.filter(fk_keyword__keyword=query)
                    comment_lst = comment_obj.values_list('comment',flat=True)
                    comments, review = Sentiment_analyzer(comment_lst)
                    response_data = {'comments': comments, 'review': review}
                else:
                    raise
            else:
                status = 404
                response_data['error'] = 'Please enter a valid search keyword'
        except:
            response_data['error'] = 'An error has occured'
            status = 500

        return HttpResponse(json.dumps(response_data),content_type='application/json',status=status)



class HomeView(APIView):
    def get(self,request):
        return HttpResponse('<h1><center>Visit 127.0.0.1:3001/3000 to make a query request !!! </center></h1>')