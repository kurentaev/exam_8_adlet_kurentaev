from django.db.models import Q
from django.utils.http import urlencode
from django.views.generic import ListView
from webapp.models import Products
from webapp.forms import SearchForm


class ProductIndexView(ListView):
    template_name = 'product/product_index.html'
    model = Products
    context_object_name = 'products'
    ordering = ('-created_at',)
    paginate_by = 10
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('search')
        return None

    def get_queryset(self):
        queryset = super(ProductIndexView, self).get_queryset()
        if self.search_value:
            query = Q(name__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductIndexView, self).get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context


# class ProjectIndexView(ListView):
#     template_name = 'review/project_index.html'
#     context_object_name = 'projects'
#     ordering = ('summary',)
#     model = Projects
#     paginate_by = 5
#     paginate_orphans = 1
#
#     def get(self, request, *args, **kwargs):
#         self.form = self.get_search_form()
#         self.search_value = self.get_search_value()
#         return super().get(request, *args, **kwargs)
#
#     def get_search_form(self):
#         return SearchForm(self.request.GET)
#
#     def get_search_value(self):
#         if self.form.is_valid():
#             return self.form.cleaned_data.get('search')
#         return None
#
#     def get_queryset(self):
#         queryset = super(ProjectIndexView, self).get_queryset()
#         if self.search_value:
#             query = Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value)
#             queryset = queryset.filter(query)
#         return queryset
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super(ProjectIndexView, self).get_context_data(object_list=object_list, **kwargs)
#         context['form'] = self.form
#         if self.search_value:
#             context['query'] = urlencode({'search': self.search_value})
#         return context
