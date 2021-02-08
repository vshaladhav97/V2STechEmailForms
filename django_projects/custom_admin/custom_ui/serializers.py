from rest_framework import serializers
from .models import HeadersMenuNavbar, HeadersSubMenuType, HeadersSubMenu, Test1, Test2, Content, Features, TechnologyStackItemCategory, TechnologyStackItem, TechnologyStackSubItem, TechnologyCategory


# class HeaderSubMenuSerializer(serializers.ModelSerializer):
#     title = serializers.ReadOnlyField(source='types.title', read_only=True)
#     class Meta:
#         model = HeadersSubMenu
        
#         fields = ('title', 'item', 'url',  'show_in_footer')






class HeaderSubMenuSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = HeadersSubMenu 
        fields = ('item', 'url', 'show_in_footer')
        

class HeaderSubMenuTypeSerializer(serializers.ModelSerializer):
    sub_menu_items = HeaderSubMenuSerializer(read_only=True, many=True)
    class Meta:
        model = HeadersSubMenuType
        fields = ('title', 'sub_menu_items')


        

class HeaderMenuNavbarSerializer(serializers.ModelSerializer):
    
    
    
    sub_menu = HeaderSubMenuTypeSerializer(read_only=True, many=True)
    
    
    class Meta:
        model = HeadersMenuNavbar
        fields = ('menu_id', 'menu', 'url', 'show_in_footer', 'sub_menu',  )
        



class Test2Serializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Test2
        fields = ("sirname",)
        
class Test1Serializer(serializers.ModelSerializer):
    names = Test2Serializer(read_only=True, many=True)
    # namess = Test2Serializer(source = "names", read_only=True, many=True)
    class Meta:
        model = Test1
        fields = ("name", "names" )
        
        

class ContentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Content
        fields = ("content_id", "title", "image", "summary")
        # fields = "__all__"
        
        
class FeaturesSerializer(serializers.ModelSerializer):
    features = ContentSerializer(read_only=True, many=True)
    
    class Meta:
        model = Features
        fields = ('title','features', )


class TechnologyStackItemCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TechnologyStackItemCategory
        fields = "__all__"
        
class TechnologyStackItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TechnologyStackItem
        fields = "__all__"
        
class TechnologyStackSubItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TechnologyStackSubItem
        fields = "__all__"
        
class TechnologyCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = TechnologyCategory
        fields = "__all__"
