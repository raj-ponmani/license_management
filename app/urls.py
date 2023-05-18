from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import OrganizationListCreateView, SubscriptionListCreateView

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('organizations/', OrganizationListCreateView.as_view(), name='organization-list-create'),
    path('subscriptions/', SubscriptionListCreateView.as_view(), name='subscriptions-list-create'),
]
