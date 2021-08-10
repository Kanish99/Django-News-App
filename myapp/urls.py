from django.urls import path, include
# from .views import place_list, place_detail, PlaceAPIView, PlaceDetails
from .views import PlaceAPIView, PlaceDetails, GenericAPIView, GenericAPIViewDetails, PlaceViewSet, PlaceGenericViewSet, PlaceModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('placevs', PlaceViewSet, basename='placevs')
router.register('placegvs', PlaceGenericViewSet, basename='placegvs')
router.register('placemvs', PlaceModelViewSet, basename='placemvs')

urlpatterns = [
    # path('place/', place_list, name='place'),
    path('place/', PlaceAPIView.as_view(), name='place'),
    # path('place/<int:pk>/', place_detail, name='place_detail'),
    path('place/<int:id>/', PlaceDetails.as_view(), name='place_detail'),

    path('generic/', GenericAPIView.as_view(), name='generic'),
    path('generic/<int:id>/', GenericAPIViewDetails.as_view(), name='generic_detail'),
    path('viewset/', include(router.urls)),
    path('viewset<int:id>/', include(router.urls)),
    
]
