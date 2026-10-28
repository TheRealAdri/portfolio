# Portfolio Profesional - Adrián Sánchez Yrure

**Autor:** Adrián Sánchez Yrure  
**Grado:** Doble Grado en Matemáticas aplicadas a la Ciencia de Datos e Ingeniería Informática  
**Universidad:** Universidad Europea (Curso 26/27)  
**URL Pública:** [https://therealadri.github.io/portfolio/](https://therealadri.github.io/portfolio/)

---

## 1. Estructura y Contenido del Sitio

El sitio web está compuesto por cuatro páginas desarrolladas en HTML5 semántico puro y accesible (WCAG 2.1 AA), sin estilos CSS propios ni dependencias de JavaScript:

1. **`index.html` (Inicio):**
   - Cabecera con logotipo SVG (`img/logo.svg`) y menú de navegación accesible.
   - Enlace de salto directo al contenido principal (`#contenido`).
   - Presentación personal con avatar responsive mediante `<picture>` (WebP nativo y PNG de respaldo).
   - Lista de definición de habilidades técnicas (`<dl>`).
   - Tabla cronológica de formación académica con encabezados semánticos (`<table>`, `<caption>`, `<th scope="col">`, `<th scope="row">`).
   - Muestra de proyectos destacados con capturas optimizadas y `loading="lazy"`.
   - Bloque de disponibilidad con fechas estandarizadas (`<time datetime>`).
   - Pie de página con enlaces a redes sociales y correo electrónico mediante iconos SVG en línea accesibles (`aria-hidden="true"`, `fill="currentColor"`).

2. **`proyectos.html` (Proyectos):**
   - Menú de navegación rápida interna a las tres categorías de proyectos.
   - Artículos detallados para cada uno de los 6 proyectos desarrollados (TFG en Deep Learning para IoT, análisis geoespacial de accidentalidad en Madrid, NODARA Hospital, AeroMap, EcoMap e investigación en domótica).
   - Capturas de pantalla optimizadas con dimensiones explícitas (`width` y `height`) y carga diferida (`loading="lazy"`).
   - Flujo metodológico de trabajo expresado en lista ordenada (`<ol>`).
   - Tabla de resumen global con datos de año, categoría y tecnologías principales.

3. **`sobre-mi.html` (Sobre mí):**
   - Sección «Mi trayectoria» con dos párrafos en tono personal y cita célebre en `<blockquote cite="...">` con atribución de autor.
   - Sección «Línea de tiempo» con lista ordenada (`<ol>`) de 6 hitos cronológicos identificados con `<time datetime="...">`.
   - Sección «Multimedia» con vídeo de divulgación técnica incrustado mediante `<iframe title="...">` accesible y reproductor de audio `<audio controls>` con banda sonora libre de derechos.
   - Sección «Preguntas frecuentes» con 5 elementos `<details>` y `<summary>`, con el primero abierto por defecto (`open`).
   - Sección «Nivel técnico» con elementos `<meter>` vinculados a sus respectivos `<label for="...">` para tres competencias clave (Python, SQL y Git).

4. **`contacto.html` (Contacto):**
   - Formulario accesible estructurado en tres bloques lógicos mediante `<fieldset>` y `<legend>`.
   - Validación nativa en el cliente con atributos estándar (`required`, `type`, `minlength`, `maxlength`, `pattern`, `autocomplete`).
   - Opciones accesibles para modalidad de trabajo, servicios requeridos y canal preferente de respuesta.

---

## 2. Fuentes de Contenido Multimedia y Recursos

- **Vídeo Incrustado:**
  - *Título:* "But what is a neural network? | Chapter 1, Deep learning"
  - *Autor / Canal:* Grant Sanderson (3Blue1Brown)
  - *Fuente:* YouTube ([https://www.youtube.com/watch?v=aircAruvnKk](https://www.youtube.com/watch?v=aircAruvnKk))
  - *Propósito:* Divulgación educativa sobre los fundamentos matemáticos del Deep Learning, temática central del TFG del autor.

- **Canción de Audio:**
  - *Título:* "Enthusiast"
  - *Artista:* Tours
  - *Álbum:* Enthusiast
  - *Fuente:* Free Music Archive ([https://freemusicarchive.org/music/Tours/Enthusiast/Tours_-_01_-_Enthusiast/](https://freemusicarchive.org/music/Tours/Enthusiast/Tours_-_01_-_Enthusiast/))
  - *Licencia:* Creative Commons Attribution 3.0 (CC BY 3.0).

- **Iconografía y Tipografía:**
  - Iconos SVG: Simple Icons y Lucide/Heroicons con `fill="currentColor"` y `aria-hidden="true"`.
  - Logotipo del encabezado: Dibujado en SVG nativo (`img/logo.svg`).
  - Tipografía: Fuente "Nunito" de Google Fonts enlazada con directiva `display=swap`.

---

## 3. Optimización, Calidad y Rendimiento

- **Imágenes (`img/`):**
  - Todas las imágenes han sido redimensionadas a su tamaño real de renderizado (máximo 800 px) y convertidas al formato moderno WebP, manteniendo respaldo en PNG.
  - Ninguna imagen supera los 300 KB (el mayor archivo ocupa 238 KB; media inferior a 70 KB).
  - El peso total de la carpeta `img/` es de solo 1,33 MB (reducción superior al 80% respecto a los archivos iniciales).
  - Todas las etiquetas `<img>` y `<picture>` incorporan dimensiones explícitas (`width` y `height`) y directiva `loading="lazy"` para prevenir desplazamientos de diseño acumulados (CLS).
- **Metadatos SEO y Redes Sociales:**
  - Títulos `<title>` exclusivos, con longitud inferior a 60 caracteres y formato `Sección | Adrián Sánchez Yrure`.
  - Descripciones `<meta name="description">` exclusivas por página, con una extensión controlada entre 120 y 155 caracteres.
  - Etiquetas canónicas (`<link rel="canonical">`) hacia la URL definitiva en GitHub Pages.
  - Metadatos Open Graph (`og:title`, `og:description`, `og:image`, `og:url`) con imagen preconfigurada en alta resolución (`1200 × 630 px`).
  - Favicon de 32 × 32 px enlazado en formato PNG.
