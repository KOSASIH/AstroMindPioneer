import numpy as np
import matplotlib.pyplot as plt

class CelestialSimulator:
    def __init__(self):
        self.bodies = []
    
    def add_body(self, position, velocity):
        """
        Add a celestial body with its initial position and velocity.
        
        Parameters:
        - position: a tuple or list representing the initial x and y coordinates of the body
        - velocity: a tuple or list representing the initial velocities in the x and y directions
        """
        body = {'position': np.array(position), 'velocity': np.array(velocity)}
        self.bodies.append(body)
    
    def update_positions(self, time_step, gravitational_constant):
        """
        Update the positions of all celestial bodies based on gravitational interactions.
        
        Parameters:
        - time_step: the time step for the simulation
        - gravitational_constant: the gravitational constant to use in the calculations
        """
        for i in range(len(self.bodies)):
            for j in range(len(self.bodies)):
                if i != j:
                    body1 = self.bodies[i]
                    body2 = self.bodies[j]
                    position1 = body1['position']
                    position2 = body2['position']
                    velocity1 = body1['velocity']
                    velocity2 = body2['velocity']
                    
                    distance = np.linalg.norm(position2 - position1)
                    acceleration = gravitational_constant * (position2 - position1) / distance**3
                    
                    body1['position'] += velocity1 * time_step
                    body1['velocity'] += acceleration * time_step
    
    def generate_visualization(self):
        """
        Generate a markdown visualization of the simulated universe at a given time step.
        The visualization includes a 2D representation of the celestial bodies' positions and labels for each body.
        """
        plt.figure(figsize=(8, 8))
        
        for body in self.bodies:
            position = body['position']
            plt.scatter(position[0], position[1], s=100, label=f"Body {self.bodies.index(body)+1}")
        
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Celestial Bodies Simulation')
        plt.legend()
        plt.grid(True)
        plt.show()
