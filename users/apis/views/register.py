from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from ..serializers import RegisterSerializer

class register_view (APIView) : 
    serializer_class = RegisterSerializer

    def post (self, request) : 
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.tokens, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    