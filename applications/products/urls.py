from django.views.decorators.cache import cache_page
from rest_framework.routers import DefaultRouter
from .views import ProductAPIView, CategoryAPIView, CommentAPIVIew


router = DefaultRouter()
router.register('category', CategoryAPIView)
router.register('comment', CommentAPIVIew)
router.register('', ProductAPIView)

urlpatterns = [

]
urlpatterns += router.urls
