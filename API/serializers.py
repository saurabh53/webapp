from django.contrib.auth.models import User, Group
from rest_framework import serializers
from API.models import Tasks, Exercise, Expense, Diet


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email')
        write_only_field = ('password',)

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Tasks
        fields = ('id ', 'owner', 'Task_Name', 'Task_Details', 'Task_By', 'Task_End_Date')


class ExerciseSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Exercise
        fields = (
        'id ', 'owner', 'Exercise_name', 'Start_date', 'End_date', 'Exercise_day', 'Exercise_sets', 'Set_repetion')


class DietSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Diet
        fields = ('id ', 'owner', 'Food_Name', 'Start_date', 'End_date', 'Diet_day', 'Diet_Time')


class ExpenseSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Expense
        fields = ('id', 'owner', 'Amount', 'Amount_type', 'Borrower_or_Lender_Name')
