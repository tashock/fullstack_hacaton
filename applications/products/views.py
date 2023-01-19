from django.utils.decorators import method_decorator
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.views.decorators.cache import cache_page

from applications.products.serializers import ProductSerializer, CategorySerializer, RatingSerializer, CommentSerializer
from applications.products.models import Product, Category, Like, Rating, Comment
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import status


class ProductPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ProductAPIView(ModelViewSet):
    pagination_class = ProductPagination
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['title']
    ordering_fields = ['price']



    def get_permissions(self):
        if self.action == 'POST':
            return [IsAuthenticatedOrReadOnly]
        else:
            return super().get_permissions()

    @action(methods=['POST'], detail=True)
    def likes(self, request, pk, *args, **kwargs):  # post/id/like/
        like_obj, _ = Like.objects.get_or_create(post_id=pk, owner=request.user)
        like_obj.like = not like_obj.like
        print(like_obj)
        like_obj.save()
        status = 'liked'
        if not like_obj.like:
            status = 'unlike'
        return Response({'status': status})

    @action(detail=True, methods=['POST'])
    def ratings(self, request, pk, *args, **kwargs):
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        rating_obj, _ = Rating.objects.get_or_create(post_id=pk, owner=request.user)
        rating_obj.rating = request.data['rating']
        rating_obj.save()
        return Response(request.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    @method_decorator(cache_page(15))
    def list(self, request, *args, **kwargs):
        return super().list(request)


class CategoryAPIView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CommentAPIVIew(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset
