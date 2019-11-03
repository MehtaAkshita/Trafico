# Trafico
# Problems Our Project Solves:
- Traffic signal timings in a road network can not only affect total user travel time and total amount of traffic emissions in the network but also create an inequity problem in terms of the change in travel costs of users traveling between different locations .Traffic congestion in peak hours in major cities of Delhi, Mumbai ,Kolkata and Bengaluru costs the economy 1.47 lakh crores annually.
- Due to heavy amount of traffic ambulances must suffer a lot. Every minute is critical for a patient and getting stuck in traffic for long hours further deteriorates their condition.

# Overview:
There are 2 models:
1)Connected Cars
2)Traffic Control

# A description of our project:
Traffic Signal Optimization: By processing live videos via CCTV footages on the streets we check the car density on each lane. Then after collecting the real-time data for 30 sec from the angle where the red light is facing or opposite to it. After 15 min we change the timings to be given to each of the traffic signals by giving higher priority to the lane which has a higher density of cars.
Connecting cars: This module has been created with the intention of assisting the ambulances in taking their patients to the hospital on time. Once the ambulance defines its path to the hospital based on its real time location all the cars within a distance of 1km in front of its defined path with get an alert SMS notifying that there is an ambulance wanting to come through and the direction the car should move to.

# How to use
- Run extra.py to see how module 1 is working.
- Run Connected_vehicle.py to see how module 2 is working.
