import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

changes = 0

# 1. Restore slide 3: Replace topic-visual stage block with original video
# Find the topic-visual block on slide 3
pattern_s3 = re.compile(
    r'<div class="topic-visual light visual-stage".*?</div>\s*</div>\s*</div>\s*</div>',
    re.DOTALL
)
match_s3 = pattern_s3.search(content)
if match_s3:
    video_block = '''<div style="margin-top: 28px; border-radius: 22px; overflow: hidden; background: #000; max-width: 900px; margin-left: auto; margin-right: auto;">
                        <video
                            src="https://oss-global-cdn.unitree.com/static/c2ecf2a5bfbd4835ab6ed442e88c6034.mp4"
                            controls
                            autoplay
                            muted
                            loop
                            playsinline
                            style="width: 100%; display: block;"
                        ></video>
                    </div>'''
    content = content[:match_s3.start()] + video_block + content[match_s3.end():]
    changes += 1
    print("✓ Slide 3: Video restored")
else:
    print("✗ Slide 3: topic-visual stage block not found")

# 2. Remove all remaining topic-visual blocks (inserted by the other AI)
# These are decorative CSS-only blocks that were added before the original content
topic_visual_pattern = re.compile(
    r'\s*<div class="topic-visual [^"]*"[^>]*>.*?</div>(?=\s*<div class="(?:framework-stack|big-num-grid|logic-grid|case-layout|case-grid|matrix-wrap|case-strip|closing-stack|compact-row|value-grid|summary-statement))',
    re.DOTALL
)

count = 0
while True:
    m = topic_visual_pattern.search(content)
    if not m:
        break
    content = content[:m.start()] + '\n' + content[m.end():]
    count += 1

if count > 0:
    changes += count
    print(f"✓ Removed {count} topic-visual decorative blocks")
else:
    print("✗ No remaining topic-visual blocks found to remove")

if changes > 0:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"\nDone! {changes} total changes applied.")
else:
    print("\nNo changes needed.")
