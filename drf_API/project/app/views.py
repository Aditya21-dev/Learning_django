from django.shortcuts import render
from .models import User
from .serializers import UserSerializers
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import io


@csrf_exempt
def User_list(request):

    # ------------------ POST METHOD ------------------
    if request.method == 'POST':
        json_data = request.body
        print("Raw JSON Data:", json_data)
        print("Type of Raw Data:", type(json_data))

        stream = io.BytesIO(json_data)
        print("Stream Data:", stream)
        print("Type of Stream:", type(stream))

        python_data = JSONParser().parse(stream)
        print("Parsed Python Data:", python_data)
        print("Type of Parsed Data:", type(python_data))

        serializer = UserSerializers(data=python_data)

        if serializer.is_valid():
            print("Validated Data:", serializer.validated_data)
            serializer.save()

            res = {'msg': 'User Created Successfully'}
            json_res = JSONRenderer().render(res)
            return HttpResponse(json_res, content_type='application/json')

        else:
            print("Errors:", serializer.errors)
            json_res = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_res, content_type='application/json')

    # ------------------ GET METHOD ------------------
    users = User.objects.all()
    print("Queryset:", users)

    serializer = UserSerializers(users, many=True)
    print("Serialized Object:", serializer)
    print("Serialized Data:", serializer.data)

    json_data = JSONRenderer().render(serializer.data)
    print("Final JSON Response:", json_data)

    return HttpResponse(json_data, content_type='application/json')