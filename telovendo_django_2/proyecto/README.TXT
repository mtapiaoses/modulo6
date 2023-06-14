Admin

En este fragmento de código, estamos "registrando" 
los modelos PerfilUsuario y Proveedores en el panel 
de administración de Django. Esto permite que podamos
administrar y controlar fácilmente dichos modelos 
desde la interfaz del panel de administración,
como si fuera una herramienta para el jefe. Una
vez que los modelos están registrados, podemos 
realizar acciones como ver, crear, editar y eliminar
instancias de esos modelos directamente desde el panel
de administración, sin tener que meter mano al código
ni complicarnos la vida. Es como tener el poder en 
nuestras manos para controlar esos modelos en nuestra aplicación


Urls

admin/: Esta ruta es para acceder a la interfaz 
de administración de Django, donde puedes gestionar los datos de tu aplicación.

'' (ruta raíz): Esta ruta se asigna a la función lanza_inicio y representa la página 
de inicio de tu aplicación.perfiles/: Esta ruta se asigna a la función perfil_usuario
 y representa la página donde se muestran los perfiles de usuario.

perfil_usuario/<int:id_entrada>: Esta ruta se asigna a la función ingresar_perfil 
y se utiliza para ingresar a un perfil de usuario específico. El parámetro <int:id_entrada> 
indica que se espera un entero como identificador del perfil.

pasos/: Esta ruta se asigna a la función pasos y representa la página que muestra los pasos 
necesarios para realizar alguna tarea en tu aplicación.

proveedores/: Esta ruta se asigna a la función registro_proveedores y representa la página 
donde se puede registrar un nuevo proveedor.

lista_proveedores/: Esta ruta se asigna a la función lista_proveedores y muestra la lista 
de proveedores registrados en tu aplicación.

pasos_formulario/: Esta ruta se asigna a la función pasos_formulario y representa la página 
que muestra los pasos a seguir para completar un formulario.

login/: Esta ruta se asigna a la vista basada en clase Login_Usuario y representa la página 
de inicio de sesión de usuario.

logout/: Esta ruta se asigna a la vista basada en clase LogoutView y se utiliza para cerrar 
la sesión de usuario.

logueo_exitoso/: Esta ruta se asigna a la función logueo_exitoso y representa la página que 
se muestra después de un inicio de sesión exitoso. Se requiere que el usuario esté autenticado para acceder a esta página.


Forms 

ProveedoresForm: Este formulario se crea utilizando la 
clase ModelForm de Django. Está asociado al modelo
 Proveedores y define los campos que se mostrarán 
 en el formulario. En este caso, se incluyen los campos 
 'nombre', 'razon_social', 'telefono', 'email' y 'rut'
  del modelo Proveedores. Este formulario se utiliza 
  para crear o editar instancias de proveedores 
  en la base de datos.

FormularioLogin: Este formulario se crea utilizando 
la clase Form de Django. No está vinculado a 
un modelo específico, ya que se utiliza 
para recopilar datos de inicio de sesión 
de los usuarios. Tiene dos campos, 'usuario'
 y 'password', que se representan como campos 
 de texto en la interfaz. El campo 'password'
  utiliza un widget especial PasswordInput 
  para ocultar los caracteres ingresados.

Readme 

lista_proveedores: Esta función recupera todos 
los proveedores de la base de datos y los pasa
 a la plantilla "lista_proveedores.html" para mostrarlos.

saludo: Esta función simplemente renderiza
 la plantilla "pasos_g2.html".

perfil_usuario: Recupera todos los perfiles
 de usuario de la base de datos y los pasa
  a la plantilla "perfiles.html" para mostrarlos.

ingresar_perfil: Recupera un perfil de usuario
 específico de la base de datos según el ID proporcionado, y lo pasa a la plantilla "perfil_usuario.html" para mostrarlo.

pasos: Renderiza la plantilla "pasos_g3.html".

registro_proveedores: Esta función maneja la 
creación de nuevos proveedores. Si se envía una solicitud POST con datos válidos, se guarda el formulario y se redirige a la página de lista de proveedores. Si es una solicitud GET, se muestra el formulario vacío.

pasos_formulario: Renderiza la plantilla
 "pasos_g4.html".

Login_Usuario: Es una clase basada 
en vista que maneja el inicio de sesión de usuarios. 
Al recibir una solicitud GET, muestra el formulario
 de inicio de sesión. Al recibir una solicitud POST,
  verifica las credenciales proporcionadas, autentica 
  al usuario y lo redirige a la página de éxito de 
  inicio de sesión.

logout_view: Cierra la sesión del usuario actual y 
redirige al formulario de inicio de sesión.

logueo_exitoso: Recupera el perfil del usuario actual 
y lo pasa a la plantilla "logueo_exitoso.html" para mostrarlo.

lanza_inicio: Renderiza la plantilla "inicio.html".


Models

PerfilUsuario: El modelo "PerfilUsuario" representa el perfil 
de un usuario en una aplicación. Este modelo almacena información
 adicional sobre cada usuario, como su edad, número de teléfono,
  dirección y ciudad. Proporciona una manera de extender los datos 
  básicos de un usuario y guardar detalles personalizados según sea necesario.

Proveedores: El modelo "Proveedores" representa a los proveedores 
que colaboran con una aplicación. En este modelo se guarda 
información relevante sobre cada proveedor, como su nombre, 
número de identificación (RUT), dirección de correo electrónico,
 número de teléfono y razón social. Permite mantener un registro
  organizado de los proveedores y acceder a sus detalles cuando sea necesario.

Incluir la apps

Se incluye 'app' en la lista INSTALLED_APPS para que Django reconozca 
y cargue la aplicación personalizada en el proyecto, permitiendo su 
funcionamiento adecuado al acceder a sus componentes, como modelos, vistas y plantillas.
