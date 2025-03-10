import time
import random

def get_heart_rate():
    """Simulate heart rate readings (between 60-120 bpm)."""
    return random.randint(60, 120)

def main():
    print("Starting heart rate monitoring...")

    try:
        while True:
            heart_rate = get_heart_rate()
            print(f"Current heart rate: {heart_rate} bpm")
            # Placeholder for sending data to server (we'll add it later)
            time.sleep(5)  # Simulate reading every 5 seconds
    except KeyboardInterrupt:
        print("Monitoring stopped.")

if __name__ == "__main__":
    main()
