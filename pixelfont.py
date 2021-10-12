import pygame


class PixelFont():  
    _a = [
        "XXX",
        "X X",
        "X X",
        "XXX",
        "X X",
    ]
    _b = [
        "XXX ",
        "X X ",
        "XXXX",
        "X  X",
        "XXXX"
    ]
    _c = [
        "XXX",
        "X  ",
        "X  ",
        "X  ",
        "XXX",
    ]
    _d = [
        "XX ",
        "X X",
        "X X",
        "X X",
        "XX ",
    ]
    _e = [
        "XXX",
        "X  ",
        "XX ",
        "X  ",
        "XXX",
    ]
    _f = [
        "XXX",
        "X  ",
        "XXX",
        "X  ",
        "X  ",
    ]
    _g = [
        "XXX",
        "X  ",
        "X X",
        "X X",
        "XXX",
    ]
    _h = [
        "X X",
        "X X",
        "XXX",
        "X X",
        "X X",
    ]
    _i = [
        "X",
        " ",
        "X",
        "X",
        "X",
    ]
    _j = [
        "  X",
        "  X",
        "  X",
        "X X",
        "XXX",
    ]
    _k = [
        "X X",
        "X X",
        "XX ",
        "X X",
        "X X",
    ]
    _l = [
        "X  ",
        "X  ",
        "X  ",
        "X  ",
        "XXX",
    ]
    _m = [
        "XXXXX",
        "X X X",
        "X X X",
        "X X X",
        "X X X"
    ]
    _n = [
        "XXX",
        "X X",
        "X X",
        "X X",
        "X X"
    ]
    _o = [
        "XXX",
        "X X",
        "X X",
        "X X",
        "XXX"
    ]
    _p = [
        "XXX",
        "X X",
        "XXX",
        "X",
        "X  ",
    ]
    _q = [
        "XXX ",
        "X X ",
        "X X ",
        "X X ",
        "XXXX"
    ]
    _r = [
        "XXX",
        "X X",
        "XX ",
        "X X",
        "X X",
    ]
    _s = [
        "XXX",
        "X  ",
        "XXX",
        "  X",
        "XXX",
    ]
    _t = [
        "XXX",
        " X ",
        " X ",
        " X ",
        " X ",
    ]
    _u = [
        "X X",
        "X X",
        "X X",
        "X X",
        "XXX",
    ]
    _v = [
        "X X",
        "X X",
        "X X",
        "XXX",
        " X ",
    ]
    _w = [
        "X X X",
        "X X X",
        "X X X",
        "X X X",
        "XXXXX",
    ]
    _x = [
        "X X",
        "X X",
        " X ",
        "X X",
        "X X",
    ]
    _y = [
        "X X",
        "X X",
        "XXX",
        " X ",
        " X ",
    ]
    _z = [
        "XXX",
        "  X",
        " X ",
        "X  ",
        "XXX",
    ]
    _1 = [
        "XX",
        " X",
        " X",
        " X",
        " X"
    ]
    _2 = [
        "XXX",
        "  X",
        "XXX",
        "X  ",
        "XXX"
    ]
    _3 = [
        "XXX",
        "  X",
        " XX",
        "  X",
        "XXX"
    ]
    _4 = [
        "X X",
        "X X",
        "XXX",
        "  X",
        "  X"
    ]
    _6 = [
        "X  ",
        "X  ",
        "XXX",
        "X X",
        "Xxx"
    ]
    _7 = [
        "XXX",
        "  X",
        "  X",
        "  X",
        "  X"
    ]
    _8 = [
        "XXX",
        "X X",
        "XXX",
        "X X",
        "XXX"
    ]
    _9 = [
        "XXX",
        "X X",
        "XXX",
        "  X",
        "  X"
    ]
    _exc = [
        "X",
        "X",
        "X",
        " ",
        "X"
    ]
    _spc = [
        "   ",
    ]
    _leters = {
        "a": _a,
        "b": _b,
        "c": _c,
        "d": _d,
        "e": _e,
        "f": _f,
        "g": _g,
        "h": _h,
        "i": _i,
        "j": _j,
        "k": _k,
        "l": _l,
        "m": _m,
        "n": _n,
        "o": _o,
        "p": _p,
        "q": _q,
        "r": _r,
        "s": _s,
        "t": _t,
        "u": _u,
        "v": _v,
        "w": _w,
        "x": _x,
        "y": _y,
        "z": _z,
        "0": _o,
        "1": _1,
        "2": _2,
        "3": _3,
        "4": _4,
        "5": _s,
        "6": _6,
        "7": _7,
        "8": _8,
        "9": _9,
        " ": _spc,
        "!": _exc
    }
    
    def __init__(self, pixel_size, img_path = None, color = None) -> None:
        self.pixel_size = pixel_size
        if img_path:
            self.img = pygame.image.load(img_path).convert_alpha()
            if self.img.get_size() != (pixel_size, pixel_size):
                self.img = pygame.transform.scale(self.img, (pixel_size, pixel_size))
        elif color:
            self.img = pygame.Surface((pixel_size, pixel_size))
            self.img.fill(color)
        else:
            self.img = pygame.Surface((pixel_size, pixel_size))
            self.img.fill("black")
    
    def _pixel_leter (self, leter: list[str]) -> pygame.Surface:
        num_rows = len(leter)
        num_cols = len(leter[0])
        surface = pygame.Surface((num_cols * self.pixel_size, num_rows * self.pixel_size), pygame.SRCALPHA, 32).convert_alpha()

        for row_index, row in enumerate(leter):
            for col_index, element in enumerate(row):
                if element == "X":
                    pos = (col_index * self.pixel_size, row_index * self.pixel_size)
                    surface.blit(self.img, pos)
        return surface

    def pixel_word (self, word: str) -> pygame.Surface:
        surface = None
        for char in word:
            char_source = self._leters.get(char.lower(), None)
            if char_source:
                leter_rows = len(char_source)
                leter_cols = len(char_source[0])
                if surface is None:
                    surface = self._pixel_leter(char_source)
                else:
                    curr_size_x, curr_size_y = surface.get_size()
                    new_size_x = curr_size_x + (leter_cols + 1) * self.pixel_size
                    new_size_y = max(curr_size_y, leter_rows * self.pixel_size)
                    new_pos_x = curr_size_x + self.pixel_size
                    new_surface = pygame.Surface((new_size_x, new_size_y), pygame.SRCALPHA, 32).convert_alpha()
                    new_surface.blit(surface, (0,0))
                    surface = self._pixel_leter(char_source)
                    new_surface.blit(surface, (new_pos_x, 0))
                    surface = new_surface
        return surface    
