import os
from PIL import Image, ImageDraw, ImageFont

img_dir = 'portfolio/img'
os.makedirs(img_dir, exist_ok=True)

# 1. Generate logo.svg
logo_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 48" width="240" height="48" role="img" aria-label="Logotipo de Adrián Sánchez Yrure">
  <rect x="2" y="4" width="40" height="40" rx="8" fill="#0D47A1"/>
  <text x="22" y="25" font-family="system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="18" font-weight="bold" fill="#FFFFFF" text-anchor="middle" dominant-baseline="central">ASY</text>
  <text x="52" y="21" font-family="system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700" fill="#1A202C">Adrián Sánchez</text>
  <text x="52" y="37" font-family="system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="500" fill="#4A5568">Data &amp; Software Engineer</text>
</svg>"""

with open(os.path.join(img_dir, 'logo.svg'), 'w', encoding='utf-8') as f:
    f.write(logo_svg)
print('logo.svg created')

# 2. Generate favicon.png (32x32)
fav = Image.new('RGBA', (32, 32), (0, 0, 0, 0))
fav_draw = ImageDraw.Draw(fav)
fav_draw.rounded_rectangle([1, 1, 30, 30], radius=6, fill='#0D47A1')
try:
    font = ImageFont.truetype('arialbd.ttf', 16)
except:
    font = ImageFont.load_default()
fav_draw.text((16, 15), 'A', font=font, fill='#FFFFFF', anchor='mm')
fav.save(os.path.join(img_dir, 'favicon.png'), 'PNG')
print('favicon.png created (32x32)')

# 3. Generate og-portfolio.png (1200x630)
og = Image.new('RGB', (1200, 630), '#0F172A')
og_draw = ImageDraw.Draw(og)
# Accent border / decorative banner
og_draw.rectangle([0, 0, 1200, 12], fill='#0D47A1')
og_draw.rounded_rectangle([60, 60, 1140, 570], radius=24, outline='#334155', width=2)
# Badge
og_draw.rounded_rectangle([100, 100, 340, 140], radius=8, fill='#1E293B', outline='#38BDF8', width=1)
try:
    font_badge = ImageFont.truetype('arialbd.ttf', 18)
    font_title = ImageFont.truetype('arialbd.ttf', 50)
    font_sub = ImageFont.truetype('arial.ttf', 24)
    font_desc = ImageFont.truetype('arial.ttf', 20)
    font_tag = ImageFont.truetype('arialbd.ttf', 16)
except:
    font_badge = font_title = font_sub = font_desc = font_tag = ImageFont.load_default()

og_draw.text((220, 120), 'PORTFOLIO OFICIAL', font=font_badge, fill='#38BDF8', anchor='mm')
og_draw.text((100, 200), 'Adrián Sánchez Yrure', font=font_title, fill='#F8FAFC')
og_draw.text((100, 270), 'Ingeniería Informática & Matemáticas Aplicadas a la Ciencia de Datos', font=font_sub, fill='#94A3B8')

desc_text = ('Proyectos destacados en Machine Learning, Deep Learning (TFG), telemetría IoT\n'
             'y desarrollo web accesible con conformidad WCAG 2.1 AA.')
og_draw.text((100, 340), desc_text, font=font_desc, fill='#CBD5E1', spacing=10)

# Tags
tags = ['Python & PyTorch', 'Deep Learning IoT', 'Bases de Datos SQL', 'HTML5 Accesible', 'GitHub Pages']
tx = 100
for t in tags:
    bbox = font_tag.getbbox(t)
    tw = bbox[2] - bbox[0] + 28
    og_draw.rounded_rectangle([tx, 450, tx + tw, 488], radius=6, fill='#1E293B', outline='#475569', width=1)
    og_draw.text((tx + tw // 2, 469), t, font=font_tag, fill='#E2E8F0', anchor='mm')
    tx += tw + 14

og_draw.text((100, 525), 'https://therealadri.github.io/portfolio/', font=font_desc, fill='#38BDF8')
og.save(os.path.join(img_dir, 'og-portfolio.png'), 'PNG', optimize=True)
print('og-portfolio.png created (1200x630)')

# 4. Optimize project images and convert to WebP
targets = {
    'images.png': (240, 240), # Avatar (displayed at 120x120)
    'proyecto-accidentalidad.png': (800, 450),
    'proyecto-aeromap.png': (800, 450),
    'proyecto-domotica.png': (800, 533),
    'proyecto-ecomap.png': (800, 446),
    'proyecto-nodara.png': (800, 450),
    'proyecto-tfg.png': (800, 445),
}

for filename, target_size in targets.items():
    filepath = os.path.join(img_dir, filename)
    if not os.path.exists(filepath):
        print(f'Warning: {filepath} not found')
        continue
    
    with Image.open(filepath) as im:
        im_converted = im.convert('RGB')
        im_resized = im_converted.resize(target_size, Image.Resampling.LANCZOS)
        
        # Save WebP version first
        webp_filename = os.path.splitext(filename)[0] + '.webp'
        webp_path = os.path.join(img_dir, webp_filename)
        im_resized.save(webp_path, 'WEBP', quality=85)
        webp_size = os.path.getsize(webp_path)

        # Save optimized PNG fallback (< 250 KB)
        if filename != 'images.png':
            im_png = im_resized.convert('P', palette=Image.Palette.ADAPTIVE, colors=220)
            im_png.save(filepath, 'PNG', optimize=True)
        else:
            im_resized.save(filepath, 'PNG', optimize=True)

        png_size = os.path.getsize(filepath)
        print(f'{filename}: PNG={png_size/1024:.1f} KB, WebP={webp_size/1024:.1f} KB, Size={target_size}')

print('\n--- ALL IMAGES AUDIT ---')
total = 0
for f in sorted(os.listdir(img_dir)):
    p = os.path.join(img_dir, f)
    if os.path.isfile(p):
        kb = os.path.getsize(p) / 1024
        total += kb
        status = 'EXCEEDS 300KB' if kb > 300 else 'PASS (<300KB)'
        print(f'{f:30} {kb:6.1f} KB  [{status}]')

print('-'*50)
print(f'Total img/ size: {total/1024:.2f} MB ({total:.1f} KB)')

