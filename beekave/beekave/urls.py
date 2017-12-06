
from django.conf.urls import url,include
from django.contrib import admin
from mainPage.views import mainPage
from beekave.views import UserCreateView, UserCreateDoneTV,search
from reviewPage.views import review_like,review_dislike,reviews
from detail.views import postReview,detail
from aboutus.views import aboutus

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',mainPage.as_view(), name ='mainPage'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
    url(r'^accounts/register/done/$', UserCreateDoneTV.as_view(), name='register_done'),
    url(r'^review/like/$', review_like, name='review_like'),
    url(r'^reivew/dislike/$',review_dislike, name='review_dislike'),
    url(r'^reivew/post/$', postReview, name='postReview'),
    url(r'^(?P<id>\d+)/$', detail, name='detail'),
    url(r'^(?P<id>\d+)/(?P<filter>[-]{0,1}[a-z]+([&]{0,1}[a-z|A-Z|가-힣|0-9|_])*)/p(?P<page>\d+)/$', reviews, name='reviews'),
    url(r'^aboutus/$', aboutus, name='aboutus'),
    url(r'^faq/$', aboutus, name='faq'),
    url(r'^contactus/$', aboutus, name='contactus'),
    url(r'^search_(?P<myfilter>.*)/$', search, name='search'),
]
