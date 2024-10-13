from BlogApp import views
from django.urls import path
urlpatterns=[
    path('index_page/',views.index_page, name="index_page"),
    # User creation, login and logout
    path('user/register/',views.BlogUserCreateView.as_view()),
    path('user/login/',views.LoginView.as_view()),
    path('user/logout/',views.LogoutView.as_view()),
    # User update
    path('user/',views.BlogUSerRetrieveUpdateView.as_view()),
    # Post creation, view, update and delete
    path('post/',views.PostCreateView.as_view()),
    path('post/<int:id>/',views.PostRetreiveUpdateDestroyView.as_view()),
    # Post list view for user and for all
    path('post/user/',views.UserPostListView.as_view(), name='blog-list'),
    path('post/public/',views.PostListView.as_view()),
]