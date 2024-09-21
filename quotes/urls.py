from django.urls import path
from .views import QuotesView  # Correct import based on views.py
import regforms.views
import login.views
import UserProfile.views

urlpatterns = [
    path('', login.views.indexview, name="index"),  # Ensure views are correctly imported
    path('about/', login.views.aboutview.as_view(), name="about"),
    path('signup/', regforms.views.signup, name="signup"),
    path('login/', login.views.loginview, name="login"),
    # Uncomment and fix UserProfile view when ready
    # path('UserProfile/', UserProfile.views.userview.as_view(), name="UserProfile"),
    path('quotes/', QuotesView.as_view(), name='quotes'),  # Use as_view()
]
