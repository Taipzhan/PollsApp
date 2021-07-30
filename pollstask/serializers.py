from rest_framework import serializers
from pollstask.models import Polls, Questions, Choice, Answers


class PollsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polls
        fields =('name', 'date_start', 'date_end', 'description')
        read_only_fields = ('date_start',)

    def create(self, validated_data):
        return Polls.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.date_end = validated_data.get('date_end', instance.date_end)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields =('text', 'poll')

    def create(self, validated_data):
        return Questions.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.name)
        instance.poll = validated_data.get('poll', instance.date_end)
        instance.save()
        return instance


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields =('question', 'choice_text')

    def create(self, validated_data):
        return Choice.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.text = validated_data.get('question', instance.name)
        instance.poll = validated_data.get('choice_text', instance.date_end)
        instance.save()
        return instance


class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields =('__all__')
        read_only_fields = ('id_user',)

    def create(self, validated_data):
        return Answers.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.poll = validated_data.get('poll', instance.poll)
        instance.question = validated_data.get('question ', instance.question)
        instance.choice = validated_data.get('choice', instance.choice)
        instance.answer = validated_data.get('answer', instance.answer)
        instance.save()
        return instance
