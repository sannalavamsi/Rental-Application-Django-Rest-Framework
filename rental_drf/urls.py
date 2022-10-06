from django.urls import include, path
from django.contrib import admin
#from .api import router

from rest_framework import routers
from rental import views as myapp_views

router = routers.DefaultRouter()
router.register(r'friends', myapp_views.FriendViewset)
router.register(r'belongings', myapp_views.BelongingViewset)
router.register(r'borrowings', myapp_views.BorrowedViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]