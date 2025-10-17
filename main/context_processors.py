"""
Context processor for providing the contact modal globally across templates
instead of reading it into every view
"""
from .forms import ContactForm


def contact_form(request):
    return {'form': ContactForm()}
