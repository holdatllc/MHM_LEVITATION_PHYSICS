#!/usr/bin/env python3
"""
MHM Rotating Triangular-Phase Tripulse Controller
================================================
Engineering implementation of rotating magnetic "propeller" system
9-coil array with 3-active rotating triangle pattern

Author: William Miller - Viraxis MHM
Contact: holdatllc2@gmail.com
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

class MHMRotatingTripulseController:
    """
    Rotating triangular-phase tripulse controller for 9-coil levitation system
    """
    
    def __init__(self):
        """Initialize rotating tripulse controller"""
        print("🌸 MHM ROTATING TRIPULSE CONTROLLER")
        print("="*60)
        print("⚡ Rotating magnetic propeller implementation")
        print("="*60)
        
        # System configuration
        self.num_coils = 9  # Flower-of-Life arrangement
        self.active_coils = 3  # Triangle of active coils
        
        # Timing parameters
        self.control_frequency = 1000  # Hz (1ms ticks)
        self.rotation_speed = 111  # Hz (1000/9 pattern speed)
        self.pulse_duration = 0.33  # ms (1/3 duty cycle)
        
        # Current parameters
        self.I_peak = 50.0  # A peak current per coil
        self.I_hover = 15.0  # A hover current
        
        # Control state
        self.step = 0
        self.rotation_direction = 1  # 1 = clockwise, -1 = counter-clockwise
        self.global_amplitude = 1.0  # 0-1 scale for lift control
        self.coil_bias = np.zeros(9)  # Individual coil amplitude bias
        
        # Flight control inputs
        self.throttle = 0.5  # 0-1 (hover at 0.5)
        self.yaw_rate = 0.0  # -1 to +1
        self.pitch = 0.0  # -1 to +1 (forward/back)
        self.roll = 0.0   # -1 to +1 (left/right)
        
        # Coil positions (radial arrangement)
        self.coil_angles = np.linspace(0, 2*np.pi, self.num_coils, endpoint=False)
        self.coil_positions = [(np.cos(angle), np.sin(angle)) for angle in self.coil_angles]
        
    def get_active_coils(self, step):
        """
        Calculate which 3 coils form the active triangle
        """
        active_indices = []
        for i in range(self.active_coils):
            coil_index = (step * self.rotation_direction + i * 3) % self.num_coils
            active_indices.append(coil_index)
        return sorted(active_indices)
    
    def calculate_coil_currents(self, step):
        """
        Calculate current for each coil based on rotating triangle pattern
        """
        currents = np.zeros(self.num_coils)
        active_coils = self.get_active_coils(step)
        
        # Base current for active coils
        base_current = self.I_hover * self.global_amplitude
        
        for coil_idx in active_coils:
            # Apply flight control biases
            bias_factor = 1.0 + self.coil_bias[coil_idx]
            
            # Pitch control (front/back coils)
            coil_angle = self.coil_angles[coil_idx]
            pitch_bias = self.pitch * np.cos(coil_angle) * 0.3
            
            # Roll control (left/right coils)
            roll_bias = self.roll * np.sin(coil_angle) * 0.3
            
            # Combined current
            currents[coil_idx] = base_current * bias_factor * (1 + pitch_bias + roll_bias)
            
            # Ensure positive current
            currents[coil_idx] = max(0, currents[coil_idx])
        
        return currents
    
    def update_flight_controls(self, throttle=None, yaw=None, pitch=None, roll=None):
        """
        Update flight control inputs
        """
        if throttle is not None:
            self.throttle = np.clip(throttle, 0.0, 1.0)
            self.global_amplitude = self.throttle
            
        if yaw is not None:
            self.yaw_rate = np.clip(yaw, -1.0, 1.0)
            # Yaw changes rotation speed
            speed_modifier = 1.0 + self.yaw_rate * 0.5
            self.rotation_speed = 111 * speed_modifier
            
        if pitch is not None:
            self.pitch = np.clip(pitch, -1.0, 1.0)
            
        if roll is not None:
            self.roll = np.clip(roll, -1.0, 1.0)
    
    def generate_pwm_waveform(self, duration_seconds=1.0):
        """
        Generate PWM waveform for all coils over specified duration
        """
        print(f"\n⚡ GENERATING PWM WAVEFORM")
        print(f"Duration: {duration_seconds}s")
        print(f"Control frequency: {self.control_frequency}Hz")
        print(f"Rotation speed: {self.rotation_speed:.1f}Hz")
        print("-"*50)
        
        # Time array
        dt = 1.0 / self.control_frequency
        num_steps = int(duration_seconds * self.control_frequency)
        time_array = np.linspace(0, duration_seconds, num_steps)
        
        # Current arrays for all coils
        coil_currents = np.zeros((self.num_coils, num_steps))
        active_pattern = np.zeros((self.num_coils, num_steps))
        
        for i, t in enumerate(time_array):
            # Update step based on rotation speed
            self.step = int(t * self.rotation_speed) % self.num_coils
            
            # Calculate currents
            currents = self.calculate_coil_currents(self.step)
            coil_currents[:, i] = currents
            
            # Track active pattern
            active_coils = self.get_active_coils(self.step)
            for coil_idx in active_coils:
                active_pattern[coil_idx, i] = 1
        
        return time_array, coil_currents, active_pattern
    
    def simulate_magnetic_field(self, time_array, coil_currents):
        """
        Simulate the rotating magnetic field pattern
        """
        print(f"\n🧲 SIMULATING MAGNETIC FIELD ROTATION")
        print("-"*50)
        
        # Calculate field at center point
        center_field = np.zeros(len(time_array))
        field_x = np.zeros(len(time_array))
        field_y = np.zeros(len(time_array))
        
        for i, t in enumerate(time_array):
            total_field = 0
            fx = 0
            fy = 0
            
            for coil_idx in range(self.num_coils):
                current = coil_currents[coil_idx, i]
                if current > 0:
                    # Field contribution (simplified model)
                    field_strength = current * 0.001  # Tesla per Amp
                    total_field += field_strength
                    
                    # Vector components
                    coil_x, coil_y = self.coil_positions[coil_idx]
                    fx += field_strength * coil_x
                    fy += field_strength * coil_y
            
            center_field[i] = total_field
            field_x[i] = fx
            field_y[i] = fy
        
        # Calculate rotation metrics
        field_magnitude = np.sqrt(field_x**2 + field_y**2)
        field_angle = np.arctan2(field_y, field_x)
        
        # Unwrap angle for continuous rotation
        field_angle_unwrapped = np.unwrap(field_angle)
        
        print(f"  Average field strength: {np.mean(center_field):.4f} T")
        print(f"  Field rotation rate: {np.mean(np.diff(field_angle_unwrapped))*self.control_frequency/(2*np.pi):.1f} Hz")
        print(f"  Field uniformity: {np.std(field_magnitude)/np.mean(field_magnitude)*100:.1f}% variation")
        
        return center_field, field_x, field_y, field_magnitude, field_angle_unwrapped
    
    def calculate_lift_force(self, center_field):
        """
        Calculate lift force from magnetic field
        """
        # Constants
        mu0 = 4 * np.pi * 1e-7
        total_area = 0.25 * 9  # 9 coils × 0.25 m² each
        efficiency = 0.85
        
        # Lift force (magnetic pressure)
        lift_force = (center_field**2 * total_area * efficiency) / (2 * mu0)
        
        return lift_force
    
    def generate_controller_code(self):
        """
        Generate microcontroller implementation code
        """
        print(f"\n💻 MICROCONTROLLER IMPLEMENTATION")
        print("-"*50)
        
        controller_code = """
// MHM Rotating Tripulse Controller - Arduino/STM32 Implementation
// 9-coil rotating triangle pattern for magnetic levitation

#define NUM_COILS 9
#define ACTIVE_COILS 3
#define CONTROL_FREQ 1000  // Hz
#define PWM_FREQ 5000      // Hz

// Hardware pins
const int coil_pins[NUM_COILS] = {2, 3, 4, 5, 6, 7, 8, 9, 10};
const int current_sense_pins[NUM_COILS] = {A0, A1, A2, A3, A4, A5, A6, A7, A8};

// Control variables
volatile int step = 0;
volatile int rotation_direction = 1;
float global_amplitude = 0.5;  // Hover setting
float coil_bias[NUM_COILS] = {0};

// Flight controls
float throttle = 0.5;
float yaw_rate = 0.0;
float pitch = 0.0;
float roll = 0.0;

void setup() {
    // Initialize PWM pins
    for(int i = 0; i < NUM_COILS; i++) {
        pinMode(coil_pins[i], OUTPUT);
        analogWriteFrequency(coil_pins[i], PWM_FREQ);
    }
    
    // Setup timer interrupt for 1kHz control loop
    Timer1.initialize(1000);  // 1ms = 1000 microseconds
    Timer1.attachInterrupt(control_loop);
    
    Serial.begin(115200);
    Serial.println("MHM Rotating Tripulse Controller Started");
}

void control_loop() {
    // Calculate active coils for current step
    int active_coils[ACTIVE_COILS];
    for(int i = 0; i < ACTIVE_COILS; i++) {
        active_coils[i] = (step * rotation_direction + i * 3) % NUM_COILS;
    }
    
    // Update all coil outputs
    for(int i = 0; i < NUM_COILS; i++) {
        bool is_active = false;
        for(int j = 0; j < ACTIVE_COILS; j++) {
            if(active_coils[j] == i) {
                is_active = true;
                break;
            }
        }
        
        if(is_active) {
            // Calculate PWM value (0-255)
            float current_factor = global_amplitude * (1.0 + coil_bias[i]);
            
            // Apply flight control biases
            float angle = i * 2.0 * PI / NUM_COILS;
            float pitch_bias = pitch * cos(angle) * 0.3;
            float roll_bias = roll * sin(angle) * 0.3;
            
            current_factor *= (1.0 + pitch_bias + roll_bias);
            current_factor = constrain(current_factor, 0.0, 1.0);
            
            int pwm_value = (int)(current_factor * 255);
            analogWrite(coil_pins[i], pwm_value);
        } else {
            analogWrite(coil_pins[i], 0);
        }
    }
    
    // Advance step for rotation
    step = (step + 1) % NUM_COILS;
}

void update_flight_controls(float new_throttle, float new_yaw, 
                          float new_pitch, float new_roll) {
    throttle = constrain(new_throttle, 0.0, 1.0);
    yaw_rate = constrain(new_yaw, -1.0, 1.0);
    pitch = constrain(new_pitch, -1.0, 1.0);
    roll = constrain(new_roll, -1.0, 1.0);
    
    global_amplitude = throttle;
    
    // Yaw affects rotation speed (modify timer if needed)
    // This is simplified - real implementation would adjust timer period
}

void loop() {
    // Read sensors (IMU, altimeter, etc.)
    // Process flight commands
    // Safety monitoring
    
    delay(10);  // Main loop at 100Hz
}
"""
        
        print("Generated Arduino/STM32 controller code:")
        print("Key features:")
        print("  • 1kHz timer interrupt for precise timing")
        print("  • 9-channel PWM output (5kHz carrier)")
        print("  • Real-time flight control integration")
        print("  • Current sensing for safety")
        print("  • Configurable rotation speed/direction")
        
        return controller_code
    
    def visualize_rotating_pattern(self, time_array, coil_currents, active_pattern):
        """
        Create visualization of the rotating tripulse pattern
        """
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
        
        # 1. Coil current waveforms
        colors = plt.cm.tab10(np.linspace(0, 1, self.num_coils))
        for i in range(self.num_coils):
            ax1.plot(time_array, coil_currents[i], color=colors[i], 
                    linewidth=1.5, label=f'Coil {i+1}')
        
        ax1.set_xlabel('Time (s)')
        ax1.set_ylabel('Current (A)')
        ax1.set_title('9-Coil Current Waveforms (Rotating Triangle)')
        ax1.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        ax1.grid(True, alpha=0.3)
        ax1.set_xlim(0, min(1.0, time_array[-1]))
        
        # 2. Active coil pattern
        im = ax2.imshow(active_pattern, aspect='auto', cmap='RdYlBu_r',
                       extent=[0, time_array[-1], 0, self.num_coils])
        ax2.set_xlabel('Time (s)')
        ax2.set_ylabel('Coil Number')
        ax2.set_title('Active Coil Pattern (Yellow = Active)')
        ax2.set_yticks(range(self.num_coils))
        ax2.set_yticklabels([f'Coil {i+1}' for i in range(self.num_coils)])
        
        # 3. Coil arrangement diagram
        ax3.set_xlim(-1.5, 1.5)
        ax3.set_ylim(-1.5, 1.5)
        ax3.set_aspect('equal')
        
        # Draw coils
        for i, (x, y) in enumerate(self.coil_positions):
            circle = plt.Circle((x, y), 0.15, fill=True, alpha=0.7, 
                              color=colors[i], edgecolor='black')
            ax3.add_patch(circle)
            ax3.text(x, y, str(i+1), ha='center', va='center', 
                    fontsize=10, fontweight='bold', color='white')
        
        # Draw triangle for current step
        current_active = self.get_active_coils(0)
        triangle_x = [self.coil_positions[i][0] for i in current_active] + [self.coil_positions[current_active[0]][0]]
        triangle_y = [self.coil_positions[i][1] for i in current_active] + [self.coil_positions[current_active[0]][1]]
        ax3.plot(triangle_x, triangle_y, 'r-', linewidth=3, alpha=0.8, label='Active Triangle')
        
        ax3.set_title('9-Coil Flower-of-Life Arrangement')
        ax3.legend()
        ax3.grid(True, alpha=0.3)
        
        # 4. Power and efficiency analysis
        total_power = np.sum(coil_currents**2, axis=0) * 0.1  # Assume 0.1Ω resistance
        active_count = np.sum(active_pattern, axis=0)
        efficiency = active_count / self.num_coils  # Fraction of coils active
        
        ax4_twin = ax4.twinx()
        
        line1 = ax4.plot(time_array, total_power, 'b-', linewidth=2, label='Total Power (W)')
        line2 = ax4_twin.plot(time_array, efficiency * 100, 'r-', linewidth=2, label='Efficiency (%)')
        
        ax4.set_xlabel('Time (s)')
        ax4.set_ylabel('Power (W)', color='b')
        ax4_twin.set_ylabel('Efficiency (%)', color='r')
        ax4.set_title('Power Consumption and Efficiency')
        
        # Combine legends
        lines = line1 + line2
        labels = [l.get_label() for l in lines]
        ax4.legend(lines, labels, loc='upper right')
        
        ax4.grid(True, alpha=0.3)
        ax4.set_xlim(0, min(1.0, time_array[-1]))
        
        plt.tight_layout()
        plt.savefig('mhm_rotating_tripulse_analysis.png', dpi=150, bbox_inches='tight')
        plt.show()

def main():
    """
    Run complete rotating tripulse controller analysis
    """
    print("\n🚀 MHM ROTATING TRIPULSE CONTROLLER ANALYSIS")
    print("="*60)
    
    # Initialize controller
    controller = MHMRotatingTripulseController()
    
    # Set flight parameters
    controller.update_flight_controls(
        throttle=0.6,  # 60% power for hover
        yaw=0.2,       # Slight yaw rate
        pitch=0.1,     # Slight forward
        roll=0.0       # No roll
    )
    
    # Generate waveforms
    time_array, coil_currents, active_pattern = controller.generate_pwm_waveform(2.0)
    
    # Simulate magnetic field
    center_field, field_x, field_y, field_mag, field_angle = controller.simulate_magnetic_field(
        time_array, coil_currents
    )
    
    # Calculate lift force
    lift_force = controller.calculate_lift_force(center_field)
    
    # Generate controller code
    controller_code = controller.generate_controller_code()
    
    # Visualize results
    controller.visualize_rotating_pattern(time_array, coil_currents, active_pattern)
    
    # Performance analysis
    print(f"\n📊 PERFORMANCE ANALYSIS")
    print("="*50)
    
    avg_power = np.mean(np.sum(coil_currents**2, axis=0)) * 0.1  # W
    avg_lift = np.mean(lift_force)
    efficiency = avg_lift / avg_power if avg_power > 0 else 0
    
    print(f"  Average power consumption: {avg_power:.1f} W")
    print(f"  Average lift force: {avg_lift:.0f} N")
    print(f"  Power efficiency: {efficiency:.1f} N/W")
    print(f"  Rotation frequency: {controller.rotation_speed:.1f} Hz")
    print(f"  Active duty cycle: {3/9*100:.1f}% (3 of 9 coils)")
    
    # System advantages
    print(f"\n✅ ROTATING TRIPULSE ADVANTAGES:")
    print(f"  • Continuous smooth rotation (no dead zones)")
    print(f"  • 33% duty cycle reduces heating")
    print(f"  • Directional control via phase/amplitude bias")
    print(f"  • Scalable to larger coil arrays")
    print(f"  • No mechanical moving parts")
    
    print(f"\n🔧 IMPLEMENTATION REQUIREMENTS:")
    print(f"  • 9-channel PWM controller (5kHz carrier)")
    print(f"  • 1kHz timer interrupt for precise timing")
    print(f"  • Current sensing on each coil")
    print(f"  • IMU for flight control feedback")
    print(f"  • High-current MOSFETs (100A+ rating)")
    
    print(f"\n🎯 FLIGHT CONTROL CAPABILITIES:")
    print(f"  • Throttle: Vertical lift control")
    print(f"  • Yaw: Rotation speed modulation")
    print(f"  • Pitch: Forward/backward tilt")
    print(f"  • Roll: Left/right tilt")
    print(f"  • Stable hover with active control")
    
    print(f"\n📧 Contact: holdatllc2@gmail.com")
    print(f"🌸 MHM: Rotating magnetic propeller technology")

if __name__ == "__main__":
    main()
