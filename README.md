# Validación de Contraseña y Nombre de Usuario

## Este repositorio contiene expresiones regulares para validar contraseñas fuertes y nombres de usuario en aplicaciones web.

### Expresión Regular para Contraseña Fuerte
La expresión regular para validar una contraseña fuerte es la siguiente:

## ^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$

![Contrasena](https://github.com/Majin0328/LeneguajesAutomatas/assets/160747765/1c849ae0-f148-4d9f-b322-1c469f398ffb)

Explicación:

^: Indica el inicio de la cadena.
(?=.*[a-z]): Asegura que la contraseña contenga al menos una letra minúscula.
(?=.*[A-Z]): Asegura que la contraseña contenga al menos una letra mayúscula.
(?=.*\d): Asegura que la contraseña contenga al menos un dígito numérico.
(?=.[@$!%?&]): Asegura que la contraseña contenga al menos un carácter especial de los especificados (@$!%*?&).
[A-Za-z\d@$!%*?&]{8,}$: Especifica que la contraseña puede contener solo letras mayúsculas y minúsculas, dígitos numéricos y los 
caracteres especiales mencionados anteriormente, y debe tener una longitud mínima de 8 caracteres.
$: Indica el final de la cadena.

#Expresión Regular para Nombre de Usuario
La expresión regular para validar un nombre de usuario es la siguiente:

##^[a-zA-Z0-9_-]{3,16}$

![User](https://github.com/Majin0328/LeneguajesAutomatas/assets/160747765/65d33f6e-77af-495b-aae9-a6f02b85af55)

Explicación:

^: Indica el inicio de la cadena.
[a-zA-Z0-9_-]: Permite letras mayúsculas y minúsculas, dígitos, y los caracteres guion medio y bajo.
{3,16}: El nombre de usuario debe tener una longitud de entre 3 y 16 caracteres.
$: Indica el final de la cadena.
