# Sprite Sheet Analysis and Asset Extraction Documentation

## Sprite Sheet Dimensions & Layout

### rpgsprites1_zip__preview.png - Character sprite sheet with 4 directions and multiple animation frames. Extract character frames to assets/sprites/player/.

### goblins3.png - Enemy sprites with green background for color-keying. Extract to assets/sprites/enemies/ with transparency.

### attack_wesnoth.png - Attack icons in grid format. Extract individual icons to assets/sprites/ui/attack_*.png.

### muzzlesmk2_collage_all_clean.png - Particle and effect sprites. Extract effect regions to assets/sprites/effects/.

### grass03.png - Background grass texture for tiling to create map.

## Implementation Notes
- Use Pillow for image processing and color keying, 
- Use numpy for efficient sprite data handling,
- Document each sprite sheet's specific dimensions and grid layout during implementation