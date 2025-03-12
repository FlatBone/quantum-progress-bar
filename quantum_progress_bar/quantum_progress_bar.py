import random
import time
import math
import sys
from datetime import datetime, timedelta

class QuantumProgressBar:
    """
    A progress bar that behaves according to quantum mechanics principles.
    The progress changes randomly when observed, and the estimated completion time
    has a high degree of uncertainty.
    """
    def __init__(self, total_steps=100, collapse_factor=0.2, uncertainty_level=0.8):
        """
        Initialize a quantum progress bar.
        
        Args:
            total_steps (int): Total number of steps to complete
            collapse_factor (float): How much the observation affects the state (0.0-1.0)
            uncertainty_level (float): Level of uncertainty in time estimates (0.0-1.0)
        """
        self.total_steps = total_steps
        self.current_state = random.randint(0, total_steps // 3)  # Start with some progress
        self.collapse_factor = collapse_factor
        self.uncertainty_level = uncertainty_level
        self.start_time = datetime.now()
        self.observed_states = []
        self.entangled_state = None

    def _collapse_wavefunction(self):
        """
        Collapse the quantum state when observed, potentially changing the progress.
        """
        # Record the current state before collapsing
        self.observed_states.append(self.current_state)
        
        # Determine if progress goes forward or backward based on previous observations
        if len(self.observed_states) > 2:
            recent_trend = self.observed_states[-1] - self.observed_states[-2]
            # Probability of continuing in same direction is higher
            direction = 1 if random.random() < (0.5 + 0.1 * (1 if recent_trend > 0 else -1)) else -1
        else:
            direction = 1 if random.random() < 0.7 else -1  # Usually progress forward
        
        # Calculate the amount of change
        max_change = int(self.total_steps * self.collapse_factor)
        change = random.randint(0, max_change) * direction
        
        # Apply the change with constraints
        new_state = self.current_state + change
        self.current_state = max(0, min(self.total_steps, new_state))

    def quantum_progress(self, width=50, quantum_bars=True):
        """
        Display the current progress as a progress bar with quantum behavior.
        
        Args:
            width (int): Width of the progress bar
            quantum_bars (bool): Whether to use quantum-style bars that change
            
        Returns:
            int: Current progress percentage
        """
        self._collapse_wavefunction()
        
        progress_percent = int(100 * self.current_state / self.total_steps)
        
        # Create a progress bar with quantum-style characters
        if quantum_bars:
            bar_chars = ['▓', '▒', '░', '█', '▓', '▄', '▌']
            filled_length = int(width * self.current_state // self.total_steps)
            bar = ''
            for i in range(width):
                if i < filled_length:
                    bar += random.choice(bar_chars)
                else:
                    # Occasionally show quantum fluctuations in empty space
                    bar += random.choice(['░', ' ', ' ', ' ', ' ']) if random.random() < 0.1 else ' '
        else:
            # Traditional style bar
            filled_length = int(width * self.current_state // self.total_steps)
            bar = '█' * filled_length + ' ' * (width - filled_length)
            
        # Create a quantum noise in percentage display
        display_percent = progress_percent
        if random.random() < 0.2:  # Occasionally show quantum fluctuation in percentage
            noise = random.randint(-5, 5)
            display_percent = max(0, min(100, progress_percent + noise))
            
        sys.stdout.write(f'\r[{bar}] {display_percent}% ')
        sys.stdout.flush()
        
        return progress_percent

    def uncertainty_estimate(self):
        """
        Provide an uncertain estimate of remaining time to completion.
        
        Returns:
            str: A time estimate with uncertainty
        """
        elapsed = (datetime.now() - self.start_time).total_seconds()
        
        if not self.observed_states or self.current_state <= 0:
            return "Unknown ± ∞"
            
        # Calculate rate based on observations with some randomness
        observed_progress = self.current_state - self.observed_states[0]
        if observed_progress <= 0:
            # If no progress or negative progress
            return "∞ ± ∞ (Heisenberg is uncertain)"
            
        seconds_per_step = elapsed / observed_progress
        
        # Add quantum uncertainty
        uncertainty_factor = random.uniform(1 - self.uncertainty_level, 1 + self.uncertainty_level * 3)
        adjusted_rate = seconds_per_step * uncertainty_factor
        
        # Calculate remaining time
        steps_remaining = self.total_steps - self.current_state
        estimated_seconds = steps_remaining * adjusted_rate
        
        # Calculate uncertainty range
        min_estimate = max(1, estimated_seconds * (1 - self.uncertainty_level))
        max_estimate = estimated_seconds * (1 + self.uncertainty_level * 2)
        
        # Format the times
        def format_time(seconds):
            if seconds < 60:
                return f"{int(seconds)} seconds"
            elif seconds < 3600:
                return f"{int(seconds / 60)} minutes"
            else:
                return f"{seconds / 3600:.1f} hours"
                
        if random.random() < 0.05:  # Occasional joke estimate
            joke_units = ["light years", "eons", "quantum cycles", "galactic rotations", "CPU cycles"]
            return f"{random.randint(1, 42)} {random.choice(joke_units)} ± uncertainty principle"
        
        main_estimate = format_time(estimated_seconds)
        range_estimate = f"{format_time(min_estimate)} - {format_time(max_estimate)}"
        
        return f"{main_estimate} (probably between {range_estimate})"

    def entangle(self, other_progress_bar):
        """
        Entangle this progress bar with another, so their states become correlated.
        
        Args:
            other_progress_bar (QuantumProgressBar): Another progress bar to entangle with
        """
        self.entangled_state = other_progress_bar
        other_progress_bar.entangled_state = self
        print("⚛️ Progress bars are now quantum entangled! ⚛️")

    def update(self, steps=1):
        """
        Update the progress by a specific number of steps.
        In quantum mechanics, this is like forcing a measurement outcome.
        
        Args:
            steps (int): Number of steps to progress
        """
        self.current_state = min(self.total_steps, self.current_state + steps)
        
        # If entangled, affect the other progress bar
        if self.entangled_state:
            # Entangled system moves in opposite direction with some probability
            if random.random() < 0.7:
                entangled_change = -steps if random.random() < 0.5 else steps
                self.entangled_state.current_state = max(0, min(
                    self.entangled_state.total_steps,
                    self.entangled_state.current_state + entangled_change
                ))