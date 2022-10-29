from django.contrib.auth.mixins import UserPassesTestMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import ProductsListForm

from webapp.models import Products


class SuccessDetailUrlMixin:
    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class CustomUserPassesTestMixin(UserPassesTestMixin):
    groups = []

    def test_func(self):
        return self.request.user.groups.filter(name__in=self.groups).exists()


class ProductView(DetailView):
    template_name = 'product/product.html'
    model = Products
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.object.products.filter(is_deleted=False)
        return context


class ProductAddView(CustomUserPassesTestMixin, PermissionRequiredMixin, SuccessDetailUrlMixin, CreateView):
    template_name = 'product/product_create.html'
    form_class = ProductsListForm
    model = Products
    permission_required = 'webapp.add_products'
    groups = ['moderator']


class ProductUpdateView(CustomUserPassesTestMixin, PermissionRequiredMixin, SuccessDetailUrlMixin, UpdateView):
    template_name = 'product/product_update.html'
    form_class = ProductsListForm
    model = Products
    context_object_name = 'product'
    permission_required = 'webapp.change_products'
    groups = ['moderator']


class ProductDeleteView(CustomUserPassesTestMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'product/product_delete.html'
    model = Products
    success_url = reverse_lazy('index')
    permission_required = 'webapp.delete_products'
    groups = ['moderator']
