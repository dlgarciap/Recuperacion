from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UsuarioPersonalizado
from .forms import CustomUserCreationForm

@login_required
def lista_usuarios(request):
    usuarios = UsuarioPersonalizado.objects.all()
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})

@login_required
def crear_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado exitosamente!')
            return redirect('usuarios:lista_usuarios')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'usuarios/crear_usuario.html', {'form': form})

@login_required
def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(UsuarioPersonalizado, id=usuario_id)
    
    if usuario == request.user:
        messages.error(request, 'No puedes eliminar tu propio usuario!')
        return redirect('usuarios:lista_usuarios')
    
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, 'Usuario eliminado exitosamente!')
        return redirect('usuarios:lista_usuarios')
    
    return render(request, 'usuarios/confirmar_eliminar.html', {'usuario': usuario})