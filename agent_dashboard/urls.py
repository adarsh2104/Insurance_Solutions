from django.urls import path
from .views import SearchPolicyView,PolicyEditView,MonthlyDataByRegion

urlpatterns = [
    path('policy_edit/',PolicyEditView.as_view(),name='policy_edit'),
    path('regions/',MonthlyDataByRegion.as_view(),name='monthly_data_lookup'),
    path('<str:query_type>/<int:request_id>',SearchPolicyView.as_view(),name='policy_search')
    
]

