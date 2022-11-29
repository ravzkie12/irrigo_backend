from rest_framework import generics
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from irrigo_app.models import Account
from irrigo_app.serializers import AccountSerializer

# Create your views here.

# ACOUNT MODEL VIEWS

class CreateAccountView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = AccountSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetAccountView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

class AllAccountsView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

class UpdateAccountView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        account = Account.objects.get(pk=request.user.id)
        serializer = AccountSerializer(account, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteAccountView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AccountSerializer
    queryset = Account.objects.all()