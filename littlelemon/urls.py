
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
import restaurant.views

router = DefaultRouter()
router.register(r'tables', restaurant.views.BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),
    path('restaurant/booking/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token)
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
