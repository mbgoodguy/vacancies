import json
from json import JSONDecodeError

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView

from ads.models import Ad
from amazing_hunting import settings


class AdsListView(ListView):
    model = Ad

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        page_number = request.GET.get("page")

        self.object_list = self.object_list.select_related('author').order_by('-price')
        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_obj = paginator.get_page(page_number)

        ads = []
        for ad in page_obj:
            ads.append({
                'id': ad.id,
                'name': ad.name,
                'author_id': ad.author_id,  # id уже содержится в объекте из page_obj и получаем его через _id
                'price': ad.price,  # id уже содержится в объекте из page_obj и получаем его через _id
                'description': ad.description,
                'is_published': ad.is_published,
                'category_id': ad.category_id,
                'image': ad.image.url if ad.image else None
            })

        response = {
            'items': ads,
            'num_pages': paginator.num_pages,
            'total': paginator.count
        }

        return JsonResponse(response, safe=False)


class AdCreateView(CreateView):
    pass


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
            "author": ad.author_id,
            "author_username": ad.author.username,
            "price": ad.price,
            "description": ad.description,
            "category_id": ad.category_id,
            "is_published": ad.is_published,
            'image': ad.image.url if ad.image else None

        })
