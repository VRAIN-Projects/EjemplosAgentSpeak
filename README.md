# Ejemplos del lenguaje AgentSpeak

Se está probando el lenguaje en el siguiente entorno:
- Python 3.9
- Python con las librerías Spade y Spade BDI.
- Servidor XMPP (Openfire), con una base de datos MySql.
- Windows 10 como sistema operativo.

## Ejecutar ASL
- Cambiar ruta del fichero ASL en el fichero basic.py
- Escribir usuario@servidor y contraseña del servidor XMPP

## Más ejemplos
http://jason.sourceforge.net/jBook/jBookWebSite/Examples.html
https://github.com/javipalanca/pygomas/tree/master/pygomas/ASL

# Símbolos
- "+" Añadir creencia
- "-" Eliminar creencia
- "+!" Añadir logro-objetivo
- "-!" Eliminar logro-objetivo
- "+?" Añadir test-objetivo
- "-?" Eliminar test-objetivo
- "!" logro
- "!!" N/S
- ":" Se usa del siguiente modo (triggering_event : context <- body)
    - El contexto es true o false.
        - "&" operador booleano and
        - "|" operador booleano or
        - "not" operador booleano negación
    - El body es lo que se ejecuta si es cierto el contexto
    
- ";" Separar los planes 
- ":-" Se usa en las creencias. Son como reglas.
- "." Fin del plan o de la creencia
- Variables. Empiezan con mayúscula. Se usan en los planes.
- Conocimiento. Pueden empezar con minúscula. Se usan en las creencias.

# Otros símbolos no testeados EN SPADE_BDI pero existentes en la versión 3.1 de JASON
- "<:" TK_GOAL_CONDITION Condición de objetivo
- "::" TK_NS_SEP
- "@" Etiquetas de planes

# Cosas no implementados
- "|" Separa el primer elemento de la lista del resto
- "ATOM" Aisla un agente del resto
- listas
- broadcast