from rest_framework import generics, permissions
from .models import Message
from .serializers import MessageSerializer

class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Message.objects.filter(sender=self.request.user) | Message.objects.filter(receiver=self.request.user)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
