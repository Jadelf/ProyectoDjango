from	django	import	forms
from	.models	import	Equipo,Medico

class	EquipoForm(forms.ModelForm):
    class	Meta:
        model	=	Equipo
        fields	=	('nombre',	'descripcion',)

class	MedicoForm(forms.ModelForm):
    class	Meta:
        model	=	Medico
        fields	=	('nombre',	'edad', 'especialidad',)
