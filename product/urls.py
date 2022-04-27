from django.urls import path, include
from product import views
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.ProductView.as_view(), name="home"),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('add-post/', views.AddPostFormView.as_view(), name='add-post'),
    path('delete/<int:pk>', views.PostDeleteView.as_view(), name='delete-post'),
    path('product/edit/<int:pk>', views.EditPostView.as_view(), name='edit-post'),
    path('search/', views.searchproduct, name='search')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   #to display database image in webpage
