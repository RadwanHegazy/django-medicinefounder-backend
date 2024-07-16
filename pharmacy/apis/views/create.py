from rest_framework.views import APIView
from rest_framework import status, permissions
from ..seiralizers import MedicineSerializer
from rest_framework.response import Response

class create_medicine (APIView) : 
    serializer_class = MedicineSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request) : 
        data = request.data
        serializer = self.serializer_class(data=data, context={
            'user' : request.user
        })
        if serializer.is_valid() : 
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
