import json
from json import JSONDecodeError

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Category, Ad


def root(request):
    return JsonResponse(data={"status": "ok"})


@method_decorator(csrf_exempt, name='dispatch')
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

    def post(self, request):
        try:  # пробуем получить данные из тела запроса. Если происходит исключение, Python переходит к блоку except
            category_data = json.loads(request.body)
        except JSONDecodeError:  # Если  запрос пустой то выбрасываем исключение
            return JsonResponse({"error": 'No data, invalid JSON format'}, status=400)

        category_name = category_data.get('name')
        if not category_name:  # Если в запросе не указано имя категории
            return JsonResponse({"error": "Category name is required"}, status=400)

        try:  # пробуем получить из БД категорию с именем как в теле запроса
            category = Category.objects.get(name=category_name)
            return JsonResponse({"error": 'Category already exists'}, status=400)
        except ObjectDoesNotExist:  # если категория с заданным именем не существует то возникнет указанный эксепшен
            pass  # Пропускаем обработку эксепшена

        category = Category(
            name=category_name
        )
        category.save()

        return JsonResponse({
            "id": category.id,
            "name": category.name,
        })


@method_decorator(csrf_exempt, name='dispatch')
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

    def post(self, request):
        try:
            ad_data = json.loads(request.body)
        except JSONDecodeError:
            return JsonResponse({"error": "no data in request"}, status=400)

        required_fields = ['name', 'author', 'price', 'description', 'address', 'is_published']
        for field in required_fields:
            if field not in ad_data:
                return JsonResponse({"error": f"missing required field '{field}'"}, status=400)

        ad = Ad(
            name=ad_data['name'],
            author=ad_data['author'],
            price=ad_data['price'],
            description=ad_data['description'],
            address=ad_data['address'],
            is_published=ad_data['is_published'],
        )
        ad.save()

        return JsonResponse({
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published
        })


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
            "address": ad.address,
            "is_published": ad.is_published,
        })


class CatDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        ad = self.get_object()

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
        })
