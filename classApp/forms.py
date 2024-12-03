
from django import forms
from .models import PersonalDataModel
from django.core.exceptions import ValidationError
from django.core.validators import validate_email



class PersonalDataForm(forms.ModelForm):

    SEX_CHOICES = [
        ('男', '男'),
        ('女', '女'),
    ]
    PREFECT_CHOICES = [
        ('北海道',     '北海道'),
        ('東京都',     '東京都'),
        ('大阪府',     '大阪府'),
    ]
    HOBBY_CHOICES = [
        ('音楽',        '音楽'),
        ('映画',        '映画'),
        ('アウトドア',  'アウトドア'),
    ]
    FOOD_CHOICES = [
        ('ラーメン',    'ラーメン'),
        ('寿司',        '寿司'),
        ('カレー',      'カレー'),
    ]

    # 性別、都道府県
    sex = forms.ChoiceField(choices=SEX_CHOICES, initial="男", 
                            widget=forms.RadioSelect())
    prefecture = forms.ChoiceField(choices=PREFECT_CHOICES, initial="東京都")

    # 趣味、食べ物 (複数選択が可能)
    hobby = forms.MultipleChoiceField(choices=HOBBY_CHOICES, 
                                      widget=forms.CheckboxSelectMultiple() )
    food  = forms.MultipleChoiceField(choices=FOOD_CHOICES )

    class Meta:
        model = PersonalDataModel
        # fields = "__all__"
        fields = [ "id", "name",  "tel", "email", "sex", "prefecture", "hobby","food"]
        labels = {
                    'id': 'ID',
                    'name': '名前',
                    'tel': '電話番号',
                    'email': 'メール',
                    'sex': '性別',
                    'prefecture': '都道府県',
                    'hobby': '趣味',
                    'food': '食べ物',
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['id'] = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))        
        # フィールド順序を明示的に設定
        self.fields = {
            "id": self.fields["id"],
            "name": self.fields["name"],
            "tel": self.fields["tel"],
            "email": self.fields["email"],
            "sex": self.fields["sex"],
            "prefecture": self.fields["prefecture"],
            "hobby": self.fields["hobby"],
            "food": self.fields["food"],
        }
        # すべてのフィールドを指定
        for field_name, field in self.fields.items():
            
            field.required = False  # フィールドのrequired属性をFalseに設定
            field.label = self.Meta.labels[field_name]
            # field.label_suffix = '$'
            field.label_suffix = ''
            # print( "field.label_suffix", field.label_suffix  )

            # ラジオボタン、チェックボックスは
            # .form-check, .form-check-input, .form-check-label             
            if not field_name in ["sex","hobby"]:
                field.widget.attrs['class'] = 'form-control'

        # フィールドを指定して設定
        self.fields["name"].required = True
        self.fields['name'].widget.attrs['placeholder'] = '名前を入力してください'

        self.fields['id'].widget.attrs = { 
                        'disabled': 'disabled',
                        # 'readonly': 'readonly',
                        'class': 'form-control bg-light text-muted',  # Bootstrapクラス指定
                        }

    """
    # モデルに保存
    def save(self, commit=True):

        instance = super(PersonalDataForm, self).save(commit=False)
        
        # フォームデータを変更
        # instance.memo = instance.memo + 'New Value'  # フィールド名と新しい値を指定

        # instance.categories.set(self.cleaned_data['categories'])
        # 選択されたカテゴリをモデルに関連付ける
        hobby10 = self.cleaned_data.get('hobby10')

        if commit:
            instance.save()
        return instance



    # 入力領域の個別チェックを行う場合はここでチェックする
    def clean_hobby10(self):
        data = self.cleaned_data.get('hobby10')
        return data        
    

    """
    # すべての入力項目のチェックをしたい場合に使用
    # return時には「return self.cleaned_data」を返却が必要
    def clean( self ):
        # self.cleaned_data["hobby"]="abcdef"
        data1 = self.cleaned_data.get('hobby')
        data2 = self.cleaned_data.get('food')
        print(data1, data2)

        return self.cleaned_data




'''
    以降のコードはテストで使用

'''
# hobby     = TestField(choices=HOBBY_CHOICES, widget=forms.CheckboxSelectMultiple(), label="Alphanumeric Field")
# hobby2      = MultiEmailField(widget=forms.CharField(), label='趣味ABC')

class MultiEmailField(forms.CharField):
    def __init__(self, *args, **kwargs):

        # self.choices = kwargs.pop('choices')
        super().__init__(*args, **kwargs)
        pass

    def to_python(self, value):
        """Normalize data to a list of strings."""
        # Return an empty list if no input was given.
        # if not value:
        #     return []
        # return value.split(",")
        return "abcd"
    
    def validate(self, value):
        """Check if value consists only of valid emails."""
        # Use the parent's handling of required fields, etc.
        super().validate(value)
        for email in value:
            validate_email(email)


class TestField(forms.MultipleChoiceField):

    def __init__(self, min_length=None, *args, **kwargs):
        self.min_length = min_length
        super().__init__(*args, **kwargs)    

    def to_python(self, value):
        print("to_python in ", value)
        """Normalize data to a list of strings."""

        # Return an empty list if no input was given.
        # if not value:
        #     return []
        # return value.split(",")
        return value

    def validate(self, value):
        print("validate in ", value)
        super().validate(value)

        # if not value.isalnum():
        #     raise ValidationError("This field must contain only alphanumeric characters.")

        # if self.min_length is not None and len(value) < self.min_length:
        #     raise ValidationError(f"This field must be at least {self.min_length} characters long.")

    def clean(self, value):
        print("clean in ", value)
        return str(value)
        # if not value:
        #     raise forms.ValidationError('Enter at least one e-mail address.')
        # emails = value.split(',')
        # for email in emails:
        #     if not is_valid_email(email):
        #         raise forms.ValidationError('%s is not a valid e-mail address.' % email)
        # return emails

        
