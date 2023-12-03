from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView
from .forms import LoginForm
from django.http import HttpResponseRedirect, Http404
from socios.views import Perfil

# Create your views here.
class Index(TemplateView):
    template_name = "core/index.html"

variable_contexto = {
        'hola' : "1",
        'menu_sports' : [
            {'name':'futbol','url_image':'core/img/pibe_pelota.jpg','descripcion':'En nuestro club, el fútbol va más allá del juego en el campo; es una pasión que compartimos y fomentamos en cada uno de nuestros jugadores. Nuestra misión es desarrollar habilidades futbolísticas sólidas, promoviendo al mismo tiempo valores esenciales como el trabajo en equipo, la disciplina y la dedicación. Contamos con instalaciones de fútbol de primera clase que incluyen 4 campos de juego completamente equipados. Nuestra infraestructura está diseñada para proporcionar un entorno óptimo para el entrenamiento y los partidos, garantizando que cada jugador tenga la oportunidad de alcanzar su máximo potencial. Nuestro equipo de entrenadores está compuesto por profesionales altamente calificados y apasionados por el fútbol. Cada entrenador aporta su experiencia táctica y técnica para guiar a nuestros jugadores en su desarrollo, no solo como futbolistas, sino también como individuos.'},
            {'name':'voley','url_image':'core/img/volley.jpg','descripcion':'En nuestro club, consideramos al vóley no solo como un deporte, sino como una forma de vida. Nuestra misión es desarrollar el talento de cada jugador, fomentando no solo habilidades técnicas sólidas, sino también valores fundamentales como el trabajo en equipo, la disciplina y el respeto. Contamos con instalaciones de vóley de última generación que incluyen 3 canchas completamente equipadas. Nuestro compromiso con la excelencia se refleja en la calidad de nuestras instalaciones, diseñadas para ofrecer un entorno óptimo para el entrenamiento y la competición. En la actualidad, nuestro club alberga 3 equipos de vóley que abarcan todas las edades y niveles de habilidad. Desde equipos de desarrollo hasta equipos de élite, cada uno recibe la atención personalizada de nuestros entrenadores expertos para maximizar su potencial. Nuestra comunidad de jugadores está compuesta por 51 apasionados amantes del vóley.'},
            {'name':'basket','url_image':'core/img/basketball.jpg','descripcion':'Contamos con 2 canchas de baloncesto de primera categoría en nuestras instalaciones, proporcionando un entorno óptimo para el desarrollo del baloncesto. En la actualidad, nuestro club alberga a 35 apasionados jugadores distribuidos en diversas categorías, desde jóvenes talentosos hasta equipos competitivos de adultos. Ofrecemos programas específicos para cada nivel, asegurando que cada miembro tenga la oportunidad de crecer y mejorar en este emocionante deporte.'},
            {'name':'tenis','url_image':'core/img/tenis.jpg','descripcion':'Contamos con 6 canchas de primera categoría en nuestras instalaciones, brindando un entorno óptimo para el desarrollo del tenis. En la actualidad, nuestro club alberga a 22 apasionados jugadores distribuidos en diversas categorías, desde jóvenes talentosos hasta jugadores experimentados. Ofrecemos programas específicos para cada nivel, asegurando que cada miembro tenga la oportunidad de crecer y mejorar en el deporte.'},
            {'name':'natación','url_image':'core/img/natacion.jpg', 'descripcion':'Contamos con instalaciones de natación de primera categoría que incluyen 2 piscinas bien equipadas, proporcionando un entorno propicio para el desarrollo de habilidades acuáticas. En la actualidad, nuestro club cuenta con 20 apasionados nadadores distribuidos en diversas categorías, desde jóvenes prometedores hasta nadadores experimentados. Ofrecemos programas específicos para cada nivel, garantizando que cada miembro tenga la oportunidad de crecer y mejorar en el fascinante mundo de la natación.'},
            {'name':'handball','url_image':'core/img/handball.jpg', 'descripcion':'Nuestras instalaciones para handball son un epicentro dinámico de acción, con 1 cancha especialmente diseñadas para este emocionante deporte de equipo. En nuestro vibrante club, albergamos a 21 apasionados jugadores de handball, desde jóvenes prometedores hasta experimentados competidores. Más que un deporte, el handball en nuestro club es una experiencia única donde la intensidad del juego se fusiona con el compañerismo y la estrategia. Ofrecemos programas adaptados a cada nivel, garantizando que cada miembro disfrute del desafío y la emoción que el handball tiene para ofrecer. ¡Únete a nosotros y sumérgete en un mundo donde la velocidad, la destreza y la camaradería convergen en cada lanzamiento!'}
        ],
        'menu_activities' : [
            {'name':'yoga','url_image':'core/img/yoga.jpg','descripcion':'Nuestro espacio de yoga ofrece un refugio sereno con 2 estudios diseñados para la tranquilidad y el equilibrio. En nuestro club, acogemos a 12 entusiastas practicantes de yoga, desde principiantes hasta aquellos que buscan profundizar su práctica. Ofrecemos clases adaptadas a todos los niveles, brindando un ambiente donde la armonía del cuerpo y la mente se fusiona con la paz interior. ¡Únete a nosotros y descubre la calma y fortaleza que el yoga puede aportar a tu vida!'},
            {'name':'expresión','url_image':'core/img/expresion.jpeg','descripcion':'Nuestro espacio de expresión corporal es un lienzo dinámico con 2 estudios diseñados para fomentar la creatividad y la libertad de movimiento. En nuestro club, acogemos a 9 apasionados participantes de expresión corporal, desde aquellos que buscan explorar su creatividad hasta los que desean mejorar su conexión cuerpo-mente. Ofrecemos sesiones adaptadas para todos los niveles, creando un entorno donde la expresión personal se fusiona con la exploración artística. ¡Únete a nosotros y sumérgete en un viaje de descubrimiento a través del movimiento y la expresión!'},
            {'name':'parrilla','url_image':'core/img/parrilla.jpeg', 'descripcion':'Nuestras parrillas son el corazón palpitante de la camaradería en nuestro club, con 14 áreas de parrilla meticulosamente diseñadas para deleitar a los amantes del asado. En este santuario culinario hay de todo, desde maestros parrilleros hasta aquellos que recién están encendiendo sus brasas. Más que solo fuego y carne, nuestras parrillas ofrecen un escenario donde la pasión por la parrilla se fusiona con la alegría compartida y la buena compañía. Ofrecemos eventos especiales, competiciones amistosas y el placer de saborear la excelencia de nuestras parrillas. ¡Únete a nosotros y descubre un mundo donde la magia de la parrilla crea momentos inolvidables!'},
            {'name':'colonia','url_image':'core/img/colonia.jpg','descripcion':'En la Colonia Recreativa de nuestro club, hemos creado un oasis de diversión, aprendizaje y amistad para niños y jóvenes. Cada verano, recibimos a más de 60 chicos, ofreciéndoles una experiencia única llena de actividades emocionantes y momentos memorables.'},
            {'name':'eventos','url_image':'core/img/recital.jpg','descripcion':'En nuestro club, la música cobra vida a través de nuestros recitales inolvidables. Con al menos 6 eventos anuales, ofrecemos a los amantes de la música una experiencia única en un ambiente íntimo y acogedor.'},
            {'name':'salón','url_image':'core/img/salon.jpeg','descripcion':'Los salones multiuso en nuestro club son la opción perfecta para cualquier ocasión. Con 3 espacios versátiles y modernos, desde reuniones corporativas hasta celebraciones privadas, ofrecemos un entorno adaptable que se ajusta a las necesidades de cada evento. Nuestros salones, equipados con las últimas comodidades, son el lienzo ideal para crear momentos inolvidables. ¡Haz de tus eventos algo extraordinario en los salones multiuso de nuestro club!'}
        ]
    }

class Contacto(TemplateView):   #a cambiar por lo que corresponda
    template_name = "core/contacto.html"

class Institucional(TemplateView):
    template_name = "core/institucional.html"

class FAQ(TemplateView):
    template_name = "core/faq.html"

class Actividad(TemplateView):
    template_name = "core/actividad.html"

def actividades(request):
    return render(request,"core/actividades.html",variable_contexto)

def actividad(request, actividad):
    
    for deporte in variable_contexto["menu_sports"]:
        if deporte["name"] == actividad:
            nuevo_contexto = {'actividad':deporte}
            return render(request,"core/actividad.html",nuevo_contexto)
    for activi in variable_contexto["menu_activities"]:
        if activi["name"] == actividad:
            nuevo_contexto = {'actividad':activi}
            return render(request,"core/actividad.html",nuevo_contexto)
    
    print("no está la actividad")
    raise Http404

def loginView(request):
    if request.method == "POST":

        # login_form = LoginForm(request.POST)
  
        # if login_form.is_valid():
        usuario = request.POST['username']
        clave = request.POST['password']

        user = authenticate(request, username = usuario, password = clave)

        if(user is not None):

            login(request,user)

            messages.info(request, "Ha iniciado sesión correctamente")

            return HttpResponseRedirect('/miPerfil')
        else:
            messages.info(request, "Error al iniciar sesion")
            return redirect(reverse('login'))

    else: 
        if request.user.is_authenticated:
            return HttpResponseRedirect('/miPerfil')

        else:
            # context = {
            #     'ingreso_socios': LoginForm()
            # }
            return render(request, 'core/login.html')