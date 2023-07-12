from rest_framework import serializers
from rest_framework.exceptions import ValidationError, PermissionDenied

from core.serializers import ProfileSerializer
from goals.models import GoalCategory, Goal, GoalComment


class GoalCategorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = GoalCategory
        fields = '__all__'
        read_only_fields = ('id', 'created', 'updated', 'user', 'is_deleted')

class GoalCategoryWithUserSerializer(GoalCategorySerializer):
    user = ProfileSerializer(read_only=True)


class GoalSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Goal
        fields = '__all__'
        read_only_fields = ('id', 'created', 'updated', 'user')

    def validated_category(self, category: GoalCategory) -> GoalCategory:
        if category.is_deleted:
            raise ValidationError('Категория не найдена')

        if self.context['request'].user != category.user:
            raise PermissionDenied

        return category


class GoalWithUserSerializer(GoalSerializer):
    user = ProfileSerializer(read_only=True)


class GoalCommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = GoalComment
        fields = '__all__'
        read_only_fields = ('id', 'created', 'updated', 'user')

    def validated_goal(self, goal: Goal) -> Goal:
        if goal.status == Goal.Status.archived:
            raise ValidationError('Цель не найдена')

        if self.context['request'].user != goal.user:
            raise PermissionDenied

        return goal

class GoalCommentWithUserSerializer(GoalCommentSerializer):
    user = ProfileSerializer(read_only=True)
    goal = serializers.PrimaryKeyRelatedField(read_only=True)