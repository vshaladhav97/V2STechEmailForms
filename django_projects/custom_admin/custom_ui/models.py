from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_photo = models.ImageField()


class Post(models.Model):
    '''Model definition for Post.'''

    title = models.CharField(_('Post'), max_length=50)
    content = models.TextField(_('Content'))
    is_publishable = models.BooleanField(_('Is Publishable ?'), default=False)
    created_at = models.DateTimeField(_('Created at '), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at '), auto_now=True)
    photo = models.ImageField()

    class Meta:
        '''Meta definition for Post.'''

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        '''Unicode representation of Post.'''
        return self.title


class Question(models.Model):
    text = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    draft = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=120)
    active = models.BooleanField(default=True)
    draft = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Category(models.Model):
    private_name = models.CharField('Private name', max_length=164)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class CategoryI18n(models.Model):
    name = models.CharField('Name i18n', max_length=164)
    language_key = models.CharField('Language', max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Category i18n'
        verbose_name_plural = 'Categories i18n'


class Item(models.Model):
    private_name = models.CharField('Private name', max_length=164)
    price = models.DecimalField('Price', decimal_places=2, max_digits=8)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'


class ItemI18n(models.Model):
    name = models.CharField('Name i18n', max_length=164)
    language_key = models.CharField('Language', max_length=20)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item i18n'
        verbose_name_plural = 'Items i18n'

# #MenuNavbar
# class HeadersMenuNavbar(models.Model):

#     menu_id = models.CharField(max_length=100)
#     menu = models.CharField(max_length=60)
#     url = models.CharField(max_length=100)
#     show_in_footer = models.BooleanField(default=True)

#     def __str__(self):
#         return self.menu_id

# #Type
# class HeadersSubMenuType(models.Model):
#     sub_menu_type_id = models.CharField(max_length=60)
#     sub_menu_type = models.CharField(max_length=60)
#     sub_menu_type_title = models.CharField(max_length=60, null=True)

#     def __str__(self):
#         return "{}".format(self.sub_menu_type)

# #MenuDropdown
# class HeadersSubMenu(models.Model):
#     sub_menu_id = models.CharField(max_length=60)
#     menu = models.ForeignKey(HeadersMenuNavbar, on_delete=models.CASCADE, related_name='sub_menu', null=True, blank=True)
#     item = models.CharField(max_length=60)
#     url = models.CharField(max_length=100)
#     types = models.ForeignKey(HeadersSubMenuType, on_delete=models.CASCADE, null=True)
#     show_in_footer = models.BooleanField(default=True)


#     def __str__(self):
#         return "{}".format(self.menu)


class HeadersMenuNavbar(models.Model):
    """for headers menu navbar"""
    menu_id = models.CharField(max_length=100, unique=True)
    menu = models.CharField(max_length=60)
    url = models.CharField(max_length=100)
    show_in_footer = models.BooleanField(default=True)

    def __str__(self):
        return self.menu_id


class HeadersSubMenuType(models.Model):
    """for headers sub menu types"""
    title = models.CharField(max_length=60, null=True)
    menu = models.ForeignKey(
        HeadersMenuNavbar, on_delete=models.CASCADE, related_name='sub_menu', null=True, blank=True)

    def __str__(self):
        return "{}".format(self.title)


class HeadersSubMenu(models.Model):
    """for headers sub menu"""
    sub_menu_id = models.CharField(max_length=60, unique=True)
    item = models.CharField(max_length=60)
    url = models.CharField(max_length=100)
    types = models.ForeignKey(
        HeadersSubMenuType, on_delete=models.CASCADE, related_name='sub_menu_items', null=True)
    show_in_footer = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.item)


# statistics =


class Statistic(models.Model):
    title = models.CharField(max_length=60, unique=True)
    description = models.TextField(max_length=2000)
    image = models.ImageField(upload_to = 'images/')
    
# title
# description
# image upload

class AssociatedWith(models.Model):
    title = models.CharField(max_length=60, unique=True)
    status = models.BooleanField(default=True)
    image = models.ImageField(upload_to = 'associated/')
    
class TrustedWith(models.Model):
    title = models.CharField(max_length=60, unique=True)
    status = models.BooleanField(default=True)
    image = models.ImageField(upload_to = 'trusted_with/')
    
    
class Test1(models.Model):
    name = models.CharField(max_length=60)
class Test2(models.Model):
    test1 = models.ManyToManyField(Test1, related_name='names')
    sirname = models.CharField(max_length=60)
    
    
class Features(models.Model):
    title = models.CharField(max_length=60)
    

class Content(models.Model):
    content_id = models.CharField(max_length=60)
    contents = models.ForeignKey(Features, on_delete=models.CASCADE, related_name="features")
    title = models.CharField(max_length=60)
    image = models.ImageField(upload_to = 'content/')
    summary = models.TextField(max_length=2000)
    
class TechnologyStackItemCategory(models.Model):
    
    technology_stack_item_category_id = models.CharField(max_length=60, unique=True)
    title = models.CharField(max_length=60)
    
    def __str__(self):
        return self.title
    
    
class TechnologyCategory(models.Model):
    technology_category_id = models.CharField(max_length=60, unique=True)
    # category_name = models.CharField(max_length=60)
    
    title = models.CharField(max_length=60)
    # category = models.ForeignKey(, on_delete=models.CASCADE, blank=True, null=True)
    # technology_stack_items = models.ForeignKey(TechnologyStackItems, on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.title

class TechnologyStackSubItem(models.Model):
    # technology_stack_item = models.ManyToManyField(TechnologyStackItem)
    technology_stack_subitem_id = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    image_icon = models.ImageField(upload_to = 'technology_stack_sub_item/')
    
    def __str__(self):
        return self.title

class TechnologyStackItem(models.Model):
    # technology_stack_item_id = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    technology_category = models.ForeignKey(TechnologyCategory, on_delete=models.CASCADE)
    technology_stack_item = models.ForeignKey(TechnologyStackItemCategory, on_delete=models.CASCADE) 
    technology_stack_sub_item = models.ManyToManyField(TechnologyStackSubItem)
    
    def __str__(self):
        return self.title
    

    

    
# class TechnologyStackItems_has_TechnologyStackSubItems(models.model):
#     technology_stack_items_id = models.ForeignKey(TechnologyStackItems, on_delete=models.CASCADE)
#     technology_stack_sub_item_id = models.ForeignKey(TechnologyStackSubItems, on_delete=models.CASCADE)
    
    