import graphene
from graphene_django import DjangoObjectType
from . import models


class RegionType(DjangoObjectType):
    class Meta:
        model = models.Region
        fields = '__all__'


class Query(graphene.ObjectType):
    all_region = graphene.List(RegionType)


schema = graphene.Schema(query=Query)
