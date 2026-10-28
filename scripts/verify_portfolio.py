import os, re
from html.parser import HTMLParser

pages = ['index.html', 'proyectos.html', 'sobre-mi.html', 'contacto.html']
base_dir = 'portfolio'

print('=' * 60)
print('PORTFOLIO AUDIT REPORT')
print('=' * 60)

all_passed = True

for page in pages:
    path = os.path.join(base_dir, page)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    print(f'\n--- Checking {page} ---')

    # 1. Title check
    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
    if title_match:
        title = title_match.group(1)
        t_len = len(title)
        t_ok = t_len < 60 and 'Adrián Sánchez Yrure' in title
        print(f"Title ({t_len} chars): '{title}' -> {'OK' if t_ok else 'FAIL'}")
        if not t_ok: all_passed = False
    else:
        print('Title: MISSING -> FAIL')
        all_passed = False

    # 2. Meta description check
    desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE)
    if desc_match:
        desc = desc_match.group(1)
        d_len = len(desc)
        d_ok = 120 <= d_len <= 155
        print(f"Description ({d_len} chars): '{desc}' -> {'OK' if d_ok else 'FAIL'}")
        if not d_ok: all_passed = False
    else:
        print('Description: MISSING -> FAIL')
        all_passed = False

    # 3. Canonical check
    can_match = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']', content, re.IGNORECASE)
    if can_match:
        can_url = can_match.group(1)
        print(f"Canonical URL: '{can_url}' -> OK")
    else:
        print('Canonical: MISSING -> FAIL')
        all_passed = False

    # 4. Open Graph check
    og_title = re.search(r'<meta\s+property=["\']og:title["\']\s+content=["\'](.*?)["\']', content)
    og_desc = re.search(r'<meta\s+property=["\']og:description["\']\s+content=["\'](.*?)["\']', content)
    og_img = re.search(r'<meta\s+property=["\']og:image["\']\s+content=["\'](.*?)["\']', content)
    og_url = re.search(r'<meta\s+property=["\']og:url["\']\s+content=["\'](.*?)["\']', content)
    og_ok = og_title and og_desc and og_img and og_url
    print(f"Open Graph tags (title, desc, image, url): {'OK' if og_ok else 'FAIL'}")
    if not og_ok: all_passed = False

    # 5. Favicon check
    fav_match = re.search(r'<link\s+rel=["\']icon["\']\s+type=["\']image/png["\']\s+href=["\'](.*?)["\']', content)
    print(f"Favicon link: {'OK' if fav_match else 'FAIL'}")
    if not fav_match: all_passed = False

    # 6. Google Fonts check with display=swap
    font_match = re.search(r'fonts\.googleapis\.com.*?[?&]display=swap', content)
    print(f"Google Fonts with display=swap: {'OK' if font_match else 'FAIL'}")
    if not font_match: all_passed = False

    # 7. No meta keywords check
    kw_match = re.search(r'<meta\s+name=["\']keywords["\']', content, re.IGNORECASE)
    print(f"No meta keywords: {'OK' if not kw_match else 'FAIL (meta keywords present!)'}")
    if kw_match: all_passed = False

    # 8. No style attributes check
    style_match = re.search(r'\sstyle=["\']', content, re.IGNORECASE)
    print(f"No inline style attributes: {'OK' if not style_match else 'FAIL (style attr found!)'}")
    if style_match: all_passed = False

    # 9. Header logo SVG check
    logo_match = re.search(r'<img\s+src=["\']img/logo\.svg["\']\s+alt=["\'].*?["\']\s+width=["\']\d+["\']\s+height=["\']\d+["\']', content)
    print(f"Header logo SVG with width and height: {'OK' if logo_match else 'FAIL'}")
    if not logo_match: all_passed = False

    # 10. Footer inline SVGs check
    gh_svg = 'fill="currentColor"' in content and 'aria-hidden="true"' in content
    print(f"Footer SVGs with aria-hidden and currentColor: {'OK' if gh_svg else 'FAIL'}")
    if not gh_svg: all_passed = False

    # 11. Skip link check
    skip_match = re.search(r'<a\s+href=["\']#contenido["\']>Saltar al contenido</a>', content)
    main_match = re.search(r'<main\s+id=["\']contenido["\']\s+tabindex=["\']-1["\']>', content)
    skip_ok = skip_match and main_match
    print(f"Skip link and target main: {'OK' if skip_ok else 'FAIL'}")
    if not skip_ok: all_passed = False

print('\n' + '=' * 60)
print(f"OVERALL AUDIT RESULT: {'ALL PASS (100%)' if all_passed else 'SOME CHECKS FAILED'}")
print('=' * 60)
