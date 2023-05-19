# MPPT Live Data Plot

For my capstone final project in Electrical Engineering at The University of Western Ontario, my team and I made a Maximum Power Point Tracker.

The purpose of our MPPT was to optimally charge a Li-Po battery from a solar array. This is done by determining the output voltage which maximizes power transfer from the solar array to the battery.

<p align="center">
  <img src=".docs/PV-Curve.jpg" alt="Image" />
</p>
<p align="center">PV Characteristics</p>

This voltage is Vmp in the above image. Operating a MPPT at this voltage facilitates maxium power transfer (Pmax).

To track the performance of our MPPT, I created a Python script which reads serial data from our MPPT and plots the PV characteristics in real-time. The script also logs the values in a CSV file.

<p align="center">
  <video controls>
    <source src=".docs/PV-Characteristics" type="video/mp4">
  </video>
</p>
