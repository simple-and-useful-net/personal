from django.shortcuts import render
from django. shortcuts import render, redirect 
from django. views. generic import ListView, DetailView, CreateView, DeleteView, UpdateView 
from django. urls import reverse_lazy 
from django. contrib. auth. models import User 
from django. db import IntegrityError
from django.core.exceptions import ValidationError
from django. contrib. auth import authenticate, login ,logout 

from .models import PersonalDataModel 
from .forms import  PersonalDataForm 


def make_context( ctx ):
    
    # リスト型変数の初期化
    # リストの各値は、辞書型で設定される
    obj =[]

    # ラベル情報の取得
    labels = PersonalDataForm._meta.labels

    for field_name,lbl_name in labels.items():

        # フィード値の取得
        field_value = getattr( ctx["object"], field_name)

        # 取得値がリスト型（趣味、食べ物）はすべて結合して文字列にする
        # （結合区切りとして「、」で結合）
        if type(field_value) is list:
            field_value = "、".join(field_value)
            
        obj.append( {"name": lbl_name, "value":field_value})
        print( f"{field_name}= {field_value}" )

    # テンプレート変数名をobject2に指定して設定
    ctx["object2"] = obj
    return ctx



# テンプレートのファイル名は、モデル名の小文字_???
# ???_list.html
# ???_detail.html
# ???_confirm_delete.html
# ???_form.html

class PersonalList( ListView ):
    model = PersonalDataModel 

    #データベースに登録された順番
    def get_queryset(self):
        return super().get_queryset().order_by('id')
        
class PersonalDetail( DetailView ):
    model = PersonalDataModel 

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx =make_context( ctx )
        return ctx

class PersonalDelete( DeleteView ): 
    model = PersonalDataModel
    success_url = reverse_lazy('list_url')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx =make_context( ctx )
        return ctx


class PersonalCreate(CreateView):
    model = PersonalDataModel 
    form_class = PersonalDataForm
    success_url = reverse_lazy('list_url')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # kwargs['label_suffix'] = ''
        return kwargs    

    extra_context = {'title': '登録'}
    # def get_context_data(self, **kwargs):
    #     ctx = super().get_context_data(**kwargs)
    #     ctx["title"] = "登録"
    #     return ctx

class PersonalUpdate(UpdateView):
    model = PersonalDataModel 
    form_class = PersonalDataForm
    success_url = reverse_lazy('list_url')

    extra_context = {'title': '修正'}
    # def get_context_data(self, **kwargs):
        # ctx = super().get_context_data(**kwargs)
        # ctx["title"] = "修正"
        # return ctx





