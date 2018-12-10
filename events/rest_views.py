from .models import UserProfile, Events
from .serialisers import ProfileSerializer, EventSerialiser
from rest_framework.response import Response
from rest_framework import permissions, generics



class AllUserProfiles(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer


class UserProfilesCRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer

class AllEvents(generics.ListAPIView):
    queryset = Events.objects.all()
    serializer_class = EventSerialiser

class DepartmentWiseEvent(generics.ListAPIView):
    serializer_class = EventSerialiser
    def get_queryset(self):
        queryset = Events.objects.filter(department=self.kwargs['slug'])
        queryset =self.get_serializer_class().setup_eager_loading(queryset=queryset)
        return queryset
