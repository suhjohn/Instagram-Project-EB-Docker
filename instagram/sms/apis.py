from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from sms.serializer import SMSSerializer


#
# class SendSMS(APIView):
#     def post(self, request):
#         api_key = "NCSGLMHSQ2FTVZUA"
#         api_secret = "2ZNM5ZPZR07QHSLHVIFAH3XZR1GAGM2F"
#         cool = Message(api_key, api_secret)
#
#         type = "sms"
#         sender = "01029953874"
#         receiver = request.data.get("receiver")
#         message = request.data.get("message")
#         params = {
#             'type': type,
#             'from': sender,
#             'to': receiver,
#             'text': message,
#         }
#         try:
#             response = cool.send(params)
#             print("Success Count : %s" % response['success_count'])
#             print("Error Count : %s" % response['error_count'])
#             print("Group ID : %s" % response['group_id'])
#
#             if "error_list" in response:
#                 print("Error List : %s" % response['error_list'])
#             return Response(status.HTTP_200_OK)
#
#         except CoolsmsException as e:
#             print("Error Code : %s" % e.code)
#             print("Error Message : %s" % e.msg)
#             return Response(status.HTTP_400_BAD_REQUEST)

class SendSMS(APIView):
    def post(self, request):
        serializer = SMSSerializer(request.data)
        if serializer.is_valid():
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)