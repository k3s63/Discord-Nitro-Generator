# Discord Nitro Generator

This project is a tool to generate and check Discord Nitro codes. The script generates random Nitro codes, checks their validity, and optionally notifies you via a Discord webhook if a valid code is found. Valid codes are saved to a text file for later use.

## Disclaimer 
This tool is only for educational purpose to show the power of python.

## Features

- Generates random Discord Nitro codes.
- Checks the validity of the generated Nitro codes.
- Optionally sends a notification via Discord webhook if a valid code is found.
- Saves valid codes to a text file named `Nitro Codes.txt`.

## Requirements

- Python 3.x
- `discord_webhook` library

## Installation

### On Termux (Android)

1. **Install Termux** from the Google Play Store or F-Droid.
2. **Update package list and install Python**:
    ```bash
    pkg update
    pkg install python
    ```
3. **Install Git**:
    ```bash
    pkg install git
    ```
4. **Clone the repository**:
    ```bash
    git clone https://github.com/k3s63/Discord-Nitro-Generator.git
    cd Discord-Nitro-Generator
    ```
5. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

### On Windows

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/), ensuring that you add Python to your PATH during installation.
2. **Open Command Prompt**:
    - Press `Win + R`, type `cmd`, and press Enter.
3. **Clone the repository**:
    ```cmd
    git clone https://github.com/k3s63/Discord-Nitro-Generator.git
    cd Discord-Nitro-Generator
    ```
4. **Install the required packages**:
    ```cmd
    pip install -r requirements.txt
    ```

### On Kali Linux

1. **Open Terminal**.
2. **Update package list and install Python**:
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip git
    ```
3. **Clone the repository**:
    ```bash
    git clone https://github.com/k3s63/Discord-Nitro-Generator.git
    cd Discord-Nitro-Generator
    ```
4. **Install the required packages**:
    ```bash
    pip3 install -r requirements.txt
    ```

## Usage

1. **Obtain Your Discord Webhook URL**:
   - Create a new webhook in your Discord server settings if you want to use this feature.
   - Note down the webhook URL.

2. **Run the Script**:
    ```bash
    python Discord_nitro_gen.py
    ```

3. **Follow the Prompts**:
   - Enter the number of codes you want to generate and check.
   - Provide your Discord webhook URL if you wish to use it for notifications (you can leave this empty if you don't want to use a webhook).

## License

This project is licensed under the MIT License. You can freely use, modify, and distribute this code with attribution to the original author.

Full license text: [MIT License](https://opensource.org/licenses/MIT)

## Contact

- Developer: K3S63 
- Telegram Channel: [@pythontoolgod](https://t.me/pythontoolgod)
- Support Bot: [@k3s63_support_bot](https://t.me/k3s63_support_bot) 
Note use our support bot to contact us!!
Thank you happy generation!
