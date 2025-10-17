"""Serializers for the search app."""
from rest_framework import serializers


class PlaceholderSerializer(serializers.Serializer):
    """Replace with real serializer fields."""
    message = serializers.CharField(read_only=True, default="Not implemented")
