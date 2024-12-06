import time
import machine
import framebuf

class SSD1306_I2C:
    def __init__(self, width, height, i2c, addr=0x3C):
        self.width = width
        self.height = height
        self.i2c = i2c
        self.addr = addr  # I2C address, default is 0x3C
        self.buffer = bytearray((width * height) // 8)  # Buffer size for MONO_VLSB
        self.framebuf = framebuf.FrameBuffer(self.buffer, width, height, framebuf.MONO_VLSB)
        self.init_display()

    def init_display(self):
        """Initialize the SSD1306 display with standard configuration commands."""
        init_sequence = [
            0xAE,              # Display off
            0xD5, 0x80,        # Set display clock divide ratio/oscillator frequency
            0xA8, self.height - 1,  # Set multiplex ratio
            0xD3, 0x00,        # Set display offset
            0x40,              # Set start line address
            0x8D, 0x14,        # Enable charge pump
            0xA1,              # Set segment re-map
            0xC8,              # Set COM output scan direction (remapped)
            0xDA, 0x12,        # Set COM pins hardware configuration
            0x81, 0x7F,        # Set contrast control
            0xD9, 0xF1,        # Set pre-charge period
            0xDB, 0x20,        # Set VCOMH deselect level
            0xA4,              # Disable entire display on
            0xA6,              # Set normal display mode
            0xAF               # Display on
        ]
        for cmd in init_sequence:
            self.write_cmd(cmd)

    def write_cmd(self, cmd):
        """Write a command byte to the display."""
        self.i2c.writeto(self.addr, bytearray([0x00, cmd]))

    def write_data(self, buf):
        """Write data to the display."""
        if isinstance(buf, list):
            buf = bytearray(buf)
        self.i2c.writeto(self.addr, b'\x40' + buf)

    def show(self):
        """Write the buffer to the display."""
        for page in range(0, self.height // 8):
            self.write_cmd(0xB0 | page)  # Set page start address
            self.write_cmd(0x00)        # Set lower column start address
            self.write_cmd(0x10)        # Set higher column start address
            self.write_data(self.buffer[page * self.width:(page + 1) * self.width])

    def fill(self, color):
        """Fill the display with a color (0 or 1)."""
        self.framebuf.fill(color)

    def pixel(self, x, y, color):
        """Set a pixel in the buffer."""
        self.framebuf.pixel(x, y, color)

    def text(self, text, x, y, color=1):
        """Draw text on the display."""
        self.framebuf.text(text, x, y, color)

    def rect(self, x, y, w, h, color):
        """Draw a rectangle outline."""
        self.framebuf.rect(x, y, w, h, color)

    def fill_rect(self, x, y, w, h, color):
        """Draw a filled rectangle."""
        self.framebuf.fill_rect(x, y, w, h, color)

    def hline(self, x, y, length, color):
        """Draw a horizontal line."""
        self.framebuf.hline(x, y, length, color)

    def vline(self, x, y, length, color):
        """Draw a vertical line."""
        self.framebuf.vline(x, y, length, color)

    def scroll(self, dx, dy):
        """Scroll the display content by the given amount."""
        self.framebuf.scroll(dx, dy)

    def invert(self, invert):
        """Invert the display (1 for inverted, 0 for normal)."""
        self.write_cmd(0xA6 | (invert & 1))
