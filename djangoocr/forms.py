from django import from

class CustomClearableFileInput(forms.ClearableFileInput):
    initial_text = ''
    input_text = ''