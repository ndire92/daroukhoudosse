
from django import forms
from .models import Post, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Requis. Entrez une adresse e-mail valide.', widget=forms.TextInput(
        attrs={'placeholder': '', 'class': 'form-control'}))
    username = forms.CharField(label='utilisateur', widget=forms.TextInput(
        attrs={'placeholder': '', 'class': 'form-control'}))
    first_name = forms.CharField(label='prénom', widget=forms.TextInput(
        attrs={'placeholder': '', 'class': 'form-control'}))
    last_name = forms.CharField(label='nom', widget=forms.TextInput(
        attrs={'placeholder': '', 'class': 'form-control'}))
    password1 = forms.CharField(label='mot de passe', widget=forms.PasswordInput(
        attrs={'placeholder': '', 'class': 'form-control'}))
    password2 = forms.CharField(label='confirmer password', widget=forms.PasswordInput(
        attrs={'placeholder': '', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data.get('username')

        # Vérifier si le nouveau nom d'utilisateur est unique
        if User.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError(
                'Le nom d\'utilisateur existe déjà. Veuillez en choisir un autre.')

        return username


class PostForm(forms.ModelForm):
    title = forms.CharField(label='Titre', widget=forms.TextInput(attrs={
        'class': 'form-controle',
    }))
    content = forms.CharField(label='Content', widget=forms.Textarea(attrs={
        'class': 'form-control',
    }))

    class Meta:
        model = Post
        fields = ('title', 'content', 'image')


class ProfileForm(forms.ModelForm):
    
    first_name = forms.CharField( label='Prénom',widget=forms.TextInput(
        attrs={'placeholder': 'Prénom', 'class': 'form-control', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px'}))
    last_name = forms.CharField( label='Nom',widget=forms.TextInput(
        attrs={'placeholder': 'Nom', 'class': 'form-control', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px'}))
    email = forms.EmailField( label='Email',widget=forms.EmailInput(
        attrs={'placeholder': 'Email', 'class': 'form-control', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px'}))
    description = forms.CharField(label='Description' ,widget=forms.TextInput(
        attrs={'placeholder': 'Description', 'class': 'form-control', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px'}))
    phone_number = forms.CharField(label='Téléphone' ,widget=forms.NumberInput(
        attrs={'placeholder': 'Téléphone', 'class': 'form-control', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px'}))
    address = forms.CharField(label='Addresse', widget=forms.TextInput(
        attrs={'placeholder': 'Adresse', 'class': 'form-control', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px'}))
    
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'description',
                  'phone_number', 'address', 'profile_picture']

    def save(self, commit=True, user=None):
        profile = super(ProfileForm, self).save(commit=False)
        profile.user = user
        if commit:
            profile.save()
        return profile
