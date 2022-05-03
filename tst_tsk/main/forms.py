from django.forms import ModelForm
from .models import Employee
from django.core.exceptions import ValidationError

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

    def clean(self):
        """
        Checks if boss isn't in his subordinates list
        """
        emp_id = self.cleaned_data.get('emp_id')
        position = self.cleaned_data.get('position')
        boss = self.cleaned_data.get('boss')

        if position and boss:
            if position.level <= boss.position.level:
                raise ValidationError('Boss should have higher ierarchy level and cant be the same employee')
            if emp_id == boss.emp_id:
                raise ValidationError('Boss cant be for boss for itself')     
        return self.cleaned_data