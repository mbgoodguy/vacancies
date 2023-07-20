import json

from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from vacancies.models import Vacancy


def hello(request):
    return HttpResponse("Hello World!")


@method_decorator(csrf_exempt, name="dispatch")
class VacanciesView(View):

    def get(self, request):
        vacancies = Vacancy.objects.all()

        search_text = request.GET.get("text", None)  # добавляем поиск по тексту
        if search_text:
            vacancies = vacancies.filter(text=search_text)  # filter - фильтрует наши данные по параметрам

        response = []
        for vacancy in vacancies:
            response.append({
                "id": vacancy.id,
                "text": vacancy.text
            })

        return JsonResponse(response, safe=False)  # safe=False - скармливаем данные как есть и говорим отключить проверки

    def post(self, request):
        vacancy_data = json.loads(
            request.body)  # забираем данные. это будут данные из request.body, приведенные к словарю

        vacancy = Vacancy()  # создаем инстанс нашей модели
        vacancy.text = vacancy_data["text"]  # в поле text сохраняем то что пришло из данных в поле text

        vacancy.save()

        return JsonResponse({
            "id": vacancy.id,
            "text": vacancy.text
        })


class VacancyDetailView(DetailView):
    model = Vacancy

    def get(self, request, *args, **kwargs):
        vacancy = self.get_object()

        return JsonResponse({
            "id": vacancy.id,
            "text": vacancy.text
        })
