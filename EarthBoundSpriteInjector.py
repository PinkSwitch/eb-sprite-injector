import os
import json
import random
from PIL import Image
# this is a dependency that AP already uses but strips from frozen builds, so currently will only work on frozen
# obv set your path correctly lol
palettes = {
    0: {
        (0, 0, 0, 0): 0,
        (240, 240, 240, 255): 1,
        (184, 200, 200, 255): 2,
        (152, 136, 152, 255): 3,
        (0, 176, 128, 255): 4,
        (0, 144, 112, 255): 5,
        (80, 112, 96, 255): 6,
        (168, 208, 240, 255): 7,
        (72, 152, 160, 255): 8,
        (88, 208, 216, 255): 9,
        (200, 0, 160, 255): 10,
        (120, 48, 80, 255): 11,
        (208, 176, 88, 255): 12,
        (184, 136, 0, 255): 13,
        (136, 112, 160, 255): 14,
        (48, 32, 32, 255): 15},

    1: {
        (0, 0, 0, 0): 0,
        (240, 240, 240, 255): 1,
        (208, 208, 208, 255): 2,
        (144, 160, 128, 255): 3,
        (0, 176, 128, 255): 4,
        (0, 144, 112, 255): 5,
        (96, 128, 104, 255): 6,
        (192, 176, 128, 255): 7,
        (192, 160, 104, 255): 8,
        (152, 120, 88, 255): 9,
        (240, 0, 96, 255): 10,
        (144, 0, 48, 255): 11,
        (224, 208, 32, 255): 12,
        (224, 152, 24, 255): 13,
        (80, 80, 200, 255): 14,
        (48, 32, 32, 255): 15},

    2: {
        (0, 0, 0, 0): 0,
        (240, 240, 240, 255): 1,
        (192, 192, 192, 255): 2,
        (152, 152, 152, 255): 3,
        (128, 128, 128, 255): 4,
        (80, 80, 80, 255): 5,
        (160, 192, 192, 255): 6,
        (140, 136, 136, 255): 7,
        (88, 112, 120, 255): 8,
        (56, 80, 80, 255): 9,
        (240, 0, 96, 255): 10,
        (144, 0, 48, 255): 11,
        (160, 136, 240, 255): 12,
        (112, 88, 224, 255): 13,
        (72, 40, 152, 255): 14,
        (48, 32, 32, 255): 15},
    3: {
        (0, 0, 0, 0): 0,
        (240, 240, 176, 255): 1,
        (192, 176, 128, 255): 2,
        (192, 1160, 104, 255): 3,
        (152, 120, 88, 255): 4,
        (128, 96, 64, 255): 5,
        (80, 64, 40, 255): 6,
        (0, 176, 128, 255): 7,
        (0, 144, 112, 255): 8,
        (80, 112, 88, 255): 9,
        (240, 176, 144, 255): 10,
        (240, 144, 144, 255): 11,
        (240, 240, 240, 255): 12,
        (200, 200, 200, 255): 13,
        (240, 0, 96, 255): 14,
        (48, 32, 32, 255): 15},

    4: {
        (0, 0, 0, 0): 0,
        (57, 160, 160, 255): 1,
        (216, 49, 0, 255): 2,
        (233, 209, 0, 255): 3,
        (168, 16, 89, 255): 4,
        (89, 224, 137, 255): 5,
        (0, 153, 1, 255): 6,
        (73, 1, 57, 255): 7,
        (72, 0, 18, 255): 8,
        (209, 208, 74, 255): 9,
        (24, 161, 170, 255): 10,
        (1, 177, 2, 255): 11,
        (248, 32, 59, 255): 12,
        (41, 8, 11, 255): 13,
        (80, 81, 91, 255): 14,
        (25, 193, 123, 255): 15,},

    5: {
        (0, 0, 0, 0): 0,
        (240, 240, 240, 255): 1,
        (200, 200, 200, 255): 2,
        (144, 160, 128, 255): 3,
        (0, 176, 128, 255): 4,
        (0, 144, 112, 255): 5,
        (80, 112, 96, 255): 6,
        (240, 176, 144, 255): 7,
        (200, 152, 120, 255): 8,
        (240, 144, 144, 255): 9,
        (240, 0, 96, 255): 10,
        (144, 0, 48, 255): 11,
        (224, 208, 32, 255): 12,
        (240, 144, 0, 255): 13,
        (112, 112, 240, 255): 14,
        (48, 32, 32, 255): 15},

    6: {
        (0, 0, 0, 0): 0,
        (240, 240, 240, 255): 1,
        (200, 200, 200, 255): 2,
        (144, 160, 128, 255): 3,
        (0, 176, 128, 255): 4,
        (0, 144, 112, 255): 5,
        (80, 112, 96, 255): 6,
        (240, 176, 144, 255): 7,
        (200, 152, 120, 255): 8,
        (240, 144, 144, 255): 9,
        (240, 0, 96, 255): 10,
        (144, 0, 48, 255): 11,
        (224, 208, 32, 255): 12,
        (240, 144, 0, 255): 13,
        (112, 112, 240, 255): 14,
        (48, 32, 32, 255): 15},

    7: {
        (0, 0, 0, 0): 0,
        (240, 248, 248, 255): 1,
        (168, 168, 168, 255): 2,
        (136, 136, 136, 255): 3,
        (152, 20, 88, 255): 4,
        (240, 48, 64, 255): 5,
        (224, 208, 32, 255): 6,
        (240, 144, 0, 255): 7,
        (192, 128, 96, 255): 8,
        (0, 232, 128, 255): 9,
        (40, 160, 112, 255): 10,
        (80, 120, 96, 255): 11,
        (240, 240, 208, 255): 12,
        (192, 208, 152, 255): 13,
        (144, 152, 96, 255): 14,
        (48, 32, 32, 255): 15},
}
# dict of a RBGA tuple to pallet index, you could probably automate this if you really wanted
# but I assume you're not working with infinite colors

files = {
    "Ness": {
        "MainDown.png": 0x11CE40,
        "MainDownWalkFrame.png": 0x11D440,
        "MainUp.png": 0x11CF00,
        "MainSide.png": 0x11CFC0,
        "MainSideWalk.png": 0x11D080,
        "MainUpSide.png": 0x11D2C0,
        "MainUpSideWalk.png": 0x11D380,
        "MainDownSide.png": 0x11D140,
        "MainDownSideWalk.png": 0x11D200,

        "MainDownBot.png": 0x11C780,
        "MainDownWalkFrameBot.png": 0x11CD80,
        "MainUpBot.png": 0x11C840,
        "MainSideBot.png": 0x11C900,
        "MainSideWalkBot.png": 0x11C9C0,
        "MainUpSideBot.png": 0x11CC00,
        "MainUpSideWalkBot.png": 0x11CCC0,
        "MainDownSideBot.png": 0x11CA80,
        "MainDownSideWalkBot.png": 0x11CB40,

        "GhostDown.png": 0x143480,
        "GhostUp.png": 0x143540,
        "GhostSide.png": 0x143600,

        "ClimbLadder.png": 0x152900,
        "ClimbRope.png": 0x14BFE0,
        "ClimbRopeFrame.png": 0x14C0A0,

        "BikeUp.png": 0x110300,
        "BikeSide.png": 0x110600,
        "BikeSidePedal.png": 0x110900,
        "BikeDown.png": 0x110000,
        "BikeUpSide.png": 0x111200,
        "BikeUpSidePedal.png": 0x111500,
        "BikeDownSide.png": 0x110C00,
        "BikeDownSidePedal.png": 0x110F00,

        "TinyDown.png": 0x14B9E0,
        "TinySide.png": 0x14BA60,
        "TinySideWalk.png": 0x14BAE0,

        "PajamaUp.png": 0x11C180,
        "PajamaSide.png": 0x11C240,
        "PajamaSideWalk.png": 0x11C300,
        "PajamaDown.png": 0x11C0C0,
        "PajamaWalkFrame.png": 0x11C6C0,
        "PajamaUpSide.png": 0x11C540,
        "PajamaUpSideWalk.png": 0x11C600,
        "PajamaDownSide.png": 0x11C3C0,
        "PajamaDownSideWalk.png": 0x11C480,

        "PhotoPose.png": 0x152A80,
        "BrokenBot.png": 0x151E80,
        "LieDown.png": 0x1529C0,
        "Surprised.png": 0x152540
    },
    "Paula": {
        "MainDown.png": 0x120C00,
        "MainUp.png": 0x120CC0,
        "MainSide.png": 0x120D80,
        "MainSideWalk.png": 0x120E40,
        "MainUpSide.png": 0x121080,
        "MainUpSideWalk.png": 0x121140,
        "MainDownSide.png": 0x120F00,
        "MainDownSideWalk.png": 0x120FC0,

        "GhostDown.png": 0x143240,
        "GhostUp.png": 0x143300,
        "GhostSide.png": 0x1433C0,

        "ClimbLadder.png": 0x152840,
        "ClimbRope.png": 0x14BE60,
        "ClimbRopeFrame.png": 0x14BF20,

        "TinyDown.png": 0x14B860,
        "TinySide.png": 0x14B8E0,
        "TinySideWalk.png": 0x14B960,

        "LieDown.png": 0x152240,
        "Surprised.png": 0x152480
    },
    "Jeff": {
        "MainDown.png": 0x120600,
        "MainUp.png": 0x1206C0,
        "MainSide.png": 0x120780,
        "MainSideWalk.png": 0x120840,
        "MainUpSide.png": 0x120A80,
        "MainUpSideWalk.png": 0x120B40,
        "MainDownSide.png": 0x120900,
        "MainDownSideWalk.png": 0x1209C0,

        "GhostDown.png": 0x143000,
        "GhostUp.png": 0x1430C0,
        "GhostSide.png": 0x143180,

        "ClimbLadder.png": 0x152780,
        "ClimbRope.png": 0x14BCE0,
        "ClimbRopeFrame.png": 0x14BDA0,

        "TinyDown.png": 0x14B6E0,
        "TinySide.png": 0x14B760,
        "TinySideWalk.png": 0x14B7E0,
        
        "LieDown.png": 0x152180,
        "Surprised.png": 0x1523C0
    },
    "Poo": {
        "MainDown.png": 0x120000,
        "MainUp.png": 0x1200C0,
        "MainSide.png": 0x120180,
        "MainSideWalk.png": 0x120240,
        "MainUpSide.png": 0x120480,
        "MainUpSideWalk.png": 0x120540,
        "MainDownSide.png": 0x120300,
        "MainDownSideWalk.png": 0x1203C0,

        "GhostDown.png": 0x142DC0,
        "GhostUp.png": 0x142E80,
        "GhostSide.png": 0x142F40,

        "ClimbLadder.png": 0x1526C0,
        "ClimbRope.png": 0x14BB60,
        "ClimbRopeFrame.png": 0x14BC20,

        "TinyDown.png": 0x14B560,
        "TinySide.png": 0x14B5E0,
        "TinySideWalk.png": 0x14B660,
        
        "LieDown.png": 0x1520C0,
        "Surprised.png": 0x152300,
        "Meditate.png": 0x14B1A0
    }
}

sprite_tables = {
    "Ness": [
        0x2F1A82, # Main
        0x2F1B4F, # Pajamas/Magicant
        0x2F1B26, # Robot
        0x2F1B78, # Bike
        0x2F1BA1, # Dead
        0x2F1C97, # Photo
        0x2F1CC9, # Lying down
        0x2F1CDF, # Ladder
        0x2F1D46, # Rope
        0x2F1DEC, # Small
        0x2F3D87, # Surprise
        0x2F4994 # Broken robot
    ],
    "Paula": [
        0x2F1AAB, # Main
        0x2F1BCA, # Dead
        0x2F4334, # Lying down
        0x2F1CFB, # Ladder
        0x2F1D5F, # Rope
        0x2F1E15, # Small
        0x2F3DA3 # Surprised
    ],
    "Jeff": [
        0x2F1AD4, # Main
        0x2F1BF3, # Dead
        0x2F434D, # Lying down
        0x2F1D14, # Ladder
        0x2F1D78, # Rope
        0x2F1E3E, # Small
        0x2F3DBC # Surprised
    ],
    "Poo": [
        0x2F1AFD, # Main
        0x2F1C1C, # Dead
        0x2F4366, # Lying down
        0x2F1D2D, # Ladder
        0x2F1D91, # Rope
        0x2F1E67, # Small
        0x2F3DD5 # Surprised
    ]
}

spr_palettes = [
    0x10,
    0x12,
    0x14,
    0x16,
    0x18,
    0x1A,
    0x1C,
    0x1E
]

big_sprites = [
    "BikeUp.png",
    "BikeSide.png",
    "BikeSidePedal.png",
    "BikeDown.png",
    "BikeUpSide.png",
    "BikeUpSidePedal.png",
    "BikeDownSide.png",
    "BikeDownSidePedal.png"
]

small_sprites = [
    "TinyDown.png",
    "TinySide.png",
    "TinySideWalk.png",
]

horizontal_sprites = [
    "BrokenBot.png",
    "LieDown.png"
]

def list_to_byte(value: list[int]) -> int:  # from https://stackoverflow.com/a/27165675
    return sum(2**i for i, v in enumerate(reversed(value)) if v)


def flats_to_4bpp(flat: list[int]) -> list[list[int]]:
    """
    Takes a 64 size list of 0-15 index pallet pointers for an 8x8 pixel image
    and transforms it to a list of list of bits in the 4bpp packed format
    """
    # assuming 8x8
    return [
        [
            (flat[row*8+column] >> planepair+offset) & 0b1
            # find the pixel by row*width + column
            # bitshift by the planepair starting index + the current offset in the pair
            # mask down to one bit
            for column in range(8)  # for each column in the image
        ]
        for planepair in range(0, 4, 2)  # for each bitplane skipping every other
        for row in range(8)  # for each row in the image
        for offset in range(2)  # for each bitplane pair
    ]


def pil_to_list_of_4bpp(img: Image, pallet: dict[tuple[int, int, int, int], int]):
    """
    Takes a PIL.Image object and a lookup pallet of (R, G, B, A) to pallet index,
    splits the image into 8x8 chunks (left to right top to bottom),
    and outputs a list of objects per chunk,
    where the chunk object is a list of byte representations,
    where the byte representations are a list of 0-1 ints
    """
    height, width = img.height, img.width
    assert not (height % 8 + width % 8), f"chosen image was {height}x{width}, both directions need to be divisible by 8"
    coord_list = []
    for h in range(0, height, 8):
        for w in range(0, width, 8):
            coord_list.append([(w+x, h+y) for y in range(8) for x in range(8)])
    for coords in coord_list:
        for coordinate in coords:
            if img.getpixel(coordinate) not in pallet and img.getpixel(coordinate):
                raise ValueError(f"ERROR! Pixel at {coordinate} not in selected palette! Sprite will not be overwritten.")
    flats = [[pallet[img.getpixel(coord)] for coord in coords] for coords in coord_list]
    return [flats_to_4bpp(flat) for flat in flats]

def inject_sprite(chosen_sprite, character, base_rom, palette):
    pallet = palettes[palette]
    for sprite in files[character]:
        mega_list = []
        FILE_PATH = os.path.join(chosen_sprite, sprite)
        if not os.path.isfile(FILE_PATH):
            print(f"{FILE_PATH} missing. Sprite will not be overwritten.")
            continue

        img = Image.open(FILE_PATH)
        if sprite in big_sprites:
            sprite_size = (32, 48)
        elif sprite in small_sprites:
            sprite_size = (16, 16)
        elif sprite in horizontal_sprites:
            sprite_size = (24, 16)
        else:
            sprite_size = (16, 24)

        with open(base_rom, "r+b") as file:
            for address in sprite_tables[character]:
                file.seek(address)
                file.write(bytes([spr_palettes[palette]]))

        if img.size != sprite_size:
            print(f"ERROR! Sprite {sprite} uses incorrect dimensions! Sprite is {img.size}, needs to be {sprite_size}. Sprite will not be overwritten.")
            continue

        try:
            for chunk in pil_to_list_of_4bpp(img, pallet):
                output = [list_to_byte(i) for i in chunk]
                mega_list += output
        except ValueError as e:
            print(e)
            print(f"Error with {sprite}")
            continue

        # Write the output to the ROM at the specified address
        with open(base_rom, "r+b") as file:
            file.seek(files[character][sprite])
            file.write(bytearray(mega_list))


base_rom = input("Input the name of your EarthBound ROM file.\n")

character = ""
valid_chars = ["Ness", "Paula", "Jeff", "Poo"]


if not os.path.exists(base_rom):
    raise FileNotFoundError(f"Error: ROM '{base_rom}' not found.")

with open(base_rom, 'rb') as file:
    data = file.read()
while True:
    while character not in valid_chars and character != "Null":
        character = input("Input which character you would like to inject a sprite for. Options are: \n[Ness], [Paula], [Jeff], [Poo]\n")
        if character not in valid_chars:
            print("ERROR: Character is invalid.")

    # Open and load the sprites.json file
    with open("sprites.json", "r") as file:
        sprites = json.load(file)

    # Get the list of sprites for the selected character
    character_sprites = sprites.get(character, [])
    sprites = list(character_sprites.keys())
    if sprites:
        print(f"Found {len(sprites)} sprite entries for {character}. Input your sprite or -r for random.")
    else:
        raise FileNotFoundError(f"Error! No loaded sprite entries for {character}!")

    chosen_sprite = ""
    while chosen_sprite not in sprites or chosen_sprite == "":
        if chosen_sprite == "-r":
            chosen_sprite = random.choice(sprites)
            break

        elif chosen_sprite not in sprites and chosen_sprite != "":
            print("Input not a valid sprite.")
        chosen_sprite = input()

    palette = character_sprites[chosen_sprite]
    if palette > 7:
        print(f"Error! {chosen_sprite} has palette out of range. Palette must be 0-7.")
        continue
    inject_sprite(chosen_sprite, character, base_rom, palette)
    print("Sprite injected successfully!")
    character = ""


# ness base palette is 1A