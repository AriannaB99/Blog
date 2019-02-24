
from django import forms
from blog.models import Comments

class CommentForm(forms.ModelForm):
    content = forms.CharField(max_length= 300, help_text= "Comment ")
    commenter = forms.CharField(max_length= 100, help_text= "Your Name")
    email_address = forms.CharField(max_length= 100,  help_text= "Your Email Address")
    class Meta:
        model = Comments
        fields = ['content', 'commenter',
                      'email_address']