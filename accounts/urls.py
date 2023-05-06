from knox import views as knox_views
from .views import LoginAPI, RegisterAPI, UserAPI, ChangePasswordView, reviewListCreateView, Review_List, \
    View_Contractors, Detail_View_Contractors, ProfileListCreateView, ProfileRetrieveUpdateDestroyView
from django.urls import path

urlpatterns = [
    path('signup/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('user/', UserAPI.as_view(), name='user'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('reviews/', reviewListCreateView, name='review-list-create'),
    path('review-view/', Review_List.as_view(), name="review"),
    path("contractors/", View_Contractors.as_view(), name='contractors' ),
    path('detail-contractors/<int:pk>/', Detail_View_Contractors.as_view(), name='contractors-detail'),
    path('profiles/', ProfileListCreateView.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', ProfileRetrieveUpdateDestroyView.as_view(), name='profile-retrieve-update-destroy'),
]
