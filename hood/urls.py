from django.urls import path
from .views import(

PostListView,
PostCreateView,
PostUpdateView,
PostDeleteView,
PostDetailView,

BusinessListView,
BusinessCreateView,
BusinessUpdateView,
BusinessDeleteView,
BusinessDetailView,

EssentialListView,
EssentialCreateView,
EssentialUpdateView,
EssentialDeleteView,
EssentialDetailView,

MtaaListView,
MtaaCreateView,
MtaaUpdateView,
MtaaDeleteView,
MtaaDetailView
)

urlpatterns = [
    path('', PostListView.as_view(), name="hood-home"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="hood-detail"),
    path('post/new/', PostCreateView.as_view(), name="hood-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="hood-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="hood-delete"),

    path('business/', BusinessListView.as_view(), name="business-home"),
    path('business/<int:pk>/', BusinessDetailView.as_view(), name="business-detail"),
    path('business/new/', BusinessCreateView.as_view(), name="business-create"),
    path('business/<int:pk>/update/',BusinessUpdateView.as_view(), name="business-update"),
    path('business/<int:pk>/delete/',BusinessDeleteView.as_view(), name="business-delete"),

    path('essential/', EssentialListView.as_view(), name="essential-home"),
    path('essential/<int:pk>/', EssentialDetailView.as_view(),name="essential-detail"),
    path('essential/new/', EssentialCreateView.as_view(), name="essential-create"),
    path('essential/<int:pk>/update/',EssentialUpdateView.as_view(), name="essential-update"),
    path('essential/<int:pk>/delete/',EssentialDeleteView.as_view(), name="essential-delete"),

    path('mtaa/', MtaaListView.as_view(), name="mtaa-home"),
    path('mtaa/<int:pk>/', MtaaDetailView.as_view(), name="mtaa-detail"),
    path('mtaa/new/', MtaaCreateView.as_view(), name="mtaa-create"),
    path('mtaa/<int:pk>/update/',MtaaUpdateView.as_view(), name="mtaa-update"),
    path('mtaa/<int:pk>/delete/',MtaaDeleteView.as_view(), name="mtaa-delete"),

]
