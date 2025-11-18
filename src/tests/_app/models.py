from django.db import models


class AdminActionsTestModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.name)
