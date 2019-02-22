
from django.forms import ModelForm
from blog.models import Comments

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['content', 'commenter',
                      'email_address']