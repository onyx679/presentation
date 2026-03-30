import re

def process_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Image list for insertion
    images = [
        "https://images.unsplash.com/photo-1518770660439-4636190af475?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",  # Tech abstract
        "https://images.unsplash.com/photo-1530124566582-a618bc2615dc?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",  # Gears
        "https://images.unsplash.com/photo-1504917595217-d4ceb2520bbd?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",  # Factory
        "https://images.unsplash.com/photo-1504868584819-eb24ff0e65eb?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",  # Data
        "https://images.unsplash.com/photo-1476820897170-9f11e2f75bd8?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",  # Path
        "https://images.unsplash.com/photo-1500462918059-b1a0cb512f1d?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",  # Hand
        "https://images.unsplash.com/photo-1522071820081-009f0129c71c?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",  # Social
        "https://images.unsplash.com/photo-1501139083538-0139583c060f?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",  # Time
        "https://images.unsplash.com/photo-1519999482648-25049ddd37b1?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",  # Future
        "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"   # Robot
    ]
    
    img_idx = 0
    sections = html.split('<section>')
    new_sections = [sections[0]]
    
    targets = ['<div class="logic-grid">', '<div class="case-layout">', '<div class="value-grid">', '<div class="case-grid"', '<div class="matrix-wrap">', '<div class="framework-stack">', '<div class="case-strip">', '<div class="closing-stack">']

    for section in sections[1:]:
        if '<img' in section or '<video' in section or '<iframe' in section or 'class="hero-question"' in section or 'class="cover-title"' in section:
            new_sections.append(section)
            continue
            
        inserted = False
        for t in targets:
            if t in section:
                url = images[img_idx % len(images)]
                img_idx += 1
                img_html = f'''
                    <div style="margin: 20px 0; border-radius: 18px; overflow: hidden; box-shadow: 0 12px 30px rgba(0,0,0,0.1); height: 260px;">
                        <img src="{url}" alt="illustration" style="width: 100%; height: 100%; object-fit: cover; border: none; margin: 0; display: block;">
                    </div>
                '''
                section = section.replace(t, img_html + t, 1)
                inserted = True
                break
                
        new_sections.append(section)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write('<section>'.join(new_sections))

if __name__ == '__main__':
    process_html()
    print("Images injected successfully!")
