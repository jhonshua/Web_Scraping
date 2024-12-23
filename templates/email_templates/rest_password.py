
def template_reset ( password, name) :
    
    html_content = f"""
    <title>¡Bienvenido a [Nombre de tu aplicación]!</title>
    </head>
    <body>
    <div class="container">
        <h1>Estimado <span class="highlight">{name}</span>!</h1>
        <p>Tu clavese se ha reseteado exitosamente.</p>
        <p>Tu contraseña es: <span class="highlight">{password}</span></p>
        <p>Si tienes alguna pregunta, no dudes en contactarnos.</p>
    </div>
    </body>
    """
    return html_content
