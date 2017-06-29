from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.decorators import api_view, authentication_classes

from .models import House, Position
from renting import settings


# 关于HyperlinkedModelSerializer
# http://www.django-rest-framework.org/api-guide/serializers/#inspecting-a-modelserializer
class PositionSerializers(serializers.HyperlinkedModelSerializer):
    """序列化中间表"""
    school = serializers.ReadOnlyField(source='school.school_name')

    class Meta(object):
        """docstring for Meta"""
        model = Position
        fields = ('school', 'distance')


class HouseSerializers(serializers.ModelSerializer):
    """在列表页和详情页使用"""
    # 'position_set'是House表中position默认字段名
    position = PositionSerializers(source='position_set', many=True)
    # SerializerMethodField的文档
    # http://www.django-rest-framework.org/api-guide/fields/#serializermethodfield
    rent_type = serializers.SerializerMethodField()
    house_show_url = serializers.SerializerMethodField('get_house_url')

    class Meta:
        model = House
        fields = '__all__'
        depth = 1

    def get_rent_type(self, obj):
        # obj.rent_type显示前面的选项
        return obj.get_rent_type_display()

    def get_house_url(self, obj):
        return '%s%s' % (settings.MEDIA_URL, obj.house_show)


@api_view(['GET'])
def house_cards(request, school):
    house = House.objects.filter(school__school_name=school)
    # School.objects.get(school_name=school).house_set.all()
    serializer = HouseSerializers(house, many=True, context={'request': request})
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def index_cards(request):
    house = House.objects.order_by("favorite_nums")[0:3]

    serializer = HouseSerializers(house, many=True, context={'request': request})
    return Response(serializer.data, status=status.HTTP_200_OK)