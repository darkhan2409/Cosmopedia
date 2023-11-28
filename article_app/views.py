from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import Article
from .serializers import ArticleSerializer
from rest_framework import status


class ArticleApiView(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request):
        article = Article.objects.all()
        data = ArticleSerializer(instance=article, many=True).data
        return Response(data, status=status.HTTP_200_OK)
