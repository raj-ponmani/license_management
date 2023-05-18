from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Organization, Subscription
from .serializers import OrganizationSerializer, SubscriptionSerializer


class OrganizationListCreateView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = (permissions.AllowAny,)


class SubscriptionListCreateView(generics.ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    authentication_classes = (JWTAuthentication,)

    def get_queryset(self):
        subs = self.queryset.filter(organization=self.request.user.pk)
        return subs

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # Set the organization field to the currently logged-in user instance
            serializer.validated_data['organization'] = request.user

            # Save the subscription
            subscription = serializer.save()

            # Return the serialized data of the created subscription
            response_serializer = self.serializer_class(subscription)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
