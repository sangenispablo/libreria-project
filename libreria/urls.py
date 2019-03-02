from django.contrib import admin
from django.urls import path

# Proyecto
urlpatterns = [
    path('admin/', admin.site.urls),
]

# App Catalogo
from django.urls import include

urlpatterns += [
    path('catalogo/', include('catalogo.urls')),
]

#Redirijimos el trafico de la raiz a la app catalogo
from django.views.generic import RedirectView

urlpatterns += [
    path('', RedirectView.as_view(url='/catalogo/', permanent=True)),
]

# Use static() para servir archivos estaticos solo durante el desarrollo
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)