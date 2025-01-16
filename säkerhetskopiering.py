import os
import shutil
from datetime import datetime

source = r'Users\Johannes\Desktop\backup'
destination = r'Users\Johannes\OneDrive\Python utveckling\Automatisering\backups'

def backup_files():
    if not os.path.exists(source):
        print(f"Source directory '{source}' not found. Creating it...")
        os.makedirs(source)  # Skapa mappen om den inte finns

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    target = f"{destination}\\{timestamp}"  # Korrekt hantering av sökvägar

    try:
        shutil.copytree(source, target, dirs_exist_ok=True)
        print('Backup completed')
    except Exception as e:
        print(f"An error occurred during backup: {e}")

if __name__ == '__main__':
    backup_files()