from django.contrib import admin
from .models import SavedPost,Follow,Comment,Post,Like
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title_post','user', 'created_on')


class CommentModelAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ('text', 'post', 'user', 'commented_on')

admin.site.register(Post,PostModelAdmin)
admin.site.register(SavedPost)
admin.site.register(Follow)
admin.site.register(Comment,CommentModelAdmin)
admin.site.register(Like)

