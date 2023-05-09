from .models import Postings, Comment
from .serializers import PostingSerializer,PostingCreateSerializer,PostingPutSerializer, CommentSerializer, CommentSerializer
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
        
class CommentView(APIView):
    def get(self, request, articles_id):
        # 게시물 id 가져오기
        # 게시물 id에 해당하는 comments들 모두 가져오기
        # CommentSerializer로 직렬화하기(불러온 comment_set)
        return Response("댓글 조회")
    def post(self, request, articles_id):
        # CommentCreateSeializer로 입력받은 데이터 직렬화, 검증
        # 직렬화된 데이터가 유효하다면
        # DB에 저장
        return Response("댓글 생성")
        # 데이터 검증 실패시
        return Response("댓글 생성 실패 - serializer.errors")
    def put(self, request, articles_id, comment_id):
        # 수정할 댓글 불러오기
        # 댓글 작성자와 로그인한 유저가 같으면
        # CommentCreateSerializer로 입력받은 데이터 직렬화, 검증
        # 직렬화된 데이터가 유효하다면
        # DB에 저장
        return Response("댓글 수정")
        # 데이터 검증 실패시
        return Response("댓글 생성 실패 - serializer.errors")
    
        # 댓글 작성자 != 로그인한 유저
        return Response("본인이 작성한 댓글만 수정할수 있습니다")
    
    def delete(self, request, article_id, comment_id):
        # 삭제할 댓글 불러오기
        # 댓글 작성자 == 로그인한 유저
        # comment 삭제
        return Response("댓글이 삭제되었습니다")
        # 댓글 작성자 != 로그인한 유저
        return Response("본인이 작성한 댓글만 삭제할수 있습니다")