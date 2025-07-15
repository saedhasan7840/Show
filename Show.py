#!/usr/bin/env python3
import os
import sys
import time
import socket
import hashlib
import subprocess
from importlib import import_module

# Constants
PASSWORD = "dzdemonic"
PASSWORD_LINK = ""
STARTUP_LINK = ""
API_URL = "https://dzsmscall-abu-rashids-projects.vercel.app/api/test?phone="
HASH_FILE = "verified_hashes.txt"

# Required modules with their import names and pip names
REQUIRED_MODULES = {
    'requests': 'requests',
    'prompt_toolkit': 'prompt-toolkit',
    'pyfiglet': 'pyfiglet',
    'termcolor': 'termcolor',
    'simple_chalk': 'simple-chalk',
    'halo': 'halo',
    'rich': 'rich',
}

# Auto-install missing modules
def install_modules():
    missing_modules = []
    for module, pip_name in REQUIRED_MODULES.items():
        try:
            import_module(module)
        except ImportError:
            missing_modules.append(pip_name)
    
    if missing_modules:
        print("\033[1;33m⚡ Installing missing dependencies...\033[0m")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade"] + missing_modules,
                                 stdout=subprocess.DEVNULL,
                                 stderr=subprocess.DEVNULL)
            print("\033[1;32m✅ Dependencies installed successfully!\033[0m")
            time.sleep(1)
        except subprocess.CalledProcessError:
            print("\033[1;31m❌ Failed to install dependencies. Try manually with: pip install", " ".join(missing_modules), "\033[0m")
            sys.exit(1)

# Now import all modules after ensuring they're installed
install_modules()

from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.shortcuts import ProgressBar
from pyfiglet import Figlet
from termcolor import colored
from simple_chalk import chalk
from halo import Halo
from rich.console import Console
from rich.panel import Panel
from rich.progress import track
from rich.text import Text
import requests

# Initialize rich console
console = Console()

# Custom Styles
style = Style.from_dict({
    '': '#ff6f00 bold',
    'prompt': '#00ff00 bold',
    'input': '#ffffff bg:#444444',
    'output': '#00ffff',
    'error': '#ff0000 bold',
    'success': '#00ff00 bold',
    'warning': '#ffff00 bold',
    'info': '#00ffff',
})

# ASCII Header with Animation
def animated_header():
    os.system("clear")
    f = Figlet(font='doom')
    print(colored(f.renderText('DZ DEMONIC'), 'red'))
    print(chalk.blue.bold("🔥 ONE OF THE MOST POWERFUL BEAST TOOL 🔥"))
    print(chalk.yellow("━" * 60))

# Custom Box implementation using rich
def create_box(content, title="", color="red"):
    color_map = {
        "red": "red1",
        "green": "green1",
        "yellow": "yellow1",
        "blue": "blue1",
    }
    panel = Panel(
        Text(content, justify="center"),
        title=title,
        border_style=color_map.get(color, "red1"),
        width=60,
        padding=(1, 2)
    )
    console.print(panel)

# IP and Hashing
def get_ip():
    with Halo(text='Fetching your IP address', spinner='dots'):
        try:
            ip = requests.get("https://api.ipify.org").text.strip()
            return ip
        except:
            return socket.gethostbyname(socket.gethostname())

def hash_ip(ip):
    return hashlib.sha256(ip.encode()).hexdigest()

def is_verified(ip_hash):
    if not os.path.exists(HASH_FILE):
        return False
    with open(HASH_FILE, "r") as f:
        return ip_hash in f.read().splitlines()

def save_verified_ip(ip_hash):
    with open(HASH_FILE, "a") as f:
        f.write(ip_hash + "\n")

# Open browser in Termux
def open_link(link):
    os.system(f"xdg-open '{link}' > /dev/null 2>&1")

# Animated Progress Bar
def show_progress():
    console.print("[green]Loading Demon Power...[/green]")
    for _ in track(range(100), description="Initializing..."):
        time.sleep(0.02)

# Send requests with visual feedback
def send_requests(phone):
    console.print("\n[red bold]⚡ INITIATING DEMONIC ATTACK SEQUENCE ⚡[/red bold]")
    print(chalk.yellow("━" * 60))
    
    with Halo(text='Preparing dark magic', spinner='hearts'):
        time.sleep(2)
    
    for i in range(10):
        try:
            response = requests.get(API_URL + phone)
            percent = (i+1) * 10
            bar = "█" * (percent//5) + " " * (20 - (percent//5))
            print(f"\r{chalk.green.bold(f'[{i+1}/10]')} {chalk.blue('[' + bar + ']')} {chalk.yellow(f'{percent}%')} {chalk.green('✔ Request sent')}", end='')
            time.sleep(1)
        except Exception as e:
            print(f"\r{chalk.red.bold(f'[{i+1}/10]')} {chalk.red('✖ Error:')} {chalk.white(str(e))}", end='')
            time.sleep(1)
    print()

# Main logic with enhanced UI
def main():
    try:
        animated_header()
        show_progress()
        
        user_ip = get_ip()
        ip_hash = hash_ip(user_ip)
        
        create_box(f"Your IP: {user_ip}\nHashed: {ip_hash[:8]}...", "IP INFORMATION", "red")
        
        console.print("\n[cyan bold]🔗 Opening the Gates to Telegram Channel...[/cyan bold]")
        with Halo(text='Redirecting', spinner='dots'):
            time.sleep(2)
            open_link(STARTUP_LINK)

        if not is_verified(ip_hash):
            create_box("Access to the demonic powers requires verification", "WARNING", "yellow")
            choice = prompt(HTML('<prompt>🔐 Do you wish to continue? (y/n): </prompt>'), style=style)
            if choice.lower() == 'y':
                console.print("\n[cyan]Opening password portal...[/cyan]")
                open_link(PASSWORD_LINK)
                password = prompt(HTML('<prompt>🔑 Enter the demonic password: </prompt>'), style=style, is_password=True)
                if password != PASSWORD:
                    create_box("INCORRECT PASSWORD - ACCESS DENIED", "ERROR", "red")
                    console.print("\n[red bold]The demon rejects your offering...[/red bold]")
                    return
                save_verified_ip(ip_hash)
                create_box("PASSWORD ACCEPTED - WELCOME TO THE DARK SIDE", "SUCCESS", "green")
            else:
                create_box("COWARDICE DETECTED - EXITING", "WARNING", "yellow")
                return
        else:
            create_box("IP VERIFIED - WELCOME BACK, USER🔥", "SUCCESS", "green")

        phone = prompt(HTML('<prompt>📲 Enter target phone number (e.g., 017xxxxxxxx): </prompt>'), style=style)
        if not phone.isdigit():
            create_box("INVALID NUMBER - MUST CONTAIN DIGITS ONLY", "ERROR", "red")
            return

        console.print("\n[red bold]🔥 PREPARING DEMONIC ASSAULT 🔥[/red bold]")
        print(chalk.yellow("━" * 60))
        
        # Countdown animation
        for i in range(3, 0, -1):
            print(f"\r{chalk.red.bold(f'Launching attack in {i}...')}", end='')
            time.sleep(1)
        print("\r" + " " * 30 + "\r", end='')
        
        send_requests(phone)
        
        # Final animation
        console.print("\n[red bold]⚡ ATTACK COMPLETE ⚡[/red bold]")
        with Halo(text='Cleaning up dark energy', spinner='dots'):
            time.sleep(2)
        
        create_box("MISSION ACCOMPLISHED - DZ DEMON SIGNING OFF", "SUCCESS", "green")
        print(chalk.yellow("━" * 60))
        console.print("[red bold]THE DEMON RETURNS TO THE SHADOWS...[/red bold]")

    except KeyboardInterrupt:
        create_box("DEMONIC RITUAL INTERRUPTED", "WARNING", "yellow")
        console.print("\n[red bold]The demon growls in frustration...[/red bold]")
    except Exception as e:
        console.print(f"[red bold]UNHANDLED ERROR: {str(e)}[/red bold]")
        console.print("\n[red bold]The demon has encountered a problem...[/red bold]")

if __name__ == "__main__":
    main()
