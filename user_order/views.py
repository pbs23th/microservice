from rest_framework import viewsets
# Create your views here.

class ShopViewSet(viewsets.ViewSet):
    def list(self, request): #/api/shop
        pass

    def create(self, request): #/api/shop
        pass

    def retrieve(self, request, pk=None): #/api/shop/<str:idx>
        pass

    def update(self, request, pk=None): #/api/shop/<str:idx>
        pass

    def destroy (self, request, pk=None): #/api/shop/<str:idx>
        pass


class OrderViewSet(viewsets.ViewSet):
    def list(self, request): #/api/Order
        pass

    def create(self, request): #/api/Order
        pass

    def retrieve(self, request, pk=None): #/api/Order/<str:idx>
        pass

    def update(self, request, pk=None): #/api/Order/<str:idx>
        pass

    def destroy (self, request, pk=None): #/api/Order/<str:idx>
        pass