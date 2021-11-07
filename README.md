# physics-hackathon-2021

## Membrane vibration with energy dissipation based on temperature

![magic](wizardry.gif)

# Introduction

Make some noise! 

You take the sound of a hammer banging on a nail, some random person screaming at an auction or perhaps record the residual noise from the birth of the universe and put these sounds together in a cohesive rhythmic way and, if done right, you might have yourself a piece of music!

The point is: we are surrounded by a ton of cool sounds/signals that can be used to make music. So why not simulate some of the systems around us in a mega bruteforce way and     H E A R     T H E    D A R N    T H I N G. This is what we're doing here. 

In a normal setting, you don't hear the thermal fluctuations affecting your guitar string or your drumhead when you play it, but let's be hardcore. Would the quality of that sound depend on the temperature? These were some of the motivating questions for our project. By combining the classical vibrations of a surface with characteristic surface thermal fluctuations, we have attempted to model a physically valid membrane which can, in principle, be parametrized to play different sounds.

# The Physics

We won't go into a big technical discussion of surfaces here. We'll only talk about the intuitive concepts.

Here we have **2** things we want to model:

1. The classic motion of an oscillating membrane/surface under the laws of Newtonian mechanics.
2. The thermal fluctuations that occur in systesm such as the interface between two phases of a substance (say at the triple point or something like that).

The classic motion of the surface is well understood using tools such as the wave equation, however, we decided to do the simulation numerically using Hooke's law and stuff of the sort (for every tiny piece of the membrane)! On top of that, we even added some thermal randomness to the system, where our "elastic" membrane reacts at 


# Method

Using odeint solve in the Numpy library, we were able to model the vibrations on the surface as a function of the tension associated with the neighbouring points. At each time step, the energy functional is evaluated and the next state of that system established with the following formula: 

<img src="https://render.githubusercontent.com/render/math?math=E_{\text{2D}}[h]=\sum_{i, j}(h_{i, j} - h_{i %2B 1, j})^2 %2B (h_{i, j} - h_{i, j %2B 1})^2">


The additional fluctuations add some noise to the classical vibrations that would mimic the behaviour of an energy dissipating membrane (as will be heard?)

I'm realizing I do not understand what is going on nearly well enough....
