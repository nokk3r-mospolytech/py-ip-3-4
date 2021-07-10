from rest_framework import serializers
from . import models


class CartListSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Region
        fields = '__all__'


class TaskListSerializers(serializers.ModelSerializer):
    ChillVariations_id = serializers.StringRelatedField()
    Avilable_id = serializers.StringRelatedField()
    Pricing_id = serializers.StringRelatedField()
    Priority_id = serializers.StringRelatedField()
    Region_id = serializers.StringRelatedField()

    class Meta:
        model = models.Task
        fields = '__all__'


class TaskDetailSerializers(serializers.ModelSerializer):
    ChillVariations_id = serializers.StringRelatedField()
    Avilable_id = serializers.StringRelatedField()
    Pricing_id = serializers.StringRelatedField()
    Priority_id = serializers.StringRelatedField()
    Region_id = serializers.StringRelatedField()

    class Meta:
        model = models.Task
        fields = '__all__'


class TaskCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = '__all__'


class CartDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Region
        fields = '__all__'


class CartChangedSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Region
        fields = '__all__'
