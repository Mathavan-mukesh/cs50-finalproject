from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.login_view, name="login"),
    path('register/', views.register, name='register'),
    path("seller/", views.seller,name="seller"),
    path("nav/", views.nav, name="navbar"),
    path('logout/', views.login_view, name='logout'),
    path("footer/",views.footer, name="footer"),
    path("policy/",views.policy, name = "policy"),
    path("terms/",views.terms,name="terms"),
    path('contact/', views.contact_view, name='contact'),
    path("base/",views.base, name="base"),
    path("services/",views.services, name="services"),
    path("about/",views.about, name="about"),
    path("news/",views.news_view, name="news")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)