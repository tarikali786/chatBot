from django.contrib import admin
from chat.models import ChatRoom, Conversation, Message
# Register your models here.
admin.site.register(ChatRoom)
admin.site.register(Message)
admin.site.register(Conversation)
