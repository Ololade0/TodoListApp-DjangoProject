
from django.urls import path
from .views import home, logoutUser, loginuser, signupuser, createtodo,completetodo,currenttodos, completedtodo, deletetodo, viewtodo

urlpatterns = [


    path('signup', signupuser,name='signupuser'),
    path('',home,name='home'),
    path('logout',logoutUser,name='logoutuser'),
    path('login',loginuser,name='loginuser'),
    path('createtodo',createtodo,name='createtodo'),
    path('completedtodo',completedtodo,name='completedtodos'),
    path('viewtodo/<int:todo_pk>',viewtodo,name='viewtodo'),
    path('viewtodo/<int:todo_pk>/complete',completetodo,name='completetodos'),
    path('viewtodo/<int:todo_pk>/delete',deletetodo,name='deletetodos'),
    path('currenttodos', currenttodos,name='currenttodos'),



]

