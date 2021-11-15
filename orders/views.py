from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import models
from .models import Order


class OrderListView(ListView):
    model = Order
    template_name = 'orders/order_list.html'


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    success_url = reverse_lazy('order_list')
    fields = (
        'employee', 'customer', 'status', 'description', 'mobile_brand', 'mobile_model', 'mobile_IMEI',
        'estimated_amount',
        'estimated_date')
    template_name = 'orders/order_create.html'

    def form_valid(self, form):
        return super().form_valid(form)


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    success_url = reverse_lazy('order_list')
    fields = '__all__'
    template_name = 'orders/order_edit.html'


class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    success_url = reverse_lazy('order_list')
    fields = '__all__'
    template_name = 'orders/order_delete.html'
