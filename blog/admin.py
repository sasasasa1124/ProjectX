from django.contrib import admin
from .models import Post, Comment, Reply, Tag


class ReplyInline(admin.StackedInline):
    model = Reply
    extra = 5


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Tag)