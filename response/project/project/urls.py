"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('landing1/',views.landing1,name='landing1'),
    path('landing2/',views.landing2,name='landing2'),
    path('text_responce/',views.text_response,name='text_responce'),
    path('html_response/',views.html_response,name='html_response'),
    path('content/',views.content,name='content'),
]




    # path('admin/', admin.site.urls),
    # path('landingpage/',views.landingpage,name='landingpage'),
    # path('landingpage2/',views.landingpage2,name='landingpage2'),
    # path('text_response/',views.text_response,name='text_response'),
  
    # path('json_response/',views.json_response,name='json_response'),
    # path('csv_response/',views.csv_response,name='csv_response'),
    # path('pdf_response/',views.pdf_response,name='pdf_response'),
    # path('zip_response/',views.zip_response,name='zip_response'),
    # path('css_response/',views.css_response,name='css_response'),
    # path('jpeg_image_response/',views.jpeg_image_response,name='jpeg_image_response'),



    # # render 
    # path('my_render1/',views.my_render1,name='my_render1'),
    # path('my_render2/',views.my_render2,name='my_render2'),
    # path('my_render3/<int:x>/',views.my_render3,name='my_render3'),
    # path('my_render4/<str:name>/',views.my_render4,name='my_render4'),
    # path('my_render5/<slug:argue>/',views.my_render5,name='my_render5'),
    # path('my_render6/<slug:name>/<slug:age>/<slug:qual>/',views.my_render6,name='my_render6'),
    # # json response
    # path('my_Json1/',views.my_Json1,name='my_json1'),
    # path('my_Json2/',views.my_Json2,name='my_json2'),
    # path('my_Json3/',views.my_Json3,name='my_json3'),
    # path('my_Json4/',views.my_Json4,name='my_json4'),
    # path('my_Json5/',views.my_Json5,name='my_json5'),
    # path('my_redirect1/',views.my_redirect1,name='my_redirect1'),
    # path('my_redirect2/',views.my_redirect2,name='my_redirect2'),
    # path('my_redirect3/',views.my_redirect3,name='my_redirect3'),
    # path('my_redirect4/',views.my_redirect4,name='my_redirect4'),
    # path('my_redirect5/',views.my_redirect5,name='my_redirect5'),
    # path('my_redirect6/',views.my_redirect6,name='my_redirect6'),


