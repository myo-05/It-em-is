from .models import Postings
from .serializers import PostingSerializer,PostingCreateSerializer,PostingPutSerializer
from rest_framework import status , permissions
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.views import TokenObtainPairView


class PostingView(APIView):
    def get(self,request):
        postings = Postings.objects.all()
        serialize = PostingSerializer(postings, many=True)
        return Response(serialize.data)
    
    def post(self,request):
        if not request.user.is_authenticated:
            return Response("로그인을 해주세요.", status=status.HTTP_401_UNAUTHORIZED) 
        serializer = PostingCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":f"{serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST) #요청오류
        
class PostingDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request,id):
        posting = get_object_or_404(Postings,id=id)
        serialize = PostingSerializer(posting)
        return Response(serialize.data)
    
    
    def put(self,request,id):
        posting = get_object_or_404(Postings,id=id)
        if request.user == posting.user:
            serializer = PostingPutSerializer(posting,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message':'권한이 없습니다'},status=status.HTTP_401_UNAUTHORIZED)
    
    def delete(self,request,id):
        posting = get_object_or_404(Postings,id=id)
        if request.user == posting.user:
            posting.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message':'권한이 없습니다'},status=status.HTTP_401_UNAUTHORIZED)
        
class LikeView(APIView):
    def get(self, request,id):
        Posting = get_object_or_404(Postings, id=id)
        if request.user in Postings.likes.all():
            # 유저가 좋아요 명단 안에 있을 때
            Posting.likes.remove(request.user)
            return Response("좋아요 취소", status=status.HTTP_200_OK)
        else:
            Posting.likes.add(request.user)
            return Response("좋아요", status=status.HTTP_200_OK)

    def post(self, request,id):
        pass