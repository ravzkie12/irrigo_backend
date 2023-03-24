from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from irrigo_app.views import (
    CreateAccountView, 
    GetAccountView, 
    AllAccountsView,
    UpdateAccountView,
    DeleteAccountView,
    LivelihoodSummary
)

urlpatterns = [
    path("register/", CreateAccountView.as_view(), name="registerAccount"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("account/<int:pk>", GetAccountView.as_view(), name="accountView"),
    path("account_list/", AllAccountsView.as_view(), name="accountListView"),
    path("account/update", UpdateAccountView.as_view(), name="updateAccount"),
    path("account/delete/<int:pk>", DeleteAccountView.as_view(), name="deleteAccount"),
    path("livelihoods_summary/", LivelihoodSummary.as_view(), name="livelihoodsSummary")
]