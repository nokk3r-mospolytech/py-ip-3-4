from django.urls import path
from graphene_django.views import GraphQLView
from . import schema
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),

    # path('graphql', GraphQLView.as_view(graphiql=True, schema=schema.schema)),

    path('admin', views.admin, name='admin'),
    path('create', views.create, name='create'),
    path('api/v1/task', views.TaskCreateView.as_view()),
    path('api/v1/task/list', views.TaskListView.as_view()),
    path('api/v1/task/list/<int:pk>', views.TaskDetailView.as_view()),
    path('api/v1/region', views.CreateView.as_view()),
    path('api/v1/region/list', views.ListView.as_view()),
    # path('api/v1/region/list/<int:pk>', views.ListView.as_view()),
]
