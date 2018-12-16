from django.urls import path
from .rest_views import UserDetails, AllUserProfiles, UserProfilesCRUD,AllEvents, AddParticipation, EventStats, UserStats


app_name = "events"

urlpatterns = [
    path('api/userprofile/all',AllUserProfiles.as_view(),name="userProfiles"),
    path('api/userprofile/<int:pk>',UserProfilesCRUD.as_view(),name="userProfileCRUD"),
    path('api/events/all',AllEvents.as_view(),name="events"),
    path('api/events/<slug:slug>',AllEvents.as_view(),name="deptEvents"),
    path('api/register/<slug:slug>/<int:pk>',AddParticipation.as_view(),name="addParticipant"),
    path('api/stats/event/<slug:slug>',EventStats.as_view(),name="EventStats"),
    path('api/stats/user/<int:pk>',UserStats.as_view(),name="UserStats"),
    path('api/user-details/<slug:slug>',UserDetails.as_view(),name="userDetails")
]
