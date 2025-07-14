
# 📱 QR Code Generator

A fast and user-friendly QR code generator built with Python and Pygame! 🐍

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

## 📋 Table of Contents
- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## 🎯 About
This QR Code Generator allows users to create QR codes quickly and easily with a sleek graphical interface. Perfect for generating codes for URLs, text, and more!

## ✨ Features
- 🎨 Beautiful and intuitive Pygame interface
- ⚡ Lightning-fast QR code generation
- 📁 Save QR codes as PNG files
- 🌈 Customizable themes via `config.yaml`
- 🌙 Dark and light mode support
- 📋 Copy QR code to clipboard functionality

## 🚀 Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/tastronaut/qr-code-generator.git
   cd qr-code-generator
   ```

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python qr_gen.py
   ```

## 💻 Usage
```
Welcome to the QR Code Generator!
Enter your text or URL in the input box and click "Generate QR" to create your QR code.
```

## 🎨 Customization
You can customize the appearance of the application by editing the `config.yaml` file. Here’s an example of how to define your themes:

```yaml
dark:
  bg: [45, 45, 45]    # Background color (RGB)
  fg: [224, 224, 224] # Text color
  button_bg: [62, 62, 62] # Button color
  button_fg: [224, 224, 224] # Button text color
  accent: [76, 175, 80]   # Highlight color

light:
  bg: [255, 255, 255]  # Background color (RGB)
  fg: [0, 0, 0]        # Text color
  button_bg: [224, 224, 224] # Button color
  button_fg: [0, 0, 0]  # Button text color
  accent: [33, 150, 243] # Highlight color
```

## 🤝 Contributing
Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest new features
- 🔧 Submit pull requests
- ⭐ Star the repository if you like it!

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎉 Acknowledgments
- Thanks to the QR code generation libraries for making this possible!
- Built with ❤️ and Python

---

**Ready to generate QR codes?** Clone the repo and start creating! 🚀

```bash
git clone https://github.com/tastronaut/qr-code-generator.git
cd qr-code-generator
python qr_gen.py
```

*Have fun generating QR codes!* 📱
