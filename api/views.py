from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Record
from .serializers import RecordSerializer
from PIL import Image
 

@api_view(['GET'])
def getData(request):
    records = Record.objects.all()
    serializer = RecordSerializer(records, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postData(request):
    serializer = RecordSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        fishname = str(request.data[u'name'])
        filename = str(request.data[u'image'].name)
        # print(fishname + '/' + filename)
        imgDir = fishname + '/' + filename
        imgDir = imgDir.replace(' ','_')
        img = Image.open("./media/images/" + imgDir)
        resImg = img.resize((140,140))
        resImg.save("./media/images/" + imgDir)

    return Response(serializer.data)