from django.db import models


class Form(models.Model):
    """
    Represents a job application form submission.

    Stores applicant details including name, email,
    availability date, and current occupation.
    """
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length=80)

    def __str__(self):
        """Return a string representation of the form submission."""
        return f"{self.first_name} {self.last_name}"