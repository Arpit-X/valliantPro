from .models import UserProfile, Events, Participations
from .serialisers import ProfileSerializer, EventSerialiser, ParticipationSerialiser
from rest_framework.response import Response
from rest_framework import permissions, generics
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes


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
@permission_classes((permissions.AllowAny,))
class AddParticipation(APIView):
    def get(self,request,*args,**kwargs):
        try:
            event = Events.objects.get(eventCode=self.kwargs['slug'])
            user = UserProfile.objects.get(id=self.kwargs['pk'])
            participation = Participations.objects.create(participant=user,event=event)
        except:
            participation = None
        print('called')
        
        serialiser = ParticipationSerialiser(participation)
        return Response(serialiser.data)

class ParticipationView(generics.ListAPIView):
    serializer_class=ParticipationSerialiser
    queryset = Participations.objects.all()

class EventStats(generics.ListAPIView):
    serializer_class = ParticipationSerialiser
    def get_queryset(self):
        try:
            event = Events.objects.get(eventCode=self.kwargs['event'])
        except:
            event = None
        participations = Participations.objects.filter(event=event)
        return participations
    
class UserStats(generics.ListAPIView):
    serializer_class = ParticipationSerialiser
    def get_queryset(self):
        try:
            user = UserProfile.objects.get(id=self.kwargs['pk'])
        except:
            user = None
        participations = Participations.objects.filter(participant=user)
        return participations