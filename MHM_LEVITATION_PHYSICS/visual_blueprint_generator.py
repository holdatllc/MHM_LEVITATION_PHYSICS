#!/usr/bin/env python3
"""
MHM Visual Blueprint Generator
=============================
Creates detailed visual blueprints and 3D models for the MHM levitation system

Author: William Miller - Viraxis MHM
Contact: holdatllc2@gmail.com
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as patches
from matplotlib.patches import Circle, Rectangle, FancyBboxPatch
import json

class MHMBlueprintGenerator:
    """
    Generate visual blueprints and technical drawings for MHM system
    """
    
    def __init__(self):
        """Initialize blueprint generator"""
        print("📐 MHM VISUAL BLUEPRINT GENERATOR")
        print("="*50)
        
        # System dimensions (in meters)
        self.platform_length = 1.2
        self.platform_width = 0.8
        self.platform_height = 0.15
        self.hover_height = 0.09
        
        # Coil specifications
        self.coil_diameter = 0.25  # 25cm
        self.coil_positions = self.calculate_coil_positions()
        
        # Colors for different components
        self.colors = {
            'platform': '#2E8B57',      # Sea green
            'coils': '#FF6347',         # Tomato red
            'magnets': '#4169E1',       # Royal blue
            'electronics': '#FFD700',   # Gold
            'person': '#DDA0DD',        # Plum
            'ground': '#8B4513'         # Saddle brown
        }
    
    def calculate_coil_positions(self):
        """Calculate Flower-of-Life coil positions"""
        positions = []
        
        # Center coil
        positions.append((0, 0))
        
        # Inner ring (6 coils)
        radius_inner = 0.3  # 30cm from center
        for i in range(6):
            angle = i * np.pi / 3  # 60 degree spacing
            x = radius_inner * np.cos(angle)
            y = radius_inner * np.sin(angle)
            positions.append((x, y))
        
        # Outer ring (2 coils for balance)
        radius_outer = 0.45  # 45cm from center
        for i in range(2):
            angle = i * np.pi  # 180 degree spacing
            x = radius_outer * np.cos(angle)
            y = radius_outer * np.sin(angle)
            positions.append((x, y))
        
        return positions
    
    def create_top_view_blueprint(self):
        """Create detailed top-view blueprint"""
        fig, ax = plt.subplots(1, 1, figsize=(14, 10))
        
        # Platform outline
        platform = Rectangle((-self.platform_length/2, -self.platform_width/2),
                           self.platform_length, self.platform_width,
                           linewidth=3, edgecolor='black', facecolor=self.colors['platform'], alpha=0.3)
        ax.add_patch(platform)
        
        # Coil positions
        for i, (x, y) in enumerate(self.coil_positions):
            coil = Circle((x, y), self.coil_diameter/2, 
                         linewidth=2, edgecolor=self.colors['coils'], 
                         facecolor=self.colors['coils'], alpha=0.6)
            ax.add_patch(coil)
            
            # Coil labels
            ax.text(x, y, f'C{i+1}', ha='center', va='center', 
                   fontsize=10, fontweight='bold', color='white')
        
        # Control electronics box
        electronics_box = FancyBboxPatch((0.1, -0.15), 0.3, 0.3,
                                       boxstyle="round,pad=0.02",
                                       facecolor=self.colors['electronics'],
                                       edgecolor='black', linewidth=2, alpha=0.7)
        ax.add_patch(electronics_box)
        ax.text(0.25, 0, 'CONTROL\nELECTRONICS', ha='center', va='center',
               fontsize=9, fontweight='bold')
        
        # Foot positions
        foot_positions = [(-0.3, -0.2), (-0.3, 0.2), (0.3, -0.2), (0.3, 0.2)]
        for x, y in foot_positions:
            foot = Circle((x, y), 0.05, facecolor=self.colors['person'], 
                         edgecolor='black', linewidth=1, alpha=0.8)
            ax.add_patch(foot)
        
        # Dimensions
        ax.annotate('', xy=(-self.platform_length/2, -0.5), xytext=(self.platform_length/2, -0.5),
                   arrowprops=dict(arrowstyle='<->', color='red', lw=2))
        ax.text(0, -0.55, f'{self.platform_length*100:.0f} cm', ha='center', va='top',
               fontsize=12, color='red', fontweight='bold')
        
        ax.annotate('', xy=(-0.7, -self.platform_width/2), xytext=(-0.7, self.platform_width/2),
                   arrowprops=dict(arrowstyle='<->', color='red', lw=2))
        ax.text(-0.75, 0, f'{self.platform_width*100:.0f} cm', ha='right', va='center',
               fontsize=12, color='red', fontweight='bold', rotation=90)
        
        # Title and labels
        ax.set_title('MHM Magnetic Levitation System - Top View Blueprint', 
                    fontsize=16, fontweight='bold', pad=20)
        
        # Legend
        legend_elements = [
            plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=self.colors['coils'], 
                      markersize=12, label='Electromagnetic Coils (9×)'),
            plt.Line2D([0], [0], marker='s', color='w', markerfacecolor=self.colors['platform'], 
                      markersize=12, label='Carbon Fiber Platform'),
            plt.Line2D([0], [0], marker='s', color='w', markerfacecolor=self.colors['electronics'], 
                      markersize=12, label='Control Electronics'),
            plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=self.colors['person'], 
                      markersize=10, label='Foot Positions')
        ]
        ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.15, 1))
        
        ax.set_xlim(-0.8, 0.8)
        ax.set_ylim(-0.6, 0.6)
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3)
        ax.set_xlabel('Distance (meters)', fontsize=12)
        ax.set_ylabel('Distance (meters)', fontsize=12)
        
        plt.tight_layout()
        plt.savefig('mhm_top_view_blueprint.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        return fig
    
    def create_side_view_blueprint(self):
        """Create detailed side-view blueprint"""
        fig, ax = plt.subplots(1, 1, figsize=(14, 8))
        
        # Ground
        ground = Rectangle((-0.8, -0.3), 1.6, 0.1, 
                          facecolor=self.colors['ground'], edgecolor='black', linewidth=2)
        ax.add_patch(ground)
        ax.text(0, -0.35, 'CONDUCTIVE GROUND SURFACE', ha='center', va='top',
               fontsize=10, fontweight='bold')
        
        # Platform
        platform = Rectangle((-self.platform_length/2, self.hover_height), 
                           self.platform_length, self.platform_height,
                           facecolor=self.colors['platform'], edgecolor='black', linewidth=3)
        ax.add_patch(platform)
        
        # Coils (simplified side view)
        coil_y = self.hover_height - 0.05
        for i in range(5):  # Show 5 coils in side view
            x_pos = -0.4 + i * 0.2
            coil = Rectangle((x_pos - 0.05, coil_y - 0.03), 0.1, 0.06,
                           facecolor=self.colors['coils'], edgecolor='black', linewidth=1)
            ax.add_patch(coil)
        
        # Magnets
        magnet_y = self.hover_height + 0.02
        for i in range(5):
            x_pos = -0.4 + i * 0.2
            magnet = Rectangle((x_pos - 0.025, magnet_y), 0.05, 0.03,
                             facecolor=self.colors['magnets'], edgecolor='black', linewidth=1)
            ax.add_patch(magnet)
        
        # Person silhouette
        person_x = 0
        person_y = self.hover_height + self.platform_height
        
        # Head
        head = Circle((person_x, person_y + 0.85), 0.08, 
                     facecolor=self.colors['person'], edgecolor='black', linewidth=2)
        ax.add_patch(head)
        
        # Body
        body = Rectangle((person_x - 0.1, person_y + 0.3), 0.2, 0.5,
                        facecolor=self.colors['person'], edgecolor='black', linewidth=2)
        ax.add_patch(body)
        
        # Arms
        ax.plot([person_x - 0.1, person_x - 0.2], [person_y + 0.6, person_y + 0.5], 
               color='black', linewidth=3)
        ax.plot([person_x + 0.1, person_x + 0.2], [person_y + 0.6, person_y + 0.5], 
               color='black', linewidth=3)
        
        # Legs
        ax.plot([person_x - 0.05, person_x - 0.1], [person_y + 0.3, person_y], 
               color='black', linewidth=3)
        ax.plot([person_x + 0.05, person_x + 0.1], [person_y + 0.3, person_y], 
               color='black', linewidth=3)
        
        # Hover height dimension
        ax.annotate('', xy=(0.7, 0), xytext=(0.7, self.hover_height),
                   arrowprops=dict(arrowstyle='<->', color='red', lw=2))
        ax.text(0.75, self.hover_height/2, f'{self.hover_height*100:.0f} cm\nHOVER HEIGHT', 
               ha='left', va='center', fontsize=10, color='red', fontweight='bold')
        
        # Platform height dimension
        ax.annotate('', xy=(-0.7, self.hover_height), 
                   xytext=(-0.7, self.hover_height + self.platform_height),
                   arrowprops=dict(arrowstyle='<->', color='blue', lw=2))
        ax.text(-0.75, self.hover_height + self.platform_height/2, 
               f'{self.platform_height*100:.0f} cm', ha='right', va='center',
               fontsize=10, color='blue', fontweight='bold', rotation=90)
        
        # Magnetic field lines (artistic representation)
        for i in range(3):
            x_start = -0.4 + i * 0.4
            y_start = coil_y
            
            # Curved field lines
            theta = np.linspace(0, np.pi, 20)
            field_x = x_start + 0.1 * np.cos(theta)
            field_y = y_start + 0.05 * np.sin(theta)
            ax.plot(field_x, field_y, 'b--', alpha=0.6, linewidth=1)
        
        ax.set_title('MHM Magnetic Levitation System - Side View Blueprint', 
                    fontsize=16, fontweight='bold', pad=20)
        
        # Legend
        legend_elements = [
            plt.Line2D([0], [0], marker='s', color='w', markerfacecolor=self.colors['coils'], 
                      markersize=10, label='Electromagnetic Coils'),
            plt.Line2D([0], [0], marker='s', color='w', markerfacecolor=self.colors['magnets'], 
                      markersize=10, label='Permanent Magnets'),
            plt.Line2D([0], [0], marker='s', color='w', markerfacecolor=self.colors['platform'], 
                      markersize=10, label='Platform Structure'),
            plt.Line2D([0], [0], color='blue', linestyle='--', alpha=0.6, 
                      label='Magnetic Field Lines')
        ]
        ax.legend(handles=legend_elements, loc='upper right')
        
        ax.set_xlim(-0.8, 0.8)
        ax.set_ylim(-0.4, 1.2)
        ax.grid(True, alpha=0.3)
        ax.set_xlabel('Distance (meters)', fontsize=12)
        ax.set_ylabel('Height (meters)', fontsize=12)
        
        plt.tight_layout()
        plt.savefig('mhm_side_view_blueprint.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        return fig
    
    def create_3d_visualization(self):
        """Create 3D visualization of the complete system"""
        fig = plt.figure(figsize=(12, 10))
        ax = fig.add_subplot(111, projection='3d')
        
        # Platform
        platform_x = np.array([-self.platform_length/2, self.platform_length/2, 
                              self.platform_length/2, -self.platform_length/2])
        platform_y = np.array([-self.platform_width/2, -self.platform_width/2, 
                              self.platform_width/2, self.platform_width/2])
        platform_z = np.full(4, self.hover_height + self.platform_height/2)
        
        # Create platform surface
        xx, yy = np.meshgrid(np.linspace(-self.platform_length/2, self.platform_length/2, 10),
                            np.linspace(-self.platform_width/2, self.platform_width/2, 10))
        zz = np.full_like(xx, self.hover_height + self.platform_height/2)
        ax.plot_surface(xx, yy, zz, alpha=0.3, color=self.colors['platform'])
        
        # Coils (as cylinders)
        for x, y in self.coil_positions:
            # Coil cylinder
            theta = np.linspace(0, 2*np.pi, 20)
            coil_x = x + self.coil_diameter/4 * np.cos(theta)
            coil_y = y + self.coil_diameter/4 * np.sin(theta)
            coil_z_bottom = np.full_like(coil_x, self.hover_height - 0.05)
            coil_z_top = np.full_like(coil_x, self.hover_height + 0.05)
            
            # Plot coil
            ax.plot(coil_x, coil_y, coil_z_bottom, color=self.colors['coils'], linewidth=2)
            ax.plot(coil_x, coil_y, coil_z_top, color=self.colors['coils'], linewidth=2)
            
            # Connect top and bottom
            for i in range(0, len(theta), 4):
                ax.plot([coil_x[i], coil_x[i]], [coil_y[i], coil_y[i]], 
                       [coil_z_bottom[i], coil_z_top[i]], 
                       color=self.colors['coils'], linewidth=1)
        
        # Ground plane
        ground_x = np.linspace(-0.8, 0.8, 10)
        ground_y = np.linspace(-0.6, 0.6, 10)
        ground_xx, ground_yy = np.meshgrid(ground_x, ground_y)
        ground_zz = np.zeros_like(ground_xx)
        ax.plot_surface(ground_xx, ground_yy, ground_zz, alpha=0.2, color=self.colors['ground'])
        
        # Person (simplified)
        person_x, person_y = 0, 0
        person_z = self.hover_height + self.platform_height
        
        # Body as vertical line
        ax.plot([person_x, person_x], [person_y, person_y], 
               [person_z, person_z + 0.8], color='black', linewidth=5)
        
        # Head
        ax.scatter([person_x], [person_y], [person_z + 0.85], 
                  s=200, c=self.colors['person'], edgecolors='black', linewidth=2)
        
        ax.set_title('MHM Magnetic Levitation System - 3D Visualization', 
                    fontsize=14, fontweight='bold')
        
        ax.set_xlabel('X (meters)')
        ax.set_ylabel('Y (meters)')
        ax.set_zlabel('Z (meters)')
        
        # Set equal aspect ratio
        ax.set_xlim(-0.6, 0.6)
        ax.set_ylim(-0.4, 0.4)
        ax.set_zlim(0, 1.0)
        
        plt.tight_layout()
        plt.savefig('mhm_3d_visualization.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        return fig
    
    def create_component_diagram(self):
        """Create detailed component diagram"""
        fig, ax = plt.subplots(1, 1, figsize=(16, 12))
        
        # Component boxes with connections
        components = {
            'Power Supply': {'pos': (2, 8), 'size': (2, 1), 'color': '#FF6B6B'},
            'Main Controller': {'pos': (6, 8), 'size': (2.5, 1), 'color': '#4ECDC4'},
            'MOSFET Drivers': {'pos': (10, 8), 'size': (2, 1), 'color': '#45B7D1'},
            'Current Sensors': {'pos': (2, 6), 'size': (2, 1), 'color': '#96CEB4'},
            'IMU Sensor': {'pos': (6, 6), 'size': (1.5, 1), 'color': '#FFEAA7'},
            'Distance Sensors': {'pos': (9, 6), 'size': (2, 1), 'color': '#DDA0DD'},
            'Emergency Stop': {'pos': (12, 6), 'size': (1.5, 1), 'color': '#FF7675'},
            'Coil 1': {'pos': (1, 3), 'size': (1.5, 1), 'color': self.colors['coils']},
            'Coil 2': {'pos': (3, 3), 'size': (1.5, 1), 'color': self.colors['coils']},
            'Coil 3': {'pos': (5, 3), 'size': (1.5, 1), 'color': self.colors['coils']},
            'Coil 4': {'pos': (7, 3), 'size': (1.5, 1), 'color': self.colors['coils']},
            'Coil 5': {'pos': (9, 3), 'size': (1.5, 1), 'color': self.colors['coils']},
            'Coil 6': {'pos': (11, 3), 'size': (1.5, 1), 'color': self.colors['coils']},
            'Coil 7': {'pos': (3, 1), 'size': (1.5, 1), 'color': self.colors['coils']},
            'Coil 8': {'pos': (6, 1), 'size': (1.5, 1), 'color': self.colors['coils']},
            'Coil 9': {'pos': (9, 1), 'size': (1.5, 1), 'color': self.colors['coils']},
        }
        
        # Draw components
        for name, spec in components.items():
            x, y = spec['pos']
            w, h = spec['size']
            
            rect = FancyBboxPatch((x-w/2, y-h/2), w, h,
                                boxstyle="round,pad=0.1",
                                facecolor=spec['color'],
                                edgecolor='black',
                                linewidth=2,
                                alpha=0.8)
            ax.add_patch(rect)
            
            # Add text
            ax.text(x, y, name, ha='center', va='center',
                   fontsize=9, fontweight='bold',
                   wrap=True)
        
        # Draw connections
        connections = [
            # Power connections
            ('Power Supply', 'Main Controller'),
            ('Power Supply', 'MOSFET Drivers'),
            
            # Control connections
            ('Main Controller', 'MOSFET Drivers'),
            ('Main Controller', 'IMU Sensor'),
            ('Main Controller', 'Distance Sensors'),
            ('Main Controller', 'Emergency Stop'),
            
            # Sensor connections
            ('Current Sensors', 'Main Controller'),
            
            # Coil connections (simplified)
            ('MOSFET Drivers', 'Coil 1'),
            ('MOSFET Drivers', 'Coil 2'),
            ('MOSFET Drivers', 'Coil 3'),
            ('MOSFET Drivers', 'Coil 4'),
            ('MOSFET Drivers', 'Coil 5'),
            ('MOSFET Drivers', 'Coil 6'),
            ('MOSFET Drivers', 'Coil 7'),
            ('MOSFET Drivers', 'Coil 8'),
            ('MOSFET Drivers', 'Coil 9'),
        ]
        
        for start, end in connections:
            start_pos = components[start]['pos']
            end_pos = components[end]['pos']
            
            ax.annotate('', xy=end_pos, xytext=start_pos,
                       arrowprops=dict(arrowstyle='->', color='gray', lw=1.5))
        
        ax.set_title('MHM System Component Diagram', fontsize=16, fontweight='bold', pad=20)
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 10)
        ax.set_aspect('equal')
        ax.axis('off')
        
        plt.tight_layout()
        plt.savefig('mhm_component_diagram.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        return fig
    
    def generate_cost_breakdown_chart(self):
        """Generate visual cost breakdown chart"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
        
        # Cost categories
        categories = ['Magnets', 'Coils', 'Electronics', 'Platform', 'Power System', 'Tools', 'Misc']
        costs = [4700, 950, 3220, 1400, 1450, 2800, 1000]
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD', '#FFB6C1']
        
        # Pie chart
        wedges, texts, autotexts = ax1.pie(costs, labels=categories, colors=colors, autopct='%1.1f%%',
                                          startangle=90, textprops={'fontsize': 10})
        ax1.set_title('Cost Breakdown by Category', fontsize=14, fontweight='bold')
        
        # Bar chart
        bars = ax2.bar(categories, costs, color=colors, edgecolor='black', linewidth=1)
        ax2.set_title('Component Costs ($USD)', fontsize=14, fontweight='bold')
        ax2.set_ylabel('Cost ($)', fontsize=12)
        ax2.tick_params(axis='x', rotation=45)
        
        # Add value labels on bars
        for bar, cost in zip(bars, costs):
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height + 50,
                    f'${cost:,}', ha='center', va='bottom', fontweight='bold')
        
        # Total cost annotation
        total_cost = sum(costs)
        fig.suptitle(f'MHM System Build Cost Analysis - Total: ${total_cost:,}', 
                    fontsize=16, fontweight='bold')
        
        plt.tight_layout()
        plt.savefig('mhm_cost_breakdown.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        return fig

def main():
    """Generate all visual blueprints"""
    print("\n📐 GENERATING MHM VISUAL BLUEPRINTS")
    print("="*50)
    
    generator = MHMBlueprintGenerator()
    
    print("\n🔄 Creating blueprints...")
    
    # Generate all visualizations
    generator.create_top_view_blueprint()
    generator.create_side_view_blueprint()
    generator.create_3d_visualization()
    generator.create_component_diagram()
    generator.generate_cost_breakdown_chart()
    
    print("\n✅ All blueprints generated successfully!")
    print("📁 Files saved:")
    print("  • mhm_top_view_blueprint.png")
    print("  • mhm_side_view_blueprint.png")
    print("  • mhm_3d_visualization.png")
    print("  • mhm_component_diagram.png")
    print("  • mhm_cost_breakdown.png")
    
    print("\n🌸 MHM: Complete visual documentation ready!")

if __name__ == "__main__":
    main()
