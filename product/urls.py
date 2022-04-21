from django.urls import path, include
from product import views
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static


# router = DefaultRouter()
# router.register('add-product', views.ProductViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('', views.ProductView.as_view(), name="home"),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('add-post/', views.AddPostFormView.as_view(), name='add-post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   #to display database image in webpage
