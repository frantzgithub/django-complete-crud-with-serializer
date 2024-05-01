from rest_framework.views import Request, Response, APIView, status
from rest_framework.pagination import PageNumberPagination
from ipdb import set_trace
from .models import User
from addresses.models import Addresses
from .serializers import UserSerializer
#from django.forms import model_to_dict

class UserView(APIView, PageNumberPagination):
    def post(self, req: Request) -> Response:
        # = User.objects.create(**req.data)
        #user_dict = model_to_dict(user)
        serializer = UserSerializer(data=req.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        
        address_data = serializer.validated_data.pop("addresses")
        user = User.objects.create(**serializer.validated_data)
        Addresses.objects.create(**address_data, user=user)
        userSerializer = UserSerializer(user)
        return Response(userSerializer.data, status.HTTP_201_CREATED)

    def get(self, req: Request) -> Response:
        by_email = req.query_params.get("email", None)
        if by_email:
            users = User.objects.filter(email__icontains=by_email)
        else:
            users = User.objects.all()
        result = self.paginate_queryset(users, req)
        userSerializer = UserSerializer(result, many=True)
        # user_dict = []
        # for user in users:
        #     user_dict.append(model_to_dict(user))
            
        return self.get_paginated_response(userSerializer.data)    
class UserDetail(APIView):
    def get(self, req: Request, user_id: int) -> Response:
        try:
         user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({"msg": "there is no user with this id"}, status.HTTP_404_NOT_FOUND)
        userSerializer = UserSerializer(user)
        return Response(userSerializer.data, status.HTTP_200_OK)
    
    def delete(self, req: Request, user_id: int) -> Response:
        try:
         user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({"msg": "there is no user with this id"}, status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response({"msg": "user was deleted successfully"}, status.HTTP_200_OK)
    
    def patch(self, req: Request, user_id: int) -> Response:
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({"msg": "there is no user with this id"}, status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(data=req.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        
        for key, value in serializer.validated_data.items():
            setattr(user, key, value)
        user.save()
        serializer = UserSerializer(user)
        
        return Response(serializer.data)
        
        