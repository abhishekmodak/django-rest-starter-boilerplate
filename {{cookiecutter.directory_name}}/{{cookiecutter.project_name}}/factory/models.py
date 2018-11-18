from django.db import models
from datetime import datetime
# Create your models here.


class BaseModel(models.Model):
    """ Factory  model for all models """

    added_at   = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes   = models.TextField(null=True, blank=True)
    status  = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        # This table is abstract and use to create other models
        abstract = True

    def delete(self):
        """ Overriding Delete method to make status=False
        """
        self.status = False
        self.deleted_at = datetime.now()
        self.save()

    def kill_object(self):
        """Delete permanently
        """
        super(BaseModel, self).delete()

