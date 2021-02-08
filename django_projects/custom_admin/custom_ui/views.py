from django.shortcuts import render, HttpResponse
from .models import HeadersSubMenuType, HeadersMenuNavbar, HeadersSubMenu, Test1, Features, TechnologyCategory, TechnologyStackSubItem, TechnologyStackItem
from rest_framework import generics
from .serializers import HeaderSubMenuSerializer, HeaderSubMenuTypeSerializer, HeaderMenuNavbarSerializer, Test1Serializer, FeaturesSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
import json
# from rest_framework.views import APIView
# Create your views here.


# class MenuNavbarListView(generics.ListCreateAPIView):
#     queryset = MenuNavbar.objects.all()
#     serializer_class = MenuNavbarSerializer


# class MenuNavbarView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = MenuNavbarSerializer
#     queryset = MenuNavbar.objects.all()

# class MenuDropdownListView(generics.ListCreateAPIView):
#     queryset = MenuDropdown.objects.all()
#     serializer_class = MenuDropdownSerializer


# class MenuDropdownView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = MenuDropdownSerializer
#     queryset = MenuDropdown.objects.all()


class Management(APIView):

    def get(self, request):

        menunavbar = HeadersMenuNavbar.objects.all()
        serializer = HeaderMenuNavbarSerializer(menunavbar, many=True)
        return Response(serializer.data)


class ManagementTest(APIView):

    def get(self, request):

        test = Test1.objects.all()
        serializer = Test1Serializer(test, many=True)
        return Response(serializer.data)


class ManagementFeatures(APIView):

    def get(self, request):

        test = Features.objects.all()
        print(test)
        serializer = FeaturesSerializer(test, many=True)
        print(serializer.data)
        return Response(serializer.data)


class TechnologyCategoryView(APIView):

    def get(self, request):

        tech = TechnologyStackItem.objects.filter(
            technology_stack_item__title="Frontend")
        technology = TechnologyStackItem.objects.filter(technology_category_id=1).filter(
            id=2).values("technology_stack_item__title", "technology_stack_sub_item__title")
        technology_items = TechnologyStackItem.objects.filter(
            technology_category_id=1).filter(id=2).values("technology_stack_sub_item__title")
        print(technology_items)
        print(technology)
        print(tech)
        return HttpResponse(tech)


def index(request):

    # send_mail('Hello from v2s', 'Hello there. This is an automated message.', 'vshaladhav@gmail.com', ['adhavv0@gmail.com'], fail_silently=False)
    if request.method == 'POST':
        message = request.POST['message']

        send_mail('Contact Form', message, settings.EMAIL_HOST_USER,
                  ['adhavv0@gmail.com'], fail_silently=False)

    return render(request, 'custom/email.html')


def contact_form(request):

    if request.method == 'POST':

        json_data = request.POST

        message = "Name: {} \nEmail ID: {} \nPage URL: {}".format(
            json_data['name'], json_data['email_id'], json_data['pageurl'])
        subject = request.POST['subject']

        send_mail(subject, message, settings.EMAIL_HOST_USER,
                  ['adhavv0@gmail.com'], fail_silently=False)

    return render(request, 'custom/contact_form.html')



def CTA(request):
    
    if request.method == 'POST':

        json_data = request.POST

        message = "Email ID: {}".format(
            json_data['email_id'])

        send_mail('CTA', message, settings.EMAIL_HOST_USER,
                  ['adhavv0@gmail.com'], fail_silently=False)

    return render(request, 'custom/cta.html')


def HireDevopCTC(request):
    
    if request.method == 'POST':

        json_data = request.POST

        message = "Name: {} \nEmail ID: {}".format(
            json_data['name'], json_data['email_id'])


        send_mail('Hire a developer', message, settings.EMAIL_HOST_USER,
                ['adhavv0@gmail.com'], fail_silently=False)

    return render(request, 'custom/cta.html')


def HiringModel(request):
    
    if request.method == 'POST':

        json_data = request.POST

        message = "Name: {} \nEmail ID: {}".format(
            json_data['name'], json_data['email_id'])


        send_mail('Hiring Model', message, settings.EMAIL_HOST_USER,
                ['adhavv0@gmail.com'], fail_silently=False)

    return render(request, 'custom/hiring_model.html')


def NewsLetter(request):
    
    if request.method == 'POST':

        json_data = request.POST

        message = "Email ID: {}".format(
            json_data['email_id'])


        send_mail('Add me to newsletter', message, settings.EMAIL_HOST_USER,
                ['adhavv0@gmail.com'], fail_silently=False)

    return render(request, 'custom/newsletter.html')


