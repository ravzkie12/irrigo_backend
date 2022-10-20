from rest_framework import serializers
from irrigo_app.models import Account

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        account = Account.objects.create(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            mobile=validated_data["mobile"],
            username=validated_data["username"],
            role=validated_data["role"]
        )
        account.set_password(validated_data["password"])
        account.save()
        return account