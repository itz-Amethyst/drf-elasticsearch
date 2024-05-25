from django.db import models
from django.utils.translation import gettext_lazy as _



class CoreModel(models.Model):
    """
        CoreModel represents a base model providing common fields and validation logic for other models.

        Attributes:
            created_at (models.DateTimeField): The time the instance was created.
            modified_at (models.DateTimeField): The time the instance was last modified.
    """


    created_at: models.DateTimeField = models.DateTimeField(
        verbose_name = _("Created At") ,
        help_text = _("The time that created") ,
        db_comment = _("The time that created") ,
        auto_now_add = True ,
        editable = False ,
        db_column = _("Created at")
    )

    modified_at: models.DateTimeField = models.DateTimeField(
        verbose_name = _("Modified At") ,
        help_text = _("The time that was last modified") ,
        db_comment = _("The time that was last modified") ,
        auto_now = True ,
        editable = False ,
        db_column = _("Modified At")
    )

    class Meta:
        abstract = True