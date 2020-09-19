import braintree
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Setting up payment gateway
gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id="kjtthnxkffrw7694",
        public_key="tpj3vqtfncfh6kvq",
        private_key="4f644111658016ea2433374b6188defd"
    )
)

# Validating user session
def validate_user_session(id, token):
    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        else:
            return False
    except UserModel.DoesNotExist():
        return False

@csrf_exempt
def generate_token(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({'error': 'Invalid session, Please login again!'})
    

    return JsonResponse({'client_token': gateway.client_token.generate(), 'success': True})


@csrf_exempt
def process_payment(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({'error': 'Invalid session, Please login again!'})

    nonce_from_the_client = request.POST['paymentMethodNonce'] # <----Nonce sent from frontend side
    amount_from_the_client = request.POST['amount'] # <----Amount sent from frontend side

    # Creating transaction based on the Nonce received from client which was given by Braintree server
    result = gateway.transaction.sale({ 
        'amount': amount_from_the_client,
        'payment_method_nonce': nonce_from_the_client,
        # 'device_data': device_data_from_the_client,
        'options': {
            'submit_for_settlement': True
        }
    })

    if result.is_success:
        return JsonResponse({
            'success': result.is_success,
            'transaction': { # From braintree documentation
                'id': result.transaction.id, 
                'amount': result.transaction.amount
            },
        })
    else:
        return JsonResponse({'error': True, 'success': False})
