
<a name="readme-top"></a>


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="img/logo.png" alt="Logo" width=50% height=50%>
  </a>

  <h3 align="center">ECE/MAE 148 Winter 2023 Team 9</h3>
    
  <p align="center">
    <li>JetBuddy</li>
    <li>Indoor Delivery Bot based on DepthAI, OpenCV and LiDAR</li>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#team-members">Team Members</a></li>
    <li>
      <a href="#hardware">Hardware and Schematics</a>
      <ul>
        <li><a href="#parts">Parts</a></li>
        <li><a href="#schematics"> Schematics</a></li>
      </ul>
    </li>
    <li><a href="#donkey">Donkey</a></li>
    <li><a href="#final-project">Final Project</a></li>
     <ul>
        <li><a href="#abstract">Abstract</a></li>
        <li><a href="#part-1-human-detection-and-following-with-depthai-and-pyvesc">Part 1: Human Detection and Following with Depthai and PyVesc</a></li>
        <li><a href="#part-2-stopping-mechanism-with-lidar"> Part 2: Stopping Mechanism with Lidar</a></li>
        <li><a href="#part-3-facial-recognition"> Part 3: Facial Recognition</a></li>
      </ul>
  </ol>
</details>
<!-- ABOUT THE TEAM -->

## Team members

* Ben Zhang (ECE)
* Joseph Katona (ECE) 
* Yichen Yang (ECE)
* Zijian Wang (MAE)

<img src="img/Team.png" alt="The Team" width=40% height=40%>



<!-- ABOUT THE PROJECT -->
## Hardware


<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Parts

#### Full Assembly

<img src="img/Robot.png" alt="The robot" width=30% height=30%>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

#### Mounting Plate
<img src="img/board2.png" alt="Mounting Board" width=30% height=30%>


#### Jetson Case
<img src="img/bot.png" alt="Case Top" width=30% height=30%>
<img src="img/bottom.png" alt="Case Bottom" width=30% height=30%>

#### Camera LiDAR Mount

<img src="img/caml.png" alt="The Camera and LiDAR mount" width=30% height=30%>

#### Final Project Delivery Box

<img src="img/box.png" alt="The box" width=30% height=30%>

### Schematics

### Wire Diagram

<img src="img/wire.png" alt="The Wire diagram" width=30% height=30%>

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- Final Project -->
## Final Project

### Abstract<a name="abstract"></a>
This project aims to develop a delivery system for our robocar that can detect and follow humans while also incorporating a stopping mechanism to prevent collisions. Additionally, the robot will utilize facial recognition to identify individuals and personalize interactions.

### Part 1: Human Detection and Following with Depthai and PyVesc <a name="part-2-human-detection-and-following-with-depthai-and-pyvesc"></a>
The OAKD camera will be used to detect and track humans in the robot's vicinity. The PyVesc motor controllers will then be used to move the robot in the direction of the detected human.

### Part 2: Stopping Mechanism with Lidar<a name="part-3-stopping-mechanism-with-lidar"></a> 
The Lidar sensor will be used to detect obstacles in the robot's path. If an obstacle is detected, the robot will stop moving and wait for the obstacle to clear before continuing on its path.

### Part 3: Facial Recognition<a name="part-4-facial-recognition"></a>  
The robot will be equipped with a facial recognition system, using a webcam, that will allow it to identify individuals and personalize interactions. Once it recognizes the right person, the delivery box will open.

### Gantt Chart

<img src="img/gantt.png" alt="The Gantt Chart" width=30% height=30%>
