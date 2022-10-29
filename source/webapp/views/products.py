from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import ProductsListForm

from webapp.models import Products


class SuccessDetailUrlMixin:
    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductView(DetailView):
    template_name = 'product/product.html'
    model = Products
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.object.products.filter(is_deleted=False)
        return context


class ProductAddView(SuccessDetailUrlMixin, LoginRequiredMixin, CreateView):
    template_name = 'product/product_create.html'
    form_class = ProductsListForm
    model = Products

# class ProductAddView(PermissionRequiredMixin, SuccessDetailUrlMixin, LoginRequiredMixin, CreateView):
#     template_name = 'product/product_create.html'
#     form_class = TasksListForm
#     model = Tasks
#     permission_required = 'webapp.create_tasks'
#
#     def has_permission(self):
#         review = get_object_or_404(Projects, pk=self.kwargs.get('pk'))
#         return (self.request.user == review.user.filter(username=self.request.user) and super().has_permission() or
#                 self.request.user.is_superuser)


class ProductUpdateView(SuccessDetailUrlMixin, LoginRequiredMixin, UpdateView):
    template_name = 'product/product_update.html'
    form_class = ProductsListForm
    model = Products
    context_object_name = 'product'

# class TaskUpdateView(PermissionRequiredMixin, SuccessDetailUrlMixin, LoginRequiredMixin, UpdateView):
#     template_name = 'product/product_update.html'
#     form_class = TasksListForm
#     model = Tasks
#     context_object_name = 'product'
#     permission_required = 'webapp.change_task'
#
#     def has_permission(self):
#         return super().has_permission() or self.get_object().author == self.request.user


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'product/product_delete.html'
    model = Products
    # context_object_name = 'product'
    success_url = reverse_lazy('index')


# class TaskDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
#     template_name = 'product/product_delete.html'
#     model = Tasks
#     context_object_name = 'product'
#     success_url = reverse_lazy('index')
#     permission_required = 'webapp.delete_tasks'
#
#     def has_permission(self):
#         return super().has_permission() or self.get_object().author == self.request.user
