from django.contrib import admin
from .models import Question, Comment


admin.site.register(Question)

class CommentAdmin(admin.ModelAdmin):
  list_display = ('ownerComment', 'question', 'comment_date',)
  list_filter = ('comment_date','ownerComment')
  search_fields = ('ownerComment', 'comment_text')
admin.site.register(Comment, CommentAdmin)

# Register your models here.
