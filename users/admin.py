from django.contrib import admin
from django.contrib import messages
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils import timezone

from .models import User

# Register your models here.
class UserAdmin(BaseUserAdmin):

    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff')
    list_filter = ('date_joined', )
    date_hierarchy = 'date_joined'
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email', 'first_name', 'last_name')
    filter_horizontal = ()

    change_list_template = 'admin/users/user_change_list.html'

    actions = [
        'activate_users',
        'deactivate_users',
    ]


    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        today = timezone.now()
        extra_context['today'] = User.objects.filter(date_joined__day=today.day).count()
        extra_context['this_week'] = User.objects.filter(date_joined__lte=today, date_joined__gt=today-timezone.timedelta(days=7)).count()
        extra_context['this_month'] = User.objects.filter(date_joined__month=today.month).count()
        extra_context['this_year'] = User.objects.filter(date_joined__year=today.month).count()

        return super(UserAdmin, self).changelist_view(request, extra_context=extra_context)


    def activate_users(self, request, queryset):
        cnt = queryset.filter(is_active=False).update(is_active=True)
        self.message_user(request, 'Activated {} users.'.format(cnt))
    activate_users.short_description = 'Activate Users'  # type: ignore

    def deactivate_users(self, request, queryset):
        cnt = queryset.filter(is_active=True).update(is_active=False)
        self.message_user(request, 'Deactivated {} users.'.format(cnt))
    deactivate_users.short_description = 'Deactivate Users'  # type: ignore


    def has_delete_permission(self, request, obj = None):
        return False



admin.site.register(User, UserAdmin)

admin.site.site_header = 'SaVest Task Dashboard Admin'
