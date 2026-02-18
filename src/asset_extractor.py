import os
from PIL import Image

class SpriteExtractor:
    def __init__(self, sprite_sheet_path, sprite_width, sprite_height, color_key=None):
        self.sprite_sheet_path = sprite_sheet_path
        self.sprite_width = sprite_width
        self.sprite_height = sprite_height
        self.color_key = color_key
        self.sprite_sheet = None

    def load_sprite_sheet(self):
        self.sprite_sheet = Image.open(self.sprite_sheet_path)

    def extract_sprites(self, output_dir):
        if not self.sprite_sheet:
            raise ValueError("Sprite sheet not loaded. Please load the sprite sheet first.")

        os.makedirs(output_dir, exist_ok=True)
        sheet_width, sheet_height = self.sprite_sheet.size

        for y in range(0, sheet_height, self.sprite_height):
            for x in range(0, sheet_width, self.sprite_width):
                sprite = self.sprite_sheet.crop((x, y, x + self.sprite_width, y + self.sprite_height))
                if self.color_key:
                    sprite = self._apply_color_key(sprite)
                sprite_name = f"sprite_{x // self.sprite_width}_{y // self.sprite_height}.png"
                sprite.save(os.path.join(output_dir, sprite_name))

    def _apply_color_key(self, sprite):
        if self.color_key:
            sprite = sprite.convert("RGBA")
            datas = sprite.getdata()
            new_data = []
            for item in datas:
                if item[0:3] == self.color_key:
                    new_data.append((255, 255, 255, 0)) # make the color transparent
                else:
                    new_data.append(item)
            sprite.putdata(new_data)
        return sprite

# Example usage
# extractor = SpriteExtractor('path_to_sprite_sheet.png', 32, 32, color_key=(255, 0, 255))
# extractor.load_sprite_sheet()
# extractor.extract_sprites('output_directory')
