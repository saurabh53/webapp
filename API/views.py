from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.core import serializers
from rest_framework import permissions, generics
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from django.conf import settings
from API.models import Tasks, Expense, Exercise, Diet
from API.serializers import TaskSerializer, ExerciseSerializer, ExpenseSerializer, DietSerializer, UserSerializer
from API.auth import TokenAuth


# Create your views here.



class TaskList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        today_date = self.kwargs['Task_End_Date']
        return Tasks.objects.filter(owner=user, Task_End_Date__gte=today_date)

    def perform_update(self, serializer):
        instance = serializer.save()



class CompletedTaskList(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        today_date = self.kwargs['Date']
        return Tasks.objects.filter(owner=user, Task_End_Date__lte=today_date)


class TaskAdd(generics.CreateAPIView):
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class DietList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DietSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        today_date = self.kwargs['Date']
        return Tasks.objects.filter(owner=user, End_Date__gte=today_date)

    def perform_update(self, serializer):
        instance = serializer.save()


class DietAdd(generics.CreateAPIView):
    serializer_class = DietSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)





class CompletedDietList(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        today_date = self.kwargs['Date']
        return Tasks.objects.filter(owner=user, End_Date__lte=today_date)


class ExerciseList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        today_date = self.kwargs['Date']
        return Tasks.objects.filter(owner=user, End_Date__gte=today_date)

    def perform_update(self, serializer):
        instance = serializer.save()


class ExerciseAdd(generics.CreateAPIView):
    serializer_class = ExerciseSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)





class CompletedExercise(generics.ListAPIView):
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        today_date = self.kwargs['Date']
        return Tasks.objects.filter(owner=user, End_Date__lte=today_date)



class ExpenseList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        today_date = self.kwargs['Date']
        return Tasks.objects.filter(owner=user, End_Date__gte=today_date)

    def perform_update(self, serializer):
        instance = serializer.save()


class ExpenseAdd(generics.CreateAPIView):
    serializer_class = ExpenseSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)





class ExpenseCompletedList(generics.ListAPIView):
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        today_date = self.kwargs['Date']
        return Tasks.objects.filter(owner=user, End_Date__lte=today_date)




class UserRegistration(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        return serializer.save()


@csrf_exempt
def logout_user(request):
    return JsonResponse({'request': request.session['auth']}, safe=False, status=200)


@csrf_exempt
def get_auth_token(request):
    print '-----request-------'
    print request.POST
    print '------end-----------'
    username = request.POST.get('username')
    password = request.POST.get('password')
    print username, password
    user = authenticate(username=username, password=password)
    print 'user --- ', user
    if user is not None:
        if user.is_active:
            token, created = Token.objects.get_or_create(user=user)
            request.session['auth'] = token.key
            print '----token----', token.key
            return JsonResponse({'token': token.key}, safe=False, status=200)
            # return redirect(settings.LOGIN_URL,request)
            # return render(request,'<h1>done right..</h1>',{})
    return redirect(settings.LOGIN_URL, request)

# Create your views here.
