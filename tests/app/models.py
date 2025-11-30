from django.db import models


class AdminActionsTestModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Admin Actions Test"
        verbose_name_plural = "Admin Actions Tests"

    def __str__(self) -> str:
        return str(self.name)
