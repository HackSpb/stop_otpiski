from django.db import models


class Issue(models.Model):
    # ACCEPTED = 'accepted'
    # REJECTED = 'rejected'
    # RESOLVED = 'resolved'
    # PARTLY_RESOLVED = 'party_resolved'
    # GOT_ANSWER = 'got_answer'
    # STATUSES = [
    #     (ACCEPTED, 'Отправлено'),
    #     (REJECTED, 'Отказ'),
    #     (RESOLVED, 'Решено'),
    #     (PARTLY_RESOLVED, 'Частично решено'),
    #     (GOT_ANSWER, 'Пришел ответ'),
    # ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    # status = models.CharField(choices=STATUSES, max_length=64)
    title = models.CharField(max_length=128)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def to_dict(self):
        return {
            "id": self.id,
            "user": self.user.to_dict(),
            # "status": self.status,
            "title": self.title
        }


class User(models.Model):
    name = models.CharField(max_length=64, blank=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

    @classmethod
    def get_default(cls):
        anon_user = cls.objects.filter(name="Anon")
        if not anon_user.exist():
            anon_user = cls.objects.create(name="anon")
        return anon_user


class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)

    def to_dict(self):
        return {
            "text": self.text,
            "date": self.ctime(),
            "user": self.user.to_dict(),
            "issue_id": self.issue.id
        }
