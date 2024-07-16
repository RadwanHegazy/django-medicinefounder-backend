from django.db import models
from users.models import User

class Medicine (models.Model) :
    name = models.CharField(max_length=225)
    img = models.ImageField(upload_to='medicine-pics/')
    user = models.ForeignKey(User, related_name='upload_by', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    