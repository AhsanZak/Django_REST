from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# from Account.models import Account
# from blog.models import BlogPost
from blog.api.serializers import BlogPostSerilizer


@api_view(['GET'])
def api_detail_blog_view(request, slug):

    try:
        blog_post = BlogPost.objects.get(slug=slug)
    except  BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogPostSerilizer(blog_post)
        return Response(serializer.data) 


@api_view(['PUT'])
def api_update_blog_view(request, slug):

    try:
        blog_post = BlogPost.objects.get(slug=slug)
    except  BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = BlogPostSerilizer(blog_post, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successfull"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_FOUND) 



@api_view(['DELETE'])
def api_delete_blog_view(request, slug):

    try:
        blog_post = BlogPost.objects.get(slug=slug)
    except  BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = blog_post.delete()
        data = {}
        if operation:
            data["success"] = "delete successfull"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)


@api_view(['POST'])
def api_delete_blog_view(request, slug):

    account = Accounts.objects.get(pk=1)

    blog_post = BLogPost(author=account)

    if request.method == 'POST':
        serializer = BlogPostSerializer(blog_post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)