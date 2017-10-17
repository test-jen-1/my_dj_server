from django.conf.urls import url
from django.contrib import admin

from guest_book.views import index_view, post_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index$', index_view),
    url(r'^post_view$', post_view),
]
