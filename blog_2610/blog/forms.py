
from django.forms import ModelForm
from blog.models import Comments

class CommentForm(ModelForm):
    def clean_content(self):
        data = self.cleaned_data['content']
        return data
    def clean_commenter(self):
        data = self.cleaned_data['commenter']
        return data
    def clean_email_address(self):
        data = self.cleaned_data['email_address']
        return data

    class Meta:
        model = Comments
        fields = ['content', 'commenter',
                      'email_address']