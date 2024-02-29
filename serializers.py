from rest_framework import serializers, viewsets
from .models import Product, Lesson


class ProductSerializer(serializers.ModelSerializer):
    num_lessons = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'start_date', 'cost', 'num_lessons']

    def get_num_lessons(self, obj):
        return obj.lesson_set.count()


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'name', 'video_link']

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
