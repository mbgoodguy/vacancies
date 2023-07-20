from django.http import JsonResponse
from django.views import View
from django.views.generic import DetailView

from ads.models import Category, Ad


def root(request):
    return JsonResponse(data={"status": "ok"})


class CategoriesView(View):
    def get(self, request):
        categories = Category.objects.all()

        result = []
        for category in categories:
            result.append({
                "id": category.id,
                "name": category.name,
            })

        return JsonResponse(result, safe=False)


class AdsView(View):
    def get(self, request):
        ads = Ad.objects.all()

        result = []
        for ad in ads:
            result.append({
                "id": ad.id,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price,

            })

        return JsonResponse(result, safe=False)


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.id,
            "is_published": ad.id,
        })


class CatDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        ad = self.get_object()

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
        })
