import random
import os
from django.views.generic import ListView
from store.models import Product
from django.core.paginator import Paginator
from store.models import Order, OrderItem, Product
from store.forms import OrderItemForm
from django.http import Http404
from django.shortcuts import redirect


class HomepageListView(ListView):
    paginate_by = 10
    model = Product
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        # file_name = os.path.join(
        #     os.path.dirname(__file__), 'static\\fruits.txt')
        # build_products_from_txt_file(file_name)
        page = Paginator(self.get_queryset(), self.paginate_by)
        context['products'] = page.page(self.request.GET.get('page') or '1')
        context['order_item_form'] = OrderItemForm()
        return context

    def get_queryset(self):
        order_by = self.request.GET.get('order_by') or 'name'
        return super().get_queryset().order_by(order_by)

def add_to_cart(request, product_id : int):
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        quantity = int(request.POST['quantity'])
        order, created = Order.objects.get_or_create(
            user=request.user,
            is_ordered=False
        )
        order_item, created = OrderItem.objects.get_or_create(
            order=order,
            product=product,
        )
        if created:
            order_item.quantity = quantity
        else:
            order_item.quantity = order_item.quantity + quantity
        order_item.save()
        return redirect('home')
    else:
        raise Http404()

class CheckoutListView(ListView):
    model = OrderItem
    template_name = 'checkout.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        order, created = Order.objects.get_or_create(
            user=self.request.user,
            is_ordered=False
        )
        order_items = OrderItem.objects.filter(
            order=order,
        )
        context['order_items'] = order_items
        context['sum'] = sum([item.product.price * item.quantity for item in order_items])
        return context



def build_products_from_txt_file(file_name: str) -> None:
    with open(file_name, 'r', encoding='UTF-8') as file:
        for line in file.readlines():
            name = line.strip()
            price = round(random.uniform(0, 4), 2)
            image = os.path.join(os.path.dirname(
                __file__), f'static\\images\\{name}.svg')
            product = Product(
                name=name, price=price, image=image)
            product.save()