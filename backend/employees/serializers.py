from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializer for Employee model.
    """
    image = serializers.SerializerMethodField()


    class Meta:
        model = Employee 
        fields = ['id', 'full_name', 'title', 'image']
        read_only_fields = ['id']  # id is automatically generated

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            url = obj.image.url
            if request is not None:
                return request.build_absolute_uri(url)
            return url
        return None