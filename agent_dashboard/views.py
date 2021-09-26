from django.http import HttpResponse, Http404, JsonResponse
from rest_framework.views import APIView
from django.db.models.functions import ExtractMonth
from django.db.models import Q, Count
from django.conf import settings
from datetime import date, datetime
import json
import logging
log = logging.getLogger(__name__)

from agent_dashboard.models import Policy, Customer
from agent_dashboard.serializers import PolicyDetailSerializer
from agent_dashboard.utils.common_functions import CommonFunctions


class PolicyEditView(APIView):
    '''
    View for handling Policy object modification requests 
    Supported Field : Premium 
    '''
    DEBUG = settings.DEBUG

    def post(self, request):
        post_data = request.POST or None
        if self.DEBUG:
            log.debug('== request.POST ==')
            log.debug(request.POST)

        policy_id = post_data.get('policy_id', '')
        errors = ''

        if policy_id:
            # Get instance of Policy Object for modification
            policy_object = Policy.objects.get(policy_id=policy_id)
            
            # Passed the update data and Policy object in Policy Model serializer
            update_serializer = PolicyDetailSerializer(
                instance=policy_object, data=post_data)

            # Perform the data validation on serializer fields
            if update_serializer.is_valid():
                update_serializer.save()
                response_message = 'Premium Updated Successfully'
            
            else:
                update_errors = update_serializer.errors
                if self.DEBUG:
                    log.debug('== PolicyDetail Serializer Error==')
                    log.debug(update_errors)
                
                response_message = 'Premium Update Failed ! Please try again'
                # Parse the field error through error_parser for clean error messages.
                errors = CommonFunctions().serializer_error_parser(update_errors)

        else:
            response_message = 'Invalid Policy Id !'
        return JsonResponse({'message': response_message, 'errors': errors})


class SearchPolicyView(APIView):
    '''
    View for handling Search sequest on Policy Model
    supported options : Search by Policy_id ,Search by Customer_id
    '''
    DEBUG = settings.DEBUG

    def get(self, request, query_type=None, request_id=None):
        '''
        Get Request handler function for SearchPolicyView
        argumenst : 
                - query_type : Defines search filters based on operation to be performed(Edit/Search) 
                - request_id : id for matching against Policy ID/Customer ID field  
        '''
        search_query = {}
        
        # Basic validation of request_id is integer (by dynamic url routing) and is not None
        if request_id:
            if query_type in ['search_by_policy', 'policy_edit']:
                search_query['policy_id'] = request_id
            elif query_type == 'search_by_customer':
                search_query['fk_customer'] = request_id

            if self.DEBUG:
                log.debug('== Search Query ==')
                log.debug(search_query)
            
            # Filter the Policy objects by search query
            policy_object = Policy.objects.filter(**search_query).order_by('-purchase_date')
            
            # Deserialize returned Policy Object instances  
            response_data = PolicyDetailSerializer(instance=policy_object, many=True)
            search_result = response_data.data

            if self.DEBUG:
                log.debug('== Policy Search Query ==')
                log.debug(search_query)

            return JsonResponse({'response_data': search_result})
        
        else:
            if self.DEBUG:
                log.debug('== Match Not Found Request ID==')
                log.debug(request_id)
    
            raise Http404("No matching ID not found....")


class MonthlyDataByRegion(APIView):
    '''
    View for handling Aggregating Month Wise Policy Purchase Data
    supported options : Group by Region
    '''

    DEBUG = settings.DEBUG

    def post(self, request):
        if self.DEBUG:
            log.debug('== request.POST ==')
            log.debug(request.POST)
        
        # Get selected region to aggregade the month wise data
        selected_region = request.POST.get('selected_region','')

        # Added filters to Count policy id month wise  based on selected region
        month_wise_region_data = Policy.objects.filter(region__iexact=selected_region).annotate(month=ExtractMonth(
            'purchase_date')).values('month').annotate(monthly_count=Count('policy_id')).values('month', 'monthly_count').order_by('month')
        
        # Add the data for missing months as 0 in returned queryset for charting.  
        response = self.add_missing_month_data_to_response(month_wise_region_data)
        return JsonResponse({'response': response})


    def add_missing_month_data_to_response(self, queryset):
        '''
        Add the missing months and setting their count values to 0.
        '''
        available_months = queryset.values_list('month', flat=True)
        available_months_counts = list(queryset.values_list('monthly_count', flat=True))
        
        response = []
        for index in range(12):
            if index+1 in available_months:
                response.append(available_months_counts[0])
                available_months_counts.pop(0)
            else:
                response.append(0)
        
        return response      
