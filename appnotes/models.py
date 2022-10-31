from django.db import models

NOTE_LABELE_CHOICES = (
    ('P', 'primary'),
    ('SE', 'secondary'),
    ('SU', 'success'),
    ('D', 'danger'),
    ('W', 'warning'),
    ('I', 'info'),
    ('L', 'light'),
    ('D', 'dark'),
)

class Note(models.Model):
    title = models.CharField(max_length=128)
    due_date = models.DateTimeField()
    note_label = models.CharField(choices=NOTE_LABELE_CHOICES, max_length=2)


    def __str__(self):
        return self.title
