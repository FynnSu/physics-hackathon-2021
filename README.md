# physics-hackathon-2021

## Membrane vibration with energy dissipation based on temperature

![magic](wizardry.gif)

# Overview

Could lakes make sound? Would the quality of that sound depend on the temperature? These were some of the motivating questions for our project. By combining the classical vibrations of a surface with characteristic surface fluctuations, we have attempted to model a physically valid membrane which can, in principle, be parametrized to play different sounds.

# The combination of the two vibrations 

Using odeint solve in the Numpy library, we were able to model the vibrations on the surface as a function of the tension associated with the neighbouring points. At each time step, the energy functional is evaluated and the next state of that system established with the following formula: 

<img src="https://render.githubusercontent.com/render/math?math=E_{\text{2D}}[h]=\sum_{i, j}(h_{i, j} - h_{i+1, j})^2+(h_{i, j} - h_{i, j+1})^2">


The additional fluctuations add some noise to the classical vibrations that would mimic the behaviour of an energy dissipating membrane (as will be heard?)

I'm realizing I do not understand what is going on nearly well enough....
