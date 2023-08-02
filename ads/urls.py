from django.urls import path

from ads.views.categories import CatDetailView, CategoryListView, CategoryUpdateView, CategoryDeleteView, \
    CategoryCreateView
from ads.views.ads import AdDetailView, AdsListView

urlpatterns = [
    path('cat/', CategoryListView.as_view()),
    path('cat/<int:pk>/', CatDetailView.as_view()),
    path('cat/create/', CategoryCreateView.as_view()),
    path('cat/<int:pk>/update/', CategoryUpdateView.as_view()),
    path('cat/<int:pk>/delete/', CategoryDeleteView.as_view()),

    path('ads/', AdsListView.as_view()),
    path('ad/<int:pk>/', AdDetailView.as_view()),
]
