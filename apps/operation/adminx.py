from .models import UserFav, UserAddress, UserNotes

import xadmin


class UserFavAdmin(object):
    list_display = ['user', 'goods', 'add_time']
    search_fields = ['user', 'goods']
    list_filter = list_display


class UserAddressAdmin(object):
    list_display = ['user', 'province', 'city', 'district', 'address', 'signer_name', 'signer_mobile', 'add_time']
    search_fields = ['user', 'district', 'address', 'signer_name', 'signer_mobile']
    list_filter = list_display


class UserNotesAdmin(object):
    list_display = ['user', 'message_type', 'subject', 'message', 'file', 'add_time']
    search_fields = ['user', 'message_type', 'subject', 'message']
    list_filter = list_display


xadmin.site.register(UserFav, UserFavAdmin)
xadmin.site.register(UserAddress, UserAddressAdmin)
xadmin.site.register(UserNotes, UserNotesAdmin)
