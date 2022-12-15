from django.urls import path
from .import views

app_name = 'company_app'
urlpatterns = [
    path('company_register/', views.CompanyRegister.as_view(), name='company_register'),
    path('login/', views.Login.as_view(), name='login'),
    path('company_home', views.Home.as_view(), name='company_home'),
    path('company-profile/', views.CompanyProfile.as_view(), name='company_profile'),
    path('update-company-profile/', views.UpdateCompanyProfile.as_view(), name='update_company_profile'),

    path('job/add', views.add_job, name='add_job'),
    path('job/<slug>/edit/', views.edit_job, name='edit-job-post'),
    path('job/<slug>', views.job_detail, name='add-job-detail'),
    path('all-jobs/', views.all_jobs, name='all_jobs'),
    # path('candidate/search/', views.search_candidates, name='search-candidates'),
    # path('job/<slug>/search/', views.job_candidate_search,
    #      name='job-candidate-search'),
    path('applicant-list/<slug>/', views.applicant_list, name='applicant_list'),
    path('selected/<slug>', views.selected_list, name='selected_list'),
    
    path('select-applicant/<job_id>/<can_id>/',
         views.select_applicant, name='select-applicant'),
    path('remove-applicant/<job_id>/<can_id>/',
         views.remove_applicant, name='remove_applicant'),
    path("<str:room_name>/", views.ChatRoom.as_view(), name="company_chat_room"),
]






