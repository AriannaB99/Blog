from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=30) #user designated title
    author_name = models.CharField(max_length=30) #who posted it
    content = models.TextField(max_length=500) # what is actually in the blog post
    date_posted = models.TimeField(auto_now_add=True) #this is going to add the current date/time of when the post
                                                    #was created to our blog post

class Comments(models.Model):
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    commenter = models.CharField(max_length=30)
    email_address = models.CharField(max_length=45)
    date_posted = models.TimeField(auto_now_add=True)

    #Want to add something to check that the email they enter is valid,
    #something like try:
    #validate_email("foo.bar@baz.qux")
#except ValidationError as e:
   # print "oops! wrong email"
#else:
   # print "hooray! email is valid"
   #which seems to be secure, and I think would be a cool validation to have
