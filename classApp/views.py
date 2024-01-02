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


def make_context( md, ctx ):
    
    # ラベル名の取得
    labels= PersonalDataForm.LABELS

    # フィールドの取得
    fields = md._meta.get_fields()

    # テンプレートファイルの引数
    obj =[]

    for field in fields:
        # フィード情報の取得
        field_name = field.name
        field_value = getattr( ctx["object"], field_name)
        print( f"{field_name}= {field_value}" )

        # フィード名からラベル名に変換
        lbl_name = ""
        if field_name in labels:       
            lbl_name = labels[field_name]

        # データ型がlistなら、漢字カンマ区切に変換
        value = field_value
        if type(value) is list:
            value = "、".join(value)
            
        obj.append( {"name": lbl_name, "value":value})
    
    
    ctx["object2"] = obj
    return ctx


# テンプレートのファイル名は、モデル名の小文字_???
# ???_list.html
# ???_detail.html
# ???_confirm_delete.html
# ???_form.html

class PersonalList( ListView ):
    model = PersonalDataModel 

class PersonalDetail( DetailView ):
    model = PersonalDataModel 

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx =make_context( PersonalDataModel, ctx )
        return ctx

class PersonalDelete( DeleteView ): 
    model = PersonalDataModel
    success_url = reverse_lazy('list_url')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx =make_context( PersonalDataModel, ctx )
        return ctx


class PersonalCreate(CreateView):
    model = PersonalDataModel 
    form_class = PersonalDataForm
    success_url = reverse_lazy('list_url')
    extra_context = {'title': '登録'}

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['label_suffix'] = ''
        return kwargs    

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
    #     ctx = super().get_context_data(**kwargs)
    #     ctx["title"] = "修正"
    #     return ctx





