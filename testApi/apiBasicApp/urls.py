from .views import articleList,article_detail,articleAPIview,articleDetails,genericAPIView,articleViewSet
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article',articleViewSet,basename='article')

urlpatterns = [
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>/',include(router.urls)),
    #path('article/', articleList),
    path('article/',articleAPIview.as_view()),
    #path('detail/<int:pk>/',article_detail),
    path('detail/<int:id>/',articleDetails.as_view()),
    path('generic/article/<int:id>/',genericAPIView.as_view())
]
