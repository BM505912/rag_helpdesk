# Inicio Sesión
- CUSP / Password
- Olvidaste tu contraseña: Ingresa a OKTA
- versiones parte inferior

- Selecciona Gerente / Asesor (Solo si es gerente da opción de elegir)

# Pantalla principal
Indicadores / Actividad Comercial / Clientes


# Menú Hamburguesa:
- Fecha
- Perfil
    - Nombre completo
    - Correo
    - Número de empleado 
    - Centro de Costos (CC)
- Menú
    - Inicio
    - Contactos
    - Citas
    - Cierrres
    - Indicadores
    - Clientes
- Salir

# Indicadores (tabla)
- Total
    - prospectos
    - referidos
    - Clientes
- Citas Atendidas
- Clientes
- % de efectividad
- Total de EDR enviados
- Apovol
- App Clientes (contador de descargas Profuturo Móvil)

# Actividad Comercial
Número de Empleado y Nombre en parte inferior
Filtro avanzado en esquina superior derecha
    - Tipo de filtro (Nombre / Curp / celular)
    - Dato
    - Habilitar búsqueda Por fecha
        - Rango de fechas
        - Semana Comercial
- Contactos 
    - Prospectos
    - Referidos
        - Parte inferior: Nuevo Prospecto
    - Info del cliente
    - EDR (Puede hacerse en los tres módulos, debería hacerse en Citas)
    - NRP (Captura en Contactos)
        - NRP
        - Nombre de la Empresa
        - Razón social
        - Fecha de registro (actualización máximo 3 veces)
    - Tres puntos
        - Notas
            - Filtro
            - Agregar notas (Nota y color asignado)
        - Agendar cita
            - Datos de contacto 
            - Trámite a realizar (Traspaso/registro)
            - Origen (Asesoría digital / Traspasos PRO)
                - Si es Asesoría digital, el tipo de estudio se envía a landing page

            - Tipo de cita (Presencial / Campo / Remota)
            - Fecha y hora inicio y fin 
            - Estado, Municipio, colonia, calle, número
            - Comentario
        - Eliminar contacto
    - Citas
        - Datos
        - EDR
        - NRP
        - Tres puntos
            - Editar cita
            - Ver histórico
            - Atender cita
            - Notas

## EDR 
- Datos de la prersona
- \+ Nuevo Estudio
    1. Fecha de ingreso a laborar (Solo patronal, distintos tipos)
    2. Tipo de estudio 
        - IMSS (Ley 97 / Ley 73)
        - ISSSTE
        - MIXTO (IMSS / ISSSTE si es mixto)
        - PATRONAL
    3. Datos personales
        - Datos personales
        - RFC (sin homoclave, se debe de ingresar manualmente)
        - Estado civil
        - Edad esposado(a)
    4. Datos de la cuenta
        - NSS (Solo IMSS)
        - Saldo RCV
        - Semanas cotizadas (Solo IMSS)
        - Saldo Básico Cotizado (SBC) Diario
        - Ahorro Solidario (Solo ISSSTE)
            - 0\%
            - 1\%
            - 2\%
        - Ahorro Voluntario Mensual (Flipper/Cantidad: Mínimo \$50)
    5. Generar preestudio
        - Corregir 
        - Enviar 
- Estatus (Siempre debe estar enviado)
- Botón de re-enviar estudio (oculto en scroll) 
Tipo de estudio se calcula automáticamente
- Atender cita
    - Comentario
    - Estatus 
        - Cancelada (regresa a Contactos, debe volver a agendar cita)
        - Seguimiento (regresa a Contactos, debe volver a agendar cita)
        - Cierre (Valida que haya un trámite, solo si existe manda a cierres)
    - Cierres
        - Botón para sincronizar
        - Mismos campos
        - Estatus (Guion Traspasos PRO)
            - Análisis
            - Aceptado
            - Rechazado
            - Pendiente (?)
            Debe estar Aceptado para continuar
        - APOVOL 
            - Autenticación
            - Fondo
                - PROFU PLUS 2
                - PROFU PLUS 12
                - PROFU PLUS DEDUCIBLE
                - PROFU PLUS 65
            - Origen
                - PORTAL CORPORATIVO (Clientes)
                - PROFUTURO MÓVIL
                - ALBA
            - Periodicidad
                - SEMANAL
                - QUINCENAL
                - MENSUAL
                - ÚNICO
            - Monto (\<\$50, $12,000,000\>)
        - App Cliente
    - Eliminados

## Contactos: Nuevo Prospecto 
- Paso 1:
Tipo trabajador
    - IMMSS: 
    - ISSSTE: 
    - MIXTO:
    - PATRONAL (fecha de inicio de cotización en el seguro para identificar tipo de estudio): 
- Paso 2:
    - CURP
- Paso 3:
    - Medio de Contacto (SMS/EMAIL)
- Paso 4:
    - Envío de Token de autenticación
- Paso 5: 
    - Validar Token
- Paso 6: 
    - Info del cliente validada en RENAPO
        - Ingresar correo
        - NSS
        - Nombre de la Empresa (o Número de empleado del analista solo en caso de no certificados)
