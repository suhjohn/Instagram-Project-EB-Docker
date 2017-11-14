from django.http import HttpResponseForbidden
from django.shortcuts import redirect, get_object_or_404

# Create your views here.
from ..forms import PostCommentForm
from ..models import Post, PostComment


__all__ = [
    "add_comment",
    "delete_comment",
]

def add_comment(request, post_pk):
    if bool(request.user.is_authenticated):
        post = Post.objects.get(pk=post_pk)
        comment = PostCommentForm(request.POST)
        next = request.GET.get('next', '').strip()
        if comment.is_valid():
            new_comment = comment.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()
        return redirect(next)
    else:
        return redirect('member:login')


def delete_comment(request, comment_pk):
    next = request.GET.get('next', '').strip()
    comment = get_object_or_404(PostComment, pk=comment_pk)
    if comment.author == request.user:
        comment.delete()
        return redirect(next)
    else:
        return HttpResponseForbidden()
