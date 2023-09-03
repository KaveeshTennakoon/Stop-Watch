import tkinter as tk
from time import time

class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.root.geometry("300x200")
        
        self.running = False
        self.start_time = None
        self.elapsed_time = 0
        self.lap_times = []
        self.lap_count = 0  # To keep track of the lap count

        self.time_label = tk.Label(root, text="00:00.000", font=("Helvetica", 36))
        self.time_label.pack(pady=10)
        
        self.button_frame = tk.Frame(root)
        self.button_frame.pack()
        
        self.start_button = tk.Button(self.button_frame, text="Start", command=self.start_stop)
        self.lap_reset_button = tk.Button(self.button_frame, text="Lap", command=self.record_lap)
        
        self.start_button.pack(side="left")
        tk.Label(self.button_frame, text="   ").pack(side="left")  # Spacer
        self.lap_reset_button.pack(side="left")
        
        self.lap_display = tk.Label(root, text="", font=("Helvetica", 12))
        self.lap_display.pack(pady=10)
        
        self.update_display()
    
    def start_stop(self):
        if self.running:
            self.running = False
            self.lap_reset_button.config(text="Reset")
            self.start_button.config(text="Start")
        else:
            self.running = True
            self.start_time = time() - self.elapsed_time
            self.lap_reset_button.config(text="Lap")
            self.start_button.config(text="Stop")
            self.update_time()
    
    def record_lap(self):
        if self.running:
            lap_time = time() - self.start_time
            self.lap_times.append(lap_time)
            self.lap_count += 1
            self.update_lap_display(lap_time, self.lap_count)
        else:
            self.lap_times = []
            self.lap_count = 0
            self.lap_display.config(text="")
            self.reset()
    
    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.start_time = None
        self.update_display()
        self.start_button.config(text="Start")
        self.lap_reset_button.config(text="Lap")
    
    def update_time(self):
        if self.running:
            self.elapsed_time = time() - self.start_time
            self.update_display()
            self.root.after(10, self.update_time)
    
    def update_display(self):
        elapsed_time_formatted = self.format_time(self.elapsed_time)
        self.time_label.config(text=elapsed_time_formatted)
    
    def update_lap_display(self, lap_time=None, lap_count=None):
        if lap_time is not None:
            lap_time_formatted = self.format_time(lap_time)
            self.lap_display.config(text=self.lap_display.cget("text") +  f" {lap_count}:   {lap_time_formatted}\n")
        else:
            lap_times_formatted = [self.format_time(lap) for lap in self.lap_times]
            self.lap_display.config(text="\n".join(lap_times_formatted))
    
    def format_time(self, elapsed_time):
        minutes, seconds = divmod(int(elapsed_time), 60)
        milliseconds = int((elapsed_time - int(elapsed_time)) * 1000)
        return f"{minutes:02d}:{seconds:02d}.{milliseconds:03d}"

def main():
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
