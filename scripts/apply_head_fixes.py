import os, re

updates = {
    'portfolio/index.html': (
        'Portfolio de Adrián Sánchez Yrure. Doble grado en matemáticas e informática con proyectos en ciencia de datos, machine learning y desarrollo web.',
        'Inicio | Adrián Sánchez Yrure'
    ),
    'portfolio/proyectos.html': (
        'Proyectos de software, inteligencia artificial, IoT y análisis de datos desarrollados por Adrián Sánchez Yrure con código fuente y documentación.',
        'Proyectos | Adrián Sánchez Yrure'
    ),
    'portfolio/sobre-mi.html': (
        'Trayectoria, formación técnica, línea de tiempo y habilidades en matemáticas y desarrollo web de Adrián Sánchez Yrure. Perfil y visión profesional.',
        'Sobre mí | Adrián Sánchez Yrure'
    ),
    'portfolio/contacto.html': (
        'Formulario de contacto para propuestas de desarrollo web, ciencia de datos o consultoría tecnológica con Adrián Sánchez Yrure. Respuesta en 24 horas.',
        'Contacto | Adrián Sánchez Yrure'
    )
}

for path, (desc, title) in updates.items():
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    c = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{desc}">', c)
    c = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{desc}">', c)
    c = c.replace('&amp;display=swap', '&display=swap')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print('Updated', path)
