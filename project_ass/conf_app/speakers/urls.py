# from django.contrib import admin
from django.urls import path
# from . import views
from speakers import views

urlpatterns = [
    # path('admin/',admin.site.urls),
    path('speak/', views.speak),
    path('show/', views.show),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
    
] 