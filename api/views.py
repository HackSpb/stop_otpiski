from django.shortcuts import render

from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response

from .models import *


class IssueView(APIView):
    def get(self, request):
        issue_id = request.GET.get('id')
        if issue_id is None:
            return JsonResponse([issue.to_dict() for issue in Issue.objects.all()])
        issue = Issue.objects.filter(id=issue_id)
        if not issue.exists():
            return JsonResponse(
                {"error": "issue not found"},
                status=404
            )
        return JsonResponse(issue[0].to_dict())

    def post(self, request):
        text = request.data.get('text')
        title = request.data.get('title')
        user = User.get_default_user()  # TODO: fix hardcode: add auth
        if not(text and title and user):
            return JsonResponse({"error": "wrong data"}, status=400)
        issue = Issue.objects.create(text=text, title=title, user=user)
        return JsonResponse({"id": issue.id})


class CommentView(APIView):
    def get(self, request):
        issue_id = request.GET.get('issue_id')
        issue = Issue.objects.filter(id=issue_id)
        if not comment.exists():
            return JsonResponse(
                {"error": "issue not found"},
                status=404
            )
        comments = JsonResponse([comment.to_dict() for comment in Comment.objects.all().order_by('id')])
        return JsonResponse(comments)

    def post(self, request):
        text = request.data.get('text')
        issue_id = request.GET.get('issue_id')
        issue = Issue.objects.filter(id=issue_id)
        user = User.get_default_user()  # TODO: fix hardcode: add auth
        if not (text and issue.exists() and user):
            return JsonResponse({"error": "wrong data"}, status=400)
        issue = Comment.objects.create(text=text, issue=issue, user=user)
        return JsonResponse({"id": issue.id})
