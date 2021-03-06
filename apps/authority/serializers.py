import models
from rest_framework import serializers
from django.contrib.auth.models import Permission
from authority.models import ExtendUser,Group

__all__ = [
    'UserSerializer', 'GroupSerializer', 'PermissionSerializer'
]

class UserSerializer(serializers.ModelSerializer):
    group_name = serializers.StringRelatedField(source="get_group_name", read_only=True)
    email8531 = serializers.StringRelatedField(source="get_8531email", read_only=True)
    groups = serializers.PrimaryKeyRelatedField(many=True, queryset=models.Group.objects.all())

    class Meta:
        model = ExtendUser
        fields = (
            'id', 'is_active', 'last_login', 'phone', 'username', 'full_name', 'group_name', 'email8531', 'groups'
        )


class GroupSerializer(serializers.ModelSerializer):
    permissions = serializers.PrimaryKeyRelatedField(many=True,queryset=Permission.objects.all())

    class Meta:
        model = Group
        fields = (
            'id', 'name', 'permissions'
        )


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = (
            'id', 'name'
        )

