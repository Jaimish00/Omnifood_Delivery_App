from rest_framework import viewsets
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .serializers import OrderSerializer
from .models import Order
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def validate_user_session(id, token):
    UserModel = get_user_model()

    try:
        customer = UserModel.objects.get(pk=id)
        if customer.session_token == token:
            return True
        else:
            return False
    except UserModel.DoesNotExist:
        return False


@csrf_exempt
def add(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({'error': 'Please login', 'code': '1'})

    if request.method == 'POST':
        customer_id = id
        transaction_id = request.POST['transaction_id']
        amount = request.POST['amount']
        food_items = request.POST['food_items']

        total_items = len(food_items.split(',')[:-1])

        UserModel = get_user_model()

        try:
            customer = UserModel.objects.get(pk=customer_id)
        except UserModel.DoesNotExist():
            return JsonResponse({'error': 'User doesn\'t exist'})

        # TODO: Getting the hotel details from the food

        order = Order.objects.create(customer=customer, food_items=food_items, total_items=total_items, transaction_id=transaction_id, total_amount=amount)

        order.save()
        return JsonResponse({'success': 'True', 'error': 'False', 'msg': 'Order placed successfully'})


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer
