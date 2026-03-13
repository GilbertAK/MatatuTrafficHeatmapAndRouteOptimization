import os
import time
from colorama import Fore, Back, Style, init
from tabulate import tabulate
from engine import MatatuEngine

# Initialize Colorama
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    print(Fore.GREEN + Style.BRIGHT + "="*60)
    print(Fore.YELLOW + Style.BRIGHT + "  🇰🇪 NAIROBI MATATU TRAFFIC HEATMAP - LIVE TELEMETRY")
    print(Fore.GREEN + Style.BRIGHT + "="*60)

def get_status_color(status):
    if status == "HEAVY": return Fore.RED + Style.BRIGHT
    if status == "MODERATE": return Fore.YELLOW
    return Fore.CYAN

def run_console_app():
    engine = MatatuEngine()
    
    try:
        while True:
            clear_screen()
            print_banner()
            
            # Update data
            fleet = engine.update_telemetry()
            metrics = engine.get_heat_metrics()
            
            # 1. Display Route Heatmap
            print(f"\n{Back.BLUE}{Fore.WHITE}  ROUTE ANALYTICS SUMMARY  ")
            
            display_table = []
            for m in metrics:
                color = get_status_color(m['Status'])
                display_table.append([
                    Fore.WHITE + m['Route'],
                    m['Active Matatus'],
                    m['Avg Speed'],
                    color + m['Status'],
                    Fore.MAGENTA + str(m['Heat Index'])
                ])
            
            print(tabulate(display_table, 
                           headers=["ROUTE", "FLEET", "SPEED", "STATUS", "HEAT"], 
                           tablefmt="grid"))

            # 2. Display Individual Matatu GPS Logs
            print(f"\n{Back.BLACK}{Fore.GREEN}  LIVE GPS STREAM (TOP 5)  ")
            for _, matatu in fleet.head(5).iterrows():
                print(f"{Fore.WHITE}{matatu['id']} | "
                      f"{Fore.YELLOW}Pos: {matatu['lat']:.4f}, {matatu['lon']:.4f} | "
                      f"{Fore.CYAN}Spd: {matatu['speed']} km/h")

            print(f"\n{Fore.WHITE}Polling GPS every 1s... {Style.DIM}(Ctrl+C to stop)")
            time.sleep(1)
            
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Simulation stopped.")

if __name__ == "__main__":
    run_console_app()

