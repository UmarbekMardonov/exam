from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.ProductView.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductGetView.as_view(), name='product-detail'),

    path('lesson/add/', views.LessonAddView.as_view(), name='lesson_add'),
    path('lesson/history/add/', views.LessonHistoryView.as_view(), name='lesson-history-add'),

    path('user/<int:pk>/product/', views.UserLessonsView.as_view(), name='user-product'),

    path('statistic/main/', views.MainStatistic.as_view(), name='static'),
    path('', views.AdsView.as_view()),

]
