from django.conf import settings
from django.conf.urls.static import static
settings.configure()
print(settings.MEDIA_URL) 