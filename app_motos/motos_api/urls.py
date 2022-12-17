from django.urls import path
from .views import MotoListApiView, MotoDetailApiView

urlpatterns = [
    path('', MotoListApiView.as_view(), name="moto_list"),
    path('<int:moto_id>/', MotoDetailApiView.as_view(), name = "moto_detail")
]
