from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime
from .models import Blog, Comments
from django.template import loader, RequestContext
from django.shortcuts import get_object_or_404, render

#def index(request):
 #   return render(request, 'blog/index.html', {'now': strftime('%c')})
filler = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed quis lacus et enim dapibus fermentum. Proin ultrices, massa eget bibendum accumsan, ante lacus maximus eros, quis auctor nibh ante malesuada elit. Phasellus rutrum condimentum varius. Integer mauris ipsum, facilisis nec aliquam a, aliquet nec massa. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Quisque scelerisque velit augue, nec convallis massa pharetra vitae. Integer tincidunt orci nec nunc lacinia, non suscipit enim vehicula. Quisque a porta sem. In facilisis purus eget pulvinar viverra. Pellentesque in tortor gravida, congue arcu sit amet, efficitur mauris. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Praesent eget vulputate nisi.Praesent vestibulum maximus mauris, nec ultricies ex rutrum sed. Aliquam laoreet nunc at condimentum interdum. Pellentesque ac arcu non enim hendrerit posuere vel vitae magna. Aenean metus arcu, porta vel tempor quis, finibus non ligula. Nulla sit amet purus at felis porta mattis. Proin id arcu velit. Sed mauris purus, vulputate vel blandit nec, pellentesque ut turpis. Donec eu fermentum quam, et efficitur sapien.Donec massa metus, pulvinar id nunc a, ornare maximus lectus. Etiam nec gravida lacus. Praesent faucibus arcu vitae mollis ultrices. Quisque eget elit auctor, varius enim vitae, lacinia nisi.",
          "Vivamus tempus augue eu enim ornare, scelerisque fermentum eros laoreet. Vestibulum quis ligula urna. Cras ac odio vulputate, maximus mauris eu, semper urna. Quisque cursus tortor vitae erat semper eleifend. Donec dapibus ante ac nulla tempus efficitur. Fusce dictum eu nulla et fermentum. Nullam at justo lorem. Ut vitae lorem ut quam vestibulum rutrum. Integer sed risus vitae purus malesuada sodales. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Phasellus sed interdum metus, at tempus est. In hac habitasse platea dictumst. Nam quis maximus felis, nec ornare ante. Aenean ultrices ornare sem id bibendum. Ut blandit eleifend justo, a tempor elit sagittis sed. Nam odio erat, venenatis rhoncus lobortis tristique, aliquet in odio. Aliquam diam dolor, pretium nec tincidunt non, hendrerit tincidunt mi. Suspendisse ut ex metus. Cras ut risus nec enim porttitor posuere. Maecenas viverra nisi metus, vitae condimentum leo rhoncus fringilla. Duis placerat ligula quis aliquet dictum. Sed congue bibendum mauris, eget viverra libero.ed quis semper erat, ac fermentum purus.",
          "Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec ut magna efficitur, vestibulum lorem eu, iaculis lacus. Ut quis lacus eget nibh faucibus tincidunt. Aliquam porttitor felis magna, vitae efficitur augue bibendum sit amet. Proin at facilisis elit. Maecenas vitae nibh ante. Suspendisse pulvinar, turpis ac sagittis placerat, justo nisi molestie ligula, eu egestas turpis massa sed enim. Maecenas porta massa non tortor dictum pharetra. Vestibulum vel aliquam lacus. Donec viverra lobortis mauris nec tincidunt. Praesent lectus felis, maximus vitae urna vitae, cursus elementum dolor. Donec varius ligula a ligula finibus aliquam. Donec malesuada finibus mauris, vitae pharetra dolor tempor eu. Proin molestie volutpat suscipit. In sagittis interdum suscipit. In vel turpis in risus fringilla vestibulum sit amet vestibulum odio. Aliquam placerat eleifend sem, sit amet interdum purus rhoncus sed.",
          "Nullam non laoreet sem. Nullam non consectetur augue. Integer congue venenatis tellus id vehicula. Cras eleifend dignissim sapien. Sed ut diam at eros congue feugiat. In lorem lacus, congue eu posuere in, ullamcorper sed turpis. Ut vel ligula sed erat finibus ultrices quis eget mauris. Pellentesque imperdiet sagittis lacus vel euismod. Nullam urna justo, tempor sit amet nulla quis, venenatis eleifend quam. Donec imperdiet tincidunt mi eget hendrerit. Donec mattis enim in eros accumsan consequat. Mauris rhoncus lorem vitae elit iaculis, eu dapibus nulla efficitur. Praesent porttitor ullamcorper est, quis semper elit hendrerit vitae. Curabitur tempus magna tellus, imperdiet elementum nisl elementum non. Vestibulum nec felis at tortor ultrices consectetur. Fusce ultrices tempus magna. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Donec et imperdiet tellus. Maecenas blandit rhoncus augue, finibus ornare nibh fermentum et. Nulla et sapien quis eros consectetur gravida. Phasellus sit amet urna quis nibh scelerisque ornare. Sed et semper quam. Aliquam nunc orci, porta vitae scelerisque id, ornare eget mauris. Pellentesque tincidunt molestie est et egestas. Nam ac felis eu ligula elementum efficitur. Curabitur id nisl viverra, tristique dolor quis, vestibulum eros. Suspendisse in feugiat ex. Mauris quam nisi, sollicitudin at nibh nec, pellentesque ultricies odio. Vivamus metus felis, dignissim volutpat urna vel, euismod consequat leo. Ut tincidunt risus sit amet elementum varius.Cras rhoncus convallis tempus. Etiam non iaculis nuncCras rhoncus convallis tempus. Etiam non iaculis nunc Cras rhoncus convallis tempus. Etiam non iaculis nuncCras rhoncus convallis tempus. Etiam non iaculis nunc",
          "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed quis lacus et enim dapibus fermentum. Proin ultrices, massa eget bibendum accumsan, ante lacus maximus eros, quis auctor nibh ante malesuada elit. Phasellus rutrum condimentum varius. Integer mauris ipsum, facilisis nec aliquam a, aliquet nec massa. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Quisque scelerisque velit augue, nec convallis massa pharetra vitae. Integer tincidunt orci nec nunc lacinia, non suscipit enim vehicula. Quisque a porta sem. In facilisis purus eget pulvinar viverra. Pellentesque in tortor gravida, congue arcu sit amet, efficitur mauris. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Praesent eget vulputate nisi.Praesent vestibulum maximus mauris, nec ultricies ex rutrum sed. Aliquam laoreet nunc at condimentum interdum. Pellentesque ac arcu non enim hendrerit posuere vel vitae magna. Aenean metus arcu, porta vel tempor quis, finibus non ligula. Nulla sit amet purus at felis porta mattis. Proin id arcu velit. Sed mauris purus, vulputate vel blandit nec, pellentesque ut turpis. Donec eu fermentum quam, et efficitur sapien.Donec massa metus, pulvinar id nunc a, ornare maximus lectus. Etiam nec gravida lacus. Praesent faucibus arcu vitae mollis ultrices. Quisque eget elit auctor, varius enim vitae, lacinia nisi.",
          "Vivamus tempus augue eu enim ornare, scelerisque fermentum eros laoreet. Vestibulum quis ligula urna. Cras ac odio vulputate, maximus mauris eu, semper urna. Quisque cursus tortor vitae erat semper eleifend. Donec dapibus ante ac nulla tempus efficitur. Fusce dictum eu nulla et fermentum. Nullam at justo lorem. Ut vitae lorem ut quam vestibulum rutrum. Integer sed risus vitae purus malesuada sodales. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Phasellus sed interdum metus, at tempus est. In hac habitasse platea dictumst. Nam quis maximus felis, nec ornare ante. Aenean ultrices ornare sem id bibendum. Ut blandit eleifend justo, a tempor elit sagittis sed. Nam odio erat, venenatis rhoncus lobortis tristique, aliquet in odio. Aliquam diam dolor, pretium nec tincidunt non, hendrerit tincidunt mi. Suspendisse ut ex metus. Cras ut risus nec enim porttitor posuere. Maecenas viverra nisi metus, vitae condimentum leo rhoncus fringilla. Duis placerat ligula quis aliquet dictum. Sed congue bibendum mauris, eget viverra libero.ed quis semper erat, ac fermentum purus.",
          "Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec ut magna efficitur, vestibulum lorem eu, iaculis lacus. Ut quis lacus eget nibh faucibus tincidunt. Aliquam porttitor felis magna, vitae efficitur augue bibendum sit amet. Proin at facilisis elit. Maecenas vitae nibh ante. Suspendisse pulvinar, turpis ac sagittis placerat, justo nisi molestie ligula, eu egestas turpis massa sed enim. Maecenas porta massa non tortor dictum pharetra. Vestibulum vel aliquam lacus. Donec viverra lobortis mauris nec tincidunt. Praesent lectus felis, maximus vitae urna vitae, cursus elementum dolor. Donec varius ligula a ligula finibus aliquam. Donec malesuada finibus mauris, vitae pharetra dolor tempor eu. Proin molestie volutpat suscipit. In sagittis interdum suscipit. In vel turpis in risus fringilla vestibulum sit amet vestibulum odio. Aliquam placerat eleifend sem, sit amet interdum purus rhoncus sed.",
          "Nullam non laoreet sem. Nullam non consectetur augue. Integer congue venenatis tellus id vehicula. Cras eleifend"
          ]

filler_names = ["Groghdns Ddong", "Vivamus Tempus", "Orci Varius",  "Jungki Cdhtine", "Ghogudn Sfsts", "Fifhgnt Johofn", "Kofnsi", "ghdafogdfg"]
filler_emails = ["kfgdfgkadjgn@example.com", "dfdsffgadoih@example.com", "djgkjdfga4341@example.com", "dfhdah47665793@example.com"]
filler_titles = ["Gronfodisf", "Ftiereot Igndsdjo", "Hisont", "Adodfngit", "dfdskjfsoudf", "dfsdofissndf", "dsfadoffisod", "dgoigjoij"]
filler_commments = ["Etiam convallis nec ligula non iaculis. Morbi id justo at nunc feugiat rhoncus. Fusce nisl orci, sollicitudin a turpis id, efficitur tempor eros. In ultrices erat fringilla tellus faucibus, eget tincidunt magna fringilla. Duis ut lectus mauris. Vivamus egestas ipsum lorem, vitae sollicitudin nisl porttitor eu. Vestibulum et vulputate augue. Nunc congue erat vel porttitor ullamcorper. Nam rhoncus tortor neque, eu molestie metus gravida quis. Cras rhoncus convallis tempus. Etiam non iaculis nunc.",
                    " Mauris quam nisi, sollicitudin at nibh nec, pellentesque ultricies odio. Vivamus metus felis, dignissim volutpat urna vel, euismod consequat leo. Ut tincidunt risus sit amet elementum varius.",
                    "Cras rhoncus convallis tempus. Etiam non iaculis nunc.",
                    "Donec massa metus, pulvinar id nunc a, ornare maximus lectus. Etiam nec gravida lacus. Praesent faucibus arcu vitae mollis ultrices. Quisque eget elit auctor, varius enim vitae, lacinia nisi."]

def bio(request):
    return render(request, 'blog/index.html')

def init(request):
    #deleting all of the blog posts which we have and their associated comments
    Blog.objects.all().delete()
    for i in range(0, 7):
        b = Blog(content = filler[i], author_name = filler_names[i], title = filler_titles[i])
        b.save()
        for j in range(0, 3):
            c = b.comments_set.create(content = filler_commments[j], commenter = filler_names[j], email_address = filler_emails[j])
            c.save()

    return render(request, 'blog/index.html')


def techtips(request):
    return render(request, 'blog/techtips.html')

'''visitors = 0
def index(request):
    global visitors
    visitors += 1
    return render(request, 'blog/index.html', {'visitors': visitors})'''

def  BiohomeView(request):
    latest_post_list = Blog.objects.order_by("-date_posted")[:3]
    template = loader.get_template('blog/biohome.html')
    context = {'latest_post_list': latest_post_list,}
    return HttpResponse(template.render(context, request))

def ArchiveView(request):
    latest_post_list = Blog.objects.order_by("-date_posted")
    template = loader.get_template('blog/archive.html')
    context = {'latest_post_list': latest_post_list, }
    return HttpResponse(template.render(context, request))

def BlogDetailView(request, question_id):
    try:
        blog = Blog.objects.get(pk = question_id)
        #latest_comments = blog.comments_set.order_by("-date_posted")
    except Blog.DoesNotExist:
        raise Http404("Blog post does not exist")
    return render(request, 'blog/blog_detail.html', {'blog': blog})


def add_comment(request, question_id):
    if request.method == 'POST':
        try:
            blog = get_object_or_404(Blog, pk=question_id)
        except (KeyError, Blog.DoesNotExist):
            return render(request, 'blog/blog_detail.html', {'blog': blog})
        else:
            #who = request.META['REMOTE_ADDR']

            '''commentContet = request.POST['Comment']
            commentEmail_address = request.POST['EmailAddress']
            commentCommenter = request.POST['Username']'''

            c = blog.comments_set.create(blog_id=question_id,
                                     content=request.POST['Comment'], commenter=request.POST['Username'],
                                     email_address=request.POST['EmailAddress'])
            c.save()

            return render(request, 'blog/blog_detail.html', {'blog': blog})
            #return HttpResponse(commentContet)

