<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width=50% height=50%>
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

<img src="img/Robot.png" alt="The robot" width=50% height=50%>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

#### Mounting Plate

#### Jetson Case

#### Camera Mount

#### Box


### Schematics

Wire Diagram
<img src="images/robot.png" alt="The robot" width="80" height="80">

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








<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 







