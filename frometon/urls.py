from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('users/', include("users.urls")),
    path('',  RedirectView.as_view(url='/users/home', permanent=False)),
    path('products/', include("products.urls")),
]
