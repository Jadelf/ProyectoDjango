from	django	import	forms
from	.models	import	Equipo,Medico

class	EquipoForm(forms.ModelForm):
    class	Meta:
        model	=	Equipo
        fields	=	('nombre',	'descripcion',)

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields	=	('nombre',	'edad', 'especialidad', 'equipos',)
        def __init__(self, *args, **kwargs):
            super(MedicoForm,self).__init__(*args,**kwargs)
            self.fields["equipos"].widget = forms.widgets.CheckboxSelectMultiple()
            self.fields["equipos"].queryset = Equipo.objects.all()
