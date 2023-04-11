"""
Module to create map with the nearest location
"""


import folium
from get_nearest import get_nearest
from get_marker import parse_markers, get_nearest_english, parse_english_markers


html_ukr = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mark</title>
    <link rel="stylesheet" href="mark.css">
</head>
<body>
    <div class="mark" style= "width: 130px;
height: 75px;
background-color: white;
border-radius: 10px;
opacity: 85%;
display: flex;
flex-direction: column;
justify-content: space-between;
align-items: center;
flex-wrap: wrap;">
        <div class="mark1" style="width: 140px;
    height: 12px;
    background-color: white;
    border-radius: 10px;
    opacity: 80%;
    font-size: 36px;
    margin-bottom: 25px;
    font-family: 'Times New Roman';
    font-weight: bold;
    text-decoration: none;
    padding: 2px;
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 3px 0;
    display: flex; /* встановлюємо flex-контейнер */
    justify-content: center; /* вирівнюємо по горизонталі */
    align-items: center;">
            <a href="#" class="mark1" style="width: 140px;
    height: 12px;
    background-color: white;
    border-radius: 10px;
    opacity: 80%;
    margin-bottom: 25px;
    font-family: 'Times New Roman';
    font-size: 36px;
    font-weight: bold;
    text-decoration: none;
    padding: 2px;
    color: black;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 3px 0;
    font-size: medium;
    display: flex; /* встановлюємо flex-контейнер */
    justify-content: center; /* вирівнюємо по горизонталі */
    align-items: center;">{address}</a>
        </div>
        <div class="mark2 d-flex justify-content-center" style = "width: 140px;
    height: 13px;
    background-color: white;
    border-radius: 10px;
    opacity: 80%;
    margin-bottom: 15px;
    font-family: 'Times New Roman';
    font-size: 36px;
    font-weight: bold;
    text-decoration: none;
    padding: 2px;
    color: black;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 3px 0;
    font-size: large;
    display: flex; /* встановлюємо flex-контейнер */
    justify-content: center; /* вирівнюємо по горизонталі */
    align-items: center;">
            <a href="#" class="mark2 d-flex justify-content-center" style="width: 140px;
    height: 13px;
    background-color: white;
    border-radius: 10px;
    opacity: 80%;
    margin-bottom: 15px;
    font-family: 'Times New Roman';
    font-size: 36px;
    font-weight: bold;
    text-decoration: none;
    padding: 2px;
    color: black;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 3px 0;
    font-size: large;
    display: flex; /* встановлюємо flex-контейнер */
    justify-content: center; /* вирівнюємо по горизонталі */
    align-items: center;">{distance}</a>
        </div>
        <div class="mark3" style ="width: 140px;
    height: 14px;
    background-color: white;
    border-radius: 10px;
    opacity: 80%;
    margin-top: 30px;
    font-family: 'Times New Roman';
    font-size: 36px;
    font-weight: bold;
    text-decoration: none;
    color: black;
    margin: 3px 0;
    padding: 1px;
    font-size: large;
    display: flex; /* встановлюємо flex-контейнер */
    justify-content: center; /* вирівнюємо по горизонталі */
    align-items: center; /* вирівнюємо по вертикалі */
    text-decoration: underline;">
            <a href="https://www.google.com.ua/maps/place/{lt}%20{ln}" class="mark3" style ="width: 140px;
    height: 14px;
    background-color: white;
    border-radius: 10px;
    opacity: 80%;
    margin-top: 30px;
    font-family: 'Times New Roman';
    font-size: 36px;
    font-weight: bold;
    text-decoration: none;
    color: black;
    margin: 3px 0;
    padding: 1px;
    font-size: large;
    display: flex; /* встановлюємо flex-контейнер */
    justify-content: center; /* вирівнюємо по горизонталі */
    align-items: center; /* вирівнюємо по вертикалі */
    text-decoration: underline;">Знайти</a>
        </div>
    </div>
</body>
</html>
"""
html_eng = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mark</title>
    <link rel="stylesheet" href="mark.css">
</head>
<body>
    <div class="mark" style= "width: 130px;
height: 75px;
background-color: white;
border-radius: 10px;
opacity: 85%;
display: flex;
flex-direction: column;
justify-content: space-between;
align-items: center;
flex-wrap: wrap;">
        <div class="mark1" style="width: 140px;
    height: 12px;
    background-color: white;
    border-radius: 10px;
    opacity: 80%;
    font-size: 36px;
    margin-bottom: 25px;
    font-family: 'Times New Roman';
    font-weight: bold;
    text-decoration: none;
    padding: 2px;
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 3px 0;
    display: flex; /* встановлюємо flex-контейнер */
    justify-content: center; /* вирівнюємо по горизонталі */
    align-items: center;">
            <a href="#" class="mark1" style="width: 140px;
    height: 12px;
    background-color: white;
    border-radius: 10px;
    opacity: 80%;
    margin-bottom: 25px;
    font-family: 'Times New Roman';
    font-size: 36px;
    font-weight: bold;
    text-decoration: none;
    padding: 2px;
    color: black;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 3px 0;
    font-size: medium;
    display: flex; /* встановлюємо flex-контейнер */
    justify-content: center; /* вирівнюємо по горизонталі */
    align-items: center;">{address}</a>
        </div>
        <div class="mark2 d-flex justify-content-center" style = "width: 140px;
    height: 13px;
    background-color: white;
    border-radius: 10px;
    opacity: 80%;
    margin-bottom: 15px;
    font-family: 'Times New Roman';
    font-size: 36px;
    font-weight: bold;
    text-decoration: none;
    padding: 2px;
    color: black;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 3px 0;
    font-size: large;
    display: flex; /* встановлюємо flex-контейнер */
    justify-content: center; /* вирівнюємо по горизонталі */
    align-items: center;">
            <a href="#" class="mark2 d-flex justify-content-center" style="width: 140px;
    height: 13px;
    background-color: white;
    border-radius: 10px;
    opacity: 80%;
    margin-bottom: 15px;
    font-family: 'Times New Roman';
    font-size: 36px;
    font-weight: bold;
    text-decoration: none;
    padding: 2px;
    color: black;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 3px 0;
    font-size: large;
    display: flex; /* встановлюємо flex-контейнер */
    justify-content: center; /* вирівнюємо по горизонталі */
    align-items: center;">{distance}</a>
        </div>
        <div class="mark3" style ="width: 140px;
    height: 14px;
    background-color: white;
    border-radius: 10px;
    opacity: 80%;
    margin-top: 30px;
    font-family: 'Times New Roman';
    font-size: 36px;
    font-weight: bold;
    text-decoration: none;
    color: black;
    margin: 3px 0;
    padding: 1px;
    font-size: large;
    display: flex; /* встановлюємо flex-контейнер */
    justify-content: center; /* вирівнюємо по горизонталі */
    align-items: center; /* вирівнюємо по вертикалі */
    text-decoration: underline;">
            <a href="https://www.google.com.ua/maps/place/{lt}%20{ln}" class="mark3" style ="width: 140px;
    height: 14px;
    background-color: white;
    border-radius: 10px;
    opacity: 80%;
    margin-top: 30px;
    font-family: 'Times New Roman';
    font-size: 36px;
    font-weight: bold;
    text-decoration: none;
    color: black;
    margin: 3px 0;
    padding: 1px;
    font-size: large;
    display: flex; /* встановлюємо flex-контейнер */
    justify-content: center; /* вирівнюємо по горизонталі */
    align-items: center; /* вирівнюємо по вертикалі */
    text-decoration: underline;">Search</a>
        </div>
    </div>
</body>
</html>
"""
checkbox_ukr_chrome = """
<style>
  body{
    overflow: hidden;
  }
  .leaflet-top.leaflet-left{
    display: none;
  }
  #menu-box{
    position: absolute;
    z-index: 900;
    /*left: 40vw;
    top: 60vh;*/
    height: auto;
    width: auto;
  }
  #menu-box-information{
    position: fixed;
    width: 20vw;
    /*height: 25vh;*/
    height: auto;
    z-index: 900;
    border: 1px solid black;
    background-color: #006e48;
    border-radius: 20px;
    opacity: 80%;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    padding: 2vh;
    overflow-y: auto;
    overflow-x: hidden;
  }
  @media (max-width: 768px) {
    #menu-box-information{
          position: fixed;
          width: 60vw;
          height: 45vh;
          height: auto;
          z-index: 900;
          border: 1px solid black;
          background-color: #006e48;
          border-radius: 20px;
          opacity: 80%;
          flex-direction: column;
          justify-content: space-between;
          align-items: center;
          padding: 2vh;
          overflow-y: auto;
          overflow-x: hidden;
    }
    .menu-box-revealed{
        transform: translate3d(19.5vw, 35vh, 0);
        transition: transform 1.0s cubic-bezier(0, .52, 0, 1);
      }
      .menu-box-hidden{
        transform: translate3d(19.5vw, 100vh, 0);
        transition: transform 2.0s cubic-bezier(0, .52, 0, 1);
  }
      #closing-checkboxes {
          position: absolute;
          z-index: 900;
          top: 32vh;
          left: 24vw;
      }
  }
  @media (min-width: 767px) {
      #menu-box-information {
          position: fixed;
          width: 40vw;
          /*height: 25vh;*/
          height: auto;
          z-index: 900;
          border: 1px solid black;
          background-color: #006e48;
          border-radius: 20px;
          opacity: 80%;
          flex-direction: column;
          justify-content: space-between;
          align-items: center;
          padding: 2vh;
          overflow-y: auto;
          overflow-x: hidden;
      }

      .menu-box-revealed {
          transform: translate3d(30vw, 46vh, 0);
          transition: transform 1.0s cubic-bezier(0, .52, 0, 1);
      }

      .menu-box-hidden {
          transform: translate3d(30vw, 100vh, 0);
          transition: transform 2.0s cubic-bezier(0, .52, 0, 1);
      }

      #closing-checkboxes {
          position: absolute;
          z-index: 900;
          top: 32vh;
          left: 18.5vw;
      }
  }

  .label{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-radius: 10px;
    margin-right: 10px;
    font-size: 2vmin;
    transition: 1s;
    flex-grow: 1;
    min-width: 0;
    padding: 5px;
    background-color: #f8f8f8;
    margin: 1px;
    padding-bottom: 1px;
    padding-top: 1px;
    color: black;
    height: auto;
  }
  .check {
    position: relative;
    width: 20px;
    height: 20px;
    border-radius: 2px;
    appearance: none;
    background-color: #bbb;
    transition: all .3s;
  }

  .check::before {
    content: '';
    position: absolute;
    border: solid #fff;
    display: block;
    width: .3em;
    height: .6em;
    border-width: 0 .2em .2em 0;
    z-index: 1;
    opacity: 0;
    right: calc(50% - .3em);
    top: calc(50% - .6em);
    transform: rotate(0deg);
    transition: all .3s;
    transform-origin: center center;
  }

  .check:checked {
    animation: a .3s ease-in forwards;
    background-color: #00a97e;
  }

  .check:checked::before {
    opacity: 1;
    transform: rotate(405deg);
  }

  @keyframes a {
    0% {
      opacity: 1;
      transform: scale(1) rotateY(0deg);
    }

    50% {
      opacity: 0;
      transform: scale(.8) rotateY(180deg);
    }

    100% {
      opacity: 1;
      transform: scale(1) rotateY(360deg);
    }
  }
  .btn {
    display: flex;
    justify-content: center;
    align-items: center;
    --color: #ffff;
    --color2: rgb(10, 25, 30);
    font-size: 2vmin;
    transition: 1s;
    flex-grow: 1;
    padding: 0.8em 1.75em;
    background-color: transparent;
    border-radius: 6px;
    border: .3px solid var(--color);
    position: relative;
    overflow: hidden;
    cursor: pointer;
    margin: 1vh auto;
    z-index: 900;
    font-family: 'Roboto', 'Segoe UI', sans-serif;
    text-transform: uppercase;
    color: var(--color);
  }

  .btn::after, .btn::before {
    content: '';
    display: block;
    height: 100%;
    width: 100%;
    transform: skew(90deg) translate(-50%, -50%);
    position: absolute;
    inset: 50%;
    left: 25%;
    z-index: -1;
    transition: .5s ease-out;
    background-color: var(--color);
  }

  .btn::before {
    top: -50%;
    left: -25%;
    transform: skew(90deg) rotate(180deg) translate(-50%, -50%);
  }

  .btn:hover::before {
    transform: skew(45deg) rotate(180deg) translate(-50%, -50%);
  }

  .btn:hover::after {
    transform: skew(45deg) translate(-50%, -50%);
  }

  .btn:hover {
    color: var(--color2);
  }

  .btn:active {
    filter: brightness(.7);
    transform: scale(.98);
  }
  @media (max-width: 768px) {
        #arrow-up{
        position: absolute;
        z-index: 900;
        top: 60vh;
        left: 44vw;
      }
  }
  @media (min-width: 767px){
        #arrow-up{
        position: absolute;
        z-index: 900;
        top: 80vh;
        left: 48vw;
      }
  }


  #menu-button {
    position: absolute;
    display: block;
    z-index: 900;
    top: 50vh;
      left: 5vw;
  }
  @media (min-width: 768px){
    #image-overlay {
      display: flex;
      z-index: 900;
      position: absolute;
      flex-direction: column;
      justify-content: flex-start;
      align-items: flex-start;
      margin: 0;
      width: 30vw;
      height: 100vh;
      background-color: #00a97e;
      opacity:85%;
      border: 2px solid rgb(5, 102, 52);
      overflow: hidden;
    }
  .donat{
      background-color: black; /* Green */
      border: none;
      color: white;
      padding: 15px 32px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 16px;
      width: 300px;
      margin-top: 3vh;
      margin-bottom: 3vh;
      margin-left: 3vw
  }
  }
  @media (max-width: 767px){
    #image-overlay {
      display: flex;
      z-index: 900;
      position: absolute;
      flex-direction: column;
      justify-content: flex-start;
      align-items: flex-start;
      margin: 0;
      width: 100vw;
      height: 100vh;
      background-color: #00a97e;
      opacity:85%;
      border: 2px solid rgb(5, 102, 52);
      overflow: hidden;
    }
  .donat{
      position: relative;
      background-color: black; /* Green */
      border: none;
      color: white;
      padding: 15px 32px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 16px;
      width: 300px;
      margin-top: 3vh;
      margin-bottom: 3vh;
      margin-left: 10vw;
  }
  }
  .menu-revealed{
    transform: translate3d(0vw, 0vh, 0);
    transition: transform 1.0s cubic-bezier(0, .52, 0, 1);
  }
  .menu-hidden{
    transform: translate3d(-100vw, 0vh, 0);
    transition: transform 2.0s cubic-bezier(0, .52, 0, 1);
  }
  #image-overlay a {
    display: block;
    z-index: 900;
    position: relative;
    color: #fff;
    text-decoration: line-under;
    margin: 10px 10px 0 10px;
    transition: 2s;
    height: 5vh;
    text-align: center;
    line-height: 1.5;
  }

  #image-overlay a:hover {
    font-size: 34px;
    color: rgb(238, 253, 236);
  }
  #logo{
    position: relative;
    z-index: 900;
    width: auto;
    height: auto;
    max-width: 30vw;
    max-height: 20vh;
  }
  h3 {
      margin-top: 2vh;
      margin-bottom: 2vh;
      font-size: 3.5vmin;
  }
  @media only screen and (max-width: 767px){
    h3{
      font-size: 20px;
    }
  }


  #legenda-button{
    position: absolute;
    z-index: 900;
    top: 50vh;
    left: 90vw;
  }
  @media (max-width: 768px){
    #legenda-button{
      left: 85vw;
    }
  }
  #sidebar {
    position: fixed;
    z-index: 900;
    background-color: #00a97e;
    opacity:85%;
    border: 2px solid rgb(5, 102, 52);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  @media (min-width: 768px){
    #sidebar {
      height: 100vh;
      width: 30vw;
    }
    .sidebar-revealed{
      transform: translate3d(70vw, 0vh, 0);
      transition: transform 1.0s cubic-bezier(0, .52, 0, 1);
    }
    .sidebar-hidden{
      transform: translate3d(200vw, 0vh, 0);
      transition: transform 3.0s cubic-bezier(0, .52, 0, 1);
    }
  }
  @media (max-width: 767px){
    #sidebar {
      width: 100vw;
      height: 100vh
    }
    .sidebar-revealed{
      transform: translate3d(0, 0, 0);
      transition: transform 1.0s cubic-bezier(0, .52, 0, 1);
    }
    .sidebar-hidden{
      transform: translate3d(200vw, 0vh, 0);
      transition: transform 2.0s cubic-bezier(0, .52, 0, 1);
    }
    #closing-legenda{
        z-index: 900;
        position: absolute;
        left: 20vw;
    }
  }
  #sidebar .image {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin: 10px 0;
    width: 100%;
    text-align: center;
  }

  #sidebar .image img {
    height: 10vh;
    margin: 7px;
    width: auto;
    max-width: 100%;
    max-height: 100%;
  }

  #sidebar .caption {
    margin-top: 5px;
    font-size: 1.5rem;
    color: #ffff;
  }

  #checked-checkbox{
      position: absolute;
      z-index: 900;
      display: none;
  }


</style>
<script>
  function showCheckBoxesMenu(){
    document.getElementById('menu-box').classList.remove('menu-box-hidden');
    document.getElementById('menu-box').classList.add('menu-box-revealed');
    document.getElementById('arrow-up').style.display = 'none';
    document.getElementById('menu-button').style.display = 'none';
    document.getElementById('legenda-button').style.display = 'none';

  }
  function hideCheckBoxesMenu(){
    document.getElementById('menu-box').classList.remove('menu-box-revealed');
    document.getElementById('menu-box').classList.add('menu-box-hidden');
    document.getElementById('arrow-up').style.display = 'block';
    document.getElementById('menu-button').style.display = 'block';
    document.getElementById('legenda-button').style.display = 'block';
  }


  function showInfoMenu(){
    document.getElementById('image-overlay').classList.remove('menu-hidden');
    document.getElementById('image-overlay').classList.add('menu-revealed');
    document.getElementById('menu-button').style.display = 'none';
    document.getElementById('arrow-up').style.display = 'none';
    document.getElementById('legenda-button').style.display = 'none';
  }
  function hideInfoMenu(){
    document.getElementById('image-overlay').classList.remove('menu-revealed');
    document.getElementById('image-overlay').classList.add('menu-hidden');
    document.getElementById('menu-button').style.display = 'block';
    document.getElementById('arrow-up').style.display = 'block';
    document.getElementById('legenda-button').style.display = 'block';
  }


  function showLegenda(){
    document.getElementById('sidebar').classList.remove('sidebar-hidden');
    document.getElementById('sidebar').classList.add('sidebar-revealed');
    document.getElementById('menu-button').style.display = 'none';
    document.getElementById('arrow-up').style.display = 'none';
    document.getElementById('legenda-button').style.display = 'none';
  }
  function hideLegenda(){
    document.getElementById('sidebar').classList.remove('sidebar-revealed');
    document.getElementById('sidebar').classList.add('sidebar-hidden');
    document.getElementById('menu-button').style.display = 'block';
    document.getElementById('arrow-up').style.display = 'block';
    document.getElementById('legenda-button').style.display = 'block';
  }

</script>
<div onclick="showInfoMenu()" id="menu-button">
  <svg color="green" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-chevron-compact-right" viewBox="0 0 16 16">
    <path fill-rule="evenodd" d="M6.776 1.553a.5.5 0 0 1 .671.223l3 6a.5.5 0 0 1 0 .448l-3 6a.5.5 0 1 1-.894-.448L9.44 8 6.553 2.224a.5.5 0 0 1 .223-.671z"/>
  </svg>
</div>
<div class="menu-hidden" id="image-overlay">
  <img id="logo" src="https://i.ibb.co/RykHJVm/logo.png" alt="logo" height="130" width="300">
  <h3 class="line"><a href="/ua">Головна сторінка</a></h3>
  <h3 class="line"><a href="/ua/about-us">Про нас</a></h3>
  <h3 class="line"><a href="/ua/policies">Правила користування</a></h3>
    <form action="https://u24.gov.ua/">
        <input class='donat' type="submit" value="UNITED 24" />
    </form>
  <div onclick="hideInfoMenu()" id="arrow-left">
    <svg color="white" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-arrow-left" viewBox="0 0 16 16">
      <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
    </svg>
  </div>
</div>


<div class="arrow-button-up">
  <svg id="arrow-up" onclick="showCheckBoxesMenu()" color="green" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-chevron-compact-up" viewBox="0 0 16 16">
    <path fill-rule="evenodd" d="M7.776 5.553a.5.5 0 0 1 .448 0l6 3a.5.5 0 1 1-.448.894L8 6.56 2.224 9.447a.5.5 0 1 1-.448-.894l6-3z"/>
  </svg>
</div>

<form method="post" action = '/ua/map'>
    <div class="menu-box-hidden" id="menu-box">
      <div id="menu-scroller">
        <div id="menu-box-information">
          <label class="label">
            <span>Укриття</span>
            <input type="checkbox" id="checkbox1" class="check" name="shelter">
          </label>
    
          <label class="label">
            <span>Пункти незламності</span>
            <input type="checkbox" id="checkbox2" class="check" name="unbreakpoint">
          </label>
    
          <label class="label">
            <span>Аптеки</span>
            <input type="checkbox" id="checkbox3" class="check" name="drugstore">
          </label>
    
          <label class="label">
            <span>Лікарні</span>
            <input type="checkbox" id="checkbox4" class="check" name="hospital">
          </label>
          <label class="label">
            <span>Поліція</span>
            <input type="checkbox" id="checkbox4" class="check" name="police_departments">
          </label>
          <div>
            <button onclick="hideCheckBoxesMenu() " type="submit" class ='btn'>Подати</button>
          </div>
        </div>
      </div>
        <div onclick="hideCheckBoxesMenu()" id="closing-checkboxes">
            <svg color="green" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-arrow-down" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M8 1a.5.5 0 0 1 .5.5v11.793l3.146-3.147a.5.5 0 0 1 .708.708l-4 4a.5.5 0 0 1-.708 0l-4-4a.5.5 0 0 1 .708-.708L7.5 13.293V1.5A.5.5 0 0 1 8 1z"/>
            </svg>
        </div>
    </div>
</form>

<div onclick="showLegenda()" id="legenda-button">
  <svg color="green" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-chevron-compact-left" viewBox="0 0 16 16">
    <path fill-rule="evenodd" d="M9.224 1.553a.5.5 0 0 1 .223.67L6.56 8l2.888 5.776a.5.5 0 1 1-.894.448l-3-6a.5.5 0 0 1 0-.448l3-6a.5.5 0 0 1 .67-.223z"/>
  </svg>
</div>
<div id="sidebar" class="sidebar-hidden">
  <div class="image">
    <img src="https://i.ibb.co/FJ6phjJ/Home-Health-place-logo-5.png" alt="Home-Health-place-logo-5">
    <div class="description">
      <div class="caption"><strong>Пункт незламності</strong></div>
    </div>
  </div>
  <div class="image">
    <img src="https://iili.io/HkhnDeR.md.png" alt="Home-Health-place-logo-6">
    <div class="description">
      <div class="caption"><strong>Укриття</strong></div>
    </div>
  </div>
  <div class="image">
    <img src="https://i.ibb.co/6v60Vwd/hospitals.png" alt="hospitals">
    <div class="description">
      <div class="caption"><strong>Лікарня</strong></div>
    </div>
  </div>
  <div class="image">
    <img src="https://i.ibb.co/pRS0mpj/pharmacy.png" alt="pharmacy">
    <div class="description">
      <div class="caption"><strong>Аптека</strong></div>
    </div>
  </div>
  <div class="image">
    <img src="https://i.ibb.co/Sfmd5QH/police.png" alt="police">
    <div class="description">
      <div class="caption"><strong>Поліція</strong></div>
    </div>
  </div>
  <div onclick="hideLegenda()" id="closing-legenda">
    <svg color="white" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
      <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8z"/>
    </svg>
  </div>
</div>
    """
checkbox_eng_chrome = """
<style>
  body{
    overflow: hidden;
  }
  .leaflet-top.leaflet-left{
    display: none;
  }
  #menu-box{
    position: absolute;
    z-index: 900;
    height: auto;
    width: auto;
  }
  #menu-box-information{
    position: fixed;
    width: 40vw;
    height: auto;
    z-index: 900;
    border: 1px solid black;
    background-color: #006e48;
    border-radius: 20px;
    opacity: 80%;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    padding: 2vh;
    overflow-y: auto;
    overflow-x: hidden;
  }
  @media (max-width: 768px) {
      #menu-box-information{
          position: fixed;
          width: 60vw;
          height: 45vh;
          height: auto;
          z-index: 900;
          border: 1px solid black;
          background-color: #006e48;
          border-radius: 20px;
          opacity: 80%;
          flex-direction: column;
          justify-content: space-between;
          align-items: center;
          padding: 2vh;
          overflow-y: auto;
          overflow-x: hidden;
      }
      .menu-box-revealed{
          transform: translate3d(19.5vw, 35vh, 0);
          transition: transform 1.0s cubic-bezier(0, .52, 0, 1);
      }
      .menu-box-hidden{
          transform: translate3d(19.5vw, 100vh, 0);
          transition: transform 2.0s cubic-bezier(0, .52, 0, 1);
      }
      #closing-checkboxes {
          position: absolute;
          z-index: 900;
          top: 32vh;
          left: 24vw;
      }
  }
  @media (min-width: 767px){
    #menu-box-information{
      position: fixed;
      width: 40vw;
      /*height: 25vh;*/
      height: auto;
      z-index: 900;
      border: 1px solid black;
      background-color: #006e48;
      border-radius: 20px;
      opacity: 80%;
      flex-direction: column;
      justify-content: space-between;
      align-items: center;
      padding: 2vh;
      overflow-y: auto;
      overflow-x: hidden;
    }
      .menu-box-revealed {
          transform: translate3d(30vw, 46vh, 0);
          transition: transform 1.0s cubic-bezier(0, .52, 0, 1);
      }
      .menu-box-hidden{
        transform: translate3d(30vw, 100vh, 0);
        transition: transform 2.0s cubic-bezier(0, .52, 0, 1);
      }
      #closing-checkboxes {
          position: absolute;
          z-index: 900;
          top: 32vh;
          left: 18.4vw;
      }
  }
  .label{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-radius: 10px;
    margin-right: 10px;
    font-size: 2vmin;
    transition: 1s;
    flex-grow: 1;
    min-width: 0;
    padding: 5px;
    background-color: #f8f8f8;
    margin: 1px;
    padding-bottom: 1px;
    padding-top: 1px;
    color: black;
    height: auto;
  }
  .check {
    position: relative;
    width: 20px;
    height: 20px;
    border-radius: 2px;
    appearance: none;
    background-color: #bbb;
    transition: all .3s;
  }

  .check::before {
    content: '';
    position: absolute;
    border: solid #fff;
    display: block;
    width: .3em;
    height: .6em;
    border-width: 0 .2em .2em 0;
    z-index: 1;
    opacity: 0;
    right: calc(50% - .3em);
    top: calc(50% - .6em);
    transform: rotate(0deg);
    transition: all .3s;
    transform-origin: center center;
  }

  .check:checked {
    animation: a .3s ease-in forwards;
    background-color: #00a97e;
  }

  .check:checked::before {
    opacity: 1;
    transform: rotate(405deg);
  }

  @keyframes a {
    0% {
      opacity: 1;
      transform: scale(1) rotateY(0deg);
    }

    50% {
      opacity: 0;
      transform: scale(.8) rotateY(180deg);
    }

    100% {
      opacity: 1;
      transform: scale(1) rotateY(360deg);
    }
  }
  .btn {
    display: flex;
    justify-content: center;
    align-items: center;
    --color: #ffff;
    --color2: rgb(10, 25, 30);
    font-size: 2vmin;
    transition: 1s;
    flex-grow: 1;
    padding: 0.8em 1.75em;
    background-color: transparent;
    border-radius: 6px;
    border: .3px solid var(--color);
    position: relative;
    overflow: hidden;
    cursor: pointer;
    margin: 1vh auto;
    z-index: 900;
    font-family: 'Roboto', 'Segoe UI', sans-serif;
    text-transform: uppercase;
    color: var(--color);
  }

  .btn::after, .btn::before {
    content: '';
    display: block;
    height: 100%;
    width: 100%;
    transform: skew(90deg) translate(-50%, -50%);
    position: absolute;
    inset: 50%;
    left: 25%;
    z-index: -1;
    transition: .5s ease-out;
    background-color: var(--color);
  }

  .btn::before {
    top: -50%;
    left: -25%;
    transform: skew(90deg) rotate(180deg) translate(-50%, -50%);
  }

  .btn:hover::before {
    transform: skew(45deg) rotate(180deg) translate(-50%, -50%);
  }

  .btn:hover::after {
    transform: skew(45deg) translate(-50%, -50%);
  }

  .btn:hover {
    color: var(--color2);
  }

  .btn:active {
    filter: brightness(.7);
    transform: scale(.98);
  }
  @media (max-width: 768px) {
        #arrow-up{
        position: absolute;
        z-index: 900;
        top: 60vh;
        left: 44vw;
      }
  }
  @media (min-width: 767px){
        #arrow-up{
        position: absolute;
        z-index: 900;
        top: 80vh;
        left: 48vw;
      }
  }
  


  #menu-button {
    position: absolute;
    display: block;
    z-index: 900;
    top: 50vh;
      left: 5vw;
  }
  @media (min-width: 768px){
    #image-overlay {
      display: flex;
      z-index: 900;
      position: absolute;
      flex-direction: column;
      justify-content: flex-start;
      align-items: flex-start;
      margin: 0;
      width: 30vw;
      height: 100vh;
      background-color: #00a97e;
      opacity:85%;
      border: 2px solid rgb(5, 102, 52);
      overflow: hidden;
    }
  .donat{
      background-color: black; /* Green */
      border: none;
      color: white;
      padding: 15px 32px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 16px;
      width: 300px;
      margin-top: 3vh;
      margin-bottom: 3vh;
      margin-left: 3vw
  }
  }
  @media (max-width: 767px){
    #image-overlay {
      display: flex;
      z-index: 900;
      position: absolute;
      flex-direction: column;
      justify-content: flex-start;
      align-items: flex-start;
      margin: 0;
      width: 100vw;
      height: 100vh;
      background-color: #00a97e;
      opacity:85%;
      border: 2px solid rgb(5, 102, 52);
      overflow: hidden;
    }
  .donat{
      position: relative;
      background-color: black; /* Green */
      border: none;
      color: white;
      padding: 15px 32px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 16px;
      width: 300px;
      margin-top: 3vh;
      margin-bottom: 3vh;
      margin-left: 10vw;
  }
  }
  .menu-revealed{
    transform: translate3d(0vw, 0vh, 0);
    transition: transform 1.0s cubic-bezier(0, .52, 0, 1);
  }
  .menu-hidden{
    transform: translate3d(-100vw, 0vh, 0);
    transition: transform 2.0s cubic-bezier(0, .52, 0, 1);
  }
  #image-overlay a {
    display: block;
    z-index: 900;
    position: relative;
    color: #fff;
    text-decoration: line-under;
    margin: 10px 10px 0 10px;
    transition: 2s;
    height: 5vh;
    text-align: center;
    line-height: 1.5;
  }

  #image-overlay a:hover {
    font-size: 34px;
    color: rgb(238, 253, 236);
  }
  #logo{
    position: relative;
    z-index: 900;
    width: auto;
    height: auto;
    max-width: 30vw;
    max-height: 20vh;
  }
  h3 {
      margin-top: 2vh;
      margin-bottom: 2vh;
      font-size: 3.5vmin;
  }
  @media only screen and (max-width: 767px){
    h3{
      font-size: 20px;
    }
  }


  #legenda-button{
      position: absolute;
      z-index: 900;
      top: 50vh;
      left: 90vw;
  }
  @media (max-width: 768px){
      #legenda-button{
          left: 85vw;
      }
  }
  #sidebar {
    position: fixed;
    z-index: 900;
    background-color: #00a97e;
    opacity:85%;
    border: 2px solid rgb(5, 102, 52);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  @media (min-width: 768px){
    #sidebar {
      height: 100vh;
      width: 30vw;
    }
    .sidebar-revealed{
      transform: translate3d(70vw, 0vh, 0);
      transition: transform 1.0s cubic-bezier(0, .52, 0, 1);
    }
    .sidebar-hidden{
      transform: translate3d(200vw, 0vh, 0);
      transition: transform 3.0s cubic-bezier(0, .52, 0, 1);
    }
  }
  @media (max-width: 767px){
    #sidebar {
      width: 100vw;
      height: 100vh
    }
    .sidebar-revealed{
      transform: translate3d(0, 0, 0);
      transition: transform 1.0s cubic-bezier(0, .52, 0, 1);
    }
    .sidebar-hidden{
      transform: translate3d(200vw, 0vh, 0);
      transition: transform 2.0s cubic-bezier(0, .52, 0, 1);
    }
      #closing-legenda{
          z-index: 900;
          position: absolute;
          left: 20vw;
      }
  }
  #sidebar .image {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin: 10px 0;
    width: 100%;
    text-align: center;
  }

  #sidebar .image img {
    height: 10vh;
    margin: 7px;
    width: auto;
    max-width: 100%;
    max-height: 100%;
  }

  #sidebar .caption {
    margin-top: 5px;
    font-size: 1.5rem;
    color: #ffff;
  }

  #checked-checkbox{
      position: absolute;
      z-index: 900;
      display: none;
  }


</style>
<script>
  function showCheckBoxesMenu(){
    document.getElementById('menu-box').classList.remove('menu-box-hidden');
    document.getElementById('menu-box').classList.add('menu-box-revealed');
    document.getElementById('arrow-up').style.display = 'none';
    document.getElementById('menu-button').style.display = 'none';
    document.getElementById('legenda-button').style.display = 'none';

  }
  function hideCheckBoxesMenu(){
    document.getElementById('menu-box').classList.remove('menu-box-revealed');
    document.getElementById('menu-box').classList.add('menu-box-hidden');
    document.getElementById('arrow-up').style.display = 'block';
    document.getElementById('menu-button').style.display = 'block';
    document.getElementById('legenda-button').style.display = 'block';
  }


  function showInfoMenu(){
    document.getElementById('image-overlay').classList.remove('menu-hidden');
    document.getElementById('image-overlay').classList.add('menu-revealed');
    document.getElementById('menu-button').style.display = 'none';
    document.getElementById('arrow-up').style.display = 'none';
    document.getElementById('legenda-button').style.display = 'none';
  }
  function hideInfoMenu(){
    document.getElementById('image-overlay').classList.remove('menu-revealed');
    document.getElementById('image-overlay').classList.add('menu-hidden');
    document.getElementById('menu-button').style.display = 'block';
    document.getElementById('arrow-up').style.display = 'block';
    document.getElementById('legenda-button').style.display = 'block';
  }


  function showLegenda(){
    document.getElementById('sidebar').classList.remove('sidebar-hidden');
    document.getElementById('sidebar').classList.add('sidebar-revealed');
    document.getElementById('menu-button').style.display = 'none';
    document.getElementById('arrow-up').style.display = 'none';
    document.getElementById('legenda-button').style.display = 'none';
  }
  function hideLegenda(){
    document.getElementById('sidebar').classList.remove('sidebar-revealed');
    document.getElementById('sidebar').classList.add('sidebar-hidden');
    document.getElementById('menu-button').style.display = 'block';
    document.getElementById('arrow-up').style.display = 'block';
    document.getElementById('legenda-button').style.display = 'block';
  }

</script>
<div onclick="showInfoMenu()" id="menu-button">
  <svg color="green" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-chevron-compact-right" viewBox="0 0 16 16">
    <path fill-rule="evenodd" d="M6.776 1.553a.5.5 0 0 1 .671.223l3 6a.5.5 0 0 1 0 .448l-3 6a.5.5 0 1 1-.894-.448L9.44 8 6.553 2.224a.5.5 0 0 1 .223-.671z"/>
  </svg>
</div>
<div class="menu-hidden" id="image-overlay">
  <img id="logo" src="https://i.ibb.co/RykHJVm/logo.png" alt="logo" height="130" width="300">
  <h3 class="line"><a href="/en">Main</a></h3>
  <h3 class="line"><a href="/en/about-us">About Us</a></h3>
  <h3 class="line"><a href="/en/policies">Terms of Use</a></h3>
    <form action="https://u24.gov.ua/">
        <input class='donat' type="submit" value="UNITED 24" />
    </form>
  <div onclick="hideInfoMenu()" id="arrow-left">
    <svg color="white" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-arrow-left" viewBox="0 0 16 16">
      <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
    </svg>
  </div>
</div>

<div class="arrow-button-up">
  <svg id="arrow-up" onclick="showCheckBoxesMenu()" color="green" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-chevron-compact-up" viewBox="0 0 16 16">
    <path fill-rule="evenodd" d="M7.776 5.553a.5.5 0 0 1 .448 0l6 3a.5.5 0 1 1-.448.894L8 6.56 2.224 9.447a.5.5 0 1 1-.448-.894l6-3z"/>
  </svg>
</div>
<form method="post" action = '/en/map'>
    <div class="menu-box-hidden" id="menu-box">
      <div id="menu-scroller">
        <div id="menu-box-information">
          <label class="label">
            <span>Shelters</span>
            <input type="checkbox" id="checkbox1" class="check" name="shelter">
          </label>
    
          <label class="label">
            <span>Invisibility</span>
            <input type="checkbox" id="checkbox2" class="check" name="unbreakpoint">
          </label>
    
          <label class="label">
            <span>Pharmacy</span>
            <input type="checkbox" id="checkbox3" class="check" name="drugstore">
          </label>
    
          <label class="label">
            <span>Hospitals</span>
            <input type="checkbox" id="checkbox4" class="check" name="hospital">
          </label>
          <label class="label">
            <span>Police</span>
            <input type="checkbox" id="checkbox4" class="check" name="police_departments">
          </label>
          <div>
            <button onclick="hideCheckBoxesMenu()" type="submit" class ='btn'>Submit</button>
          </div>
        </div>
      </div>
        <div onclick="hideCheckBoxesMenu()" id="closing-checkboxes">
            <svg color="green" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-arrow-down" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M8 1a.5.5 0 0 1 .5.5v11.793l3.146-3.147a.5.5 0 0 1 .708.708l-4 4a.5.5 0 0 1-.708 0l-4-4a.5.5 0 0 1 .708-.708L7.5 13.293V1.5A.5.5 0 0 1 8 1z"/>
            </svg>
        </div>
    </div>
</form>

<div onclick="showLegenda()" id="legenda-button">
  <svg color="green" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-chevron-compact-left" viewBox="0 0 16 16">
    <path fill-rule="evenodd" d="M9.224 1.553a.5.5 0 0 1 .223.67L6.56 8l2.888 5.776a.5.5 0 1 1-.894.448l-3-6a.5.5 0 0 1 0-.448l3-6a.5.5 0 0 1 .67-.223z"/>
  </svg>
</div>
<div id="sidebar" class="sidebar-hidden">
  <div class="image">
    <img src="https://i.ibb.co/FJ6phjJ/Home-Health-place-logo-5.png" alt="Home-Health-place-logo-5">
    <div class="description">
      <div class="caption"><strong>Invisibility</strong></div>
    </div>
  </div>
  <div class="image">
    <img src="https://iili.io/HkhnDeR.md.png" alt="Home-Health-place-logo-6">
    <div class="description">
      <div class="caption"><strong>Shelter</strong></div>
    </div>
  </div>
  <div class="image">
    <img src="https://i.ibb.co/6v60Vwd/hospitals.png" alt="hospitals">
    <div class="description">
      <div class="caption"><strong>Hospital</strong></div>
    </div>
  </div>
  <div class="image">
    <img src="https://i.ibb.co/pRS0mpj/pharmacy.png" alt="pharmacy">
    <div class="description">
      <div class="caption"><strong>Pharmacy</strong></div>
    </div>
  </div>
  <div class="image">
    <img src="https://i.ibb.co/Sfmd5QH/police.png" alt="police">
    <div class="description">
      <div class="caption"><strong>Police</strong></div>
    </div>
  </div>
  <div onclick="hideLegenda()" id="closing-legenda">
    <svg color="white" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
      <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8z"/>
    </svg>
  </div>
</div>
"""
checkbox_ukr_all_browsers = """
<style>
  body{
    overflow: hidden;
  }
  .leaflet-top.leaflet-left{
    display: none;
  }
  #menu-box{
    position: absolute;
    z-index: 900;
    /*left: 40vw;
    top: 60vh;*/
    height: auto;
    width: auto;
  }
  #menu-box-information{
    position: fixed;
    width: 20vw;
    /*height: 25vh;*/
    height: auto;
    z-index: 900;
    border: 1px solid black;
    background-color: #006e48;
    border-radius: 20px;
    opacity: 80%;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    padding: 2vh;
    overflow-y: auto;
    overflow-x: hidden;
  }
  @media (max-width: 768px) {
    #menu-box-information{
          position: fixed;
          width: 60vw;
          height: 45vh;
          height: auto;
          z-index: 900;
          border: 1px solid black;
          background-color: #006e48;
          border-radius: 20px;
          opacity: 80%;
          flex-direction: column;
          justify-content: space-between;
          align-items: center;
          padding: 2vh;
          overflow-y: auto;
          overflow-x: hidden;
    }
    .menu-box-revealed{
        transform: translate3d(19.5vw, 35vh, 0);
        transition: transform 1.0s cubic-bezier(0, .52, 0, 1);
      }
      .menu-box-hidden{
        transform: translate3d(19.5vw, 100vh, 0);
        transition: transform 2.0s cubic-bezier(0, .52, 0, 1);
  }
      #closing-checkboxes {
          position: absolute;
          z-index: 900;
          top: 32vh;
          left: 24vw;
      }
  }
  @media (min-width: 767px) {
      #menu-box-information {
          position: fixed;
          width: 40vw;
          /*height: 25vh;*/
          height: auto;
          z-index: 900;
          border: 1px solid black;
          background-color: #006e48;
          border-radius: 20px;
          opacity: 80%;
          flex-direction: column;
          justify-content: space-between;
          align-items: center;
          padding: 2vh;
          overflow-y: auto;
          overflow-x: hidden;
      }

      .menu-box-revealed {
          transform: translate3d(30vw, 46vh, 0);
          transition: transform 1.0s cubic-bezier(0, .52, 0, 1);
      }

      .menu-box-hidden {
          transform: translate3d(30vw, 100vh, 0);
          transition: transform 2.0s cubic-bezier(0, .52, 0, 1);
      }

      #closing-checkboxes {
          position: absolute;
          z-index: 900;
          top: 32vh;
          left: 18.5vw;
      }
  }

  .label{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-radius: 10px;
    margin-right: 10px;
    font-size: 2vmin;
    transition: 1s;
    flex-grow: 1;
    min-width: 0;
    padding: 5px;
    background-color: #f8f8f8;
    margin: 1px;
    padding-bottom: 1px;
    padding-top: 1px;
    color: black;
    height: auto;
  }
  .check {
    position: relative;
    width: 20px;
    height: 20px;
    border-radius: 2px;
    appearance: none;
    background-color: #bbb;
    transition: all .3s;
  }

  .check::before {
    content: '';
    position: absolute;
    border: solid #fff;
    display: block;
    width: .3em;
    height: .6em;
    border-width: 0 .2em .2em 0;
    z-index: 1;
    opacity: 0;
    right: calc(50% - .3em);
    top: calc(50% - .6em);
    transform: rotate(0deg);
    transition: all .3s;
    transform-origin: center center;
  }

  .check:checked {
    animation: a .3s ease-in forwards;
    background-color: #00a97e;
  }

  .check:checked::before {
    opacity: 1;
    transform: rotate(405deg);
  }

  @keyframes a {
    0% {
      opacity: 1;
      transform: scale(1) rotateY(0deg);
    }

    50% {
      opacity: 0;
      transform: scale(.8) rotateY(180deg);
    }

    100% {
      opacity: 1;
      transform: scale(1) rotateY(360deg);
    }
  }
  button {
      display: flex;
      justify-content: center;
      align-items: center;
      width: fit-content;
      justify-content: center;
      align-items: center;
      font-size: 1.5vmin;
      color: black;
      min-width: 100px;
      height: 45px;
      padding: 8px;
      border-radius: 5px;
      border: 2.5px solid #E0E1E4;
      box-shadow: 0px 0px 20px -20px;
      cursor: pointer;
      background-color: white;
      transition: all 0.2s ease-in-out 0ms;
      user-select: none;
      z-index: 900;
      margin: 1vh auto;
      font-family: 'Poppins', sans-serif;
    }

    button:hover {
      background-color: #F2F2F2;
      box-shadow: 0px 0px 20px -18px;
      color: black;
    }

    button:active {
      transform: scale(0.95);
      color: black;
    }
  @media (max-width: 768px) {
        #arrow-up{
        position: absolute;
        z-index: 900;
        top: 60vh;
        left: 44vw;
      }
  }
  @media (min-width: 767px){
        #arrow-up{
        position: absolute;
        z-index: 900;
        top: 80vh;
        left: 48vw;
      }
  }


  #menu-button {
    position: absolute;
    display: block;
    z-index: 900;
    top: 50vh;
      left: 5vw;
  }
  @media (min-width: 768px){
    #image-overlay {
      display: flex;
      z-index: 900;
      position: absolute;
      flex-direction: column;
      justify-content: flex-start;
      align-items: flex-start;
      margin: 0;
      width: 30vw;
      height: 100vh;
      background-color: #00a97e;
      opacity:85%;
      border: 2px solid rgb(5, 102, 52);
      overflow: hidden;
    }
  .donat{
      background-color: black; /* Green */
      border: none;
      color: white;
      padding: 15px 32px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 16px;
      width: 300px;
      margin-top: 3vh;
      margin-bottom: 3vh;
      margin-left: 3vw
  }
  }
  @media (max-width: 767px){
    #image-overlay {
      display: flex;
      z-index: 900;
      position: absolute;
      flex-direction: column;
      justify-content: flex-start;
      align-items: flex-start;
      margin: 0;
      width: 100vw;
      height: 100vh;
      background-color: #00a97e;
      opacity:85%;
      border: 2px solid rgb(5, 102, 52);
      overflow: hidden;
    }
  .donat{
      position: relative;
      background-color: black; /* Green */
      border: none;
      color: white;
      padding: 15px 32px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 16px;
      width: 300px;
      margin-top: 3vh;
      margin-bottom: 3vh;
      margin-left: 10vw;
  }
  }
  .menu-revealed{
    transform: translate3d(0vw, 0vh, 0);
    transition: transform 1.0s cubic-bezier(0, .52, 0, 1);
  }
  .menu-hidden{
    transform: translate3d(-100vw, 0vh, 0);
    transition: transform 2.0s cubic-bezier(0, .52, 0, 1);
  }
  #image-overlay a {
    display: block;
    z-index: 900;
    position: relative;
    color: #fff;
    text-decoration: line-under;
    margin: 10px 10px 0 10px;
    transition: 2s;
    height: 5vh;
    text-align: center;
    line-height: 1.5;
  }

  #image-overlay a:hover {
    font-size: 34px;
    color: rgb(238, 253, 236);
  }
  #logo{
    position: relative;
    z-index: 900;
    width: auto;
    height: auto;
    max-width: 30vw;
    max-height: 20vh;
  }
  h3 {
      margin-top: 2vh;
      margin-bottom: 2vh;
      font-size: 3.5vmin;
  }
  @media only screen and (max-width: 767px){
    h3{
      font-size: 20px;
    }
  }


  #legenda-button{
    position: absolute;
    z-index: 900;
    top: 50vh;
    left: 90vw;
  }
  @media (max-width: 768px){
    #legenda-button{
      left: 85vw;
    }
  }
  #sidebar {
    position: fixed;
    z-index: 900;
    background-color: #00a97e;
    opacity:85%;
    border: 2px solid rgb(5, 102, 52);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  @media (min-width: 768px){
    #sidebar {
      height: 100vh;
      width: 30vw;
    }
    .sidebar-revealed{
      transform: translate3d(70vw, 0vh, 0);
      transition: transform 1.0s cubic-bezier(0, .52, 0, 1);
    }
    .sidebar-hidden{
      transform: translate3d(200vw, 0vh, 0);
      transition: transform 3.0s cubic-bezier(0, .52, 0, 1);
    }
  }
  @media (max-width: 767px){
    #sidebar {
      width: 100vw;
      height: 100vh
    }
    .sidebar-revealed{
      transform: translate3d(0, 0, 0);
      transition: transform 1.0s cubic-bezier(0, .52, 0, 1);
    }
    .sidebar-hidden{
      transform: translate3d(200vw, 0vh, 0);
      transition: transform 2.0s cubic-bezier(0, .52, 0, 1);
    }
    #closing-legenda{
        z-index: 900;
        position: absolute;
        left: 20vw;
    }
  }
  #sidebar .image {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin: 10px 0;
    width: 100%;
    text-align: center;
  }

  #sidebar .image img {
    height: 10vh;
    margin: 7px;
    width: auto;
    max-width: 100%;
    max-height: 100%;
  }

  #sidebar .caption {
    margin-top: 5px;
    font-size: 1.5rem;
    color: #ffff;
  }

  #checked-checkbox{
      position: absolute;
      z-index: 900;
      display: none;
  }


</style>
<script>
  function showCheckBoxesMenu(){
    document.getElementById('menu-box').classList.remove('menu-box-hidden');
    document.getElementById('menu-box').classList.add('menu-box-revealed');
    document.getElementById('arrow-up').style.display = 'none';
    document.getElementById('menu-button').style.display = 'none';
    document.getElementById('legenda-button').style.display = 'none';

  }
  function hideCheckBoxesMenu(){
    document.getElementById('menu-box').classList.remove('menu-box-revealed');
    document.getElementById('menu-box').classList.add('menu-box-hidden');
    document.getElementById('arrow-up').style.display = 'block';
    document.getElementById('menu-button').style.display = 'block';
    document.getElementById('legenda-button').style.display = 'block';
  }


  function showInfoMenu(){
    document.getElementById('image-overlay').classList.remove('menu-hidden');
    document.getElementById('image-overlay').classList.add('menu-revealed');
    document.getElementById('menu-button').style.display = 'none';
    document.getElementById('arrow-up').style.display = 'none';
    document.getElementById('legenda-button').style.display = 'none';
  }
  function hideInfoMenu(){
    document.getElementById('image-overlay').classList.remove('menu-revealed');
    document.getElementById('image-overlay').classList.add('menu-hidden');
    document.getElementById('menu-button').style.display = 'block';
    document.getElementById('arrow-up').style.display = 'block';
    document.getElementById('legenda-button').style.display = 'block';
  }


  function showLegenda(){
    document.getElementById('sidebar').classList.remove('sidebar-hidden');
    document.getElementById('sidebar').classList.add('sidebar-revealed');
    document.getElementById('menu-button').style.display = 'none';
    document.getElementById('arrow-up').style.display = 'none';
    document.getElementById('legenda-button').style.display = 'none';
  }
  function hideLegenda(){
    document.getElementById('sidebar').classList.remove('sidebar-revealed');
    document.getElementById('sidebar').classList.add('sidebar-hidden');
    document.getElementById('menu-button').style.display = 'block';
    document.getElementById('arrow-up').style.display = 'block';
    document.getElementById('legenda-button').style.display = 'block';
  }

</script>
<div onclick="showInfoMenu()" id="menu-button">
  <svg color="green" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-chevron-compact-right" viewBox="0 0 16 16">
    <path fill-rule="evenodd" d="M6.776 1.553a.5.5 0 0 1 .671.223l3 6a.5.5 0 0 1 0 .448l-3 6a.5.5 0 1 1-.894-.448L9.44 8 6.553 2.224a.5.5 0 0 1 .223-.671z"/>
  </svg>
</div>
<div class="menu-hidden" id="image-overlay">
  <img id="logo" src="https://i.ibb.co/RykHJVm/logo.png" alt="logo" height="130" width="300">
  <h3 class="line"><a href="/ua">Головна сторінка</a></h3>
  <h3 class="line"><a href="/ua/about-us">Про нас</a></h3>
  <h3 class="line"><a href="/ua/policies">Правила користування</a></h3>
    <form action="https://u24.gov.ua/">
        <input class='donat' type="submit" value="UNITED 24" />
    </form>
  <div onclick="hideInfoMenu()" id="arrow-left">
    <svg color="white" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-arrow-left" viewBox="0 0 16 16">
      <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
    </svg>
  </div>
</div>


<div class="arrow-button-up">
  <svg id="arrow-up" onclick="showCheckBoxesMenu()" color="green" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-chevron-compact-up" viewBox="0 0 16 16">
    <path fill-rule="evenodd" d="M7.776 5.553a.5.5 0 0 1 .448 0l6 3a.5.5 0 1 1-.448.894L8 6.56 2.224 9.447a.5.5 0 1 1-.448-.894l6-3z"/>
  </svg>
</div>

<form method="post" action = '/ua/map'>
    <div class="menu-box-hidden" id="menu-box">
      <div id="menu-scroller">
        <div id="menu-box-information">
          <label class="label">
            <span>Укриття</span>
            <input type="checkbox" id="checkbox1" class="check" name="shelter">
          </label>
    
          <label class="label">
            <span>Пункти незламності</span>
            <input type="checkbox" id="checkbox2" class="check" name="unbreakpoint">
          </label>
    
          <label class="label">
            <span>Аптеки</span>
            <input type="checkbox" id="checkbox3" class="check" name="drugstore">
          </label>
    
          <label class="label">
            <span>Лікарні</span>
            <input type="checkbox" id="checkbox4" class="check" name="hospital">
          </label>
          <label class="label">
            <span>Поліція</span>
            <input type="checkbox" id="checkbox4" class="check" name="police_departments">
          </label>
          <div>
            <button onclick="hideCheckBoxesMenu() " type="submit" class ='button'>Подати</button>
          </div>
        </div>
      </div>
        <div onclick="hideCheckBoxesMenu()" id="closing-checkboxes">
            <svg color="green" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-arrow-down" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M8 1a.5.5 0 0 1 .5.5v11.793l3.146-3.147a.5.5 0 0 1 .708.708l-4 4a.5.5 0 0 1-.708 0l-4-4a.5.5 0 0 1 .708-.708L7.5 13.293V1.5A.5.5 0 0 1 8 1z"/>
            </svg>
        </div>
    </div>
</form>

<div onclick="showLegenda()" id="legenda-button">
  <svg color="green" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-chevron-compact-left" viewBox="0 0 16 16">
    <path fill-rule="evenodd" d="M9.224 1.553a.5.5 0 0 1 .223.67L6.56 8l2.888 5.776a.5.5 0 1 1-.894.448l-3-6a.5.5 0 0 1 0-.448l3-6a.5.5 0 0 1 .67-.223z"/>
  </svg>
</div>
<div id="sidebar" class="sidebar-hidden">
  <div class="image">
    <img src="https://i.ibb.co/FJ6phjJ/Home-Health-place-logo-5.png" alt="Home-Health-place-logo-5">
    <div class="description">
      <div class="caption"><strong>Пункт незламності</strong></div>
    </div>
  </div>
  <div class="image">
    <img src="https://iili.io/HkhnDeR.md.png" alt="Home-Health-place-logo-6">
    <div class="description">
      <div class="caption"><strong>Укриття</strong></div>
    </div>
  </div>
  <div class="image">
    <img src="https://i.ibb.co/6v60Vwd/hospitals.png" alt="hospitals">
    <div class="description">
      <div class="caption"><strong>Лікарня</strong></div>
    </div>
  </div>
  <div class="image">
    <img src="https://i.ibb.co/pRS0mpj/pharmacy.png" alt="pharmacy">
    <div class="description">
      <div class="caption"><strong>Аптека</strong></div>
    </div>
  </div>
  <div class="image">
    <img src="https://i.ibb.co/Sfmd5QH/police.png" alt="police">
    <div class="description">
      <div class="caption"><strong>Поліція</strong></div>
    </div>
  </div>
  <div onclick="hideLegenda()" id="closing-legenda">
    <svg color="white" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
      <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8z"/>
    </svg>
  </div>
</div>
    """
checkbox_eng_all_browsers = """
<style>
  body{
    overflow: hidden;
  }
  .leaflet-top.leaflet-left{
    display: none;
  }
  #menu-box{
    position: absolute;
    z-index: 900;
    height: auto;
    width: auto;
  }
  #menu-box-information{
    position: fixed;
    width: 40vw;
    height: auto;
    z-index: 900;
    border: 1px solid black;
    background-color: #006e48;
    border-radius: 20px;
    opacity: 80%;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    padding: 2vh;
    overflow-y: auto;
    overflow-x: hidden;
  }
  @media (max-width: 768px) {
      #menu-box-information{
          position: fixed;
          width: 60vw;
          height: 45vh;
          height: auto;
          z-index: 900;
          border: 1px solid black;
          background-color: #006e48;
          border-radius: 20px;
          opacity: 80%;
          flex-direction: column;
          justify-content: space-between;
          align-items: center;
          padding: 2vh;
          overflow-y: auto;
          overflow-x: hidden;
      }
      .menu-box-revealed{
          transform: translate3d(19.5vw, 35vh, 0);
          transition: transform 1.0s cubic-bezier(0, .52, 0, 1);
      }
      .menu-box-hidden{
          transform: translate3d(19.5vw, 100vh, 0);
          transition: transform 2.0s cubic-bezier(0, .52, 0, 1);
      }
      #closing-checkboxes {
          position: absolute;
          z-index: 900;
          top: 32vh;
          left: 24vw;
      }
  }
  @media (min-width: 767px){
    #menu-box-information{
      position: fixed;
      width: 40vw;
      /*height: 25vh;*/
      height: auto;
      z-index: 900;
      border: 1px solid black;
      background-color: #006e48;
      border-radius: 20px;
      opacity: 80%;
      flex-direction: column;
      justify-content: space-between;
      align-items: center;
      padding: 2vh;
      overflow-y: auto;
      overflow-x: hidden;
    }
      .menu-box-revealed {
          transform: translate3d(30vw, 46vh, 0);
          transition: transform 1.0s cubic-bezier(0, .52, 0, 1);
      }
      .menu-box-hidden{
        transform: translate3d(30vw, 100vh, 0);
        transition: transform 2.0s cubic-bezier(0, .52, 0, 1);
      }
      #closing-checkboxes {
          position: absolute;
          z-index: 900;
          top: 32vh;
          left: 18.4vw;
      }
  }
  .label{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-radius: 10px;
    margin-right: 10px;
    font-size: 2vmin;
    transition: 1s;
    flex-grow: 1;
    min-width: 0;
    padding: 5px;
    background-color: #f8f8f8;
    margin: 1px;
    padding-bottom: 1px;
    padding-top: 1px;
    color: black;
    height: auto;
  }
  .check {
    position: relative;
    width: 20px;
    height: 20px;
    border-radius: 2px;
    appearance: none;
    background-color: #bbb;
    transition: all .3s;
  }

  .check::before {
    content: '';
    position: absolute;
    border: solid #fff;
    display: block;
    width: .3em;
    height: .6em;
    border-width: 0 .2em .2em 0;
    z-index: 1;
    opacity: 0;
    right: calc(50% - .3em);
    top: calc(50% - .6em);
    transform: rotate(0deg);
    transition: all .3s;
    transform-origin: center center;
  }

  .check:checked {
    animation: a .3s ease-in forwards;
    background-color: #00a97e;
  }

  .check:checked::before {
    opacity: 1;
    transform: rotate(405deg);
  }

  @keyframes a {
    0% {
      opacity: 1;
      transform: scale(1) rotateY(0deg);
    }

    50% {
      opacity: 0;
      transform: scale(.8) rotateY(180deg);
    }

    100% {
      opacity: 1;
      transform: scale(1) rotateY(360deg);
    }
  }
  button {
      display: flex;
      justify-content: center;
      align-items: center;
      width: fit-content;
      justify-content: center;
      align-items: center;
      font-size: 1.5vmin;
      color: black;
      min-width: 100px;
      height: 45px;
      padding: 8px;
      border-radius: 5px;
      border: 2.5px solid #E0E1E4;
      box-shadow: 0px 0px 20px -20px;
      cursor: pointer;
      background-color: white;
      transition: all 0.2s ease-in-out 0ms;
      user-select: none;
      z-index: 900;
      margin: 1vh auto;
      font-family: 'Poppins', sans-serif;
    }

    button:hover {
      background-color: #F2F2F2;
      box-shadow: 0px 0px 20px -18px;
      color: black;
    }

    button:active {
      transform: scale(0.95);
      color: black;
    }
  @media (max-width: 768px) {
        #arrow-up{
        position: absolute;
        z-index: 900;
        top: 60vh;
        left: 44vw;
      }
  }
  @media (min-width: 767px){
        #arrow-up{
        position: absolute;
        z-index: 900;
        top: 80vh;
        left: 48vw;
      }
  }
  


  #menu-button {
    position: absolute;
    display: block;
    z-index: 900;
    top: 50vh;
      left: 5vw;
  }
  @media (min-width: 768px){
    #image-overlay {
      display: flex;
      z-index: 900;
      position: absolute;
      flex-direction: column;
      justify-content: flex-start;
      align-items: flex-start;
      margin: 0;
      width: 30vw;
      height: 100vh;
      background-color: #00a97e;
      opacity:85%;
      border: 2px solid rgb(5, 102, 52);
      overflow: hidden;
    }
  .donat{
      background-color: black; /* Green */
      border: none;
      color: white;
      padding: 15px 32px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 16px;
      width: 300px;
      margin-top: 3vh;
      margin-bottom: 3vh;
      margin-left: 3vw
  }
  }
  @media (max-width: 767px){
    #image-overlay {
      display: flex;
      z-index: 900;
      position: absolute;
      flex-direction: column;
      justify-content: flex-start;
      align-items: flex-start;
      margin: 0;
      width: 100vw;
      height: 100vh;
      background-color: #00a97e;
      opacity:85%;
      border: 2px solid rgb(5, 102, 52);
      overflow: hidden;
    }
  .donat{
      position: relative;
      background-color: black; /* Green */
      border: none;
      color: white;
      padding: 15px 32px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 16px;
      width: 300px;
      margin-top: 3vh;
      margin-bottom: 3vh;
      margin-left: 10vw;
  }
  }
  .menu-revealed{
    transform: translate3d(0vw, 0vh, 0);
    transition: transform 1.0s cubic-bezier(0, .52, 0, 1);
  }
  .menu-hidden{
    transform: translate3d(-100vw, 0vh, 0);
    transition: transform 2.0s cubic-bezier(0, .52, 0, 1);
  }
  #image-overlay a {
    display: block;
    z-index: 900;
    position: relative;
    color: #fff;
    text-decoration: line-under;
    margin: 10px 10px 0 10px;
    transition: 2s;
    height: 5vh;
    text-align: center;
    line-height: 1.5;
  }

  #image-overlay a:hover {
    font-size: 34px;
    color: rgb(238, 253, 236);
  }
  #logo{
    position: relative;
    z-index: 900;
    width: auto;
    height: auto;
    max-width: 30vw;
    max-height: 20vh;
  }
  h3 {
      margin-top: 2vh;
      margin-bottom: 2vh;
      font-size: 3.5vmin;
  }
  @media only screen and (max-width: 767px){
    h3{
      font-size: 20px;
    }
  }


  #legenda-button{
      position: absolute;
      z-index: 900;
      top: 50vh;
      left: 90vw;
  }
  @media (max-width: 768px){
      #legenda-button{
          left: 85vw;
      }
  }
  #sidebar {
    position: fixed;
    z-index: 900;
    background-color: #00a97e;
    opacity:85%;
    border: 2px solid rgb(5, 102, 52);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  @media (min-width: 768px){
    #sidebar {
      height: 100vh;
      width: 30vw;
    }
    .sidebar-revealed{
      transform: translate3d(70vw, 0vh, 0);
      transition: transform 1.0s cubic-bezier(0, .52, 0, 1);
    }
    .sidebar-hidden{
      transform: translate3d(200vw, 0vh, 0);
      transition: transform 3.0s cubic-bezier(0, .52, 0, 1);
    }
  }
  @media (max-width: 767px){
    #sidebar {
      width: 100vw;
      height: 100vh
    }
    .sidebar-revealed{
      transform: translate3d(0, 0, 0);
      transition: transform 1.0s cubic-bezier(0, .52, 0, 1);
    }
    .sidebar-hidden{
      transform: translate3d(200vw, 0vh, 0);
      transition: transform 2.0s cubic-bezier(0, .52, 0, 1);
    }
      #closing-legenda{
          z-index: 900;
          position: absolute;
          left: 20vw;
      }
  }
  #sidebar .image {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin: 10px 0;
    width: 100%;
    text-align: center;
  }

  #sidebar .image img {
    height: 10vh;
    margin: 7px;
    width: auto;
    max-width: 100%;
    max-height: 100%;
  }

  #sidebar .caption {
    margin-top: 5px;
    font-size: 1.5rem;
    color: #ffff;
  }

  #checked-checkbox{
      position: absolute;
      z-index: 900;
      display: none;
  }


</style>
<script>
  function showCheckBoxesMenu(){
    document.getElementById('menu-box').classList.remove('menu-box-hidden');
    document.getElementById('menu-box').classList.add('menu-box-revealed');
    document.getElementById('arrow-up').style.display = 'none';
    document.getElementById('menu-button').style.display = 'none';
    document.getElementById('legenda-button').style.display = 'none';

  }
  function hideCheckBoxesMenu(){
    document.getElementById('menu-box').classList.remove('menu-box-revealed');
    document.getElementById('menu-box').classList.add('menu-box-hidden');
    document.getElementById('arrow-up').style.display = 'block';
    document.getElementById('menu-button').style.display = 'block';
    document.getElementById('legenda-button').style.display = 'block';
  }


  function showInfoMenu(){
    document.getElementById('image-overlay').classList.remove('menu-hidden');
    document.getElementById('image-overlay').classList.add('menu-revealed');
    document.getElementById('menu-button').style.display = 'none';
    document.getElementById('arrow-up').style.display = 'none';
    document.getElementById('legenda-button').style.display = 'none';
  }
  function hideInfoMenu(){
    document.getElementById('image-overlay').classList.remove('menu-revealed');
    document.getElementById('image-overlay').classList.add('menu-hidden');
    document.getElementById('menu-button').style.display = 'block';
    document.getElementById('arrow-up').style.display = 'block';
    document.getElementById('legenda-button').style.display = 'block';
  }


  function showLegenda(){
    document.getElementById('sidebar').classList.remove('sidebar-hidden');
    document.getElementById('sidebar').classList.add('sidebar-revealed');
    document.getElementById('menu-button').style.display = 'none';
    document.getElementById('arrow-up').style.display = 'none';
    document.getElementById('legenda-button').style.display = 'none';
  }
  function hideLegenda(){
    document.getElementById('sidebar').classList.remove('sidebar-revealed');
    document.getElementById('sidebar').classList.add('sidebar-hidden');
    document.getElementById('menu-button').style.display = 'block';
    document.getElementById('arrow-up').style.display = 'block';
    document.getElementById('legenda-button').style.display = 'block';
  }

</script>
<div onclick="showInfoMenu()" id="menu-button">
  <svg color="green" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-chevron-compact-right" viewBox="0 0 16 16">
    <path fill-rule="evenodd" d="M6.776 1.553a.5.5 0 0 1 .671.223l3 6a.5.5 0 0 1 0 .448l-3 6a.5.5 0 1 1-.894-.448L9.44 8 6.553 2.224a.5.5 0 0 1 .223-.671z"/>
  </svg>
</div>
<div class="menu-hidden" id="image-overlay">
  <img id="logo" src="https://i.ibb.co/RykHJVm/logo.png" alt="logo" height="130" width="300">
  <h3 class="line"><a href="/en">Main</a></h3>
  <h3 class="line"><a href="/en/about-us">About Us</a></h3>
  <h3 class="line"><a href="/en/policies">Terms of Use</a></h3>
    <form action="https://u24.gov.ua/">
        <input class='donat' type="submit" value="UNITED 24" />
    </form>
  <div onclick="hideInfoMenu()" id="arrow-left">
    <svg color="white" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-arrow-left" viewBox="0 0 16 16">
      <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
    </svg>
  </div>
</div>

<div class="arrow-button-up">
  <svg id="arrow-up" onclick="showCheckBoxesMenu()" color="green" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-chevron-compact-up" viewBox="0 0 16 16">
    <path fill-rule="evenodd" d="M7.776 5.553a.5.5 0 0 1 .448 0l6 3a.5.5 0 1 1-.448.894L8 6.56 2.224 9.447a.5.5 0 1 1-.448-.894l6-3z"/>
  </svg>
</div>
<form method="post" action = '/en/map'>
    <div class="menu-box-hidden" id="menu-box">
      <div id="menu-scroller">
        <div id="menu-box-information">
          <label class="label">
            <span>Shelters</span>
            <input type="checkbox" id="checkbox1" class="check" name="shelter">
          </label>
    
          <label class="label">
            <span>Invisibility</span>
            <input type="checkbox" id="checkbox2" class="check" name="unbreakpoint">
          </label>
    
          <label class="label">
            <span>Pharmacy</span>
            <input type="checkbox" id="checkbox3" class="check" name="drugstore">
          </label>
    
          <label class="label">
            <span>Hospitals</span>
            <input type="checkbox" id="checkbox4" class="check" name="hospital">
          </label>
          <label class="label">
            <span>Police</span>
            <input type="checkbox" id="checkbox4" class="check" name="police_departments">
          </label>
          <div>
            <button onclick="hideCheckBoxesMenu()" type="submit" class ='button'>Submit</button>
          </div>
        </div>
      </div>
        <div onclick="hideCheckBoxesMenu()" id="closing-checkboxes">
            <svg color="green" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-arrow-down" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M8 1a.5.5 0 0 1 .5.5v11.793l3.146-3.147a.5.5 0 0 1 .708.708l-4 4a.5.5 0 0 1-.708 0l-4-4a.5.5 0 0 1 .708-.708L7.5 13.293V1.5A.5.5 0 0 1 8 1z"/>
            </svg>
        </div>
    </div>
</form>

<div onclick="showLegenda()" id="legenda-button">
  <svg color="green" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-chevron-compact-left" viewBox="0 0 16 16">
    <path fill-rule="evenodd" d="M9.224 1.553a.5.5 0 0 1 .223.67L6.56 8l2.888 5.776a.5.5 0 1 1-.894.448l-3-6a.5.5 0 0 1 0-.448l3-6a.5.5 0 0 1 .67-.223z"/>
  </svg>
</div>
<div id="sidebar" class="sidebar-hidden">
  <div class="image">
    <img src="https://i.ibb.co/FJ6phjJ/Home-Health-place-logo-5.png" alt="Home-Health-place-logo-5">
    <div class="description">
      <div class="caption"><strong>Invisibility</strong></div>
    </div>
  </div>
  <div class="image">
    <img src="https://iili.io/HkhnDeR.md.png" alt="Home-Health-place-logo-6">
    <div class="description">
      <div class="caption"><strong>Shelter</strong></div>
    </div>
  </div>
  <div class="image">
    <img src="https://i.ibb.co/6v60Vwd/hospitals.png" alt="hospitals">
    <div class="description">
      <div class="caption"><strong>Hospital</strong></div>
    </div>
  </div>
  <div class="image">
    <img src="https://i.ibb.co/pRS0mpj/pharmacy.png" alt="pharmacy">
    <div class="description">
      <div class="caption"><strong>Pharmacy</strong></div>
    </div>
  </div>
  <div class="image">
    <img src="https://i.ibb.co/Sfmd5QH/police.png" alt="police">
    <div class="description">
      <div class="caption"><strong>Police</strong></div>
    </div>
  </div>
  <div onclick="hideLegenda()" id="closing-legenda">
    <svg color="white" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
      <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8z"/>
    </svg>
  </div>
</div>
"""
checkbox_ukr_all_browsers_mobile = """
<style>
#image{
    position: absolute;
    display: none;
    height: 100%;
    width: 100%;
  }
@media screen and (orientation: landscape){
    .main{
      display: none;
    }
    .folium-map{
      display: none;
    }
    #image{
      display: block;
    }
}
  body{
    overflow: hidden;
  }
  .leaflet-top.leaflet-left{
    display: none;
  }
  #menu-box{
    position: absolute;
    z-index: 900;
    /*left: 40vw;
    top: 60vh;*/
    height: auto;
    width: auto;
  }
  #menu-box-information{
    position: fixed;
    width: 20vw;
    /*height: 25vh;*/
    height: auto;
    z-index: 900;
    border: 1px solid black;
    background-color: #006e48;
    border-radius: 20px;
    opacity: 80%;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    padding: 2vh;
    overflow-y: auto;
    overflow-x: hidden;
  }
  @media (max-width: 768px) {
    #menu-box-information{
          position: fixed;
          width: 60vw;
          height: 45vh;
          height: auto;
          z-index: 900;
          border: 1px solid black;
          background-color: #006e48;
          border-radius: 20px;
          opacity: 80%;
          flex-direction: column;
          justify-content: space-between;
          align-items: center;
          padding: 2vh;
          overflow-y: auto;
          overflow-x: hidden;
    }
    .menu-box-revealed{
        transform: translate3d(19.5vw, 35vh, 0);
        transition: transform 1.0s cubic-bezier(0, .52, 0, 1);
      }
      .menu-box-hidden{
        transform: translate3d(19.5vw, 100vh, 0);
        transition: transform 2.0s cubic-bezier(0, .52, 0, 1);
  }
      #closing-checkboxes {
          position: absolute;
          z-index: 900;
          top: 32vh;
          left: 24vw;
      }
  }
  @media (min-width: 767px) {
      #menu-box-information {
          position: fixed;
          width: 40vw;
          /*height: 25vh;*/
          height: auto;
          z-index: 900;
          border: 1px solid black;
          background-color: #006e48;
          border-radius: 20px;
          opacity: 80%;
          flex-direction: column;
          justify-content: space-between;
          align-items: center;
          padding: 2vh;
          overflow-y: auto;
          overflow-x: hidden;
      }

      .menu-box-revealed {
          transform: translate3d(30vw, 46vh, 0);
          transition: transform 1.0s cubic-bezier(0, .52, 0, 1);
      }

      .menu-box-hidden {
          transform: translate3d(30vw, 100vh, 0);
          transition: transform 2.0s cubic-bezier(0, .52, 0, 1);
      }

      #closing-checkboxes {
          position: absolute;
          z-index: 900;
          top: 32vh;
          left: 18.5vw;
      }
  }

  .label{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-radius: 10px;
    margin-right: 10px;
    font-size: 2vmin;
    transition: 1s;
    flex-grow: 1;
    min-width: 0;
    padding: 5px;
    background-color: #f8f8f8;
    margin: 1px;
    padding-bottom: 1px;
    padding-top: 1px;
    color: black;
    height: auto;
  }
  .check {
    position: relative;
    width: 20px;
    height: 20px;
    border-radius: 2px;
    appearance: none;
    background-color: #bbb;
    transition: all .3s;
  }

  .check::before {
    content: '';
    position: absolute;
    border: solid #fff;
    display: block;
    width: .3em;
    height: .6em;
    border-width: 0 .2em .2em 0;
    z-index: 1;
    opacity: 0;
    right: calc(50% - .3em);
    top: calc(50% - .6em);
    transform: rotate(0deg);
    transition: all .3s;
    transform-origin: center center;
  }

  .check:checked {
    animation: a .3s ease-in forwards;
    background-color: #00a97e;
  }

  .check:checked::before {
    opacity: 1;
    transform: rotate(405deg);
  }

  @keyframes a {
    0% {
      opacity: 1;
      transform: scale(1) rotateY(0deg);
    }

    50% {
      opacity: 0;
      transform: scale(.8) rotateY(180deg);
    }

    100% {
      opacity: 1;
      transform: scale(1) rotateY(360deg);
    }
  }
  button {
      display: flex;
      justify-content: center;
      align-items: center;
      width: fit-content;
      justify-content: center;
      align-items: center;
      font-size: 1.5vmin;
      color: black;
      min-width: 100px;
      height: 45px;
      padding: 8px;
      border-radius: 5px;
      border: 2.5px solid #E0E1E4;
      box-shadow: 0px 0px 20px -20px;
      cursor: pointer;
      background-color: white;
      transition: all 0.2s ease-in-out 0ms;
      user-select: none;
      z-index: 900;
      margin: 1vh auto;
      font-family: 'Poppins', sans-serif;
    }

    button:hover {
      background-color: #F2F2F2;
      box-shadow: 0px 0px 20px -18px;
      color: black;
    }

    button:active {
      transform: scale(0.95);
      color: black;
    }
  @media (max-width: 768px) {
        #arrow-up{
        position: absolute;
        z-index: 900;
        top: 60vh;
        left: 44vw;
      }
  }
  @media (min-width: 767px){
        #arrow-up{
        position: absolute;
        z-index: 900;
        top: 80vh;
        left: 48vw;
      }
  }


  #menu-button {
    position: absolute;
    display: block;
    z-index: 900;
    top: 50vh;
      left: 5vw;
  }
  @media (min-width: 768px){
    #image-overlay {
      display: flex;
      z-index: 900;
      position: absolute;
      flex-direction: column;
      justify-content: flex-start;
      align-items: flex-start;
      margin: 0;
      width: 30vw;
      height: 100vh;
      background-color: #00a97e;
      opacity:85%;
      border: 2px solid rgb(5, 102, 52);
      overflow: hidden;
    }
  .donat{
      background-color: black; /* Green */
      border: none;
      color: white;
      padding: 15px 32px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 16px;
      width: 300px;
      margin-top: 3vh;
      margin-bottom: 3vh;
      margin-left: 3vw
  }
  }
  @media (max-width: 767px){
    #image-overlay {
      display: flex;
      z-index: 900;
      position: absolute;
      flex-direction: column;
      justify-content: flex-start;
      align-items: flex-start;
      margin: 0;
      width: 100vw;
      height: 100vh;
      background-color: #00a97e;
      opacity:85%;
      border: 2px solid rgb(5, 102, 52);
      overflow: hidden;
    }
  .donat{
      position: relative;
      background-color: black; /* Green */
      border: none;
      color: white;
      padding: 15px 32px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 16px;
      width: 300px;
      margin-top: 3vh;
      margin-bottom: 3vh;
      margin-left: 10vw;
  }
  }
  .menu-revealed{
    transform: translate3d(0vw, 0vh, 0);
    transition: transform 1.0s cubic-bezier(0, .52, 0, 1);
  }
  .menu-hidden{
    transform: translate3d(-100vw, 0vh, 0);
    transition: transform 2.0s cubic-bezier(0, .52, 0, 1);
  }
  #image-overlay a {
    display: block;
    z-index: 900;
    position: relative;
    color: #fff;
    text-decoration: line-under;
    margin: 10px 10px 0 10px;
    transition: 2s;
    height: 5vh;
    text-align: center;
    line-height: 1.5;
  }

  #image-overlay a:hover {
    font-size: 34px;
    color: rgb(238, 253, 236);
  }
  #logo{
    position: relative;
    z-index: 900;
    width: auto;
    height: auto;
    max-width: 30vw;
    max-height: 20vh;
  }
  h3 {
      margin-top: 2vh;
      margin-bottom: 2vh;
      font-size: 3.5vmin;
  }
  @media only screen and (max-width: 767px){
    h3{
      font-size: 20px;
    }
  }


  #legenda-button{
    position: absolute;
    z-index: 900;
    top: 50vh;
    left: 90vw;
  }
  @media (max-width: 768px){
    #legenda-button{
      left: 85vw;
    }
  }
  #sidebar {
    position: fixed;
    z-index: 900;
    background-color: #00a97e;
    opacity:85%;
    border: 2px solid rgb(5, 102, 52);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  @media (min-width: 768px){
    #sidebar {
      height: 100vh;
      width: 30vw;
    }
    .sidebar-revealed{
      transform: translate3d(70vw, 0vh, 0);
      transition: transform 1.0s cubic-bezier(0, .52, 0, 1);
    }
    .sidebar-hidden{
      transform: translate3d(200vw, 0vh, 0);
      transition: transform 3.0s cubic-bezier(0, .52, 0, 1);
    }
  }
  @media (max-width: 767px){
    #sidebar {
      width: 100vw;
      height: 100vh
    }
    .sidebar-revealed{
      transform: translate3d(0, 0, 0);
      transition: transform 1.0s cubic-bezier(0, .52, 0, 1);
    }
    .sidebar-hidden{
      transform: translate3d(200vw, 0vh, 0);
      transition: transform 2.0s cubic-bezier(0, .52, 0, 1);
    }
    #closing-legenda{
        z-index: 900;
        position: absolute;
        left: 20vw;
    }
  }
  #sidebar .image {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin: 10px 0;
    width: 100%;
    text-align: center;
  }

  #sidebar .image img {
    height: 10vh;
    margin: 7px;
    width: auto;
    max-width: 100%;
    max-height: 100%;
  }

  #sidebar .caption {
    margin-top: 5px;
    font-size: 1.5rem;
    color: #ffff;
  }

  #checked-checkbox{
      position: absolute;
      z-index: 900;
      display: none;
  }


</style>
<script>
  function showCheckBoxesMenu(){
    document.getElementById('menu-box').classList.remove('menu-box-hidden');
    document.getElementById('menu-box').classList.add('menu-box-revealed');
    document.getElementById('arrow-up').style.display = 'none';
    document.getElementById('menu-button').style.display = 'none';
    document.getElementById('legenda-button').style.display = 'none';

  }
  function hideCheckBoxesMenu(){
    document.getElementById('menu-box').classList.remove('menu-box-revealed');
    document.getElementById('menu-box').classList.add('menu-box-hidden');
    document.getElementById('arrow-up').style.display = 'block';
    document.getElementById('menu-button').style.display = 'block';
    document.getElementById('legenda-button').style.display = 'block';
  }


  function showInfoMenu(){
    document.getElementById('image-overlay').classList.remove('menu-hidden');
    document.getElementById('image-overlay').classList.add('menu-revealed');
    document.getElementById('menu-button').style.display = 'none';
    document.getElementById('arrow-up').style.display = 'none';
    document.getElementById('legenda-button').style.display = 'none';
  }
  function hideInfoMenu(){
    document.getElementById('image-overlay').classList.remove('menu-revealed');
    document.getElementById('image-overlay').classList.add('menu-hidden');
    document.getElementById('menu-button').style.display = 'block';
    document.getElementById('arrow-up').style.display = 'block';
    document.getElementById('legenda-button').style.display = 'block';
  }


  function showLegenda(){
    document.getElementById('sidebar').classList.remove('sidebar-hidden');
    document.getElementById('sidebar').classList.add('sidebar-revealed');
    document.getElementById('menu-button').style.display = 'none';
    document.getElementById('arrow-up').style.display = 'none';
    document.getElementById('legenda-button').style.display = 'none';
  }
  function hideLegenda(){
    document.getElementById('sidebar').classList.remove('sidebar-revealed');
    document.getElementById('sidebar').classList.add('sidebar-hidden');
    document.getElementById('menu-button').style.display = 'block';
    document.getElementById('arrow-up').style.display = 'block';
    document.getElementById('legenda-button').style.display = 'block';
  }

</script>
<img id="image" src="https://i.ibb.co/T8TjLxK/sValK.png">
<div class="main">
    <div onclick="showInfoMenu()" id="menu-button">
      <svg color="green" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-chevron-compact-right" viewBox="0 0 16 16">
        <path fill-rule="evenodd" d="M6.776 1.553a.5.5 0 0 1 .671.223l3 6a.5.5 0 0 1 0 .448l-3 6a.5.5 0 1 1-.894-.448L9.44 8 6.553 2.224a.5.5 0 0 1 .223-.671z"/>
      </svg>
    </div>
    <div class="menu-hidden" id="image-overlay">
      <img id="logo" src="https://i.ibb.co/RykHJVm/logo.png" alt="logo" height="130" width="300">
      <h3 class="line"><a href="/ua">Головна сторінка</a></h3>
      <h3 class="line"><a href="/ua/about-us">Про нас</a></h3>
      <h3 class="line"><a href="/ua/policies">Правила користування</a></h3>
        <form action="https://u24.gov.ua/">
            <input class='donat' type="submit" value="UNITED 24" />
        </form>
      <div onclick="hideInfoMenu()" id="arrow-left">
        <svg color="white" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-arrow-left" viewBox="0 0 16 16">
          <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
        </svg>
      </div>
    </div>
    
    
    <div class="arrow-button-up">
      <svg id="arrow-up" onclick="showCheckBoxesMenu()" color="green" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-chevron-compact-up" viewBox="0 0 16 16">
        <path fill-rule="evenodd" d="M7.776 5.553a.5.5 0 0 1 .448 0l6 3a.5.5 0 1 1-.448.894L8 6.56 2.224 9.447a.5.5 0 1 1-.448-.894l6-3z"/>
      </svg>
    </div>
    
    <form method="post" action = '/ua/map'>
        <div class="menu-box-hidden" id="menu-box">
          <div id="menu-scroller">
            <div id="menu-box-information">
              <label class="label">
                <span>Укриття</span>
                <input type="checkbox" id="checkbox1" class="check" name="shelter">
              </label>
        
              <label class="label">
                <span>Пункти незламності</span>
                <input type="checkbox" id="checkbox2" class="check" name="unbreakpoint">
              </label>
        
              <label class="label">
                <span>Аптеки</span>
                <input type="checkbox" id="checkbox3" class="check" name="drugstore">
              </label>
        
              <label class="label">
                <span>Лікарні</span>
                <input type="checkbox" id="checkbox4" class="check" name="hospital">
              </label>
              <label class="label">
                <span>Поліція</span>
                <input type="checkbox" id="checkbox4" class="check" name="police_departments">
              </label>
              <div>
                <button onclick="hideCheckBoxesMenu() " type="submit" class ='button'>Подати</button>
              </div>
            </div>
          </div>
            <div onclick="hideCheckBoxesMenu()" id="closing-checkboxes">
                <svg color="green" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-arrow-down" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 1a.5.5 0 0 1 .5.5v11.793l3.146-3.147a.5.5 0 0 1 .708.708l-4 4a.5.5 0 0 1-.708 0l-4-4a.5.5 0 0 1 .708-.708L7.5 13.293V1.5A.5.5 0 0 1 8 1z"/>
                </svg>
            </div>
        </div>
    </form>
    
    <div onclick="showLegenda()" id="legenda-button">
      <svg color="green" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-chevron-compact-left" viewBox="0 0 16 16">
        <path fill-rule="evenodd" d="M9.224 1.553a.5.5 0 0 1 .223.67L6.56 8l2.888 5.776a.5.5 0 1 1-.894.448l-3-6a.5.5 0 0 1 0-.448l3-6a.5.5 0 0 1 .67-.223z"/>
      </svg>
    </div>
    <div id="sidebar" class="sidebar-hidden">
      <div class="image">
        <img src="https://i.ibb.co/FJ6phjJ/Home-Health-place-logo-5.png" alt="Home-Health-place-logo-5">
        <div class="description">
          <div class="caption"><strong>Пункт незламності</strong></div>
        </div>
      </div>
      <div class="image">
        <img src="https://iili.io/HkhnDeR.md.png" alt="Home-Health-place-logo-6">
        <div class="description">
          <div class="caption"><strong>Укриття</strong></div>
        </div>
      </div>
      <div class="image">
        <img src="https://i.ibb.co/6v60Vwd/hospitals.png" alt="hospitals">
        <div class="description">
          <div class="caption"><strong>Лікарня</strong></div>
        </div>
      </div>
      <div class="image">
        <img src="https://i.ibb.co/pRS0mpj/pharmacy.png" alt="pharmacy">
        <div class="description">
          <div class="caption"><strong>Аптека</strong></div>
        </div>
      </div>
      <div class="image">
        <img src="https://i.ibb.co/Sfmd5QH/police.png" alt="police">
        <div class="description">
          <div class="caption"><strong>Поліція</strong></div>
        </div>
      </div>
      <div onclick="hideLegenda()" id="closing-legenda">
        <svg color="white" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
          <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8z"/>
        </svg>
      </div>
    </div>
</div>
    """
checkbox_eng_all_browsers_mobile = """
<style>
    #image{
    position: absolute;
    display: none;
    height: 100%;
    width: 100%;
  }
@media screen and (orientation: landscape){
    .main{
      display: none;
    }
    .folium-map{
      display: none;
    }
    #image{
      display: block;
    }
}
  body{
    overflow: hidden;
  }
  .leaflet-top.leaflet-left{
    display: none;
  }
  #menu-box{
    position: absolute;
    z-index: 900;
    height: auto;
    width: auto;
  }
  #menu-box-information{
    position: fixed;
    width: 40vw;
    height: auto;
    z-index: 900;
    border: 1px solid black;
    background-color: #006e48;
    border-radius: 20px;
    opacity: 80%;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    padding: 2vh;
    overflow-y: auto;
    overflow-x: hidden;
  }
  @media (max-width: 768px) {
      #menu-box-information{
          position: fixed;
          width: 60vw;
          height: 45vh;
          height: auto;
          z-index: 900;
          border: 1px solid black;
          background-color: #006e48;
          border-radius: 20px;
          opacity: 80%;
          flex-direction: column;
          justify-content: space-between;
          align-items: center;
          padding: 2vh;
          overflow-y: auto;
          overflow-x: hidden;
      }
      .menu-box-revealed{
          transform: translate3d(19.5vw, 35vh, 0);
          transition: transform 1.0s cubic-bezier(0, .52, 0, 1);
      }
      .menu-box-hidden{
          transform: translate3d(19.5vw, 100vh, 0);
          transition: transform 2.0s cubic-bezier(0, .52, 0, 1);
      }
      #closing-checkboxes {
          position: absolute;
          z-index: 900;
          top: 32vh;
          left: 24vw;
      }
  }
  @media (min-width: 767px){
    #menu-box-information{
      position: fixed;
      width: 40vw;
      /*height: 25vh;*/
      height: auto;
      z-index: 900;
      border: 1px solid black;
      background-color: #006e48;
      border-radius: 20px;
      opacity: 80%;
      flex-direction: column;
      justify-content: space-between;
      align-items: center;
      padding: 2vh;
      overflow-y: auto;
      overflow-x: hidden;
    }
      .menu-box-revealed {
          transform: translate3d(30vw, 46vh, 0);
          transition: transform 1.0s cubic-bezier(0, .52, 0, 1);
      }
      .menu-box-hidden{
        transform: translate3d(30vw, 100vh, 0);
        transition: transform 2.0s cubic-bezier(0, .52, 0, 1);
      }
      #closing-checkboxes {
          position: absolute;
          z-index: 900;
          top: 32vh;
          left: 18.4vw;
      }
  }
  .label{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-radius: 10px;
    margin-right: 10px;
    font-size: 2vmin;
    transition: 1s;
    flex-grow: 1;
    min-width: 0;
    padding: 5px;
    background-color: #f8f8f8;
    margin: 1px;
    padding-bottom: 1px;
    padding-top: 1px;
    color: black;
    height: auto;
  }
  .check {
    position: relative;
    width: 20px;
    height: 20px;
    border-radius: 2px;
    appearance: none;
    background-color: #bbb;
    transition: all .3s;
  }

  .check::before {
    content: '';
    position: absolute;
    border: solid #fff;
    display: block;
    width: .3em;
    height: .6em;
    border-width: 0 .2em .2em 0;
    z-index: 1;
    opacity: 0;
    right: calc(50% - .3em);
    top: calc(50% - .6em);
    transform: rotate(0deg);
    transition: all .3s;
    transform-origin: center center;
  }

  .check:checked {
    animation: a .3s ease-in forwards;
    background-color: #00a97e;
  }

  .check:checked::before {
    opacity: 1;
    transform: rotate(405deg);
  }

  @keyframes a {
    0% {
      opacity: 1;
      transform: scale(1) rotateY(0deg);
    }

    50% {
      opacity: 0;
      transform: scale(.8) rotateY(180deg);
    }

    100% {
      opacity: 1;
      transform: scale(1) rotateY(360deg);
    }
  }
  button {
      display: flex;
      justify-content: center;
      align-items: center;
      width: fit-content;
      justify-content: center;
      align-items: center;
      font-size: 1.5vmin;
      color: black;
      min-width: 100px;
      height: 45px;
      padding: 8px;
      border-radius: 5px;
      border: 2.5px solid #E0E1E4;
      box-shadow: 0px 0px 20px -20px;
      cursor: pointer;
      background-color: white;
      transition: all 0.2s ease-in-out 0ms;
      user-select: none;
      z-index: 900;
      margin: 1vh auto;
      font-family: 'Poppins', sans-serif;
    }

    button:hover {
      background-color: #F2F2F2;
      box-shadow: 0px 0px 20px -18px;
      color: black;
    }

    button:active {
      transform: scale(0.95);
      color: black;
    }
  @media (max-width: 768px) {
        #arrow-up{
        position: absolute;
        z-index: 900;
        top: 60vh;
        left: 44vw;
      }
  }
  @media (min-width: 767px){
        #arrow-up{
        position: absolute;
        z-index: 900;
        top: 80vh;
        left: 48vw;
      }
  }
  


  #menu-button {
    position: absolute;
    display: block;
    z-index: 900;
    top: 50vh;
      left: 5vw;
  }
  @media (min-width: 768px){
    #image-overlay {
      display: flex;
      z-index: 900;
      position: absolute;
      flex-direction: column;
      justify-content: flex-start;
      align-items: flex-start;
      margin: 0;
      width: 30vw;
      height: 100vh;
      background-color: #00a97e;
      opacity:85%;
      border: 2px solid rgb(5, 102, 52);
      overflow: hidden;
    }
  .donat{
      background-color: black; /* Green */
      border: none;
      color: white;
      padding: 15px 32px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 16px;
      width: 300px;
      margin-top: 3vh;
      margin-bottom: 3vh;
      margin-left: 3vw
  }
  }
  @media (max-width: 767px){
    #image-overlay {
      display: flex;
      z-index: 900;
      position: absolute;
      flex-direction: column;
      justify-content: flex-start;
      align-items: flex-start;
      margin: 0;
      width: 100vw;
      height: 100vh;
      background-color: #00a97e;
      opacity:85%;
      border: 2px solid rgb(5, 102, 52);
      overflow: hidden;
    }
  .donat{
      position: relative;
      background-color: black; /* Green */
      border: none;
      color: white;
      padding: 15px 32px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 16px;
      width: 300px;
      margin-top: 3vh;
      margin-bottom: 3vh;
      margin-left: 10vw;
  }
  }
  .menu-revealed{
    transform: translate3d(0vw, 0vh, 0);
    transition: transform 1.0s cubic-bezier(0, .52, 0, 1);
  }
  .menu-hidden{
    transform: translate3d(-100vw, 0vh, 0);
    transition: transform 2.0s cubic-bezier(0, .52, 0, 1);
  }
  #image-overlay a {
    display: block;
    z-index: 900;
    position: relative;
    color: #fff;
    text-decoration: line-under;
    margin: 10px 10px 0 10px;
    transition: 2s;
    height: 5vh;
    text-align: center;
    line-height: 1.5;
  }

  #image-overlay a:hover {
    font-size: 34px;
    color: rgb(238, 253, 236);
  }
  #logo{
    position: relative;
    z-index: 900;
    width: auto;
    height: auto;
    max-width: 30vw;
    max-height: 20vh;
  }
  h3 {
      margin-top: 2vh;
      margin-bottom: 2vh;
      font-size: 3.5vmin;
  }
  @media only screen and (max-width: 767px){
    h3{
      font-size: 20px;
    }
  }


  #legenda-button{
      position: absolute;
      z-index: 900;
      top: 50vh;
      left: 90vw;
  }
  @media (max-width: 768px){
      #legenda-button{
          left: 85vw;
      }
  }
  #sidebar {
    position: fixed;
    z-index: 900;
    background-color: #00a97e;
    opacity:85%;
    border: 2px solid rgb(5, 102, 52);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  @media (min-width: 768px){
    #sidebar {
      height: 100vh;
      width: 30vw;
    }
    .sidebar-revealed{
      transform: translate3d(70vw, 0vh, 0);
      transition: transform 1.0s cubic-bezier(0, .52, 0, 1);
    }
    .sidebar-hidden{
      transform: translate3d(200vw, 0vh, 0);
      transition: transform 3.0s cubic-bezier(0, .52, 0, 1);
    }
  }
  @media (max-width: 767px){
    #sidebar {
      width: 100vw;
      height: 100vh
    }
    .sidebar-revealed{
      transform: translate3d(0, 0, 0);
      transition: transform 1.0s cubic-bezier(0, .52, 0, 1);
    }
    .sidebar-hidden{
      transform: translate3d(200vw, 0vh, 0);
      transition: transform 2.0s cubic-bezier(0, .52, 0, 1);
    }
      #closing-legenda{
          z-index: 900;
          position: absolute;
          left: 20vw;
      }
  }
  #sidebar .image {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin: 10px 0;
    width: 100%;
    text-align: center;
  }

  #sidebar .image img {
    height: 10vh;
    margin: 7px;
    width: auto;
    max-width: 100%;
    max-height: 100%;
  }

  #sidebar .caption {
    margin-top: 5px;
    font-size: 1.5rem;
    color: #ffff;
  }

  #checked-checkbox{
      position: absolute;
      z-index: 900;
      display: none;
  }


</style>
<script>
  function showCheckBoxesMenu(){
    document.getElementById('menu-box').classList.remove('menu-box-hidden');
    document.getElementById('menu-box').classList.add('menu-box-revealed');
    document.getElementById('arrow-up').style.display = 'none';
    document.getElementById('menu-button').style.display = 'none';
    document.getElementById('legenda-button').style.display = 'none';

  }
  function hideCheckBoxesMenu(){
    document.getElementById('menu-box').classList.remove('menu-box-revealed');
    document.getElementById('menu-box').classList.add('menu-box-hidden');
    document.getElementById('arrow-up').style.display = 'block';
    document.getElementById('menu-button').style.display = 'block';
    document.getElementById('legenda-button').style.display = 'block';
  }


  function showInfoMenu(){
    document.getElementById('image-overlay').classList.remove('menu-hidden');
    document.getElementById('image-overlay').classList.add('menu-revealed');
    document.getElementById('menu-button').style.display = 'none';
    document.getElementById('arrow-up').style.display = 'none';
    document.getElementById('legenda-button').style.display = 'none';
  }
  function hideInfoMenu(){
    document.getElementById('image-overlay').classList.remove('menu-revealed');
    document.getElementById('image-overlay').classList.add('menu-hidden');
    document.getElementById('menu-button').style.display = 'block';
    document.getElementById('arrow-up').style.display = 'block';
    document.getElementById('legenda-button').style.display = 'block';
  }


  function showLegenda(){
    document.getElementById('sidebar').classList.remove('sidebar-hidden');
    document.getElementById('sidebar').classList.add('sidebar-revealed');
    document.getElementById('menu-button').style.display = 'none';
    document.getElementById('arrow-up').style.display = 'none';
    document.getElementById('legenda-button').style.display = 'none';
  }
  function hideLegenda(){
    document.getElementById('sidebar').classList.remove('sidebar-revealed');
    document.getElementById('sidebar').classList.add('sidebar-hidden');
    document.getElementById('menu-button').style.display = 'block';
    document.getElementById('arrow-up').style.display = 'block';
    document.getElementById('legenda-button').style.display = 'block';
  }

</script>
<img id="image" src="https://i.ibb.co/T8TjLxK/sValK.png">
<div class="main">
    <div onclick="showInfoMenu()" id="menu-button">
      <svg color="green" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-chevron-compact-right" viewBox="0 0 16 16">
        <path fill-rule="evenodd" d="M6.776 1.553a.5.5 0 0 1 .671.223l3 6a.5.5 0 0 1 0 .448l-3 6a.5.5 0 1 1-.894-.448L9.44 8 6.553 2.224a.5.5 0 0 1 .223-.671z"/>
      </svg>
    </div>
    <div class="menu-hidden" id="image-overlay">
      <img id="logo" src="https://i.ibb.co/RykHJVm/logo.png" alt="logo" height="130" width="300">
      <h3 class="line"><a href="/en">Main</a></h3>
      <h3 class="line"><a href="/en/about-us">About Us</a></h3>
      <h3 class="line"><a href="/en/policies">Terms of Use</a></h3>
        <form action="https://u24.gov.ua/">
            <input class='donat' type="submit" value="UNITED 24" />
        </form>
      <div onclick="hideInfoMenu()" id="arrow-left">
        <svg color="white" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-arrow-left" viewBox="0 0 16 16">
          <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
        </svg>
      </div>
    </div>
    
    <div class="arrow-button-up">
      <svg id="arrow-up" onclick="showCheckBoxesMenu()" color="green" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-chevron-compact-up" viewBox="0 0 16 16">
        <path fill-rule="evenodd" d="M7.776 5.553a.5.5 0 0 1 .448 0l6 3a.5.5 0 1 1-.448.894L8 6.56 2.224 9.447a.5.5 0 1 1-.448-.894l6-3z"/>
      </svg>
    </div>
    <form method="post" action = '/en/map'>
        <div class="menu-box-hidden" id="menu-box">
          <div id="menu-scroller">
            <div id="menu-box-information">
              <label class="label">
                <span>Shelters</span>
                <input type="checkbox" id="checkbox1" class="check" name="shelter">
              </label>
        
              <label class="label">
                <span>Invisibility</span>
                <input type="checkbox" id="checkbox2" class="check" name="unbreakpoint">
              </label>
        
              <label class="label">
                <span>Pharmacy</span>
                <input type="checkbox" id="checkbox3" class="check" name="drugstore">
              </label>
        
              <label class="label">
                <span>Hospitals</span>
                <input type="checkbox" id="checkbox4" class="check" name="hospital">
              </label>
              <label class="label">
                <span>Police</span>
                <input type="checkbox" id="checkbox4" class="check" name="police_departments">
              </label>
              <div>
                <button onclick="hideCheckBoxesMenu()" type="submit" class ='button'>Submit</button>
              </div>
            </div>
          </div>
            <div onclick="hideCheckBoxesMenu()" id="closing-checkboxes">
                <svg color="green" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-arrow-down" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 1a.5.5 0 0 1 .5.5v11.793l3.146-3.147a.5.5 0 0 1 .708.708l-4 4a.5.5 0 0 1-.708 0l-4-4a.5.5 0 0 1 .708-.708L7.5 13.293V1.5A.5.5 0 0 1 8 1z"/>
                </svg>
            </div>
        </div>
    </form>
    
    <div onclick="showLegenda()" id="legenda-button">
      <svg color="green" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-chevron-compact-left" viewBox="0 0 16 16">
        <path fill-rule="evenodd" d="M9.224 1.553a.5.5 0 0 1 .223.67L6.56 8l2.888 5.776a.5.5 0 1 1-.894.448l-3-6a.5.5 0 0 1 0-.448l3-6a.5.5 0 0 1 .67-.223z"/>
      </svg>
    </div>
    <div id="sidebar" class="sidebar-hidden">
      <div class="image">
        <img src="https://i.ibb.co/FJ6phjJ/Home-Health-place-logo-5.png" alt="Home-Health-place-logo-5">
        <div class="description">
          <div class="caption"><strong>Invisibility</strong></div>
        </div>
      </div>
      <div class="image">
        <img src="https://iili.io/HkhnDeR.md.png" alt="Home-Health-place-logo-6">
        <div class="description">
          <div class="caption"><strong>Shelter</strong></div>
        </div>
      </div>
      <div class="image">
        <img src="https://i.ibb.co/6v60Vwd/hospitals.png" alt="hospitals">
        <div class="description">
          <div class="caption"><strong>Hospital</strong></div>
        </div>
      </div>
      <div class="image">
        <img src="https://i.ibb.co/pRS0mpj/pharmacy.png" alt="pharmacy">
        <div class="description">
          <div class="caption"><strong>Pharmacy</strong></div>
        </div>
      </div>
      <div class="image">
        <img src="https://i.ibb.co/Sfmd5QH/police.png" alt="police">
        <div class="description">
          <div class="caption"><strong>Police</strong></div>
        </div>
      </div>
      <div onclick="hideLegenda()" id="closing-legenda">
        <svg color="white" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
          <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8z"/>
        </svg>
      </div>
    </div>
</div>
"""


def create_map_ukrainian(latitude, longitude, filter_list, chrome, mobile):

    m = folium.Map(location=[latitude, longitude], tiles="CartoDB Positron", zoom_start=12
                   )
    fg = folium.FeatureGroup(name="SA creators map")
    fg.add_child(folium.Marker(location=[latitude, longitude],
                               icon=folium.features.CustomIcon('https://iili.io/HkhEsJR.md.png', icon_size=(52, 50)),
                               id='location').add_to(fg))

    shelter = get_nearest('files/shelters_coor_ukrainian.csv', latitude, longitude)
    punkts = get_nearest('files/invicibility_coor_ukrainian.csv', latitude, longitude)
    police = get_nearest('files/police_coor_ukrainian.csv', latitude, longitude)
    hospitals = get_nearest('files/hospitals_coor_ukrainian.csv', latitude, longitude)
    pharmacy = get_nearest('files/apotheke_coor_ukrainian.csv', latitude, longitude)
    if 'shelter' in filter_list:
        parse_markers(shelter, 'shelter', 'https://iili.io/HkhnDeR.md.png', html_ukr, fg)
    if 'unbreakable' in filter_list:
        parse_markers(punkts, "punkts", 'https://i.ibb.co/FJ6phjJ/Home-Health-place-logo-5.png', html_ukr, fg)
    if 'police' in filter_list:
        parse_markers(police, 'police', 'https://i.ibb.co/Sfmd5QH/police.png', html_ukr, fg)
    if 'hospitals' in filter_list:
        parse_markers(hospitals, "hospitals", 'https://i.ibb.co/6v60Vwd/hospitals.png', html_ukr, fg)
    if 'drugstores' in filter_list:
        parse_markers(pharmacy, 'pharmacy', 'https://i.ibb.co/pRS0mpj/pharmacy.png', html_ukr, fg)


    m.get_root().header.add_child(folium.Element("""
    <link rel="shortcut icon" type="image/png" href="https://i.ibb.co/xYsVqhf/logo.png"/>
    <title>SA</title>
    """))
    if mobile:
        m.get_root().html.add_child(folium.Element(checkbox_ukr_all_browsers_mobile))
    else:
        if chrome:
            m.get_root().html.add_child(folium.Element(checkbox_ukr_chrome))
        else:
            m.get_root().html.add_child(folium.Element(checkbox_ukr_all_browsers))
    m.add_child(fg)
    m.save('templates/mapa_ukrainian.html')

    with open('templates/mapa_ukrainian.html', 'r') as file:
        file = file.read()
        return file


def create_map_english(latitude, longitude, filter_list, chrome, mobile):
    m = folium.Map(location=[latitude, longitude], tiles="CartoDB Positron", zoom_start=12
                   )
    fg = folium.FeatureGroup(name="SA creators map")
    fg.add_child(folium.Marker(location=[latitude, longitude],
                               icon=folium.features.CustomIcon('https://iili.io/HkhEsJR.md.png', icon_size=(52, 50)),
                               id='location').add_to(fg))

    shelter = get_nearest_english('files/english_coord/shelters_english_coord.csv', latitude, longitude)
    punkts = get_nearest_english('files/english_coord/invisibly_english_coord.csv', latitude, longitude)
    police = get_nearest_english('files/english_coord/police_english_coord.csv', latitude, longitude)
    hospitals = get_nearest_english('files/english_coord/hospitals_english_coord.csv', latitude, longitude)
    pharmacy = get_nearest_english('files/english_coord/pharmacy_enlish_coord.csv', latitude, longitude)
    #
    if 'shelter' in filter_list:
        parse_english_markers(shelter, 'shelter', 'https://iili.io/HkhnDeR.md.png', html_eng, fg)
    if 'unbreakable' in filter_list:
        parse_english_markers(punkts, "punkts", 'https://i.ibb.co/FJ6phjJ/Home-Health-place-logo-5.png', html_eng, fg)
    if 'police' in filter_list:
        parse_english_markers(police, 'police', 'https://i.ibb.co/Sfmd5QH/police.png', html_eng, fg)
    if 'hospitals' in filter_list:
        parse_english_markers(hospitals, "hospitals", 'https://i.ibb.co/6v60Vwd/hospitals.png', html_eng, fg)
    if 'drugstores' in filter_list:
        parse_english_markers(pharmacy, 'pharmacy', 'https://i.ibb.co/pRS0mpj/pharmacy.png', html_eng, fg)

    m.get_root().header.add_child(folium.Element("""
    <link rel="shortcut icon" type="image/png" href="https://i.ibb.co/xYsVqhf/logo.png"/>
    <title>SA</title>
    """))
    if mobile:
        m.get_root().html.add_child(folium.Element(checkbox_eng_all_browsers_mobile))
    else:
        if chrome:
            m.get_root().html.add_child(folium.Element(checkbox_eng_chrome))
        else:
            m.get_root().html.add_child(folium.Element(checkbox_eng_all_browsers))
    m.add_child(fg)
    m.save('templates/mapa_english.html')

    with open('templates/mapa_english.html', 'r') as file:
        file = file.read()
        return file
    
