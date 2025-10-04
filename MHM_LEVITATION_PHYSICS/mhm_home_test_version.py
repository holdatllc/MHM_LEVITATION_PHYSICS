#!/usr/bin/env python3
"""
MHM Home Test Version - Low Cost Proof of Concept
=================================================
Scaled-down version for testing MHM principles at home
Budget: $500-800 instead of $15,000+

Author: William Miller - Viraxis MHM
Contact: holdatllc2@gmail.com
"""

import numpy as np
import matplotlib.pyplot as plt
import json

class MHMHomeTestSystem:
    """
    Low-cost home testing version of MHM levitation system
    """
    
    def __init__(self):
        """Initialize home test system"""
        print("🏠 MHM HOME TEST VERSION - LOW COST PROOF OF CONCEPT")
        print("="*60)
        print("💰 Budget: $500-800 (vs $15,000+ full system)")
        print("🎯 Goal: Demonstrate MHM principles at small scale")
        print("="*60)
        
        # Scaled-down specifications
        self.scale_factor = 0.2  # 1/5 scale
        self.test_payload = 5    # kg (small object, not person)
        self.hover_height = 0.02 # 2cm (vs 9cm full scale)
        self.platform_size = 0.25 # 25cm square (vs 120cm)
        
        # Simplified coil array (3 coils instead of 9)
        self.num_coils = 3
        self.coil_diameter = 0.08  # 8cm diameter
        self.coil_current = 5.0    # 5A (vs 50A full scale)
        
        # Power requirements
        self.test_power = 50  # W (vs 434W full scale)
        self.test_voltage = 12 # V (vs 48V full scale)
    
    def design_specifications(self):
        """Define home test system specifications"""
        print(f"\n🔧 HOME TEST SYSTEM SPECIFICATIONS")
        print("-"*50)
        
        specs = {
            'Physical_Dimensions': {
                'Platform_Size': f'{self.platform_size*100:.0f}cm × {self.platform_size*100:.0f}cm',
                'Platform_Height': '3cm',
                'Total_Weight': '2kg (system only)',
                'Test_Payload': f'{self.test_payload}kg max',
                'Hover_Height': f'{self.hover_height*100:.0f}cm target'
            },
            'Electromagnetic_System': {
                'Number_of_Coils': f'{self.num_coils} (simplified triangle)',
                'Coil_Diameter': f'{self.coil_diameter*100:.0f}cm each',
                'Coil_Turns': '50 turns (vs 108 full scale)',
                'Wire_Gauge': '16 AWG (vs 14 AWG full scale)',
                'Operating_Current': f'{self.coil_current}A per coil',
                'Magnet_Type': 'N42 grade (vs N52 full scale)'
            },
            'Power_System': {
                'Input_Voltage': f'{self.test_voltage}V DC',
                'Total_Power': f'{self.test_power}W',
                'Power_Supply': 'Desktop PC power supply (repurposed)',
                'Battery_Option': '12V car battery for portable testing',
                'Safety_Current': '10A maximum (built-in limiting)'
            },
            'Control_System': {
                'Controller': 'Arduino Uno (vs STM32H7)',
                'Control_Frequency': '100Hz (vs 1kHz full scale)',
                'Sensors': 'Basic IMU + 1 distance sensor',
                'Safety': 'Manual emergency stop button',
                'Interface': 'Simple potentiometer controls'
            }
        }
        
        for category, details in specs.items():
            print(f"\n  {category.replace('_', ' ')}:")
            for key, value in details.items():
                print(f"    {key.replace('_', ' ')}: {value}")
        
        return specs
    
    def component_list_and_costs(self):
        """Generate component list with costs for home version"""
        print(f"\n💰 HOME TEST VERSION - COMPONENT COSTS")
        print("-"*50)
        
        components = {
            'Electromagnetic_Components': {
                'Ferrite_Cores_3x': {'cost': 45, 'source': 'Amazon/eBay'},
                'Magnet_Wire_16AWG': {'cost': 25, 'source': 'Electronics store'},
                'Neodymium_Magnets_N42_12x': {'cost': 120, 'source': 'K&J Magnetics'},
                'Magnet_Mounting_Hardware': {'cost': 20, 'source': 'Hardware store'}
            },
            'Platform_Structure': {
                'Plywood_Base_25cm': {'cost': 15, 'source': 'Home Depot'},
                'Aluminum_Angle_Brackets': {'cost': 25, 'source': 'Hardware store'},
                'Screws_and_Fasteners': {'cost': 15, 'source': 'Hardware store'},
                'Non_Slip_Surface': {'cost': 10, 'source': 'Amazon'}
            },
            'Electronics': {
                'Arduino_Uno_R3': {'cost': 25, 'source': 'Arduino.cc'},
                'Motor_Driver_Shield': {'cost': 35, 'source': 'Adafruit'},
                'MOSFETs_IRFZ44N_3x': {'cost': 15, 'source': 'DigiKey'},
                'Current_Sensors_ACS712': {'cost': 20, 'source': 'Amazon'},
                'IMU_MPU6050': {'cost': 8, 'source': 'Amazon'},
                'Ultrasonic_Sensor_HC_SR04': {'cost': 5, 'source': 'Amazon'},
                'Breadboard_and_Jumpers': {'cost': 20, 'source': 'Electronics store'},
                'Enclosure_Box': {'cost': 15, 'source': 'Amazon'}
            },
            'Power_System': {
                'PC_Power_Supply_12V_10A': {'cost': 40, 'source': 'Used computer store'},
                'Power_Connectors': {'cost': 10, 'source': 'Electronics store'},
                'Fuses_and_Switches': {'cost': 15, 'source': 'Auto parts store'},
                'Emergency_Stop_Button': {'cost': 12, 'source': 'Amazon'}
            },
            'Tools_and_Supplies': {
                'Soldering_Iron_Kit': {'cost': 30, 'source': 'Amazon'},
                'Multimeter_Basic': {'cost': 25, 'source': 'Harbor Freight'},
                'Wire_Strippers': {'cost': 15, 'source': 'Hardware store'},
                'Heat_Shrink_Tubing': {'cost': 10, 'source': 'Electronics store'},
                'Electrical_Tape': {'cost': 5, 'source': 'Hardware store'},
                'Safety_Glasses': {'cost': 10, 'source': 'Hardware store'}
            },
            'Optional_Upgrades': {
                'Better_Power_Supply_Adjustable': {'cost': 80, 'source': 'Amazon'},
                'Oscilloscope_USB_Basic': {'cost': 60, 'source': 'Amazon'},
                'Function_Generator_Kit': {'cost': 40, 'source': 'Amazon'},
                'Better_IMU_9DOF': {'cost': 25, 'source': 'SparkFun'}
            }
        }
        
        total_cost = 0
        category_totals = {}
        
        for category, items in components.items():
            category_cost = sum(item['cost'] for item in items.values())
            category_totals[category] = category_cost
            total_cost += category_cost
            
            print(f"\n  {category.replace('_', ' ')}:")
            for item, details in items.items():
                print(f"    {item.replace('_', ' ')}: ${details['cost']} ({details['source']})")
            print(f"    Subtotal: ${category_cost}")
        
        print(f"\n💰 COST SUMMARY:")
        print(f"  Core Components: ${category_totals['Electromagnetic_Components'] + category_totals['Platform_Structure'] + category_totals['Electronics'] + category_totals['Power_System']}")
        print(f"  Tools (one-time): ${category_totals['Tools_and_Supplies']}")
        print(f"  Optional Upgrades: ${category_totals['Optional_Upgrades']}")
        print(f"  ─────────────────────")
        print(f"  TOTAL (with tools): ${total_cost}")
        print(f"  TOTAL (core only): ${total_cost - category_totals['Tools_and_Supplies'] - category_totals['Optional_Upgrades']}")
        
        return components, total_cost
    
    def build_instructions_simplified(self):
        """Simplified build instructions for home version"""
        print(f"\n🛠️ HOME VERSION BUILD INSTRUCTIONS")
        print("-"*50)
        
        build_phases = {
            'Phase_1_Coil_Winding': {
                'duration': '1 weekend',
                'difficulty': 'Easy',
                'steps': [
                    'Cut 3 ferrite rods to 10cm length',
                    'Wind 50 turns of 16 AWG wire on each core',
                    'Leave 20cm leads on each end',
                    'Test resistance (should be ~0.5 ohms)',
                    'Secure windings with electrical tape'
                ]
            },
            'Phase_2_Platform_Assembly': {
                'duration': '1 day',
                'difficulty': 'Easy',
                'steps': [
                    'Cut plywood base to 25cm × 25cm',
                    'Drill holes for coil mounting (triangle pattern)',
                    'Mount aluminum brackets for coil support',
                    'Install magnets above each coil position',
                    'Add non-slip surface for test objects'
                ]
            },
            'Phase_3_Electronics_Assembly': {
                'duration': '1 weekend',
                'difficulty': 'Medium',
                'steps': [
                    'Assemble Arduino with motor driver shield',
                    'Connect MOSFETs for coil control',
                    'Wire current sensors in series with coils',
                    'Install IMU and distance sensor',
                    'Add emergency stop button circuit',
                    'Test all connections with multimeter'
                ]
            },
            'Phase_4_Software_Setup': {
                'duration': '1 day',
                'difficulty': 'Medium',
                'steps': [
                    'Install Arduino IDE and libraries',
                    'Upload basic coil control sketch',
                    'Calibrate current sensors',
                    'Test individual coil activation',
                    'Implement basic hover control loop'
                ]
            },
            'Phase_5_Testing_and_Tuning': {
                'duration': '1 weekend',
                'difficulty': 'Medium',
                'steps': [
                    'Start with 1A current limit',
                    'Test with lightweight objects (100g)',
                    'Gradually increase current and payload',
                    'Tune control parameters',
                    'Document performance vs power'
                ]
            }
        }
        
        for phase, details in build_phases.items():
            print(f"\n  {phase.replace('_', ' ')}:")
            print(f"    Duration: {details['duration']}")
            print(f"    Difficulty: {details['difficulty']}")
            print(f"    Steps:")
            for i, step in enumerate(details['steps'], 1):
                print(f"      {i}. {step}")
        
        print(f"\n⏱️ TOTAL BUILD TIME: 2-3 weekends")
        print(f"🎯 EXPECTED RESULT: 2cm hover with 1-5kg objects")
        
        return build_phases
    
    def performance_expectations(self):
        """Set realistic performance expectations for home version"""
        print(f"\n📊 EXPECTED PERFORMANCE - HOME TEST VERSION")
        print("-"*50)
        
        performance = {
            'Hover_Capabilities': {
                'Maximum_Height': '2-3cm (vs 9cm full scale)',
                'Payload_Range': '0.1-5kg (vs 120kg full scale)',
                'Hover_Duration': '5-10 minutes continuous',
                'Power_Consumption': '30-50W (vs 434W full scale)',
                'Stability': 'Basic (manual control required)'
            },
            'Test_Objects': {
                'Lightweight_Demo': '100g smartphone (easy)',
                'Medium_Demo': '1kg textbook (moderate)',
                'Heavy_Demo': '5kg dumbbell (challenging)',
                'Proof_of_Concept': 'Any stable hover = SUCCESS',
                'Not_Suitable_For': 'Human transport (safety/power)'
            },
            'Learning_Outcomes': {
                'Physics_Validation': 'Magnetic levitation principles',
                'Control_Systems': 'Feedback loop tuning',
                'Power_Electronics': 'MOSFET switching, current control',
                'Safety_Systems': 'Emergency stops, current limiting',
                'Scaling_Understanding': 'How to scale up to full system'
            },
            'Upgrade_Path': {
                'Phase_1': 'Basic hover demonstration',
                'Phase_2': 'Add more coils (6-coil version)',
                'Phase_3': 'Increase power and payload',
                'Phase_4': 'Better control system (STM32)',
                'Phase_5': 'Full-scale system development'
            }
        }
        
        for category, details in performance.items():
            print(f"\n  {category.replace('_', ' ')}:")
            for key, value in details.items():
                print(f"    {key.replace('_', ' ')}: {value}")
        
        return performance
    
    def safety_considerations_home(self):
        """Safety considerations for home testing"""
        print(f"\n⚠️ HOME VERSION SAFETY CONSIDERATIONS")
        print("-"*50)
        
        safety_points = {
            'Electrical_Safety': [
                'Use 12V DC only (safer than 48V full system)',
                'Install 10A fuse protection',
                'Emergency stop button within easy reach',
                'Ground all metal components',
                'Never exceed 5A per coil',
                'Use insulated tools only'
            ],
            'Mechanical_Safety': [
                'Test objects only (no human contact)',
                'Secure all components to prevent flying parts',
                'Clear 1-meter radius around test area',
                'Stable, level surface required',
                'Eye protection when adjusting magnets',
                'Keep fingers away from coil gaps'
            ],
            'Operational_Safety': [
                'Adult supervision required',
                'Start with lowest power settings',
                'Monitor component temperatures',
                'Have fire extinguisher nearby',
                'Test in well-ventilated area',
                'Document all test parameters'
            ],
            'What_NOT_to_Do': [
                'Never attempt human levitation',
                'Do not exceed voltage/current limits',
                'Avoid wet conditions',
                'Do not leave system unattended',
                'Never bypass safety systems',
                'Do not use near pacemakers/electronics'
            ]
        }
        
        for category, points in safety_points.items():
            print(f"\n  {category.replace('_', ' ')}:")
            for point in points:
                print(f"    • {point}")
        
        return safety_points
    
    def arduino_code_example(self):
        """Generate basic Arduino code for home version"""
        print(f"\n💻 BASIC ARDUINO CODE EXAMPLE")
        print("-"*50)
        
        arduino_code = '''
// MHM Home Test Version - Basic Arduino Control
// Simple 3-coil magnetic levitation controller

#include <Wire.h>
#include <MPU6050.h>

// Pin definitions
#define COIL1_PIN 3    // PWM pin for coil 1
#define COIL2_PIN 5    // PWM pin for coil 2  
#define COIL3_PIN 6    // PWM pin for coil 3
#define CURRENT1_PIN A0 // Current sensor 1
#define CURRENT2_PIN A1 // Current sensor 2
#define CURRENT3_PIN A2 // Current sensor 3
#define DISTANCE_TRIG 7 // Ultrasonic trigger
#define DISTANCE_ECHO 8 // Ultrasonic echo
#define EMERGENCY_STOP 2 // Emergency stop button
#define POWER_CONTROL A3 // Potentiometer for power

// System parameters
const int MAX_PWM = 200;        // Maximum PWM (out of 255)
const int TARGET_HEIGHT = 20;   // Target height in mm
const float KP = 2.0;           // Proportional gain
const float KI = 0.1;           // Integral gain
const float KD = 0.5;           // Derivative gain

// Global variables
MPU6050 mpu;
float height_error = 0;
float integral_error = 0;
float last_error = 0;
bool emergency_stop = false;

void setup() {
  Serial.begin(9600);
  Serial.println("MHM Home Test System Starting...");
  
  // Initialize pins
  pinMode(COIL1_PIN, OUTPUT);
  pinMode(COIL2_PIN, OUTPUT);
  pinMode(COIL3_PIN, OUTPUT);
  pinMode(DISTANCE_TRIG, OUTPUT);
  pinMode(DISTANCE_ECHO, INPUT);
  pinMode(EMERGENCY_STOP, INPUT_PULLUP);
  
  // Initialize IMU
  Wire.begin();
  mpu.initialize();
  
  // Safety check
  if (!mpu.testConnection()) {
    Serial.println("IMU connection failed - STOPPING");
    while(1);
  }
  
  Serial.println("System ready - Press emergency stop to begin");
  while(digitalRead(EMERGENCY_STOP) == LOW);
}

void loop() {
  // Check emergency stop
  if (digitalRead(EMERGENCY_STOP) == LOW) {
    emergency_stop = true;
    shutdownSystem();
    return;
  }
  
  // Read sensors
  float current_height = readDistance();
  float power_setting = analogRead(POWER_CONTROL) / 1023.0;
  
  // Calculate height error
  height_error = TARGET_HEIGHT - current_height;
  integral_error += height_error;
  float derivative_error = height_error - last_error;
  
  // PID control calculation
  float control_output = KP * height_error + 
                        KI * integral_error + 
                        KD * derivative_error;
  
  // Apply power setting
  control_output *= power_setting;
  
  // Limit output
  control_output = constrain(control_output, 0, MAX_PWM);
  
  // Distribute power to coils (simplified)
  int coil1_power = control_output;
  int coil2_power = control_output;
  int coil3_power = control_output;
  
  // Apply to coils
  analogWrite(COIL1_PIN, coil1_power);
  analogWrite(COIL2_PIN, coil2_power);
  analogWrite(COIL3_PIN, coil3_power);
  
  // Monitor currents (safety)
  float current1 = readCurrent(CURRENT1_PIN);
  float current2 = readCurrent(CURRENT2_PIN);
  float current3 = readCurrent(CURRENT3_PIN);
  
  // Current limiting
  if (current1 > 5.0 || current2 > 5.0 || current3 > 5.0) {
    Serial.println("OVERCURRENT - SHUTDOWN");
    shutdownSystem();
    return;
  }
  
  // Debug output
  Serial.print("Height: "); Serial.print(current_height);
  Serial.print(" Error: "); Serial.print(height_error);
  Serial.print(" Output: "); Serial.print(control_output);
  Serial.print(" Currents: "); 
  Serial.print(current1); Serial.print(" ");
  Serial.print(current2); Serial.print(" ");
  Serial.println(current3);
  
  last_error = height_error;
  delay(10); // 100Hz control loop
}

float readDistance() {
  // Ultrasonic distance measurement
  digitalWrite(DISTANCE_TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(DISTANCE_TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(DISTANCE_TRIG, LOW);
  
  long duration = pulseIn(DISTANCE_ECHO, HIGH);
  float distance = duration * 0.034 / 2; // Convert to mm
  
  return distance;
}

float readCurrent(int pin) {
  // Read current sensor (ACS712)
  int raw = analogRead(pin);
  float voltage = raw * 5.0 / 1023.0;
  float current = (voltage - 2.5) / 0.185; // ACS712-5A sensitivity
  return abs(current);
}

void shutdownSystem() {
  // Emergency shutdown
  analogWrite(COIL1_PIN, 0);
  analogWrite(COIL2_PIN, 0);
  analogWrite(COIL3_PIN, 0);
  
  Serial.println("SYSTEM SHUTDOWN - Reset to restart");
  while(1); // Stop execution
}
'''
        
        print("Basic Arduino code generated for home testing.")
        print("Features:")
        print("  • 3-coil control with PWM")
        print("  • PID height control")
        print("  • Current monitoring and limiting")
        print("  • Emergency stop functionality")
        print("  • Serial debugging output")
        
        return arduino_code
    
    def success_criteria(self):
        """Define success criteria for home version"""
        print(f"\n🎯 SUCCESS CRITERIA - HOME TEST VERSION")
        print("-"*50)
        
        criteria = {
            'Minimum_Success': {
                'Achievement': 'Any stable hover for 10+ seconds',
                'Object': '100g smartphone or similar',
                'Height': '5mm minimum',
                'Power': 'Under 30W',
                'Significance': 'Proves MHM principles work'
            },
            'Good_Success': {
                'Achievement': 'Stable hover with control',
                'Object': '500g-1kg objects',
                'Height': '10-20mm controlled',
                'Power': '30-40W',
                'Significance': 'Demonstrates practical control'
            },
            'Excellent_Success': {
                'Achievement': 'Multiple objects, height control',
                'Object': 'Up to 5kg payload',
                'Height': '20-30mm with adjustment',
                'Power': '40-50W',
                'Significance': 'Ready for scaling up'
            },
            'Next_Steps_After_Success': {
                'Documentation': 'Record all test data and videos',
                'Sharing': 'Post results on GitHub/YouTube',
                'Scaling': 'Plan 6-coil or 9-coil upgrade',
                'Community': 'Connect with other builders',
                'Research': 'Study full-scale implementation'
            }
        }
        
        for level, details in criteria.items():
            print(f"\n  {level.replace('_', ' ')}:")
            for key, value in details.items():
                print(f"    {key}: {value}")
        
        return criteria

def main():
    """
    Generate complete home test version documentation
    """
    print("\n🏠 MHM HOME TEST VERSION ANALYSIS")
    print("="*60)
    
    home_system = MHMHomeTestSystem()
    
    # Generate all documentation
    specs = home_system.design_specifications()
    components, cost = home_system.component_list_and_costs()
    build_guide = home_system.build_instructions_simplified()
    performance = home_system.performance_expectations()
    safety = home_system.safety_considerations_home()
    code = home_system.arduino_code_example()
    success = home_system.success_criteria()
    
    # Summary
    print(f"\n" + "="*60)
    print(f"🎯 HOME VERSION SUMMARY")
    print("="*60)
    
    print(f"\n💰 TOTAL COST: $500-800 (vs $15,000+ full system)")
    print(f"⏱️ BUILD TIME: 2-3 weekends")
    print(f"🎯 GOAL: Demonstrate MHM principles at small scale")
    print(f"📏 SCALE: 1/5 size, 1/10 power, 1/25 payload")
    print(f"🏆 SUCCESS: Any stable hover = proof of concept")
    
    print(f"\n🌟 WHY BUILD THE HOME VERSION:")
    benefits = [
        "Learn MHM principles hands-on",
        "Validate physics before full investment",
        "Develop control system skills",
        "Create impressive demonstrations",
        "Build foundation for scaling up",
        "Low cost, low risk proof of concept"
    ]
    
    for benefit in benefits:
        print(f"  ✓ {benefit}")
    
    print(f"\n📧 Contact: holdatllc2@gmail.com")
    print(f"🌸 MHM: Start small, think big!")

if __name__ == "__main__":
    main()
