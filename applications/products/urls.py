from rest_framework.routers import SimpleRouter
from .views import ProductAPIView, CategoryAPIView, CommentAPIVIew


router = SimpleRouter()
router.register('category', CategoryAPIView)
router.register('comment', CommentAPIVIew)
router.register('', ProductAPIView)
print(router.urls)

urlpatterns = [

]
urlpatterns += router.urls
