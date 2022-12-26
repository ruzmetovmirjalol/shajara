from rest_framework.response import Response
from rest_framework.views import APIView

from job.serializers import AddJobSerializer


class AddJobView(APIView):
    """
    Jobni qo'shish
    """
    def post(self, request):
        serializer = AddJobSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)

        serializer.save()

        return Response(serializer.data)
