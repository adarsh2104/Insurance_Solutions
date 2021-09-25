from django.http import HttpResponse,Http404,JsonResponse
from rest_framework.views import APIView
from policy_dashboard.models import Policy,Customer
from policy_dashboard.serializers import PolicyDetailSerializer
from django.db.models import Q,Count
from datetime import date,datetime
import json

from django.db.models.functions import ExtractMonth
# Policy.objects.annotate(month=ExtractMonth('purchase_date')).values('month').annotate(count=Count('id')).values('month', 'count')          



class SearchPolicyView(APIView):
    def get(self, request,query_type=None,request_id=None):
        print('-------------',request_id,query_type)
        search_query = {}
        if request_id:
            if query_type in ['search_by_policy','policy_edit']:
                search_query['policy_id'] = request_id
            elif query_type == 'search_by_customer':
                search_query['fk_customer'] = request_id
            policy_object = Policy.objects.filter(**search_query)
            print('====>',search_query,policy_object)
            response_data = PolicyDetailSerializer(instance=policy_object,many=True)
            return JsonResponse({'response_data':response_data.data})
        else:
            raise Http404("No matching ID not found....")


class PolicyEditView(APIView):
    def post(self,request):
        post_data = request.POST or None
        policy_id = post_data.get('policy_id','')
        response_message= ''
        errors = ''
        if policy_id:
            policy_object =  Policy.objects.get(policy_id=policy_id)
            update_serializer = PolicyDetailSerializer(instance= policy_object,data = post_data)
            if update_serializer.is_valid():
                update_serializer.save()
                response_message = 'Premium Updated Successfully'
            else:
                response_message = 'Premium Update Failed ! Please try again'
                errors = str(update_serializer.errors)
        else:
            response_message = 'Invalid Policy Id !'
        return JsonResponse({'message':response_message,'errors':errors})



class MonthlyDataByRegion(APIView):
    
    def add_missing_month_data_to_response(self,queryset):
        available_months = queryset.values_list('month',flat=True)
        response = list(queryset.values('month', 'monthly_count'))
        
        for month in range(1,13):
            if month not in available_months:
                response.append({'month':month,'monthly_count':0})
        sorted_data = sorted(response,key=lambda x:x['month'])

        return [data['monthly_count'] for data in sorted_data]


    def post(self,request):
        selected_region = request.POST['selected_region']
        month_wise_region_data = Policy.objects.filter(region__iexact=selected_region).annotate(month=ExtractMonth('purchase_date')).values('month').annotate(monthly_count=Count('policy_id')).values('month', 'monthly_count')
        response = self.add_missing_month_data_to_response(month_wise_region_data)
        return JsonResponse({'response':response})
        # all_regions = Policy.objects.only('region').distinct().value


        # if isinstance(monthly_data_date,str):
        #     # monthly_data_date = datetime.strptime(monthly_data_date,'%Y-%m')
        #     date_part =  monthly_data_date.split('-')
        # policy_objects = Policy.objects.filter(region=)