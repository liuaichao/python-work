from django.conf.urls import include, url
from django.contrib import admin
from Django.django_test.teachar import views as sv
urlpatterns = [
    # Examples:
    # url(r'^$', 'django_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^teachar/(?P<num>[0-9]{4})', sv.withparam),

]
