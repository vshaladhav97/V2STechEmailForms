from django.contrib import admin
from nested_admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline
from .models import Post, Answer, Question, Category, CategoryI18n, Item, ItemI18n, User, HeadersSubMenu, HeadersMenuNavbar, HeadersSubMenuType, Statistic, AssociatedWith, TrustedWith, Test1, Test2, Features, Content, TechnologyStackItem, TechnologyStackSubItem, TechnologyCategory, TechnologyStackItemCategory
from django.utils.html import format_html

admin.site.register(User)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    def image_tag(self, obj):
        return format_html('<img src="{}" width="80" height="50" />'.format(obj.photo.url))

    image_tag.short_description = 'Photo'

    # list_display = ['image_tag',]
    list_display = [
        'title',
        'is_publishable',
        'created_at',
        'updated_at',
        'image_tag',
    ]

    list_filter = (
        'is_publishable',
        'created_at',
        'updated_at',
    )


class AnswerTabularInLine(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerTabularInLine]

    class Meta:
        model = Question


admin.site.register(Question, QuestionAdmin)

admin.site.register(Answer)


class CategoryI18nTabularInline(NestedTabularInline):
    model = CategoryI18n
    extra = 1


class ItemI18nTabularInline(NestedTabularInline):
    model = ItemI18n
    extra = 1


class ItemStackedInline(NestedStackedInline):
    model = Item
    extra = 1
    inlines = [ItemI18nTabularInline, ]


class CategoryAdmin(NestedModelAdmin):
    inlines = [CategoryI18nTabularInline, ItemStackedInline]


admin.site.register(Category, CategoryAdmin)

admin.site.register(HeadersMenuNavbar)
admin.site.register(HeadersSubMenuType)
admin.site.register(HeadersSubMenu)
admin.site.register(Statistic)
admin.site.register(AssociatedWith)
admin.site.register(TrustedWith)
admin.site.register(Test1)
admin.site.register(Test2)
admin.site.register(Content)
admin.site.register(Features)

admin.site.register(TechnologyStackItemCategory)
admin.site.register(TechnologyStackItem)
admin.site.register(TechnologyStackSubItem)
admin.site.register(TechnologyCategory)
