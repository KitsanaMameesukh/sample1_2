from distutils.command.build_scripts import first_line_re
from rest_framework import serializers
from .models import Emails


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'email',
            'title',
            'content',
            'replyContent',
            'sendDate',
            'sendForm',
        )
        model = Emails
