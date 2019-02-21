from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=30) #user designated title
    author_name = models.CharField(max_length=30) #who posted it
    content = models.TextField(max_length=500) # what is actually in the blog post
    date_posted = models.DateTimeField(auto_now_add=True) #this is going to add the current date/time of when the post
                                                    #was created to our blog post
    #pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.title


class Comments(models.Model):
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    commenter = models.CharField(max_length=30)
    email_address = models.CharField(max_length=45)
    date_posted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.commenter

    #Want to add something to check that the emdateail they enter is valid,
    #something like try:
    #validate_email("foo.bar@baz.qux")
#except ValidationError as e:
   # print "oops! wrong email"
#else:
   # print "hooray! email is valid"
   #which seems to be secure, and I think would be a cool validation to have
