import stripe
from django.conf import settings
from django.shortcuts import render
from .models import Item, Discount, Tax, Order, OrderDetail
from django.shortcuts import redirect
from django.http import HttpResponse

stripe.api_key = settings.STRIPE_SECRET_KEY


# Create your views here.


def first_page(request, id=0):
    if id == 0:
        item = Item()
        item.name = 'Товар не выбран'
        item.description = ' '
        item.price = 0
    else:
        item = Item.objects.get(pk=id)
    list_items = Item.objects.all()
    dict_obj = {'item': item,
                'list_items': list_items}
    return render(request, './index.html', dict_obj)


def get_order_line_items(order_id):
    order_items_dict = {}
    tax = Tax.objects.get(id=Order.objects.get(id=order_id).order_tax.id).Tax_percent
    discount = Discount.objects.get(id=Order.objects.get(id=order_id).order_discount.id).Discount_percent
    order_items = OrderDetail.objects.values('item_binding_id', 'item_count').filter(detail_binding=order_id)
    for i in order_items:
        order_items_dict.update({i['item_binding_id']: {'item_count': i['item_count']}})
    description_items = Item.objects.values('id', 'name', 'price', 'description').filter(id__in=order_items_dict.keys())
    for i in description_items:
        order_items_dict[i['id']].update({'name': i['name'], 'price': i['price'], 'description': i['description']})
    line_items_for_stripe = []
    for item in order_items_dict:
        price = order_items_dict[item]['price'] + order_items_dict[item]['price'] * (tax / 100) - \
                order_items_dict[item]['price'] * (discount / 100)
        line_items_for_stripe.append(
            {
                'price_data': {
                    'currency': 'rub',
                    'product_data': {
                        'name': order_items_dict[item]['name'],
                        'description': f" Описание:{order_items_dict[item]['description']}. "
                                       f"Налог: {tax}%. Скидка: {discount}%"
                    },
                    'unit_amount': round(price),
                },
                'quantity': order_items_dict[item]['item_count'],
            }
        )
    return line_items_for_stripe


def create_checkout_session(list_items,host):
    session = stripe.checkout.Session.create(
        line_items=list_items,
        mode='payment',
        success_url=f'http://{host}/success',
        cancel_url=f'http://{host}/cancel',
    )
    return session


def buy_item_page(request):
    item_id = request.POST['id']
    host=request.headers['Host']
    item = Item.objects.get(pk=item_id)
    line_items = [{
        'price_data': {
            'currency': 'rub',
            'product_data': {
                'name': f'{item.name}',
            },
            'unit_amount': item.price,
        },
        'quantity': 2,
    }]
    session = create_checkout_session(line_items,host)
    return redirect(session.url, code=303)


def buy_order_page(request, id=0):
    order_id = id
    host = request.headers['Host']
    session = create_checkout_session(get_order_line_items(order_id),host)
    return redirect(session.url, code=303)


def success_page(request):
    return render(request, './success.html')


def cancel_page(request):
    return render(request, './cancel.html')


def get_stripe_id(request, id=0):
    host = request.headers['Host']
    item = Item.objects.get(pk=id)
    line_items = [{
        'price_data': {
            'currency': 'rub',
            'product_data': {
                'name': f'{item.name}',
            },
            'unit_amount': item.price,
        },
        'quantity': 2,
    }]
    session = create_checkout_session(line_items,host)
    return HttpResponse(f'session_id:{session.id}\nurl:{session.url}')

def get_default(request):
    data = {'host':request.headers['Host'],
            'order_list':list(Order.objects.all().values('id')),
            'item_list':list(Item.objects.all().values('id'))}
    return render(request, './empty.html',data)