from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Reviews, Products
from webapp.forms import ReviewForm


class SuccessDetailUrlMixin:
    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


# class CustomUserPassesTestMixin(UserPassesTestMixin):
#     groups = []
#
#     def test_func(self):
#         return self.request.user.groups.filter(name__in=self.groups).exists()

# class ReviewAddView(SuccessDetailUrlMixin, LoginRequiredMixin, CreateView):
#     template_name = 'review/review_create.html'
#     form_class = ProjectForm
#     model = Projects
#     groups = ['manager']

# class ProjectAddView(CustomUserPassesTestMixin, SuccessDetailUrlMixin, LoginRequiredMixin, CreateView):
#     template_name = 'review/review_create.html'
#     form_class = ProjectForm
#     model = Projects
#     groups = ['manager']


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'review/review_update.html'
    form_class = ReviewForm
    model = Reviews
    context_object_name = 'review'

    def get_success_url(self):
        return reverse("product_detail", kwargs={"pk": self.object.product.pk})


class ReviewAddView(SuccessDetailUrlMixin, LoginRequiredMixin, CreateView):
    template_name = 'review/review_create.html'
    form_class = ReviewForm
    model = Reviews

    def form_valid(self, form):
        product = get_object_or_404(Products, pk=self.kwargs.get('pk'))
        form.instance.author = self.request.user
        review = form.save(commit=False)
        review.product = product
        review.save()
        return redirect('product_detail', pk=product.pk)

    # def has_permission(self):
    #     print(self.request.user.is_superuser)
    #     project = get_object_or_404(Projects, pk=self.kwargs.get('pk'))
    #     return (self.request.user == project.user.filter(username=self.request.user) and super().has_permission() or
    #             self.request.user.is_superuser)


class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'review/review_delete.html'
    model = Reviews
    context_object_name = 'review'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        return reverse("product_detail", kwargs={"pk": self.object.product.pk})
