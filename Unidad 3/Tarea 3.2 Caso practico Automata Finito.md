# Caso de uso de un Automata Finito

## Verificación de Contraseñas:
En sistemas de inicio de sesión, es esencial asegurar que las contraseñas proporcionadas por los usuarios cumplan con ciertos requisitos de seguridad, como una longitud mínima, la inclusión de caracteres especiales, letras mayúsculas, números, etc. Un autómata finito se puede utilizar para definir y verificar estas reglas de complejidad de contraseña.
Implementación:

#### Definición de Reglas de Verificación:
Se definen las reglas que deben cumplir las contraseñas de los usuarios. Por ejemplo: 
La contraseña debe tener al menos 8 caracteres.
Debe contener al menos una letra mayúscula y una minúscula.
Debe incluir al menos un número y un carácter especial (como @, #, $, etc.).

#### Diseño del Autómata:
Se diseña un autómata finito que represente las reglas de verificación definidas. Cada estado del autómata representa una etapa de verificación de la contraseña, y las transiciones entre estados están determinadas por los caracteres de la contraseña.

#### Implementación del Autómata:
El autómata diseñado se implementa en el sistema de verificación de contraseñas. Esto puede realizarse mediante la codificación de la lógica del autómata en el backend del sistema de inicio de sesión, donde se verifica cada contraseña ingresada por el usuario.

#### Verificación de Contraseñas:
Cuando un usuario intenta iniciar sesión y proporciona una contraseña, esta contraseña se pasa al autómata para su verificación. El autómata procesa la cadena de caracteres de la contraseña, siguiendo las transiciones definidas, y determina si la contraseña cumple con las reglas de verificación. Si la contraseña es válida, se permite el acceso al sistema. Si la contraseña no es válida, se le solicita al usuario que proporcione una contraseña que cumpla con los requisitos de seguridad establecidos.

#### Veamos ahora el diagrama de transicion hecho con fines teoricos:

![image](https://github.com/Majin0328/LeneguajesAutomatas/assets/160747765/47285458-adf9-4c80-84ef-33c205b27dde)

 
