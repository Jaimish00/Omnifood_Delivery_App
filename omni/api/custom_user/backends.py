import jwt
from django.conf import settings
from rest_framework import authentication, exceptions
from .models import Customer, DeliveryPerson, HotelAdmin
 
class JWTCustomerAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = 'Token'
 
    def authenticate(self, request):
        request.user = None
 
        # `auth_header` should be an array with two elements: 1) the name of
        # the authentication header (in this case, "Token") and 2) the JWT 
        # that we should authenticate against.
        auth_header = authentication.get_authorization_header(request).split()
        auth_header_prefix = self.authentication_header_prefix.lower()
 
        if not auth_header:
            return None
 
        if len(auth_header) == 1:
            # Invalid token header. No credentials provided. Do not attempt to
            # authenticate.
            return None
 
        elif len(auth_header) > 2:
            # Invalid token header. The Token string should not contain spaces. Do
            # not attempt to authenticate.
            return None
 
        # The JWT library we're using can't handle the `byte` type, which is
        # commonly used by standard libraries in Python 3. To get around this,
        # we simply have to decode `prefix` and `token`. This does not make for
        # clean code, but it is a good decision because we would get an error
        # if we didn't decode these values.
        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')
 
        if prefix.lower() != auth_header_prefix:
            return None
        return self._authenticate_credentials(request, token)
 
    def _authenticate_credentials(self, request, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
        except:
            msg = 'Invalid authentication. Could not decode token.'
            raise exceptions.AuthenticationFailed(msg)
 
        try:
            user = Customer.objects.get(pk=payload['id'])
        except Customer.DoesNotExist:
            msg = 'No user matching this token was found.'
            raise exceptions.AuthenticationFailed(msg)
 
        if not user.is_active:
            msg = 'This user has been deactivated.'
            raise exceptions.AuthenticationFailed(msg)
        return (user, token)
 
class JWTHotelAdminAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = 'Token'
 
    def authenticate(self, request):
        request.user = None
 
        auth_header = authentication.get_authorization_header(request).split()
        auth_header_prefix = self.authentication_header_prefix.lower()
 
        if not auth_header:
            return None
 
        if len(auth_header) == 1:
            return None
 
        elif len(auth_header) > 2:
            return None
 
        
        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')
 
        if prefix.lower() != auth_header_prefix:
            return None
        return self._authenticate_credentials(request, token)
 
    def _authenticate_credentials(self, request, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
        except:
            msg = 'Invalid authentication. Could not decode token.'
            raise exceptions.AuthenticationFailed(msg)
 
        try:
            user = HotelAdmin.objects.get(pk=payload['id'])
        except HotelAdmin.DoesNotExist:
            msg = 'No user matching this token was found.'
            raise exceptions.AuthenticationFailed(msg)
 
        if not user.is_active:
            msg = 'This user has been deactivated.'
            raise exceptions.AuthenticationFailed(msg)
        return (user, token)

class JWTDeliveryPersonAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = 'Token'
 
    def authenticate(self, request):
        request.user = None
 
        auth_header = authentication.get_authorization_header(request).split()
        auth_header_prefix = self.authentication_header_prefix.lower()
 
        if not auth_header:
            return None
 
        if len(auth_header) == 1:
            return None
 
        elif len(auth_header) > 2:
            return None
 
        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')
 
        if prefix.lower() != auth_header_prefix:
            return None
        return self._authenticate_credentials(request, token)
 
    def _authenticate_credentials(self, request, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
        except:
            msg = 'Invalid authentication. Could not decode token.'
            raise exceptions.AuthenticationFailed(msg)
 
        try:
            user = DeliveryPerson.objects.get(pk=payload['id'])
        except DeliveryPerson.DoesNotExist:
            msg = 'No user matching this token was found.'
            raise exceptions.AuthenticationFailed(msg)
 
        if not user.is_active:
            msg = 'This user has been deactivated.'
            raise exceptions.AuthenticationFailed(msg)
        return (user, token)