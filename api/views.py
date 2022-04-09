from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from base.models import Record
from .serializers import RecordSerializer
from PIL import Image
 

@api_view(['GET'])
def getData(request):
    records = Record.objects.all()
    serializer = RecordSerializer(records, many=True)
    return Response(serializer.data)

# Gets the records ordered by the latest
@api_view(['GET'])
def getDataSeq(request):
    records = Record.objects.all().order_by('-timestamp')
    serializer = RecordSerializer(records, many=True)
    return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def getReq(request):
    query = request.GET.dict()
    queryKey = list(query.items())[0][0]
    queryitem = list(query.items())[0][1]
    if query:
      #records = Record.objects.all()
      records = Record.objects.filter(**{queryKey: queryitem})
      serializer = RecordSerializer(records, many=True)
      return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
    return Response({"status": "error", "data": "no query"}, status=status.HTTP_400_BAD_REQUEST)   
      

# Posts a new record
@api_view(['POST'])
def postData(request):
    serializer = RecordSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        
        # this will get the path of the image 
        # fishname = str(request.data[u'name'])
        fileDir = str(serializer.data["image"])

        # print(fishname + '/' + filename)
        img = Image.open('.' + fileDir)

        # This is resize the image to 140x140 and save it
        resImg = img.resize((140,140))
        resImg.save('.' + fileDir)

        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)    