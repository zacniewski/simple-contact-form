from rest_framework import generics, permissions
from rest_framework.renderers import TemplateHTMLRenderer

from .models import Contact
from .permissions import IsAuthorOrReadOnly
from .serializers import ContactSerializer, FullContactSerializer


class ContactList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser, )
    queryset = Contact.objects.all()
    serializer_class = FullContactSerializer


class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser, )
    queryset = Contact.objects.all()
    serializer_class = FullContactSerializer


class CreateContact(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
