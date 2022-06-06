from apps.modelo.models import Cliente, Agente, Barrio, Persona
from .forms import FormularioCliente, FormularioAgente, FormularioPersona, FormularioBarrio
from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User

@login_required
def index(request):
    usuario = request.user
    if usuario.groups.filter(name='admin').exists():
        #manejo del ORM
        listaAgentes = Agente.objects.all()
        return render (request, 'administrador/index.html', locals())
    
    if usuario.groups.filter(name='call center').exists():
        #manejo del ORM
        listaClientes = Cliente.objects.all()
        return render (request, 'callCenter/index.html', locals())

    if usuario.groups.filter(name='chofer').exists():
        #manejo del ORM
        listaClientes = Cliente.objects.all()
        return render (request, 'chofer/index.html', locals())

    return render(request, 'login/forbidden.html', locals())

@login_required
def crearAgente(request):
    usuario = request.user
    if usuario.groups.filter(name='admin').exists():
        formulario_persona = FormularioPersona(request.POST)
        formulario_agente = FormularioAgente(request.POST)
        if request.method == 'POST':
            if formulario_persona.is_valid() and formulario_agente.is_valid():
                
                persona = Persona()
                datos_persona= formulario_persona.cleaned_data
                persona.cedula = datos_persona.get('cedula')
                persona.apellidos = datos_persona.get('apellidos')
                persona.nombres = datos_persona.get('nombres')
                persona.genero = datos_persona.get('genero')
                persona.correo = datos_persona.get('correo')
                persona.telefono = datos_persona.get('telefono')
                persona.celular = datos_persona.get('celular')
                #ORM
                persona.save()

                agente = Agente()
                datos_agente = formulario_agente.cleaned_data
                agente.funcion = datos_agente.get('funcion')
                agente.persona = persona
                #ORM
                agente.save()

                user = User.objects.create_user(persona.nombres, persona.correo, persona.cedula)
                user.first_name = persona.nombres
                user.last_name = persona.apellidos
                if (agente.funcion == "chofer"):
                    grupo = Group.objects.get(name='Chofer')
                else:
                    grupo = Group.objects.get(name='Call Center')
                user.groups.add(grupo)
                user.save()
            
            return redirect(index)
        return render (request, 'administrador/crearAgente.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())

@login_required
def modificarAgente(request, agente_id):
    usuario = request.user
    if usuario.groups.filter(name='admin').exists():
        agente = Agente.objects.get(agente_id = agente_id)
        persona = Persona.objects.get(cedula = agente.persona.cedula)
        if request.method == 'GET':
            formulario_agente = FormularioAgente(instance = agente)
            formulario_persona = FormularioPersona(instance = persona)
        else:
            formulario_agente = FormularioAgente(request.POST, instance = agente)
            formulario_persona = FormularioPersona(request.POST, instance = persona)
            if formulario_persona.is_valid() and formulario_agente.is_valid():
                formulario_agente.save()
                formulario_persona.save()
            return redirect(index)
        return render (request, 'administrador/modificarAgente.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())

@login_required
def eliminarAgente(request, agente_id):
    usuario = request.user
    if usuario.groups.filter(name='admin').exists():
        agente = Agente.objects.get(agente_id=agente_id)
        persona = Persona.objects.get(cedula = agente.persona.cedula)
        user = User.objects.get(username = persona.nombres)
        user.delete()
        persona.delete()
        return redirect(index)
    else:
        return render(request, 'login/forbidden.html', locals())

@login_required
def indexBarrio(request):
    usuario = request.user
    if usuario.groups.filter(name='Call Center').exists():
        listaBarrios = Barrio.objects.all()
        return render (request, 'callCenter/indexBarrios.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())

@login_required
def crearBarrio(request):
    usuario = request.user
    if usuario.groups.filter(name='Call Center').exists():
        formulario_barrio = FormularioBarrio(request.POST)
        if request.method == 'POST':
            if formulario_barrio.is_valid():
                
                barrio = Barrio()
                datos_barrio = formulario_barrio.cleaned_data
                barrio.nombre = datos_barrio.get('nombre')
                #ORM
                barrio.save()

            return redirect(indexBarrio)
        return render (request, 'callCenter/crearBarrio.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())

@login_required
def modificarBarrio(request, barrio_id):
    usuario = request.user
    if usuario.groups.filter(name='Call Center').exists():
        barrio = Barrio.objects.get(barrio_id = barrio_id)
        if request.method == 'GET':
            formulario_barrio = FormularioBarrio(instance = barrio)
        else:
            formulario_barrio = FormularioBarrio(request.POST, instance = barrio)
            if formulario_barrio.is_valid():
                formulario_barrio.save()

            return redirect(indexBarrio)
        return render (request, 'callCenter/modificarBarrio.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())

@login_required
def eliminarBarrio(request, barrio_id):
    usuario = request.user
    if usuario.groups.filter(name='Call Center').exists():
        barrio = Barrio.objects.get(barrio_id=barrio_id)
        barrio.delete()
        return redirect(indexBarrio)
    else:
        return render(request, 'login/forbidden.html', locals())

@login_required
def crearCliente(request, barrio_id):
    usuario = request.user
    barrio = Barrio.objects.get(barrio_id = barrio_id)
    if usuario.groups.filter(name='Call Center').exists():
        formulario_persona = FormularioPersona(request.POST)
        formulario_cliente = FormularioCliente(request.POST)
        if request.method == 'POST':
            if formulario_persona.is_valid() and formulario_cliente.is_valid():
                
                persona = Persona()
                datos_persona= formulario_persona.cleaned_data
                persona.cedula = datos_persona.get('cedula')
                persona.apellidos = datos_persona.get('apellidos')
                persona.nombres = datos_persona.get('nombres')
                persona.genero = datos_persona.get('genero')
                persona.correo = datos_persona.get('correo')
                persona.telefono = datos_persona.get('telefono')
                persona.celular = datos_persona.get('celular')
                #ORM
                persona.save()

                cliente = Cliente()
                datos_cliente= formulario_cliente.cleaned_data
                cliente.calle1 = datos_cliente.get('calle1')
                cliente.calle2 = datos_cliente.get('calle2')
                cliente.referencia1 = datos_cliente.get('referencia1')
                cliente.referencia2 = datos_cliente.get('referencia2')
                cliente.persona = persona
                cliente.barrio = barrio
                #ORM
                cliente.save()
            
            return redirect(indexBarrio)
        return render (request, 'callCenter/crearClientes.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())

@login_required
def modificarCliente(request, cliente_id):
    usuario = request.user
    if usuario.groups.filter(name='Call Center').exists():
        cliente = Cliente.objects.get(cliente_id = cliente_id)
        persona = Persona.objects.get(cedula = cliente.persona.cedula)
        barrio = Barrio.objects.get(barrio_id = cliente.barrio.barrio_id)
        if request.method == 'GET':
            formulario_cliente = FormularioCliente(instance = cliente)
            formulario_persona = FormularioPersona(instance = persona)
        else:
            formulario_cliente = FormularioCliente(request.POST, instance = cliente)
            formulario_persona = FormularioPersona(request.POST, instance = persona)
            if formulario_persona.is_valid() and formulario_cliente.is_valid():
                formulario_cliente.save()
                formulario_persona.save()
            return redirect(index)
        return render (request, 'callCenter/modificarCliente.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())

@login_required
def eliminarCliente(request, cliente_id):
    usuario = request.user
    if usuario.groups.filter(name='Call Center').exists():
        cliente = Cliente.objects.get(cliente_id=cliente_id)
        persona = Persona.objects.get(cedula = cliente.persona.cedula)
        persona.delete()
        return redirect(index)
    else:
        return render(request, 'login/forbidden.html', locals())

@login_required
def indexChofer(request):
    usuario = request.user
    if usuario.groups.filter(name='Chofer').exists():
        listaClientes = Cliente.objects.all()
        return render (request, 'chofer/index.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())