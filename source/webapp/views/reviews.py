from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Reviews, Products
from webapp.forms import ReviewForm


class ReviewUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'review/review_update.html'
    form_class = ReviewForm
    model = Reviews
    context_object_name = 'review'
    permission_required = 'webapp.change_reviews'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse("product_detail", kwargs={"pk": self.object.product.pk})


class ReviewAddView(LoginRequiredMixin, CreateView):
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


class ReviewDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'review/review_delete.html'
    model = Reviews
    context_object_name = 'review'
    permission_required = 'webapp.delete_reviews'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("product_detail", kwargs={"pk": self.object.product.pk})
