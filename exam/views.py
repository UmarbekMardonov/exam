from rest_framework import generics
from django.contrib.auth import get_user_model
from django.db.models import Sum, Count

from rest_framework.response import Response

from . import models
from . import serializers

User = get_user_model()


class ProductView(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductGetView(generics.RetrieveAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductAllSerializer


class LessonAddView(generics.CreateAPIView):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonMainSerializer


class LessonHistoryView(generics.CreateAPIView):
    queryset = models.LessonHistory.objects.all()
    serializer_class = serializers.LessonHistorySerializer


class UserLessonsView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserLessonSerializer


class MainStatistic(generics.GenericAPIView):
    def get(self, request):
        queryset = models.Product.objects.aggregate(
            main_view_count=Sum('view_count'),
            time_spent=Sum('product_history__end_point'),
            hits_lesson=Count('product_history'),
            product_sale_percent=Count(
                'view_count') / Count("subscribers__subscribers") * 100,
        )

        return Response(queryset)


class AdsView(generics.ListAPIView):
    # queryset = models.Ads.objects.all().order_by('?')
    queryset = models.Ads.objects.all().select_related('category').order_by('-id')
    serializer_class = serializers.AdsSerializer
