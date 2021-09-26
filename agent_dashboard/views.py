from django.http import HttpResponse, Http404, JsonResponse
from rest_framework.views import APIView
from django.db.models.functions import ExtractMonth
from django.db.models import Q, Count
from datetime import date, datetime
import json

from agent_dashboard.models import Policy, Customer
from agent_dashboard.serializers import PolicyDetailSerializer


class PolicyEditView(APIView):

    def post(self, request):
        post_data = request.POST or None
        policy_id = post_data.get('policy_id', '')
        errors = ''

        if policy_id:
            policy_object = Policy.objects.get(policy_id=policy_id)
            update_serializer = PolicyDetailSerializer(
                instance=policy_object, data=post_data)

            if update_serializer.is_valid():
                update_serializer.save()
                response_message = 'Premium Updated Successfully'
            else:
                response_message = 'Premium Update Failed ! Please try again'
                # Check for better way to show errors
                errors = str(update_serializer.errors)

        else:
            response_message = 'Invalid Policy Id !'
        return JsonResponse({'message': response_message, 'errors': errors})


class SearchPolicyView(APIView):
    def get(self, request, query_type=None, request_id=None):
        search_query = {}

        if request_id:
            if query_type in ['search_by_policy', 'policy_edit']:
                search_query['policy_id'] = request_id
            elif query_type == 'search_by_customer':
                search_query['fk_customer'] = request_id

            policy_object = Policy.objects.filter(**search_query).order_by('-purchase_date')
            response_data = PolicyDetailSerializer(instance=policy_object, many=True)
            
            return JsonResponse({'response_data': response_data.data})
        else:
            raise Http404("No matching ID not found....")


class MonthlyDataByRegion(APIView):
    def post(self, request):
        selected_region = request.POST['selected_region']
        
        month_wise_region_data = Policy.objects.filter(region__iexact=selected_region).annotate(month=ExtractMonth(
            'purchase_date')).values('month').annotate(monthly_count=Count('policy_id')).values('month', 'monthly_count').order_by('month')
        
        response = self.add_missing_month_data_to_response(month_wise_region_data)
        return JsonResponse({'response': response})

    def add_missing_month_data_to_response(self, queryset):
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
