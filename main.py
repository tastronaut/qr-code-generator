import os
import yaml
import qrcode
import pygame
import pyperclip

# Constants
WIDTH, HEIGHT = 500, 650
FONT_SIZE = 24
BUTTON_HEIGHT = 50
BUTTON_WIDTH = 150


class QRGenerator:
    def __init__(self):
        self.load_config()
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("QR Code Generator")
        self.font = pygame.font.Font(None, FONT_SIZE)
        self.input_text = ""
        self.qr_image = None
        self.theme = self.themes["dark"]
        self.run()

    def load_config(self):
        """Load or create config.yaml"""
        self.config_path = os.path.join(os.path.dirname(__file__), "config.yaml")
        self.themes = {
            "dark": {
                "bg": (45, 45, 45),
                "fg": (224, 224, 224),
                "button_bg": (62, 62, 62),
                "button_fg": (224, 224, 224),
                "accent": (76, 175, 80)
            },
            "light": {
                "bg": (255, 255, 255),
                "fg": (0, 0, 0),
                "button_bg": (224, 224, 224),
                "button_fg": (0, 0, 0),
                "accent": (33, 150, 243)
            }
        }

        try:
            with open(self.config_path, 'r') as config_file:
                user_themes = yaml.safe_load(config_file) or {}
                self.themes.update(user_themes)
        except FileNotFoundError:
            self.create_default_config()
        except Exception as e:
            print(f"Using default themes. Error: {e}")

    def create_default_config(self):
        """Create default config.yaml if not exists"""
        default_config = {
            "custom_theme": {
                "bg": (26, 26, 46),
                "fg": (233, 69, 96),
                "button_bg": (22, 33, 62),
                "button_fg": (255, 255, 255),
                "accent": (15, 52, 96)
            }
        }
        with open(self.config_path, 'w') as config_file:
            yaml.dump(default_config, config_file)

    def generate_qr(self):
        """Generate QR code from input text"""
        if self.input_text:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(self.input_text)
            qr.make(fit=True)
            self.qr_image = qr.make_image(fill_color="black", back_color="white")
            self.qr_image.save("qr_code.png")
            print("QR Code generated and saved as qr_code.png")

    def draw_button(self, text, x, y, action=None):
        """Draw a button on the screen"""
        button_rect = pygame.Rect(x, y, BUTTON_WIDTH, BUTTON_HEIGHT)
        pygame.draw.rect(self.screen, self.theme["button_bg"], button_rect)
        pygame.draw.rect(self.screen, self.theme["accent"], button_rect, 2)
        label = self.font.render(text, True, self.theme["button_fg"])
        self.screen.blit(label,
                         (x + (BUTTON_WIDTH - label.get_width()) // 2, y + (BUTTON_HEIGHT - label.get_height()) // 2))
        return button_rect

    def run(self):
        """Main loop"""
        running = True
        while running:
            self.screen.fill(self.theme["bg"])
            input_box = pygame.Rect(50, 50, 400, 50)
            pygame.draw.rect(self.screen, self.theme["button_bg"], input_box)
            label = self.font.render(self.input_text, True, self.theme["fg"])
            self.screen.blit(label, (input_box.x + 5, input_box.y + 5))

            # Draw buttons
            generate_button = self.draw_button("Generate QR", 50, 120, self.generate_qr)
            quit_button = self.draw_button("Quit", 50, 200)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.generate_qr()
                    elif event.key == pygame.K_BACKSPACE:
                        self.input_text = self.input_text[:-1]
                    else:
                        self.input_text += event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if generate_button.collidepoint(event.pos):
                        self.generate_qr()
                    if quit_button.collidepoint(event.pos):
                        running = False

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    QRGenerator()
