from django.urls import path
from . import views
import regforms.views
import login.views
import quotes.views
import about.views
import quotesform.views
import UserProfile.views
from quotes.views import QuotesView  # Correct import of QuotesView

urlpatterns = [
    path('', views.indexview, name="index"),
    path('about/', about.views.aboutview.as_view(), name="about"),
    path('signup/', regforms.views.signup, name="signup"),
    path('login/', login.views.loginview, name="login"),
    path('quotes/', QuotesView.as_view(), name="quotes"),  # Use QuotesView, as imported correctly
    # Uncomment if needed:
    # path('UserProfile/', UserProfile.views.userview.as_view(), name="UserProfile")
]
