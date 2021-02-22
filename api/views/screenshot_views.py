from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.shortcuts import render
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.screenshot import Screenshot
from ..serializers import ScreenshotSerializer, UserSerializer
from ..forms import ScreenshotForm

# Create your views here.
class Screenshots(generics.ListCreateAPIView):
    # authentication_classes = ()
    # permission_classes = ()
    # permission_classes=(IsAuthenticated,)
    serializer_class = ScreenshotSerializer

    def get(self, request):
        """Index request"""
        # Get all the screenshots:
        screenshots = Screenshot.objects.all()
        # Filter the screenshots by owner, so you can only see your owned screenshots

        screenshots = Screenshot.objects.filter(owner=request.user.id)

        # Run the data through the serializer
        # data = ScreenshotForm(screenshots,).data
        data = ScreenshotSerializer(screenshots, many=True).data
        return Response({ 'screenshots': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['screenshot']['owner'] = request.user.id
        # request.data.owner = request.user.id
        # Serialize/create screenshot
        screenshot = ScreenshotSerializer(data=request.data['screenshot'])
        # screenshot = ScreenshotSerializer(data=request.data)
        # If the screenshot data is valid according to our serializer...
        if screenshot.is_valid():
            # Save the created screenshot & send a response
            screenshot.save()
            return Response({ 'screenshot': screenshot.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(screenshot.errors, status=status.HTTP_400_BAD_REQUEST)

class ScreenshotDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the screenshot to show
        screenshot = get_object_or_404(Screenshot, pk=pk)
        # Only want to show owned screenshots?
        if not request.user.id == screenshot.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this screenshot')

        # Run the data through the serializer so it's formatted
        data = ScreenshotSerializer(screenshot).data
        return Response({ 'screenshot': data })

    def get(self, request):
        """Authenticated Search request"""
        # Locate the screenshot to show
        screenshot = get_list_or_404(Screenshot, title_contains='',
            description_contains='', imagefile_contains='')
        # Only want to show owned screenshots?
        if not request.user.id == screenshot.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this screenshot')

        # Run the data through the serializer so it's formatted
        data = ScreenshotSerializer(screenshot).data
        return Response({ 'screenshot': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate screenshot to delete
        screenshot = get_object_or_404(Screenshot, pk=pk)
        # Check the screenshot's owner agains the user making this request
        if not request.user.id == screenshot.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this screenshot')
        # Only delete if the user owns the  screenshot
        screenshot.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Remove owner from request object
        # This "gets" the owner key on the data['screenshot'] dictionary
        # and returns False if it doesn't find it. So, if it's found we
        # remove it.
        if request.data['screenshot'].get('owner', False):
            del request.data['screenshot']['owner']

        # Locate Screenshot
        # get_object_or_404 returns a object representation of our Screenshot
        screenshot = get_object_or_404(Screenshot, pk=pk)
        # Check if user is the same as the request.user.id
        if not request.user.id == screenshot.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this screenshot')

        # Add owner to data object now that we know this user owns the resource
        # request.data.owner = request.user.id
        request.data['screenshot']['owner'] = request.user.id
        # Validate updates with serializer
        data = ScreenshotSerializer(screenshot, data=request.data['screenshot'])
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
