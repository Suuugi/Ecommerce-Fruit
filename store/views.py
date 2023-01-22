import random
import os
from django.views import generic
from store.models import Product
from django.core.paginator import Paginator
from store.models import Catalog, Order, OrderItem, Product
from django.shortcuts import redirect


class IndexTemplateView(generic.ListView):
    paginate_by = 12
    model = Product
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        # file_name = os.path.join(
        #     os.path.dirname(__file__), 'static\\fruits.txt')
        # build_products_from_txt_file(file_name)
        page = Paginator(self.get_queryset(), 12)
        context['products'] = page.page(self.request.GET.get('page') or '1')
        context['css'] = 'index.css'
        return context

    def get_queryset(self):
        order_by = self.request.GET.get('order_by') or 'name'
        return super().get_queryset().order_by(order_by)

# TODO


def add_to_cart(request, product_id):
    order, created = Order.objects.get_or_create(
        user=request.user,
        # is_ordered=False
    )
    product = Product.objects.get(id=product_id)
    print(order)
    print(product)
    order_item, created = OrderItem.objects.get_or_create(
        order=order,
        product=product,
        # quantity=1
    )
    if not created:
        order_item.quantity = order_item.quantity + 1
        order_item.save()
    return redirect('index')


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
