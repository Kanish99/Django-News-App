from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.parsers import JSONParser
from .models import Place
from .serializers import PlaceSerializer, PlaceModelSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class PlaceGenericViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
	serializer_class = PlaceModelSerializer
	queryset = Place.objects.all()

class PlaceModelViewSet(viewsets.ModelViewSet):
	serializer_class = PlaceModelSerializer
	queryset = Place.objects.all()

class PlaceViewSet(viewsets.ViewSet):
	lookup_field = 'id'

	def list(self, request):
		places = Place.objects.all()
		serializer = PlaceModelSerializer(places, many=True)
		return Response(serializer.data, status=status.HTTP_201_CREATED)

	def create(self, request):
		serializer = PlaceModelSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def retrieve(self, request, id=None):
		queryset = Place.objects.all()
		place = get_object_or_404(queryset, id=id)
		serializer = PlaceModelSerializer(place)
		return Response(serializer.data)

	def update(self, request, id=None):
		place = Place.objects.get(id=id)
		serializer = PlaceModelSerializer(place, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def partial_update(self, request, id=None):
		place = Place.objects.get(id=id)
		serializer = PlaceModelSerializer(place, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def destroy(self, request, id=id):
		place = Place.objects.get(id=id)
		place.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)




class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
	serializer_class =PlaceModelSerializer
	queryset = Place.objects.all()
	authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]

	def get(self, request):
		return self.list(request)

	def post(self, request):
		return self.create(request)

class GenericAPIViewDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
	serializer_class = PlaceModelSerializer
	queryset = Place.objects.all()

	lookup_field = 'id'

	def get(self, request, id):
		return self.retrieve(request, id)

	def put(self, request, id):
		return self.update(request, id)

	def delete(self, request, id):
		return self.destroy(request, id)

class PlaceAPIView(APIView):

	def get(self, request):
		places = Place.objects.all()
		serializer = PlaceModelSerializer(places, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = PlaceModelSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlaceDetails(APIView):

	def get_object(self, id):
		try:
			return Place.objects.get(id=id)

		except Place.DoesNotExist:
			raise Http404

	def get(self, request, id):
		place = self.get_object(id)
		serializer = PlaceModelSerializer(place)
		return Response(serializer.data)

	def put(self, request, id):
		place = self.get_object(id)
		serializer = PlaceModelSerializer(place, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, id):
		place = self.get_object(id)
		place.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def place_list(request):

# 	if request.method == 'GET':
# 		places = Place.objects.all()
# 		serializer = PlaceSerializer(places, many=True)
# 		return Response(serializer.data)

# 	elif request.method == 'POST':
# 		# data = JSONParser().parse(request)
# 		serializer = PlaceSerializer(data=request.data)

# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def place_detail(request, pk):
# 	try:
# 		place = Place.objects.get(pk=pk)

# 	except Place.DoesNotExist:
# 		return HttpResponse(status=status.HTTP_404_NOT_FOUND)

# 	if request.method == 'GET':
# 		serializer = PlaceSerializer(place)
# 		return Response(serializer.data)

# 	elif request.method == 'PUT':
# 		serializer = PlaceSerializer(place, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 	elif request.method == 'DELETE':
# 		place.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)