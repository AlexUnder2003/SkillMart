from django.contrib import admin

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls', namespace='pages')),
    path('login/', include('login.urls', namespace='login')),
    path('registration/', include('registration.urls',
                                  namespace='registration')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('catalog/', include('catalog.urls', namespace='catalog')),
    path('account/', include('account.urls', namespace='account')),
    path('mycourses/', include('mycourses.urls', namespace='mycourses')),
    path('', include('main.urls', namespace='main')),
]
