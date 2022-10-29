from django.urls import path
from webapp.views.base import ProductIndexView
from webapp.views.products import ProductView, ProductAddView, ProductUpdateView, ProductDeleteView
from webapp.views.reviews import ReviewAddView, ReviewUpdateView, ReviewDeleteView

# from webapp.views.projects import ProjectView, ProjectUpdateView, ProjectAddView, ProjectTaskAddView, ProjectDeleteView
# from webapp.views.projects import ProjectUserAddView

urlpatterns = [
    path('', ProductIndexView.as_view(), name='index'),
    path('reviewer/', ProductIndexView.as_view(), name='home'),
    path('reviewer/product/<int:pk>', ProductView.as_view(), name='product_detail'),
    path('reviewer/product/add/', ProductAddView.as_view(), name='product_add'),
    path('reviewer/delete_product/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('reviewer/update_product/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('reviewer/product/review/add/<int:pk>', ReviewAddView.as_view(), name='review_add'),
    path('reviewer/product/review/delete/<int:pk>', ReviewDeleteView.as_view(), name='review_delete'),
    path('reviewer/product/review/update/<int:pk>', ReviewUpdateView.as_view(), name='review_update'),
]
