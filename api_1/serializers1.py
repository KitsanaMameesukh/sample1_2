from distutils.command.build_scripts import first_line_re
from rest_framework import serializers
from .models import TodoLists


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'todo',
            'startDate',
            'endDate',
            'status',
        )
        model = TodoLists