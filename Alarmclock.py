import datetime
import time
import os
import platform

def play_sound():
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(1000, 1000)  # Beep at 1000 Hz for 1000 ms
    else:
        duration = 1  # seconds
        freq = 440  # Hz
        os.system(f'play -nq -t alsa synth {duration} sine {freq}')

def set_alarm():
    while True:
        alarm_time = input("Enter the time for the alarm (HH:MM, 24-hour format): ")
        try:
            valid_time = datetime.datetime.strptime(alarm_time, "%H:%M")
            return valid_time.time()
        except ValueError:
            print("Invalid time format. Please try again.")

def main():
    alarm_time = set_alarm()
    print(f"Alarm is set for {alarm_time}.")
    
    while True:
        current_time = datetime.datetime.now().time().replace(second=0, microsecond=0)
        if current_time == alarm_time:
            print("Alarm time! Wake up!")
            play_sound()
            break
        time.sleep(1)

if __name__ == "__main__":
    main()
