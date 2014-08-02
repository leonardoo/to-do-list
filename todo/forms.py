from django.forms import ModelForm
from models import Todo


# Create the form class.
class TodoForm(ModelForm):
    class Meta:
        model = Todo
