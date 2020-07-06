from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from .models import Post  # Comment
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from .forms import UploadForm

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-Dibuat_Pada')
    template_name = 'blog/templates/index.html'


# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'blog/templates/post_detail.html'

class HttpRespone(object):
    pass


def post_detail(request, slug):
    template_name = 'blog/templates/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                                'comments': comments,
                                                'new_comment': new_comment,
                                                'comment_form': comment_form})

def upload_form(request):
    template_name = 'blog/templates/upload.html'
    if request.method == 'POST':
        upload_form = UploadForm(data=request.POST)
        if upload_form.is_valid():
            upload_form = upload_form.save()
        else:
            return HttpRespone('Maaf! Silahkan coba lagi!')
    else:
        upload_form = UploadForm()
    return render(request, template_name, {
        'upload_form':upload_form,
    })

