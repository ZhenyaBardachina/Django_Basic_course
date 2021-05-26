from django.contrib.auth import get_user_model
from django.forms import ModelForm

from authapp.forms import ShopUserEditForm
from mainapp.models import ProductCategory


class AdminShopUserUpdateForm(ShopUserEditForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'password', 'email', 'age', 'avatar', 'is_staff',
                  'is_superuser', 'is_active')


class ProductCategoryCreateForm(ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''