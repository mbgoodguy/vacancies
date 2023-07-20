from django.urls import path

from ads.views import CategoriesView, AdsView, CatDetailView, AdDetailView

urlpatterns = [
    path('cat/', CategoriesView.as_view()),
    path('ad/', AdsView.as_view()),
    path('cat/<int:pk>/', CatDetailView.as_view()),
    path('ad/<int:pk>/', AdDetailView.as_view()),
]
