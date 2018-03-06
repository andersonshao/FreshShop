import xadmin
from xadmin import views
from .models import VerifyCode


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = '生鲜电商'
    site_footer = '生鲜电商'
    # menu_style = 'accordion'


class VerifyCodeAdmin(object):
    list_display = ['code', 'mobile', 'add_time']
    search_fields = ['code', 'email']
    list_filter = list_display
    model_icon = 'fa fa-ticket'


xadmin.site.register(VerifyCode, VerifyCodeAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
