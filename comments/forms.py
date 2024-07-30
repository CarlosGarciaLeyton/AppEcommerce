#User form

#DJANGO
from django import forms
#Models
from comments.models import Comment
# DJANGO
from django import forms

# Models
from comments.models import Comment


class CreateCommentForm(forms.ModelForm):
    #Post model form
    comment = forms.CharField(widget=forms.Textarea)

    class Meta:
        #form setting
        model = Comment
        fields = ('user', 'profile', 'post', 'comment')
