import os
from html.parser import HTMLParser

class StrictHTMLValidator(HTMLParser):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.tag_stack = []
        self.errors = []
        self.ids = set()
        self.void_tags = {
            'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input',
            'link', 'meta', 'param', 'source', 'track', 'wbr'
        }

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        # Check lowercase tag
        if tag != tag.lower():
            self.errors.append(f"Tag <{tag}> should be lowercase")
        # Check attributes
        for k, v in attrs:
            if k != k.lower():
                self.errors.append(f"Attribute '{k}' on <{tag}> should be lowercase")
        # Check duplicate ID
        if 'id' in attrs_dict:
            el_id = attrs_dict['id']
            if el_id in self.ids:
                self.errors.append(f"Duplicate id '{el_id}' found")
            self.ids.add(el_id)
        # Check void tags
        if tag not in self.void_tags:
            self.tag_stack.append(tag)

    def handle_endtag(self, tag):
        if tag in self.void_tags:
            self.errors.append(f"Void tag <{tag}> should not have a closing tag </{tag}>")
            return
        if not self.tag_stack:
            self.errors.append(f"Unexpected closing tag </{tag}> with empty stack")
            return
        last_tag = self.tag_stack.pop()
        if last_tag != tag:
            self.errors.append(f"Mismatched closing tag </{tag}>, expected </{last_tag}>")

    def validate_file(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        self.feed(content)
        if self.tag_stack:
            self.errors.append(f"Unclosed tags at EOF: {self.tag_stack}")
        return self.errors

pages = ['portfolio/index.html', 'portfolio/proyectos.html', 'portfolio/sobre-mi.html', 'portfolio/contacto.html']
total_errors = 0
for p in pages:
    validator = StrictHTMLValidator(p)
    errs = validator.validate_file(p)
    if errs:
        print(f"FAILED {p}:")
        for e in errs:
            print(f"  - {e}")
        total_errors += len(errs)
    else:
        print(f"PASSED {p}: 0 structural errors, all tags balanced, all IDs unique.")

if total_errors == 0:
    print("\nALL HTML FILES 100% VALID!")
