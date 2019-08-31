from django.urls import path

from . import views

urlpatterns = [
    path('members',views.members, name='teammembers'),
    path('organogram',views.org_chart, name='teamorg'),
    path('committee',views.committee, name='teamcommittee'),
    path('seniority',views.seniority, name='teamseniority'),
]