# Que es un Mixin en Django? 
# Es una clase que no hereda de ningun modelo de Django, pero se puede usar para compartir logica entre diferentes clases (herencia multiple)

class TemplateTitleMixin(object):   # Definimos una clase que servirá como Mixin
    title = None                    # Por defecto, el Mixin no tiene un título definido

    def get_context_data(self, *args, **kwargs):    # Sobreescribimos el metodo get_context_data para añadirle o modificar variables que se envian al template
        context = super().get_context_data(*args, **kwargs)        # Llamamos al metodo get_context_data del padre para obtener el contexto por defecto / le pasamos los argumentos que recibe el metodo get_context_data
        context["title"] = self.title   # Añadimos la variable title al contexto
        return context  # Devolvemos el contexto con la nueva variable

    def get_title(self):  # Metodo auxiliar para obtener el título
        return self.title   # Devolvemos el título
    
    