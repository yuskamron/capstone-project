from django.urls import path
from .views import HomePage, InboxPage

urlpatterns = [
		path('', HomePage.as_view(), name = 'home'),		
		path('inbox', InboxPage.as_view(), name = 'inbox'),
]

