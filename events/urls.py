from django.urls import path
from .rest_views import AllUserProfiles, UserProfilesCRUD,AllEvents


app_name = "events"

urlpatterns = [
    path('api/userprofile/all',AllUserProfiles.as_view(),name="userProfiles"),
    path('api/userprofile/<int:pk>',UserProfilesCRUD.as_view(),name="userProfileCRUD"),
    path('api/events/all',AllEvents.as_view(),name="events"),
    path('api/events/<slug:slug>',AllEvents.as_view(),name="events"),
]
