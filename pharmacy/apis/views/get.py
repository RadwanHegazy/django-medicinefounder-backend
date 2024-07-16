from rest_framework.views import APIView
from rest_framework import status
from ..seiralizers import MedicineSerializer, Medicine
from rest_framework.response import Response

class get_medicine (APIView) : 
    serializer_class = MedicineSerializer
    
    def get(self, request) : 
        search = request.GET.get('search', None)

        if search:
            query = Medicine.objects.filter(name__icontains=search)
        else:
            query = Medicine.objects.all()
        
        serializer = self.serializer_class(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)