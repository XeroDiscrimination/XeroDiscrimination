from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from .models import User, Applicant, Company, Industry, Comment, Recommendations
from .forms import UserAdminCreationForm, UserAdminChangeForm

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'is_superuser')
    list_filter = ('is_superuser', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('full_name', 'email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'company', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    # prepopulated_fields = {'slug': ('company')} 

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


class RecommendationsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'organization', 'reasons', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'organization')
    actions = ['processed_nominations']

    # prepopulated_fields = {'slug': ('company')} 

    def processed_nominations(self, request, queryset):
        queryset.update(active=True)

admin.site.register(User, UserAdmin)

admin.site.unregister(Group) 

admin.site.register(Applicant)
admin.site.register(Company)

admin.site.register(Industry)

admin.site.register(Comment, CommentAdmin)

admin.site.register(Recommendations, RecommendationsAdmin)

# admin.site.site_header = 'Xero Discrimination Administration'
