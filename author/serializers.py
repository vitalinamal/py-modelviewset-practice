from rest_framework import serializers

from author.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=64)
    last_name = serializers.CharField(max_length=64)
    pseudonym = serializers.CharField(required=False, max_length=64)
    age = serializers.IntegerField()
    retired = serializers.BooleanField()

    class Meta:
        model = Author
        fields = [
            "id",
            "first_name",
            "last_name",
            "pseudonym",
            "age",
            "retired"
        ]
