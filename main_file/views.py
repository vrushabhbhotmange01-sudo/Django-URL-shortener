from rest_framework.decorators import api_view,throttle_classes
from rest_framework import status ,throttling
from rest_framework.response import Response
from django.shortcuts import redirect
 
from .models import URLSTORAGE
from .searilizer import URLserializer
from .functionality import generate_random_code

class CreateRateThrottle(throttling.UserRateThrottle):
    rate = "5/min"

@api_view(['POST'])
@throttle_classes([CreateRateThrottle])
def create_store(request):
    serializer= URLserializer(data=request.data)

    if serializer.is_valid():
        original_url = serializer.validated_data['original_url']
        custom_code = serializer.validated_data['custom_code']
        expires_at = serializer.validated_data['expires_at']
        

        exists = URLSTORAGE.objects.filter(original_url=original_url).first()
        if exists :
            return Response(
                {'short_url':request.build_absolute_uri(f"/main/call/{exists.short_code}")},
                status= status.HTTP_200_OK
            )
        short_code= custom_code if custom_code else generate_random_code()

        obj = URLSTORAGE.objects.create(
            original_url=original_url,
            short_code = short_code,
            expires_at=expires_at
        )
        return Response(
            {'short_url':request.build_absolute_uri(f'/main/call/{obj.short_code}'),
             "expires_at":obj.expires_at
             },
            status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def redirect_short_url(request,code):
    try:
        obj = URLSTORAGE.objects.get(short_code=code)
        if obj.is_expired():
            return Response({
                "error":"This link has expired"
            },
            status=status.HTTP_410_GONE)
        
        obj.click_count+=1
        obj.save(update_fields=["click_count"])

        return redirect(obj.original_url
                        )
    except URLSTORAGE.DoesNotExist:

        return Response({"error":"Short Url Not Found"},status=status.HTTP_404_NOT_FOUND)
    

# @api_view(["DELETE"])

# def delete(request):
#     URLSTORAGE.objects.all().delete
#     return Response("Objects deleted successfully")

# @api_view(["GET"])

# def get(request):
#     obj= URLSTORAGE.objects.all()
#     searilizer = URLserializer(obj,many=True)

#     return Response(searilizer.data)
