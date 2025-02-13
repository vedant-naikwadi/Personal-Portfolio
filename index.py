#!C:\Python312\Python.exe
import cgi
import cgitb
cgitb.enable()
print("Content-Type:text/html\n")
print(''' <!--
Author: W3layouts
Author URL: http://w3layouts.com
-->
<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <link rel="shortcut icon" href="assets/images/v/vlogo-removebg2.png" type="image/x-icon">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Home</title>
    <!-- google font -->
    <link href="//fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;400;500;600;700;800;900&display=swap"
        rel="stylesheet">
    <!-- Template CSS Style link -->
    <link rel="stylesheet" href="assets/css/style-starter.css">
    
    <!-- Bootstrap core CSS -->
    <link href="assets/css/bootstrap.min.css" rel="stylesheet" />
    
    <!-- Animations -->
    <link href="assets/css/animate.min.css" rel="stylesheet" />


    <!-- <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous"> -->

    <style>
        #pre-loader{
        /* background: #395d58 url(/starter/assets/images/Infinity@1x-1.0s-200px-200px.gif) no-repeat center center; */
        background: #fff url(assets/images/v/Fidget-spinner.gif) no-repeat center center;
        background-size: 5%;
        height: 100vh;
        width: 100%;
        position: fixed;
        z-index: 100;
        }

        .card{
        padding:0;
        }

    </style>


</head>

<body>
    <div id="pre-loader"></div>

    <!-- header -->
    <header id="site-header" class="fixed-top">
        <div class="container">
            <nav class="navbar navbar-expand-lg navbar-light">
                <a class="navbar-brand" href="index.py">
                    <img src="assets\images\img\logo.png" alt="">
                </a>
                <button class="navbar-toggler collapsed" type="button" data-bs-toggle="collapse"
                    data-bs-target="#navbarScroll" aria-controls="navbarScroll" aria-expanded="false"
                    aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon fa icon-expand fa-bars"></span>
                    <span class="navbar-toggler-icon fa icon-close fa-times"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarScroll">
                    <ul class="navbar-nav mx-auto my-2 my-lg-0 navbar-nav-scroll">
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="index.py">Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="about.py">About Me</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link " href="project.py">Projects</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="services.py">Services</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="achievement.py">Achievements</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="gallery.py">Gallery</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="contact.py">Contact</a>
                        </li>
                    </ul>
                    <!-- <form action="#search" method="GET" class="d-flex search-header">
                        <input class="form-control" type="search" placeholder="Search" aria-label="Search"
                            required>
                        <button class="btn btn-style" type="submit"><i class="fa fa-search" aria-hidden="true"></i></button>
                    </form> -->
                </div>
                <!-- toggle switch for light and dark theme -->
                <div class="cont-ser-position">
                    <nav class="navigation">
                        <div class="theme-switch-wrapper">
                            <label class="theme-switch" for="checkbox">
                                <input type="checkbox" id="checkbox">
                                <div class="mode-container">
                                    <i class="gg-sun"></i>
                                    <i class="gg-moon"></i>
                                </div>
                            </label>
                        </div>
                    </nav>
                </div>
                <!-- //toggle switch for light and dark theme -->
            </nav>
        </div>
    </header>
    <!-- //header -->

    <!-- banner section -->
    <section class="w3l-banner py-5" id="home">
        <div class="container py-md-5 py-4">
            <div class="row align-items-center pt-4">
                <div class="col-md-6">
                </div>
                <div class="col-md-6 banner-left pe-xl-5">
                    <h4 style="color: black;">Hi, I'm VEDANT NAIKWADI</h4>
                    <h3 class="mb-3 mt-1" style="color: black;">Developer. </h3>
                    <p class="banner-sub me-md-5" style="color: black;">I love to work in designing & developing.
                        
                         I always try my best to make good UI with the best UX.
                    </p>
                    <div class="d-flex align-items-center buttons-banner mt-sm-5 mt-4">
                        <a href="about.py" class="btn btn-style me-2">More</a>
                    </div>
                </div>
                
            </div>
        </div>
        <!-- animations icons -->
        <!-- <div class="icon-effects-w3-1 text-right">
            <img src="assets/images/icon3.png" alt="" class="img-fluid">
        </div>
        <div class="icon-effects-w3-2 text-right">
            <img src="assets/images/icon3.png" alt="" class="img-fluid">
        </div>
        <div class="icon-effects-w3-3 text-right">
            <img src="assets/images/icon3.png" alt="" class="img-fluid">
        </div>
        <div class="icon-effects-w3-4 text-right">
            <img src="assets/images/icon3.png" alt="" class="img-fluid">
        </div> -->
        <!-- //animations icons -->
    </section>
    <!-- //banner section -->

    <!-- grids section -->
    <section class="w3l-bottom-grids-6 pt-sm-5 pb-5" id="features">
        <div class="container pt-lg-4">
            <div class="grids-area-hny main-cont-wthree-fea row">
                <div class="col-md-3 col-sm-4 ps-xl-5">
                    <h4 class="ab-exper-count mb-sm-4 ps-lg-4"><img src="assets/images/v/web-development.png" alt=""></h4>
                    <p class="ab-content ps-lg-4">Fresher</p>
                </div>
                <div class="col-xl-8 col-md-9 col-sm-8 offset-xl-1 ps-xl-0 pe-xl-5 mt-sm-0 mt-4">
                    <h3 class="title-style mb-sm-5 mb-4">I'm a designer & developer with a passion for web design</h3>
                    <div class="row">
                        <div class="col-lg-4 col-md-6 grids-feature">
                            <div class="area-box active">
                                <div class="icon-style">
                                    <i class="fas fa-lightbulb"></i>
                                </div>
                                <h4><a href="#feature" class="title-head">Creative Design</a></h4>
                                <a href="about.py" class="btn more p-0">Explore More<i
                                        class="fas fa-long-arrow-alt-right ms-1"></i></a>
                            </div>
                        </div>
                        <div class="col-lg-4 col-md-6 grids-feature mt-md-0 mt-4">
                            <div class="area-box">
                                <div class="icon-style">
                                    <i class="fas fa-laptop-code"></i>
                                </div>
                                <h4><a href="#feature" class="title-head">Web Design</a></h4>
                                <a href="about.py" class="btn more p-0">Explore More<i
                                        class="fas fa-long-arrow-alt-right ms-1"></i></a>
                            </div>
                        </div>
                        <div class="col-lg-4 col-md-6 grids-feature mt-lg-0 mt-4">
                            <div class="area-box">
                                <div class="icon-style">
                                    <i class="fas fa-layer-group"></i>
                                </div>
                                <h4><a href="#feature" class="title-head">Brand Identity</a></h4>
                                <a href="about.py" class="btn more p-0">Explore More<i
                                        class="fas fa-long-arrow-alt-right ms-1"></i></a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- //grids section -->

    <!-- about section -->
    <section class="w3l-aboutblock1 pt-lg-5 pt-2 pb-5" id="about">
        <div class="container py-md-5 py-4">
            <div class="row align-items-center">
                <div class="col-lg-4">
                    <div class="position-relative">
                        <img src="assets/images/v/photo.jpg" alt="" class="radius-image img-fluid">
                    </div>
                </div>
                <div class="col-lg-8 ps-lg-5 mt-lg-0 mt-5">
                    <h5 class="title-small mb-1">Introduction</h5>
                    <h3 class="title-style">VEDANT NAIKWADI</h3>
                    <p class="mt-3">Hi there! I'm Vedant, a budding web developer eager to make my mark in the digital realm. 
                        Armed with a passion for coding and a hunger for innovation, 
                        I'm excited to dive into projects and bring fresh ideas to the table.
                        I'm ready to embark on this exhilarating journey of learning and creativity. 
                        Let's build something amazing together!.</p>
                    <div class="my-info mt-md-5 mt-4">
                        <ul class="single-info">
                            <li class="name-style">Name</li>
                            <li>:</li>
                            <li>
                                <p>Vedant Naikwadi</p>
                            </li>
                        </ul>
                        <ul class="single-info">
                            <li class="name-style">Age</li>
                            <li>:</li>
                            <li>
                                <p>22 Years</p>
                            </li>
                        </ul>
                        <ul class="single-info">
                            <li class="name-style">From</li>
                            <li>:</li>
                            <li>
                                <p>Kolhapur, Maharashtra</p>
                            </li>
                        </ul>
                        <ul class="single-info">
                            <li class="name-style">Email</li>
                            <li>:</li>
                            <li>
                                <p><a href="mailto:vedantnaikwadi007@gmail.com">vedantnaikwadi007@gmail.com</a></p>
                            </li>
                        </ul>
                    </div>
                    <a href="assets/pdf/v_resume.pdf" class="btn btn-style mt-5">Download CV</a>
                </div>
            </div>
        </div>
    </section>
    <!-- //about section -->

    <!-- qualification section -->
    <section class="w3l-timeline-1 py-5">
        <div class="container py-lg-5 py-4">
            <div class="title-heading-w3 text-center mb-sm-5 mb-4">
                <h5 class="title-small">Resume</h5>
                <h3 class="title-style">Qualification</h3>
            </div>
            <div class="row">
                <div class="col-lg-6">
                    <h5 class="sub-title-timeline"><i class="fas fa-graduation-cap"></i> Education</h5>
                    <div class="timeline">
                        <div class="column">
                            <div class="title">
                                <h2>Master in Computer Application</h2>
                            </div>
                            <div class="description">
                                <p>KIT's Institute of Management Education & Research, Kolhapur</p>
                                <h6><i class="fas fa-calendar-alt"></i> 2023 - Current</h6>
                            </div>
                        </div>
                        <div class="column">
                            <div class="title">
                                <h2>Bachelor in Science(Computer Science)</h2>
                            </div>
                            <div class="description">
                                <p>Shri Vijaysinha Yadav Mahavidyalya, Peth Vadgaon</p>
                                <h6><i class="fas fa-calendar-alt"></i> 2020 - 2023</h6>
                            </div>
                        </div>
                        <div class="column">
                            <div class="title">
                                <h2>12<sup>th</sup></h2>
                            </div>
                            <div class="description">
                                <p>Shri Balwantrao Yadav Jr. College, Peth Vadgaon</p>
                                <h6><i class="fas fa-calendar-alt"></i> 2018 - 2020</h6>
                            </div>
                        </div>
                        <div class="column">
                            <div class="title">
                                <h2>10<sup>th</sup></h2>
                            </div>
                            <div class="description">
                                <p>Holy Mother English Medium School, Peth Vadgaon</p>
                                <h6><i class="fas fa-calendar-alt"></i> - 2018</h6>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="col-lg-6 mt-lg-0 mt-4">
                    <h5 class="sub-title-timeline"><i class="fas fa-briefcase"></i> Experience</h5>
                    <div class="timeline">
                        <div class="column">
                            <div class="title">
                                <h2>Intern</h2>
                            </div>
                            <div class="description">
                                <p>Wolfox Services Pvt. Ltd.</p>
                                <h6><i class="fas fa-calendar-alt"></i> 2024 - Current</h6>
                            </div>
                        </div>
                        <!-- <div class="column">
                            <div class="title">
                                <h2>Jr. Font End Developer</h2>
                            </div>
                            <div class="description">
                                <p>W3Layouts</p>
                                <h6><i class="fas fa-calendar-alt"></i> 2018 - 2020</h6>
                            </div>
                        </div>
                        <div class="column">
                            <div class="title">
                                <h2>HTML Developer</h2>
                            </div>
                            <div class="description">
                                <p>Agile info</p>
                                <h6><i class="fas fa-calendar-alt"></i> 2017 - 2018</h6>
                            </div>
                        </div> -->
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- //qualification section -->

    <section id="about-us" class="page-section">
        <div class="container">
            <div class="section-title wow bounceInDown" data-wow-delay="1s" >
                <h1 class="title-style" style="color: black !important; text-align: center; font-weight: 700; padding-bottom: 25px;">Hobbies</h1>
            </div>
            <div class="row">
                <div class="col-md-12 text-center" data-animation="fadeInUp">
                    <!-- Text -->
                    <p class="title-description" style="font-weight: 600;">Exploring Passions: A Glimpse into My Hobbies. Discover the activities that fuel my creativity and bring balance to my life.</p>
                </div>
            </div>
            <div class="row special-feature">
                <!-- Special Feature Box 1 -->
                <div class="col-md-3 col-sm-6 wow bounceInLeft" data-wow-delay="2s" data-animation="fadeInUp">
                    <div class="s-feat-box text-center">
                        <div class="mask-top">
                        <!-- Icon -->
                        <i class='fas fa-motorcycle'></i> 
                        <!-- Title -->
                        <h4>Cars & Bikes</h4></div>
                        <div class="mask-bottom">
                        <!-- Icon -->
                        <i class="fas fa-motorcycle" style="color: white;"></i> 
                        <!-- Title -->
                        <h4 style="color: white;">Cars & Bikes</h4>
                        <!-- Text -->
                        <p style="color: white;">Driven by Passion: Cars and Bikes Fuel My Soul.</p></div>
                    </div>
                </div>
                <!-- Special Feature Box 2 -->
                <div class="col-md-3 col-sm-6 wow bounceInLeft" data-wow-delay="3s" data-animation="fadeInRight">
                    <div class="s-feat-box text-center">
                        <div class="mask-top">
                        <!-- Icon -->
                        <i class='fas fa-map-marked-alt'></i>
                        <!-- Title -->
                        <h4>Traveling</h4></div>
                        <div class="mask-bottom">
                        <!-- Icon -->
                        <i class='fas fa-map-marked-alt' style="color: white;"></i> 
                        <!-- Title -->
                        <h4 style="color: white;">Traveling</h4>
                        <!-- Text -->
                        <p style="color: white;">Embarking on Adventures Near and Far. Delve into tales of my travels, where every journey becomes a profound exploration of personal growth.</p></div>
                    </div>
                </div>
                <!-- Special Feature Box 3 -->
                <div class="col-md-3 col-sm-6 wow bounceInLeft" data-wow-delay="4s" data-animation="fadeInLeft">
                    <div class="s-feat-box text-center">
                        <div class="mask-top">
                        <!-- Icon -->
                        <i class='fas fa-camera-retro'></i>
                        <!-- Title -->
                        <h4>Photography</h4></div>
                        <div class="mask-bottom">
                        <!-- Icon -->
                        <i class='fas fa-camera-retro' style="color: white;"></i>
                        <!-- Title -->
                        <h4 style="color: white;">Photography</h4>
                        <!-- Text -->
                        <p style="color: white;">Through the Lens: Capturing Moments, Creating Memories. Explore my world through the art of photography, where every click tells a story.</p></div>
                    </div>
                </div>
                <!-- Special Feature Box 4 -->
                <div class="col-md-3 col-sm-6 wow bounceInLeft" data-wow-delay="5s" data-animation="fadeInDown">
                    <div class="s-feat-box text-center">
                        <div class="mask-top">
                        <!-- Icon -->
                        <i class='fas fa-peace'></i> 
                        <!-- Title -->
                        <h4>Music</h4></div>
                        <div class="mask-bottom">
                        <!-- Icon -->
                        <i class='fas fa-peace' style="color: white;"></i>  
                        <!-- Title -->
                        <h4 style="color: white;">Music</h4>
                        <!-- Text -->
                        <p style="color: white;">Harmonies in Life: Where Music Transforms Moments.</p></div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- about-us -->

    <!-- skills section -->
    <!-- <section class="w3l-progress py-5" id="progress">
        <div class="container py-md-5 py-4">
            <div class="title-heading-w3 text-center mb-sm-5 mb-4">
                <h5 class="title-small mb-1">My Skills</h5>
                <h3 class="title-style">My Expertise Area</h3>
            </div>
            <div class="row py-lg-4">
                <div class="col-lg-6 pe-lg-5">
                    <div class="progress-info info1">
                        <h6 class="progress-tittle">Web Design <span class="">80%</span></h6>
                        <div class="progress">
                            <div class="progress-bar progress-bar-striped gradient-1" role="progressbar"
                                style="width: 80%" aria-valuenow="90" aria-valuemin="0" aria-valuemax="100">
                            </div>
                        </div>
                    </div>
                    <div class="progress-info info2">
                        <h6 class="progress-tittle">HTML/CSS <span class="">95%</span>
                        </h6>
                        <div class="progress">
                            <div class="progress-bar progress-bar-striped gradient-2" role="progressbar"
                                style="width: 95%" aria-valuenow="95" aria-valuemin="0" aria-valuemax="100">
                            </div>
                        </div>
                    </div> -->
                    <!-- <div class="progress-info info3">
                        <h6 class="progress-tittle">JavaScript <span class="">60%</span></h6>
                        <div class="progress">
                            <div class="progress-bar progress-bar-striped gradient-3" role="progressbar"
                                style="width: 60%" aria-valuenow="95" aria-valuemin="0" aria-valuemax="100">
                            </div>
                        </div>
                    </div>
                    <div class="progress-info info4 mb-0">
                        <h6 class="progress-tittle">Bootstrap <span class="">85%</span></h6>
                        <div class="progress">
                            <div class="progress-bar progress-bar-striped gradient-4" role="progressbar"
                                style="width: 85%" aria-valuenow="95" aria-valuemin="0" aria-valuemax="100">
                            </div>
                        </div>
                    </div> -->
                <!-- </div>
                <div class="col-lg-6 ps-lg-5 mt-lg-0 mt-5">
                    <div class="progress-info info1">
                        <h6 class="progress-tittle">JavaScript <span class="">60%</span></h6>
                        <div class="progress">
                            <div class="progress-bar progress-bar-striped gradient-3" role="progressbar"
                                style="width: 60%" aria-valuenow="95" aria-valuemin="0" aria-valuemax="100">
                            </div>
                        </div>
                    </div>
                    <div class="progress-info info2">
                        <h6 class="progress-tittle">Bootstrap <span class="">95%</span>
                        </h6>
                        <div class="progress">
                            <div class="progress-bar progress-bar-striped gradient-2" role="progressbar"
                                style="width: 95%" aria-valuenow="95" aria-valuemin="0" aria-valuemax="100">
                            </div>
                        </div>
                    </div> -->
                    <!-- <div class="progress-info info3">
                        <h6 class="progress-tittle">Graphic Design <span class="">60%</span></h6>
                        <div class="progress">
                            <div class="progress-bar progress-bar-striped gradient-3" role="progressbar"
                                style="width: 60%" aria-valuenow="95" aria-valuemin="0" aria-valuemax="100">
                            </div>
                        </div>
                    </div>
                    <div class="progress-info info4 mb-0">
                        <h6 class="progress-tittle">UI/UX Design <span class="">85%</span></h6>
                        <div class="progress">
                            <div class="progress-bar progress-bar-striped gradient-4" role="progressbar"
                                style="width: 85%" aria-valuenow="95" aria-valuemin="0" aria-valuemax="100">
                            </div>
                        </div>
                    </div> -->
                <!-- </div>
            </div>
        </div>
    </section> -->
    <!-- //skills section -->

    <!-- projects section -->
    <section class="w3l-gallery pb-5" id="gallery">
        <div class="container py-md-5 py-4">
            <div class="title-heading-w3 text-center mb-sm-5 mb-4">
                <h5 class="title-small mb-1">Portfolio</h5>
                <h3 class="title-style">Some of my most recent projects</h3>
            </div>
            <div class="row">
                <div class="col-lg-6 col-md-6 item">
                    <a href="assets/images/v/project1.jpg" data-lightbox="example-set" data-title="Project 1"
                        class="zoom d-block">
                        <img class="card-img-bottom d-block" src="assets/images/v/project1.jpg" alt="Card image cap">
                        <span class="overlay__hover"></span>
                        <span class="hover-content">
                            <span class="title">Project 1</span>
                            <span class="content">Stock Management System</span>
                        </span>
                    </a>
                </div>
                <div class="col-lg-6 col-md-6 item mt-md-0 mt-4">
                    <a href="assets/images/v/project2.jpg" data-lightbox="example-set" data-title="Project 2"
                        class="zoom d-block">
                        <img class="card-img-bottom d-block" src="assets/images/v/project2.jpg" alt="Card image cap">
                        <span class="overlay__hover"></span>
                        <span class="hover-content">
                            <span class="title">Project 2</span>
                            <span class="content">Online Book Store</span>
                        </span>
                    </a>
                </div>

                <!-- <div class="col-lg-4 col-md-6 item mt-lg-0 mt-4">
                    <a href="assets/images/g3.jpg" data-lightbox="example-set" data-title="Project 3"
                        class="zoom d-block">
                        <img class="card-img-bottom d-block" src="assets/images/g3.jpg" alt="Card image cap">
                        <span class="overlay__hover"></span>
                        <span class="hover-content">
                            <span class="title">Project 3</span>
                            <span class="content">Quisque ut lectus, eros et, sed commodo risus.</span>
                        </span>
                    </a>
                </div>

                <div class="col-lg-4 col-md-6 item mt-4 pt-lg-2">
                    <a href="assets/images/g5.jpg" data-lightbox="example-set" data-title="Project 4"
                        class="zoom d-block">
                        <img class="card-img-bottom d-block" src="assets/images/g5.jpg" alt="Card image cap">
                        <span class="overlay__hover"></span>
                        <span class="hover-content">
                            <span class="title">Project 4</span>
                            <span class="content">Quisque ut lectus, eros et, sed commodo risus.</span>
                        </span>
                    </a>
                </div>

                <div class="col-lg-4 col-md-6 item mt-4 pt-lg-2">
                    <a href="assets/images/g6.jpg" data-lightbox="example-set" data-title="Project 5"
                        class="zoom d-block">
                        <img class="card-img-bottom d-block" src="assets/images/g6.jpg" alt="Card image cap">
                        <span class="overlay__hover"></span>
                        <span class="hover-content">
                            <span class="title">Project 5</span>
                            <span class="content">Quisque ut lectus, eros et, sed commodo risus.</span>
                        </span>
                    </a>
                </div>

                <div class="col-lg-4 col-md-6 item mt-4 pt-lg-2">
                    <a href="assets/images/g4.jpg" data-lightbox="example-set" data-title="Project 6"
                        class="zoom d-block">
                        <img class="card-img-bottom d-block" src="assets/images/g4.jpg" alt="Card image cap">
                        <span class="overlay__hover"></span>
                        <span class="hover-content">
                            <span class="title">Project 6</span>
                            <span class="content">Quisque ut lectus, eros et, sed commodo risus.</span>
                        </span>
                    </a>
                </div> -->
            </div>
        </div>
    </section>
    <!-- //projects section -->

    <!-- home service section -->
    <section class="w3l-servicesblock1 py-5" id="services">
        <div class="container py-md-5 py-4">
            <div class="title-heading-w3 text-center mb-sm-5 mb-4">
                <h5 class="title-small mb-1">What i do?</h5>
                <h3 class="title-style">How I can help your next project</h3>
            </div>
            <div class="w3-services-grids py-lg-4">
                <div class="fea-gd-vv row">
                    <div class="col-lg-3 col-md-6">
                        <div class="feature-gd icon-yellow">
                            <div class="icon">
                                <i class="fas fa-laptop"></i>
                            </div>
                            <div class="icon-info">
                                <a href="#url">Web design<br> and development </a>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6 mt-md-0 mt-4">
                        <div class="feature-gd icon-light-blue">
                            <div class="icon">
                                <i class="fas fa-code"></i>
                            </div>
                            <div class="icon-info">
                                <a href="#url">Java<br> programming</a>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6 mt-lg-0 mt-md-5 mt-4">
                        <div class="feature-gd icon-pink">
                            <div class="icon">
                                <i class="fas fa-code-branch"></i>
                            </div>
                            <div class="icon-info">
                                <a href="#url">.net program<br> development</a>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6 mt-lg-0 mt-md-5 mt-4">
                        <div class="feature-gd icon-red">
                            <div class="icon">
                                <i class="fab fa-php"></i>
                            </div>
                            <div class="icon-info">
                                <a href="#url">Php Web<br> development</a>
                            </div>
                        </div>
                    </div>
                    <!-- <div class="col-lg-3 col-md-6 mt-md-5 mt-4">
                        <div class="feature-gd icon-light-green">
                            <div class="icon">
                                <i class="fab fa-apple"></i>
                            </div>
                            <div class="icon-info">
                                <a href="#url">iOS App<br> development </a>
                            </div>
                        </div>
                    </div> -->
                    <!-- <div class="col-lg-3 col-md-6 mt-md-5 mt-4">
                        <div class="feature-gd icon-light-blue">
                            <div class="icon">
                                <i class="fas fa-code"></i>
                            </div>
                            <div class="icon-info">
                                <a href="#url">JQuery & Java<br> programming</a>
                            </div>
                        </div>
                    </div> -->
                    <!-- <div class="col-lg-3 col-md-6 mt-md-5 mt-4">
                        <div class="feature-gd icon-dark-green">
                            <div class="icon">
                                <i class="fas fa-link"></i>
                            </div>
                            <div class="icon-info">
                                <a href="#url">Blockchain<br> development</a>
                            </div>
                        </div>
                    </div> -->
                    <!-- <div class="col-lg-3 col-md-6 mt-md-5 mt-4">
                        <div class="feature-gd icon-pink">
                            <div class="icon">
                                <i class="fas fa-code-branch"></i>
                            </div>
                            <div class="icon-info">
                                <a href="#url">.net program<br> development</a>
                            </div>
                        </div>
                    </div> -->
                </div>
            </div>
            <div class="text-center mt-5">
                <a href="services.py" class="btn btn-style">Learn More</a>
            </div>
        </div>
    </section>
    <!-- //home service section -->

    
    <!-- Achievement Slider Section -->

    <section class="w3l-gallery" style="background-color: #fff; padding-top: 70px; padding-bottom: 100px; margin-bottom: 110px;">
        <div class="title-heading-w3 text-center mb-sm-5 mb-4">
            <h2 class="title-style" style="color: black; font-weight: 700;">Achievements</h2>
        </div>
        <div id="carouselExampleControls" class="carousel carousel-dark slide" data-bs-ride="carousel">
            <div class="carousel-inner">
            <div class="carousel-item active">
                <div class="card-wrapper container-sm d-flex  justify-content-around">
                    <div class="card  " style="width: 18rem;">
                        <a href="assets/images/v/c1 (1).jpeg" data-lightbox="example-set" data-title="Certificate" class="zoom d-block">
                            <img class="card-img-bottom d-block" src="assets/images/v/c1 (1).jpeg" alt="Card image cap">
                            <span class="overlay__hover"></span>
                            <span class="hover-content">
                                <!-- <span class="title">Project 2</span>
                                <span class="content">Online Book Store</span> -->
                            </span>
                        </a>
                    </div>
                    <div class="card" style="width: 18rem;">
                        <a href="assets/images/v/c1 (2).jpeg" data-lightbox="example-set" data-title="Certificate" class="zoom d-block">
                            <img class="card-img-bottom d-block" src="assets/images/v/c1 (2).jpeg" alt="Card image cap">
                            <span class="overlay__hover"></span>
                            <span class="hover-content">
                                <!-- <span class="title">Project 2</span>
                                <span class="content">Online Book Store</span> -->
                            </span>
                        </a>
                    </div>
                    <div class="card" style="width: 18rem;">
                        <a href="assets/images/v/c1 (3).jpeg" data-lightbox="example-set" data-title="Certificate" class="zoom d-block">
                        <img class="card-img-bottom d-block" src="assets/images/v/c1 (3).jpeg" alt="Card image cap">
                        <span class="overlay__hover"></span>
                        <span class="hover-content">
                            <!-- <span class="title">Project 2</span>
                            <span class="content">Online Book Store</span> -->
                        </span>
                        </a>
                    </div>
                </div>
            </div>
                <div class="carousel-item">
                    <div class="card-wrapper container-sm d-flex   justify-content-around">
                        <div class="card  " style="width: 18rem;">
                            <a href="assets/images/v/c1 (4).jpeg" data-lightbox="example-set" data-title="Certificate" class="zoom d-block">
                                <img class="card-img-bottom d-block" src="assets/images/v/c1 (4).jpeg" alt="Card image cap">
                                <span class="overlay__hover"></span>
                                <span class="hover-content">
                                    <!-- <span class="title">Project 2</span>
                                    <span class="content">Online Book Store</span> -->
                                </span>
                            </a>
                        </div>
                        <div class="card" style="width: 18rem;">
                            <a href="assets/images/v/c1 (5).jpeg" data-lightbox="example-set" data-title="Certificate" class="zoom d-block">
                                <img class="card-img-bottom d-block" src="assets/images/v/c1 (5).jpeg" alt="Card image cap">
                                <span class="overlay__hover"></span>
                                <span class="hover-content">
                                    <!-- <span class="title">Project 2</span>
                                    <span class="content">Online Book Store</span> -->
                                </span>
                            </a>
                        </div>
                        <div class="card" style="width: 18rem;">
                            <a href="assets/images/v/c1 (6).jpeg" data-lightbox="example-set" data-title="Certificate" class="zoom d-block">
                                <img class="card-img-bottom d-block" src="assets/images/v/c1 (6).jpeg" alt="Card image cap">
                                <span class="overlay__hover"></span>
                                <span class="hover-content">
                                    <!-- <span class="title">Project 2</span>
                                    <span class="content">Online Book Store</span> -->
                                </span>
                            </a>
                        </div>
                    </div>
                </div>
              
            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
              <span class="carousel-control-prev-icon" aria-hidden="true"></span>
              <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
              <span class="carousel-control-next-icon" aria-hidden="true"></span>
              <span class="visually-hidden">Next</span>
            </button>
        </div>
              

        
    </section>      
    <!-- // Achievement Slider Section -->

    <div class="row">

    </div>


    <!-- testimonials section -->
    <!-- <section class="w3l-testimonials py-5" id="testimonials">
        <div class="container py-md-5 py-4">
            <div class="row">
                <div class="col-md-10 mx-auto">
                    <div class="owl-two owl-carousel owl-theme">
                        <div class="item">
                            <div class="slider-info mt-lg-4 mt-3">
                                <div class="message">
                                    <img src="assets/images/quote.png" alt="" class="img-fluid mb-2" />
                                    <p><q>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ea sit id
                                            accusantium
                                            officia quod quasi necessitatibus perspiciatis Harum error provident
                                            quibusdam tenetur.</q></p>
                                    <div class="name mt-4 mb-4">
                                        <h4>Phillip Hunt</h4>
                                        <p>Subtitle goes here</p>
                                    </div>
                                </div>
                                <div class="img-circle">
                                    <img src="assets/images/c1.jpg" class="img-fluid radius-image" alt="client">
                                </div>
                            </div>
                        </div>
                        <div class="item">
                            <div class="slider-info mt-lg-4 mt-3">
                                <div class="message">
                                    <img src="assets/images/quote.png" alt="" class="img-fluid mb-2" />
                                    <p><q>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ea sit id
                                            accusantium
                                            officia quod quasi necessitatibus perspiciatis Harum error provident
                                            quibusdam tenetur.</q></p>
                                    <div class="name mt-4 mb-4">
                                        <h4>Sara Grant</h4>
                                        <p>Subtitle goes here</p>
                                    </div>
                                </div>
                                <div class="img-circle">
                                    <img src="assets/images/c2.jpg" class="img-fluid radius-image" alt="client">
                                </div>
                            </div>
                        </div>
                        <div class="item">
                            <div class="slider-info mt-lg-4 mt-3">
                                <div class="message">
                                    <img src="assets/images/quote.png" alt="" class="img-fluid mb-2" />
                                    <p><q>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ea sit id
                                            accusantium
                                            officia quod quasi necessitatibus perspiciatis Harum error provident
                                            quibusdam tenetur.</q></p>
                                    <div class="name mt-4 mb-4">
                                        <h4>Luke Jacobs</h4>
                                        <p>Subtitle goes here</p>
                                    </div>
                                </div>
                                <div class="img-circle">
                                    <img src="assets/images/c3.jpg" class="img-fluid radius-image" alt="client">
                                </div>
                            </div>
                        </div>
                        <div class="item">
                            <div class="slider-info mt-lg-4 mt-3">
                                <div class="message">
                                    <img src="assets/images/quote.png" alt="" class="img-fluid mb-2" />
                                    <p><q>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ea sit id
                                            accusantium
                                            officia quod quasi necessitatibus perspiciatis Harum error provident
                                            quibusdam tenetur.</q></p>
                                    <div class="name mt-4 mb-4">
                                        <h4>Claire Olson</h4>
                                        <p>Subtitle goes here</p>
                                    </div>
                                </div>
                                <div class="img-circle">
                                    <img src="assets/images/c4.jpg" class="img-fluid radius-image" alt="client">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section> -->
    <!-- //testimonials section -->

    <!-- footer -->
    <footer class="footer-w3ls text-center py-5">
        <div class="container pt-4">
            <div class="mx-auto" style="max-width:600px;">
                <a href="index.py" class="footer-logo py-1" style="text-align: center;">
                    <img src="assets/images/v/vlogo-removebg1.png" alt="">
                </a>
                <p class="mt-4 text-white" style="text-align: center;">Hustle. Believe. Respect.</p>
                <div class="social-icons-main mt-4 pb-3">
                    <ul class="social-icons3" style="text-align: center;">
                        <li>
                            <a href="https://www.facebook.com/vedant.naikwadi.31/">
                                <i class="fab fa-facebook-f"></i>
                            </a>
                        </li>
                        <li>
                            <a href="https://x.com/vednntt">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-twitter-x" viewBox="0 0 16 16">
                                    <path d="M12.6.75h2.454l-5.36 6.142L16 15.25h-4.937l-3.867-5.07-4.425 5.07H.316l5.733-6.57L0 .75h5.063l3.495 4.633L12.601.75Zm-.86 13.028h1.36L4.323 2.145H2.865z"/>
                                  </svg>
                            </a>
                        </li>
                        <li>
                            <a href="https://in.linkedin.com/in/vedant-naikwadi-7ab0911b2">
                                <i class="fab fa-linkedin-in"></i>
                            </a>
                        </li>
                        <li>
                            <a href="https://api.whatsapp.com/send?phone=919325561681">
                                <i class="fab fa-whatsapp"></i>
                            </a>
                        </li>
                        <li>
                            <a href="https://www.instagram.com/vednnt/?hl=en">
                                <i class="fab fa-instagram"></i>
                            </a>
                        </li>
                    </ul>
                </div>
            </div>
            <!-- copyright -->
            <p class="copy-right-w3 text-white mt-5 pt-4">© 2024 All rights reserved | Design by VEDANT
                <!-- <a href="http://w3layouts.com" target="_blank"> W3layouts.</a> -->
            </p>
        </div>
    </footer>
    <!-- //footer -->

    <!-- Js scripts -->
    <!-- move top -->
    <button onclick="topFunction()" id="movetop" title="To The Moon">
        <span class="fa fa-fighter-jet" aria-hidden="true"></span>
    </button>
    <script>
        // When the user scrolls down 20px from the top of the document, show the button
        window.onscroll = function () {
            scrollFunction()
        };

        function scrollFunction() {
            if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
                document.getElementById("movetop").style.display = "block";
            } else {
                document.getElementById("movetop").style.display = "none";
            }
        }

        // When the user clicks on the button, scroll to the top of the document
        function topFunction() {
            document.body.scrollTop = 0;
            document.documentElement.scrollTop = 0;
        }
    </script>
    <!-- //move top -->

    <!-- common jquery plugin -->
    <script src="assets/js/jquery-3.3.1.min.js"></script>
    <!-- //common jquery plugin -->

    <!-- libhtbox -->
    <script src="assets/js/lightbox-plus-jquery.min.js"></script>
    <!-- libhtbox -->

  

    <!-- testimonials owlcarousel -->
    <!-- <script src="assets/js/owl.carousel.js"></script>



    <script>
        $(document).ready(function () {
            $('.owl-two').owlCarousel({
                loop: true,
                margin: 30,
                nav: false,
                responsiveClass: true,
                autoplay: true,
                autoplayTimeout: 5000,
                autoplaySpeed: 1000,
                autoplayHoverPause: false,
                responsive: {
                    0: {
                        items: 1,
                        nav: false
                    },
                    480: {
                        items: 1,
                        nav: false
                    },
                    667: {
                        items: 1,
                        nav: false
                    },
                    1000: {
                        items: 1,
                        nav: false
                    }
                }
            })
        })
    </script> -->
    <!-- //script for Testimonials-->

    

    <!-- theme switch js (light and dark)-->
    <script src="assets/js/theme-change.js"></script>
    <!-- //theme switch js (light and dark)-->

    <!-- MENU-JS -->
    <script>
        $(window).on("scroll", function () {
            var scroll = $(window).scrollTop();

            if (scroll >= 80) {
                $("#site-header").addClass("nav-fixed");
            } else {
                $("#site-header").removeClass("nav-fixed");
            }
        });

        //Main navigation Active Class Add Remove
        $(".navbar-toggler").on("click", function () {
            $("header").toggleClass("active");
        });
        $(document).on("ready", function () {
            if ($(window).width() > 991) {
                $("header").removeClass("active");
            }
            $(window).on("resize", function () {
                if ($(window).width() > 991) {
                    $("header").removeClass("active");
                }
            });
        });
    </script>
    <!-- //MENU-JS -->

    <!-- disable body scroll which navbar is in active -->
    <script>
        $(function () {
            $('.navbar-toggler').click(function () {
                $('body').toggleClass('noscroll');
            })
        });
    </script>
    <!-- //disable body scroll which navbar is in active -->

    <!-- bootstrap -->
    <script src="assets/js/bootstrap.min.js"></script>
    <!-- //bootstrap -->

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
   

    <script>
        var loader = document.getElementById("pre-loader");
              window.addEventListener("load", function () {
                  setTimeout(function () {
                      loader.style.display = "none";
                  }, 1500);
              });
  
    </script>
   
    <!-- //Js scripts -->
</body>

</html> ''')