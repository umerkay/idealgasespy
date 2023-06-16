# Gas Molecules Simulation

This project is a gas molecules simulation that visualizes the behavior of particles in a gas environment. It provides a sandbox interface built with Tkinter that allows users to interactively edit simulation variables.

## Getting Started

### Prerequisites
- Python 3.x
- Pygame
- Tkinter

### Installation
1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/gas-molecules-simulation.git
   ```

2. Install the dependencies:

   ```bash
   pip install pygame
   ```

## Usage

1. Run the simulation:

   ```bash
   python main.py
   ```

2. The simulation window will open, displaying the gas molecules and their movements.

3. Sandbox Interface:
   - **Reset**: Click the "Reset" button to clear all particles and start a new simulation.
   - **Show Cloud**: Toggle this checkbox to show/hide the visualization of gas cloud.
   - **Electron Interactions**: Toggle this checkbox to enable/disable electron interactions.
   - **Anti-aliasing**: Toggle this checkbox to enable/disable anti-aliasing for smoother graphics.
   - **Temperature**: Use the slider to adjust the temperature (in Kelvin) of the gas molecules.
   - **IMF Coefficient**: Use the slider to adjust the coefficient of intermolecular forces.
   - **Gravity**: Use the slider to adjust the strength of gravity.

4. Interacting with the simulation:
   - Clicking on the simulation window will add a new gas molecule at the clicked position.
   - Moving the mouse while holding the left mouse button pressed will continuously add new gas molecules.

5. Close the simulation window or press Ctrl+C in the terminal to stop the simulation.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to submit a pull request.
