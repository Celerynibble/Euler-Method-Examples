These are examples for Euler's method using python code. Euler's method is a method to solve diff equations where the problem is handled from the initial condition and nudged slightly based on the equation to the next state. A slow plot eventually provides us with a complete description of what happened.
if each nudge took dt long, we would recover the exact motion since that is what calculus is all about but on the computer we can only take values that are small enough relative to the other values. Therefore, what we obtain is only an approximation.
First three examples are examples of recursively updating the arrays and allowing the system to evolve. Fourth example, there is a more explicit use of a differential equation.

Air Resistance

using a velocity dependant air resistance, arrays for position, velocity and acceleration are repeatedly updated to see its changes. The acceleration is updated based on the net force, the velocity is updated based on acceleration and position is updated based on velocity.
A projectile's trajectory with air resistance is plotted

Orbits

A central force problem. Arrays are updated based on the acceleration, velocity and position at each moment. The trajectory is plotted. Each conic section is observed in the orbit for different intial velocities

Rutherford Scattering

A repulsive central force problem. Arrays are similarly updated and trajectory is plotted. Impact parameter is varied to see changes in trajectory and scattering angle
