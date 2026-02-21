from collections import Counter
from sys import argv
from pathlib import Path

def parse_log_line(line: str) -> dict:
    parts = line.strip().split()
    return {
    "date": parts[0],
    "time": parts[1],
    "level": parts[2],
    "message": " ".join(parts[3:])
    }
    
def load_logs(file_path: str) -> list:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return [
                parse_log_line(line) 
                for line in file
                if line.strip()]
            
    except FileNotFoundError:
        print("File not found")
        return []
    except (IndexError, ValueError):
        print("File format is incorrect")
        return []
    
def count_logs_by_level(logs: list) -> dict:
    return Counter(log["level"] for log in logs)

def filter_logs_by_level(logs: list, level: str) -> list:
    return list(
        filter(lambda log: log["level"].lower() == level.lower(), 
               logs)
    )
    
def display_log_counts(counts: dict):
    print(f"{'Рівень логування':<18} | {'Кількість':<10}")
    print("-" * 18 + "-+-" + "-" * 10)
    for level, count in counts.items():
        print(f"{level:<18} | {count:<10}")
        
def main():
    if len(argv) < 2:
        print("Usage: python main.py <log_file_path> [level]")
        return

    file_path = Path(argv[1])
    
    if not file_path.exists():
        print("Path does not exist")
        return
    
    level = argv[2] if len(argv) > 2 else None

    logs = load_logs(str(file_path))
    if not logs:
        print("No logs found")
        return None
    
    logs_counts = count_logs_by_level(logs)

    display_log_counts(logs_counts)

    if level:
        filtered = filter_logs_by_level(logs, level)
        print(f"\nДеталі логів для рівня '{level.upper()}':")
        if not filtered:
            print("Записів цього рівня не знайдено.")
        else:
            for log in filtered:
                print(f"{log['date']} {log['time']} - {log['message']}")

        
if __name__ == "__main__":
    main()