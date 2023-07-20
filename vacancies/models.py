from django.db import models


class Vacancy(models.Model):
    STATUS = [
        ("draft", "Черновик"),  # второй аргумент - человекочитаемое значение для админки
        ("open", "Открыта"),
        ("closed", "Закрыта"),

    ]

    slug = models.SlugField(max_length=75)
    text = models.CharField(max_length=2000)
    status = models.CharField(max_length=6, choices=STATUS, default="draft")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.slug
