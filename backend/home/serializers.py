from rest_framework import serializers
from .models import Home


class HomePageSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()
    
    class Meta:
        model = Home
        fields = ['id', 'title', 'description', 'logo']
        read_only_fields = ['id']

    def get_logo(self, obj):
        request = self.context.get('request')
        if obj.logo:
            url = obj.logo.url
            if request is not None:
                return request.build_absolute_uri(url)
            return url
        return None