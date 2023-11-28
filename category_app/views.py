from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Category
from .serializers import CategorySerializer


class CategoryApiView(APIView):
    permissions_classes = [permissions.AllowAny, ] # AllowAny - АПИ доступен всем, даже без авторизации

    def get(self, request):  # Метод, ответственный за get запрос
        categories = Category.objects.all() # all, filter - Возвращают QuerySet из объектов данного класса
        data = CategorySerializer(instance=categories, many=True).data
        #  many=True - Потому что в переменной categories лежит много объектов класса Category
        #.data - получение наших данных
        return Response(data, status=status.HTTP_200_OK)

    # def post(self, request):
    #     name = request.data.get('name')  # request.data['name']
    #     category = Category(name=name)
    #     category.save()
    #     return Response({'message': 'Category created!'}, status=status.HTTP_201_CREATED)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid(): # is_valid() - True/False, метод проверяет все ли поля есть и правильно ли заполнены
            serializer.save() # save() - Сохранить объект в БД
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # errors - Ошибки сериалайзера


class CategoryDetailApiView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request, pk):
        category = Category.objects.get(id=pk)
        data = CategorySerializer(instance=category).data
        return Response(data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(instance=category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)









