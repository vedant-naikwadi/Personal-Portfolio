#!C:\Python312\Python.exe
import cgi
import cgitb
cgitb.enable()
print("Content-Type:text/html\n")
print(''' <!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <link rel="shortcut icon" href="assets/images/v/vlogo-removebg2.png" type="image/x-icon">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Project-2</title>
    <!-- google font -->
    <link href="//fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;400;500;600;700;800;900&display=swap"
        rel="stylesheet">
    <!-- Template CSS Style link -->
    <link rel="stylesheet" href="assets/css/style-starter.css">

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.8.2/css/lightbox.min.css">
    <link rel="stylesheet" href="assets/css/gallery.css">

    <style>
        
        .project h4{
            padding-bottom: 5px;


        }

        .project p{
            text-align: justify;
        }

        
    </style>

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
                            <a class="nav-link" href="about.py">About Me</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link active" href="project.py">Projects</a>
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
                <h4 class="inner-text-title font-weight-bold pt-sm-5 pt-4">Online Bookstore Website</h4>
                <ul class="breadcrumbs-custom-path">
                    <li><a href="project.py">Projects</a></li>
                    <li class="active"><i class="fas fa-angle-right mx-2"></i>Project-2</li>
                </ul>
            </div>
        </div>
    </section>
    <!-- //inner banner -->


    <section class="w3l-gallery pb-5" id="gallery" style="background-color: white;">
        <div class="container py-md-5 py-4">
            <div class="title-heading-w3 text-center mb-sm-5 mb-4">
                <h3 class="title-style" style="color: black;">Online Bookstore Website</h3>
            </div>
            <div class="row" style="padding-bottom: 100px;">
                <div class="col-lg-6 col-md-6 item">
                    <a href="assets/images/v/project1.jpg" data-lightbox="example-set" data-title="Project 1"
                        class="zoom d-block">
                        <img class="card-img-bottom d-block" src="assets/images/v/project2.jpg" alt="Card image cap">
                        <span class="overlay__hover"></span>
                        <span class="hover-content">
                            <span class="title">Project 2</span>
                            <span class="content">Online Bookstore Website</span>
                        </span>
                    </a>
                </div>
                <div class="col-lg-6 col-md-6 item mt-md-0 mt-4 project" style="text-align: center;">
                    <p>Efficient Inventory Control: This Stock Management System streamlines the process of tracking and managing inventory in real-time. With features for automated reordering, detailed reporting, and inventory analytics, it helps businesses reduce stockouts, optimize storage, and enhance operational efficiency. The system is designed to integrate seamlessly with existing workflows, providing a user-friendly interface and robust functionality to ensure precise stock oversight and management.</p>
                </div>
            </div>
            <div class="row">
                
               <div class="photo-gallery">
                    <div class="container">
                        <div class="intro">
                            <h4 class="text-center" style="color: black;">More</h4>
                        </div>
                        <div class="row photos">
                            <div class="col-sm-6 col-md-4 col-lg-3 item">
                                <a href="assets/images/v/b1.jpg" data-lightbox="photos">
                                    <img class="img-fluid" src="assets/images/v/b1.jpg">
                                </a>
                            </div>
                            <div class="col-sm-6 col-md-4 col-lg-3 item">
                                <a href="assets/images/v/b2.jpg" data-lightbox="photos">
                                    <img class="img-fluid" src="assets/images/v/b2.jpg">
                                </a>
                            </div>
                            <div class="col-sm-6 col-md-4 col-lg-3 item">
                                <a href="assets/images/v/b3.jpg" data-lightbox="photos">
                                    <img class="img-fluid" src="assets/images/v/b3.jpg">
                                </a>
                            </div>
                            <div class="col-sm-6 col-md-4 col-lg-3 item">
                                <a href="assets/images/v/b4.jpg" data-lightbox="photos">
                                    <img class="img-fluid" src="assets/images/v/b4.jpg">
                                </a>
                            </div>
                            
                        </div>
                    </div>
                </div>




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


    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.8.2/js/lightbox.min.js"></script>
    <!-- //Js scripts -->
</body>

</html> ''')