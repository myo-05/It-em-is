from .models import Postings, Comments
from .serializers import PostingSerializer,PostingCreateSerializer,PostingPutSerializer, CommentSerializer, CommentCreateSerializer
from rest_framework import status , permissions
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models.query_utils import Q

from rest_framework_simplejwt.views import TokenObtainPairView


class PostingView(APIView):
    def get(self,request):
        postings = Postings.objects.all()
        serialize = PostingSerializer(postings, many=True)
        return Response(serialize.data, status=status.HTTP_200_OK)
    
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
    # permission_classes = [permissions.IsAuthenticated]
    def get(self, request, posting_id):
        # 게시물 id 가져오기
        posting = Postings.objects.get(id=posting_id)
        # 게시물 id에 해당하는 comments들 모두 가져오기
        comments = posting.comments_set.all()
        # CommentSerializer로 직렬화하기(불러온 comments_set)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def post(self, request, posting_id):
        if not request.user.is_authenticated:
            return Response("댓글을 작성하기 전에 먼저 로그인 해주세요.", status=status.HTTP_401_UNAUTHORIZED)
        # CommentCreateSeializer로 입력받은 데이터 직렬화, 검증
        serializer = CommentCreateSerializer(data=request.data)
        # 직렬화된 데이터가 유효하다면
        if serializer.is_valid():
            # DB에 저장
            serializer.save(user=request.user, posting_id=posting_id)
            return Response(serializer.data, status=status.HTTP_200_OK)
        # 데이터 검증 실패시
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CommentDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def put(self, request, pk):
        # 수정할 댓글 불러오기
        comment = get_object_or_404(Comments, id=pk)
        # 댓글 작성자와 로그인한 유저가 같으면
        if request.user == comment.user:
        # CommentCreateSerializer로 입력받은 데이터 직렬화, 검증
            serializer = CommentCreateSerializer(comment, data=request.data)
            # 직렬화된 데이터가 유효하다면
            if serializer.is_valid():
            # DB에 저장
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            # 데이터 검증 실패시
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        # 댓글 작성자 != 로그인한 유저
        return Response("본인이 작성한 댓글만 수정할수 있습니다", status=status.HTTP_403_FORBIDDEN)
    
    def delete(self, request, pk):
        # 삭제할 댓글 불러오기
        comment = get_object_or_404(Comments, id=pk)
        # 댓글 작성자 == 로그인한 유저
        if request.user == comment.user:
        # comment 삭제
            comment.delete()
            return Response("댓글이 삭제되었습니다", status=status.HTTP_204_NO_CONTENT)
        # 댓글 작성자 != 로그인한 유저
        return Response("본인이 작성한 댓글만 삭제할수 있습니다", status=status.HTTP_403_FORBIDDEN)
    
    # 마이페이지의 내가 작성한 댓글 모아 보기
class MyCommentView(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return Response("로그인 먼저 해주세요", status=status.HTTP_401_UNAUTHORIZED)
        user = request.user.id
        query = Q(user=user)
        comments = Comments.objects.filter(query)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
class LikeView(APIView):
    def post(self, request, id):
        posting = get_object_or_404(Postings, id=id)
        if request.user in posting.likes.all():
            # 유저가 좋아요 명단 안에 있을 때
            posting.likes.remove(request.user)
            return Response("좋아요 취소", status=status.HTTP_200_OK)
        else:
            posting.likes.add(request.user)
            return Response("좋아요", status=status.HTTP_200_OK)