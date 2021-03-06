from django.urls import path
from pols import views

app_name = 'pols'

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:question_id>/',views.detail, name='detail'),
    path('<int:question_id>/vote/',views.vote,name='vote'),
    path('<int:question_id>/results/',views.results,name='results'),
    path('registerQ/', views.registerQ, name='registerQ'),
    path('registerC/<int:question_id>/', views.registerC, name='registerC'),
    path('deleteQ/<int:question_id>',views.deleteQ,name = 'deleteQ'),
    path('deleteC/<int:choice_id>',views.deleteC,name='deleteC'),
    path('search/',views.search,name='search'),
]
