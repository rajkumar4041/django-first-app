from django.forms import ModelForm
from .models import Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        # we can define it only specified field to show 
        #  we can do like @Example : fields-=["name","updated_at",topic]
        fields = "__all__"
