def template_new_account (email, password, name) :
    
    html_content = f"""
    <title>¡Bienvenido a [Nombre de tu aplicación]!</title>
    </head>
    <body>
    <div class="container">
        <h1>¡Bienvenido a [Nombre de tu aplicación], <span class="highlight">{name}</span>!</h1>
        <p>Tu cuenta se ha creado exitosamente.</p>
        <p>Tu usuario es: <span class="highlight">{email}</span></p>
        <p>Tu contraseña es: <span class="highlight">{password}</span></p>
        <p>Si tienes alguna pregunta, no dudes en contactarnos.</p>
    </div>
    </body>
    """
    return html_content

