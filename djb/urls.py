from django.contrib import admin
from django.urls import path

import demo_app.views

admin.autodiscover()

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", demo_app.views.index, name="index"),
    path(demo_app.views.adr_bot, demo_app.views.run_bot, name="run_bot"),
    path("start_polling/", demo_app.views.start_polling, name="start_polling"),
    path("stop_polling/", demo_app.views.stop_polling, name="stop_polling"),
    path("admin/", admin.site.urls),
]
