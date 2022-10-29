from django.urls import path
from webapp.views.base import TaskIndexView, ProjectIndexView
from webapp.views.tasks import TaskView, TaskAddView, TaskDeleteView, TaskUpdateView
from webapp.views.projects import ProjectView, ProjectUpdateView, ProjectAddView, ProjectTaskAddView, ProjectDeleteView
from webapp.views.projects import ProjectUserAddView

urlpatterns = [
    path('', TaskIndexView.as_view(), name='index'),
    path('todo_list/', TaskIndexView.as_view(), name='home'),
    path('todo_list/task/<int:pk>', TaskView.as_view(), name='todo_detail'),
    path('todo_list/task/add/', TaskAddView.as_view(), name='todo_add'),
    path('delete_task/<int:pk>', TaskDeleteView.as_view(), name='todo_delete'),
    path('todo_list/update_task/<int:pk>', TaskUpdateView.as_view(), name='todo_update'),
    path('todo_list/projects', ProjectIndexView.as_view(), name='projects'),
    path('todo_list/projects/<int:pk>', ProjectView.as_view(), name='project_detail'),
    path('todo_list/projects/add/', ProjectAddView.as_view(), name='project_add'),
    path('todo_list/projects/task/add/<int:pk>', ProjectTaskAddView.as_view(), name='project_todo_add'),
    path('delete_project/<int:pk>', ProjectDeleteView.as_view(), name='project_delete'),
    path('todo_list/projects/update/<int:pk>', ProjectUpdateView.as_view(), name='project_update'),
    path('todo_list/projects/add/user/<int:pk>', ProjectUserAddView.as_view(), name='project_add_user'),
]
