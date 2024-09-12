from django.shortcuts import render
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from io import BytesIO


from books.models import Books,BookDetail
from books.serializers import BookDetailSerializer,BookSerializer

# Create your views here.

@api_view(['GET','POST'])
def book_list(request):
    if request.method == 'GET':
        book = Books.objects.all()
        name = request.GET.get('name',None)
        publish = request.GET.get('publish',None)
        editor = request.GET.get('editor',None)
        if name is not None:
            book_filter = book.filter(name__icontains=name)
            book_list_serializer = BookSerializer(book_filter,many=True)
        elif publish is not None:
            book_filter = book.filter(publish__icontains=publish)
            book_list_serializer = BookSerializer(book_filter,many=True)
        elif editor is not None:
            book_filter = book.filter(editor__icontains=editor)
            book_list_serializer = BookSerializer(book_filter,many=True)
        else:
            book_list_serializer = BookSerializer(book,many=True)
        return JsonResponse(book_list_serializer.data,safe=False)
    elif request.method == 'POST':
        book_list_serializer = BookSerializer(data = request.data)
        if book_list_serializer.is_valid():
            book_list_serializer.save()
            return JsonResponse(book_list_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(book_list_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','PUT','DELETE'])
def book_detail(request,pk):
    try:
        book = Books.objects.get(pk=pk)
        if request.method == 'POST':
            request.data['model_Book']=pk
            book_descript_serializer = BookDetailSerializer(data = request.data) 
            if book_descript_serializer.is_valid(): 
                book_descript_serializer.save()
                return JsonResponse(book_descript_serializer.data,status=status.HTTP_201_CREATED) 
            else:
                return JsonResponse(book_descript_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:    
            book_detail_pk = BookDetail.objects.get(model_Book=pk)

    except Books.DoesNotExist:
        return JsonResponse({'message':'This book does not exist'},status=status.HTTP_404_NOT_FOUND)  
    except BookDetail.DoesNotExist:
        return JsonResponse({'message':'Book''s detail does not exist'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        book_name = book_detail_pk.model_Book.name
        book_detail_serializer = BookDetailSerializer(book_detail_pk)
        response_data = book_detail_serializer.data
        response_data['book_name'] = book_name
        return JsonResponse(response_data,safe=False)
    elif request.method == 'PUT':
        book_descript_serializer = BookDetailSerializer(book_detail_pk,data=request.data,partial=True)
        if book_descript_serializer.is_valid():
            book_descript_serializer.save()
            return JsonResponse(book_descript_serializer.data,status=status.HTTP_201_CREATED) 
        else:
            return JsonResponse(book_descript_serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE':
        book_detail_pk.delete()
        book.delete()
        return JsonResponse({'message':'delete scucceed'},status=status.HTTP_204_NO_CONTENT)
