from django.urls import path
from app.views import playerRegister,playerRegister_change_and_delete

urlpatterns = [
    path('', playerRegister),
    path('<int:pk>/',playerRegister_change_and_delete)
]