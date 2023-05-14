from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('about.html', views.about, name="about"),
    path('pricing.html', views.pricing, name="pricing"),
    path('UserPage.html', views.userPage, name="userPage"),
    path('service.html', views.service, name="service"),
    path('offers/<int:pk>/media/', views.book_media, name='book_media'),
    path('regis.html', views.regis, name="regis"),
    path('login.html', views.loginPage, name="login"),
    path('home.html', views.logoutUser, name="logout"),
    path('appointment.html', views.appointment, name="appointment"),
    path('news.html', views.news_list, name="news"),
    path('offers/<int:offer_pk>/reviews/new/', views.review_edit, name='review_create'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('create_service/new/', views.create_service, name='create_service'),
    path('service_added/<int:pk>/', views.service_added, name='services'),
]

