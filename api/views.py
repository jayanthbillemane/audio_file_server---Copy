from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SongSerializer,PodcastSerializer,AudiobookSerializer
from .models import Song,Podcast,Audiobook


@api_view(['GET'])
def songList(request):
	songs=Song.objects.all().order_by('id')
	serializer=SongSerializer(songs,many=True)
	return Response(serializer.data)

@api_view(['POST'])
def songCreate(request):
	serializer = SongSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def songUpdate(request, pk):
	song = Song.objects.get(id=pk)
	serializer = SongSerializer(instance=song, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['DELETE'])
def songDelete(request, pk):
	song = Song.objects.get(id=pk)
	song.delete()

	return Response('Item succsesfully delete!')


@api_view(['GET'])
def podcastList(request):
	poscasts=Podcast.objects.all().order_by('id')
	serializer=PodcastSerializer(poscasts,many=True)
	return Response(serializer.data)

@api_view(['POST'])
def podcastCreate(request):
	serializer = PodcastSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def podcastUpdate(request, pk):
	podcast = Podcast.objects.get(id=pk)
	serializer = PodcastSerializer(instance=podcast, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['DELETE'])
def podcastDelete(request, pk):
	podcast = Podcast.objects.get(id=pk)
	podcast.delete()

	return Response('Item succsesfully delete!')


@api_view(['GET'])
def audiobooktList(request):
	audiobooks=Audiobook.objects.all().order_by('id')
	serializer=AudiobookSerializer(audiobooks,many=True)
	return Response(serializer.data)

@api_view(['POST'])
def audiobookCreate(request):
	serializer = AudiobookSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def audiobookUpdate(request, pk):
	audiobooks = Audiobook.objects.get(id=pk)
	serializer = AudiobookSerializer(instance=audiobooks, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['DELETE'])
def audiobookDelete(request, pk):
	audiobook = Audiobook.objects.get(id=pk)
	audiobook.delete()

	return Response('Item succsesfully delete!')