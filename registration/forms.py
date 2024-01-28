from django import forms
from .models import Participant
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['first_name','last_name','username','password1','password2','categories', 'date_of_birth', 'gender', 'email_address', 'street_address', 'city', 'zip_code', 'mobile', 'emergency_contact_number', 'relationship']



        


# class ParticipantForm(forms.ModelForm):
#     class Meta:
#         model = Participant
#         fields = ['name', 'date_of_birth', 'gender', 'email_address', 'street_address', 'city', 'zip_code', 'mobile', 'emergency_contact_number', 'relationship']


# User = get_user_model()

# class UserParticipantForm(UserCreationForm):
#     name = forms.CharField(max_length=100)
#     date_of_birth = forms.DateField()
#     gender = forms.CharField(max_length=10)
#     street_address = forms.CharField(max_length=200)
#     city = forms.CharField(max_length=100)
#     zip_code = forms.CharField(max_length=20)
#     mobile = forms.CharField(max_length=20)
#     emergency_contact_number = forms.CharField(max_length=20)
#     relationship = forms.CharField(max_length=50)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         if commit:
#             user.save()
#             participant = Participant(user=user, name=self.cleaned_data['name'], date_of_birth=self.cleaned_data['date_of_birth'],
#                                       gender=self.cleaned_data['gender'], street_address=self.cleaned_data['street_address'],
#                                       city=self.cleaned_data['city'], zip_code=self.cleaned_data['zip_code'],
#                                       mobile=self.cleaned_data['mobile'], emergency_contact_number=self.cleaned_data['emergency_contact_number'],
#                                       relationship=self.cleaned_data['relationship'])
#             participant.save()
#         return user
