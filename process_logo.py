import os
import base64
from PIL import Image

input_path = r"C:\Users\MC VIP\.gemini\antigravity-ide\brain\7a40afb1-8097-4e69-8be2-38b5984d4a04\.user_uploaded\media_1793080961070.png"
img = Image.open(input_path).convert("RGBA")

# Extract pixels
pixels = list(img.getdata())

# 1. White logo (for dark backgrounds)
white_data = []
# 2. Black/Dark logo (for white backgrounds)
dark_data = []

for item in pixels:
    brightness = max(item[0], item[1], item[2])
    if brightness < 40:
        white_data.append((255, 255, 255, 0))
        dark_data.append((10, 10, 10, 0))
    else:
        alpha = min(255, int(brightness * (255 / 210)))
        white_data.append((255, 255, 255, alpha))
        dark_data.append((15, 15, 15, alpha))

img_white = Image.new("RGBA", img.size)
img_white.putdata(white_data)

img_dark = Image.new("RGBA", img.size)
img_dark.putdata(dark_data)

# Output paths
pub_dir = r"c:\Users\MC VIP\OneDrive\Desktop\SWEAT-Final-Web\frontend\public"
assets_dir = r"c:\Users\MC VIP\OneDrive\Desktop\SWEAT-Final-Web\frontend\src\assets"

os.makedirs(pub_dir, exist_ok=True)
os.makedirs(assets_dir, exist_ok=True)

img_white.save(os.path.join(pub_dir, "sweat-logo.png"), "PNG")
img_white.save(os.path.join(pub_dir, "sweat-logo-white.png"), "PNG")
img_dark.save(os.path.join(pub_dir, "sweat-logo-dark.png"), "PNG")

img_white.save(os.path.join(assets_dir, "sweat-logo.png"), "PNG")
img_dark.save(os.path.join(assets_dir, "sweat-logo-dark.png"), "PNG")

# Also write base64 JS module for zero-latency instant rendering
import io
buf_white = io.BytesIO()
img_white.save(buf_white, format="PNG")
b64_white = base64.b64encode(buf_white.getvalue()).decode("utf-8")

buf_dark = io.BytesIO()
img_dark.save(buf_dark, format="PNG")
b64_dark = base64.b64encode(buf_dark.getvalue()).decode("utf-8")

js_content = f'''// Auto-generated logo data URIs
export const SWEAT_LOGO_WHITE = "data:image/png;base64,{b64_white}";
export const SWEAT_LOGO_DARK = "data:image/png;base64,{b64_dark}";
export default SWEAT_LOGO_WHITE;
'''

with open(os.path.join(assets_dir, "logoBase64.js"), "w", encoding="utf-8") as f:
    f.write(js_content)

print("Generated sweat-logo.png, sweat-logo-white.png, sweat-logo-dark.png, and logoBase64.js!")
