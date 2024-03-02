import logging

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView
from django.views.generic.edit import ModelFormMixin

from actions.utils import create_action
from vet_clinic.utils import DataMixin
from .forms import CommentForm
from .models import Post, Category


logger = logging.getLogger('blog')


class BlogView(DataMixin, ListView):
    context_object_name = 'posts'
    template_name = 'blog/blog.html'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Blog')


class BlogDetailView(DataMixin, ModelFormMixin, DetailView):
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'blog_slug'
    form_class = CommentForm

    def get_object(self, queryset=None):
        return get_object_or_404(Post, slug=self.kwargs[self.slug_url_kwarg])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.get_object().comment_post.filter(active=True)  # check related name
        return self.get_mixin_context(context, title=context['post'].title)

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = self.get_object()
            new_comment.name = request.user
            new_comment.save()
            create_action(request.user, 'commented post', new_comment.post)
            logger.info(f'{request.user.username} has commented a post')
            return redirect('blog:blog_detail', blog_slug=self.kwargs[self.slug_url_kwarg])


@login_required
@require_POST
def post_like(request):
    post_id = request.POST.get('id')
    action = request.POST.get('action')

    if post_id and action:
        try:
            post = Post.objects.get(id=post_id)
            if action == 'like':
                post.users_like.add(request.user)
                create_action(request.user, 'likes', post)
                logger.info(f'{request.user.username} has liked a post')
            else:
                post.users_like.remove(request.user)
                logger.info(f'{request.user.username} has disliked a post')
            return JsonResponse({'status': 'ok'})
        except Post.DoesNotExists:
            pass
            logger.warning(f'post does not exist')
    return JsonResponse({'status': 'error'})


class CategoryBlogView(ListView):
    model = Category
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        # category_slug from its url
        return Post.objects.filter(category__slug=self.kwargs['category_blog_slug']).select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = context['posts'].first().category  # from queryset first item then its category
        context['title'] = 'Category - ' + category.name  # name from category
        return context
