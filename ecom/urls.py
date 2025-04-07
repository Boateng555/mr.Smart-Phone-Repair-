from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

urlpatterns = [ # New info app as homepage
    path('', include('info.urls')),  # Root URL now points to Info app
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')), 
    path('cart/', include('cart.urls')),
    path('payment/', include('payment.urls')),
    path('return/', include('return.urls')), 
    path('reparatur/', include('reparatur.urls')), 
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)