from django import forms

class AddCardForm(forms.Form):
    quantity=forms.IntegerField(min_value=1, max_value=20)
    
    

class CouponApplyForm(forms.Form):
    code=forms.CharField()