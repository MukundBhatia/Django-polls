from django.urls import path
from . import views

app_name = 'polls'
# add this to let django differentiate which url to select if there is
# conflict while using multiple apps
urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
# using generic views to remove redundancy

# https://stackoverflow.com/questions/39574813/error-loading-mysqldb-module-no-module-named-mysqldb
