from django.urls import path
from .views import ContactList, ContactDetail, CreateContact

urlpatterns = [
    path("contact-list/", ContactList.as_view(), name="contact_list"),
    path("contact/<int:pk>", ContactDetail.as_view(), name="contact_vote"),
    path("contact/", CreateContact.as_view(), name="create_contact"),
]
