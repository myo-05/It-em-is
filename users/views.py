from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomTokenObtainPairSerializer, Userserializer, ModifyingPutSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from users.models import User

class Userview(APIView):
    def post(self, request):
      serializer = Userserializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response({"message":"회원가입완료"}, status=status.HTTP_201_CREATED)
      else:
        return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class mockview(APIView):
      permission_classes = [permissions.IsAuthenticated]
      def get(self, request):
          return Response("get 요청")
      
class followView(APIView):
    def post(self, request, user_id):
        you = get_object_or_404(User, id=user_id)
        me = request.user
        if me in you.followers.all():
            you.followers.remove(me)
            return Response("팔로우 취소!",status=status.HTTP_200_OK)
        else:
            you.followers.add(me)
            return Response("팔로우 완료!",status=status.HTTP_200_OK)
        
class ProfileModify(APIView):
    def put(self,request,id):
        modifying = get_object_or_404(User, id=id)
        if request.user == modifying.user:
            serializer = ModifyingPutSerializer(modifying,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message':'권한이 없습니다'},status=status.HTTP_401_UNAUTHORIZED)