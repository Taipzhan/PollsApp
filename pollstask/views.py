from pollstask.models import Polls, Questions, Choice, Answers
from pollstask.serializers import PollsSerializer, QuestionsSerializer, ChoiceSerializer, AnswersSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny


class PollsListAllView(APIView):
    permission_classes = [AllowAny ,]

    def get(self, request):
        poll = Polls.objects.all()
        serializer = PollsSerializer(poll, many=True)
        return Response(serializer.data)


class PollsListView(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAdminUser)

    def get(self, request):
        poll = Polls.objects.all()
        serializer = PollsSerializer(poll, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PollsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PollsDetailView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminUser]

    def get(self, request, pk):
        try:
            poll = Polls.objects.get(id=pk)
            serializer = PollsSerializer(poll)
            return Response(serializer.data)
        except Polls.DoesNotExist:
            return Response(status=404)

    def put(self, request, pk):
        poll = Polls.objects.get(id=pk)
        serializer = PollsSerializer(poll, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        poll = Polls.objects.get(id=pk)
        poll.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class QuestionsView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminUser]

    def get(self, request):
        question = Questions.objects.all()
        serializer = QuestionsSerializer(question , many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionsDetailView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminUser]

    def get(self, request, pk):
        try:
            question = Questions.objects.get(id=pk)
            serializer = QuestionsSerializer(question)
            return Response(serializer.data)
        except Polls.DoesNotExist:
            return Response(status=404)

    def put(self, request, pk):
        question = Questions.objects.get(id=pk)
        serializer = QuestionsSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        question = Questions.objects.get(id=pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ChoiceView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminUser]

    def get(self, request):
        choice = Choice.objects.all()
        serializer = ChoiceSerializer(choice, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ChoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChoiceDetailView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminUser]

    def get(self, request, pk):
        try:
            choice = Choice.objects.get(id=pk)
            serializer = ChoiceSerializer(choice)
            return Response(serializer.data)
        except Polls.DoesNotExist:
            return Response(status=404)

    def put(self, request, pk):
        choice = Choice.objects.get(id=pk)
        serializer = ChoiceSerializer(choice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        choice = Choice.objects.get(id=pk)
        choice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AnswersView(APIView):
    permission_classes = [AllowAny,]

    def get(self, request):
        choice = Answers.objects.all()
        serializer = AnswersSerializer(choice, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AnswersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerDetailView(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request, pk):
        try:
            answer = Answers.objects.get(id=pk)
            serializer = AnswersSerializer(answer)
            return Response(serializer.data)
        except Polls.DoesNotExist:
            return Response(status=404)

    def put(self, request, pk):
        answer = Answers.objects.get(id=pk)
        serializer = AnswersSerializer(answer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        answer = Answers.objects.get(id=pk)
        answer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)