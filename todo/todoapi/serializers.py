from rest_framework import serializers
from todoapi.models import Todo
 

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    # user = serializers.ReadOnlyField(source='user.username')
 
    class Meta:
        model = Todo
        fields = ('url', 'id', 'created', 'name', 'user')
        # extra_kwargs = {
        #     'url': {
        #         'view_name': 'todoapi:todo-detail',
        #     }
# }