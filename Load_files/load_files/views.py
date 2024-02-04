import time
from load_files.models import *
from load_files.serializers import *
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from load_files.tasks import load_file_and_changing_status


class FileUploadAPIView(APIView):
    serializer_class = FileSerializer

    def post(self, request, *args, **kwargs):
        if 'file' not in request.FILES:
            return Response({'error': 'File not found'})
        else:
            uploaded_file = request.FILES.get('file')
            file_name = uploaded_file.name
            file_content = uploaded_file.read()
            load_file_and_changing_status.delay(file_content, file_name)
            return Response({'code': status.HTTP_201_CREATED,
                             'file': file_name})


class FileViewSet(ReadOnlyModelViewSet):
    queryset = File.objects.all()
    serializer_class = AllFileSerializer
