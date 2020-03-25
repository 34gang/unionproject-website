from django.shortcuts import render
from django.views import generic
from .models import Post # Comment
#from .forms import CommentForm
from django.shortcuts import render, get_object_or_404

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-Dibuat_Pada')
    template_name = 'blog/templates/index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/templates/post_detail.html'
    #post = get_object_or_404(Post, slug=slug)
    #comments = post.comments.filter(active=True)
    #new_comment = None
    #initial_data = {
     #   "content_type":post.get_content_type
    #}
    # Comment posted
    #if request.method == 'POST':
        #comment_form = CommentForm(data=request.POST)
        #if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            #new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            #new_comment.post = post
            # Save the comment to the database
            #new_comment.save()
    #else:
        #comment_form = CommentForm()