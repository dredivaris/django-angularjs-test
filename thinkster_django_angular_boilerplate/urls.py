from django.conf.urls import patterns, url, include
from rest_framework_nested import routers
from authentication.views import AccountViewSet, LoginView, LogoutView
from thinkster_django_angular_boilerplate.views import IndexView

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)


urlpatterns = patterns(
  '',

  url(r'^api/v1/', include(router.urls)),
  url(r'^api/v1/auth/login/', LoginView.as_view(), name='login'),
  url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),

  url('^.*$', IndexView.as_view(), name='index'),
)
