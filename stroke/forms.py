from django import forms

class Parameters(forms.Form):
    age = forms.IntegerField(max_value=120,min_value=1 , widget=forms.NumberInput(attrs={'id':'a1' , 'type':'text','class':'validate'}) , error_messages={'invalid':'Please enter a number'})
    hypertension= forms.IntegerField(widget=forms.NumberInput(attrs={'id':'a2' , 'type':'text','class':'validate'}))
    heartdisease = forms.IntegerField(widget=forms.NumberInput(attrs={'id':'a3' , 'type':'text','class':'validate'}))
    avgglucoselevel = forms.IntegerField(widget=forms.NumberInput(attrs={'id':'a4' , 'type':'text','class':'validate'}))
    bmi = forms.IntegerField(widget=forms.NumberInput(attrs={'id':'a5' , 'type':'text','class':'validate'}))
    genderMale = forms.IntegerField(widget=forms.NumberInput(attrs={'id':'a6' , 'type':'text','class':'validate'}))
    genderOther = forms.IntegerField(widget=forms.NumberInput(attrs={'id':'a7' , 'type':'text','class':'validate'}))
    evermarriedYes = forms.IntegerField(widget=forms.NumberInput(attrs={'id':'a8' , 'type':'text','class':'validate'}))
    worktypeNeverworked = forms.IntegerField(widget=forms.NumberInput(attrs={'id':'a9' , 'type':'text','class':'validate'}))
    worktypePrivate = forms.FloatField(widget=forms.NumberInput(attrs={'id':'a10' , 'type':'text','class':'validate'}))
    worktypeSelfemployed = forms.IntegerField(widget=forms.NumberInput(attrs={'id':'a11' , 'type':'text','class':'validate'}))
    worktypechildren = forms.IntegerField(widget=forms.NumberInput(attrs={'id':'a12' , 'type':'text','class':'validate'}))
    ResidencetypeUrban= forms.IntegerField(widget=forms.NumberInput(attrs={'id':'a13' , 'type':'text','class':'validate'}))
    smokingstatusformerlysmoked = forms.IntegerField(widget=forms.NumberInput(attrs={'id':'a14' , 'type':'text','class':'validate'}))
    smokingstatusneversmoked= forms.IntegerField(widget=forms.NumberInput(attrs={'id':'a15' , 'type':'text','class':'validate'}))
    smokingstatussmokes= forms.IntegerField(widget=forms.NumberInput(attrs={'id':'a16' , 'type':'text','class':'validate'}))   
