LICENSE = """The MIT License (MIT)
Copyright (c) 2021 Abhijeet Srivastav

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute,
sublicense, and/or sell copies of the Software, and to permit persons to whom the Software
is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

USAGE = """"""

INFO = """"""


def DpiAwareness(app):
    """Activates DPI awareness to increase the pixel density of ui to enhance the graphics"""
    """Woks in windows OS only"""
    try:
        import ctypes
        awareness = ctypes.c_int()
        ctypes.windll.shcore.SetProcessDpiAwareness(2)
    except ImportError:
        raise Exception("Unable to import ctypes")


def fromRGB(rgb):
    """translates a rgb tuple of int to a tkinter friendly color code
    """
    r, g, b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'


def ImageConfigurator(path: str, dimension: tuple) -> object:
    """Loads and resizes an image"""
    try:
        from PIL import ImageTk, Image

        image_path = Image.open(path)
        image_resized = image_path.resize(size=dimension)
        image = ImageTk.PhotoImage(image_resized)
        return image
    except ImportError:
        raise Exception("Unable to import PIL")


def WinCenter(screen, screen_width: float, screen_height: float) -> tuple:
    """Centres the Tkinter Window"""
    try:
        import tkinter
        PIXEL_COUNT_WIDTH = screen.winfo_screenwidth()
        PIXEL_COUNT_HEIGHT = screen.winfo_screenheight()
        x_coordinate = (PIXEL_COUNT_WIDTH / 2) - (screen_width / 2)
        y_coordinate = (PIXEL_COUNT_HEIGHT / 2) - (screen_height / 2)
        return x_coordinate, y_coordinate
    except Exception:
        raise Exception('Unable to import tkinter or parameteers invalid!')
