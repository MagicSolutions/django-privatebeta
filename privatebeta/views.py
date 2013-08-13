from django.shortcuts import render, redirect
from privatebeta.forms import InviteRequestForm


def invite(request, form_class=InviteRequestForm, template_name="privatebeta/invite.html", extra_context=None):
    """
    Allow a user to request an invite at a later date by entering their email address.
    
    **Arguments:**
    
    ``template_name``
        The name of the tempalte to render.  Optional, defaults to
        privatebeta/invite.html.

    ``extra_context``
        A dictionary to add to the context of the view.  Keys will become
        variable names and values will be accessible via those variables.
        Optional.
    
    **Context:**
    
    The context will contain an ``InviteRequestForm`` that represents a
    :model:`invitemelater.InviteRequest` accessible via the variable ``form``.
    If ``extra_context`` is provided, those variables will also be accessible.
    
    **Template:**
    
    :template:`privatebeta/invite.html` or the template name specified by
    ``template_name``.
    """
    form = form_class(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('privatebeta_sent')

    context = {'form': form}

    if extra_context is not None:
        context.update(extra_context)

    return render(request, template_name, context)


def sent(request, template_name="privatebeta/sent.html", extra_context=None):
    """
    Display a message to the user after the invite request is completed
    successfully.
    
    **Arguments:**
    
    ``template_name``
        The name of the tempalte to render.  Optional, defaults to
        privatebeta/sent.html.

    ``extra_context``
        A dictionary to add to the context of the view.  Keys will become
        variable names and values will be accessible via those variables.
        Optional.
    
    **Context:**
    
    There will be nothing in the context unless a dictionary is passed to
    ``extra_context``.
    
    **Template:**
    
    :template:`privatebeta/sent.html` or the template name specified by
    ``template_name``.
    """
    return render(request, template_name, extra_context)
