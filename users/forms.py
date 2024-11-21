from django import forms
from users.models import OAuthCredential
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp

class OAuthCredentialForm(forms.ModelForm):
    class Meta:
        model = OAuthCredential
        fields = "__all__"
        exclude = ['is_default']

    def __init__(self, *args, **kwargs) -> None:
        super(OAuthCredentialForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'input_form flex-grow-1'

    def clean(self):
        cleaned_data = super().clean()
        val_domain_name = self.cleaned_data['domain_name']
        val_client_id = self.cleaned_data['client_id']
        val_client_secret = self.cleaned_data['client_secret']
        val_desc = self.cleaned_data['desc']
        if val_domain_name == None or val_client_id == None or val_client_secret == None or val_desc == None:
            raise forms.ValidationError("Fields Can't Be Empty...")

        if self.instance.id:
            if OAuthCredential.objects.filter(domain_name = val_domain_name).exclude(id = self.instance.id).exists():
                raise forms.ValidationError("Domain Entered Already Exists..")
        else:
            if Site.objects.filter(domain = val_domain_name).exists():
                raise forms.ValidationError("Domain Entered Already Exists..")

        return cleaned_data

    def save(self, commit: bool = True) :       
        instance = super().save(commit = False)
           
        instance.domain_name = instance.domain_name.strip()
        instance.name = instance.name.strip()
        instance.client_id = instance.client_id.strip()
        instance.client_secret = instance.client_secret.strip()
        
        if commit:
            if instance.id is None:
                site, created = Site.objects.get_or_create(domain = instance.domain_name, name = instance.domain_name)
                social_app, created2 = SocialApp.objects.get_or_create(
                    provider = "google", 
                    name = f"google_{site.id}", 
                    client_id = instance.client_id,
                    secret = instance.client_secret
                    )
                social_app.sites.add(site)
            else:
                pass
            instance.save()

        return instance