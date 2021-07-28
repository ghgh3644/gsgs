from django.urls import path

from profileapp.views import ProfileCreateView, ProfileUpdateView

app_name = 'profileapp'

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create'),     #장고에서 사용하는 것 가져오기
    path('update/<int:pk>', ProfileUpdateView.as_view(), name='update'),
]