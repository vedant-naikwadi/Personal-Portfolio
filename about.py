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
    <title>About</title>
    <!-- google font -->
    <link href="//fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;400;500;600;700;800;900&display=swap"
        rel="stylesheet">
    <!-- Template CSS Style link -->
    <link rel="stylesheet" href="assets/css/style-starter.css">
</head>

<body>
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
                            <a class="nav-link" aria-current="page" href="index.py">Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link active" href="about.py">About Me</a>
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

    <!-- inner banner -->
    <section class="inner-banner py-5">
        <div class="w3l-breadcrumb py-lg-5">
            <div class="container pt-4 pb-sm-4">
                <h4 class="inner-text-title font-weight-bold pt-sm-5 pt-4">About Me</h4>
                <ul class="breadcrumbs-custom-path">
                    <li><a href="index.py">Home</a></li>
                    <li class="active"><i class="fas fa-angle-right mx-2"></i>Introduction</li>
                </ul>
            </div>
        </div>
    </section>
    <!-- //inner banner -->

    <!-- about section -->
    <section class="w3l-aboutblock1 py-5" id="about">
        <div class="container py-md-5 py-4">
            <div class="row align-items-center">
                <div class="col-lg-4">
                    <div class="position-relative">
                        <img src="assets/images/v/photo.jpg" alt="" class="radius-image img-fluid">
                    </div>
                </div>
                <div class="col-lg-8 ps-lg-5 mt-lg-0 mt-5">
                    <h5 class="title-small mb-1">Introduction</h5>
                    <h3 class="title-style">About Me</h3>
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

    <!-- text with button -->
    <section class="w3l-timeline-1 text-center py-5">
        <div class="container py-lg-5 py-4">
            <div class="mx-auto" style="max-width:800px">
                <h3 class="title-style mb-4">Why hire me for your next project?</h3>
                <p>I love to work in User Experience & User Interface designing. Because I love to solve the design
                    problem
                    and find easy and better solutions to solve it. I always try my best to make good user interface
                    with
                    the best user experience.</p>
                <a href="services.py" class="btn btn-style mt-5">Learn More</a>
            </div>
        </div>
    </section>
    <!-- //text with button -->

    <!-- about2 section -->
    <section class="w3l-about2 py-5">
        <div class="container py-lg-5 py-md-4 py-2">
            <div class="row align-items-center">
                <div class="col-lg-6 pe-lg-5">
                    <h5 class="title-small mb-1">Web Design</h5>
                    <h3 class="title-style">I Would Love to make your Ideas real</h3>
                    <div class="cwp23-text-cols mt-lg-5 mt-4">
                        <!-- <div class="column">
                            <span></span>
                            <h4>Happy Clients</h4>
                            <p>We help our clients increase profits by increasing their visibility online.</p>
                        </div> -->
                        <div class="column">
                            <span><i class="fa fa-desktop" aria-hidden="true" style="color: black;"></i>
                            </span>
                            <h4></h4>
                            <p>By helping clients increase profits by increasing their visibility online. </p>
                        </div>

                    </div>
                </div>
                <div class="col-lg-6 cwp23-text align-self mt-lg-0 mt-5">
                    <img src="assets/images/v/543_378726_tech.hero.jpg" alt="" class="radius-image img-fluid">
                </div>
            </div>
        </div>
    </section>
    <!-- //about2 section -->

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

    <!-- skills section -->
    <section class="w3l-progress py-5" id="progress">
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
                    </div>
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
                </div>
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
                    </div>
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
                </div>
            </div>
        </div>
    </section>
    <!-- //skills section -->

   <!-- footer -->
   <footer class="footer-w3ls text-center py-5">
    <div class="container pt-4">
        <div class="mx-auto" style="max-width:600px;">
            <a href="index.py" class="footer-logo py-1">
                <img src="assets/images/v/vlogo-removebg1.png" alt="">
            </a>
            <p class="mt-4 text-white">Hustle. Believe. Respect.</p>
            <div class="social-icons-main mt-4 pb-3">
                <ul class="social-icons3">
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
    <button onclick="topFunction()" id="movetop" title="Go to top">
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
    <!-- //Js scripts -->
</body>

</html> ''')