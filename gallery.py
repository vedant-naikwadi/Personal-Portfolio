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
    <title>Gallery</title>
    <!-- google font -->
    <link href="//fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;400;500;600;700;800;900&display=swap"
        rel="stylesheet">
    <!-- Template CSS Style link -->
    <link rel="stylesheet" href="assets/css/style-starter.css">

    <!-- <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/css/bootstrap.min.css"> -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.8.2/css/lightbox.min.css">
    <style>
        .photo-gallery {
  color:#313437;
  background-color:#fff;
}

.photo-gallery p {
  color:#7d8285;
}

.photo-gallery h2 {
  font-weight:bold;
  margin-bottom:40px;
  padding-top:40px;
  color:inherit;
}

@media (max-width:767px) {
  .photo-gallery h2 {
    margin-bottom:25px;
    padding-top:25px;
    font-size:24px;
  }
}

.photo-gallery .intro {
  font-size:16px;
  max-width:500px;
  margin:0 auto 40px;
}

.photo-gallery .intro p {
  margin-bottom:0;
}

.photo-gallery .photos {
  padding-bottom:20px;
}

.photo-gallery .item {
  padding-bottom:30px;
}


    </style>
</head>

<body>
    <!-- header -->
    <header id="site-header" class="fixed-top" style=" position: fixed;
    top: 0;
    right: 0;
    left: 0;
    z-index: 1030;">
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
                            <a class="nav-link " href="project.py">Projects</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="services.py">Services</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="achievement.py">Achievements</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link active" href="gallery.py">Gallery</a>
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
                <h4 class="inner-text-title pt-sm-5 pt-4">Gallery</h4>
                <ul class="breadcrumbs-custom-path mt-2">
                    <li><a href="index.py">Home</a></li>
                    <li class="active"><i class="fas fa-angle-right mx-2"></i>Gallery</li>
                </ul>
            </div>
        </div>
    </section>
    <!-- //inner banner -->

    <div class="photo-gallery">
        <div class="container">
            <div class="intro">
                <h2 class="text-center" style="color: black;">Gallery</h2>
                <p class="text-center">Moments Captured: A Glimpse into My Journey</p>
            </div>
            <div class="row photos">
                <div class="col-sm-6 col-md-4 col-lg-3 item">
                    <a href="assets/images/v/vg/v1.jpeg" data-lightbox="photos">
                        <img class="img-fluid" src="assets/images/v/vg/v1.jpeg">
                    </a>
                </div>
                <div class="col-sm-6 col-md-4 col-lg-3 item">
                    <a href="assets/images/v/vg/v2.jpeg" data-lightbox="photos">
                        <img class="img-fluid" src="assets/images/v/vg/v2.jpeg">
                    </a>
                </div>
                <div class="col-sm-6 col-md-4 col-lg-3 item">
                    <a href="assets/images/v/vg/v5 (1).jpeg" data-lightbox="photos">
                        <img class="img-fluid" src="assets/images/v/vg/v5 (1).jpeg">
                    </a>
                </div>
                <div class="col-sm-6 col-md-4 col-lg-3 item">
                    <a href="assets/images/v/vg/v5 (2).jpeg" data-lightbox="photos">
                        <img class="img-fluid" src="assets/images/v/vg/v5 (2).jpeg">
                    </a>
                </div>
                <div class="col-sm-6 col-md-4 col-lg-3 item">
                    <a href="assets/images/v/vg/v3.jpeg" data-lightbox="photos">
                        <img class="img-fluid" src="assets/images/v/vg/v3.jpeg">
                    </a>
                </div>
                <div class="col-sm-6 col-md-4 col-lg-3 item">
                    <a href="assets/images/v/vg/v5 (4).jpeg" data-lightbox="photos">
                        <img class="img-fluid" src="assets/images/v/vg/v5 (4).jpeg">
                    </a>
                </div>
                <div class="col-sm-6 col-md-4 col-lg-3 item">
                    <a href="assets/images/v/vg/v5 (5).jpeg" data-lightbox="photos">
                        <img class="img-fluid" src="assets/images/v/vg/v5 (5).jpeg">
                    </a>
                </div>
                <div class="col-sm-6 col-md-4 col-lg-3 item">
                    <a href="assets/images/v/vg/v6.jpeg" data-lightbox="photos">
                        <img class="img-fluid" src="assets/images/v/vg/v6.jpeg">
                    </a>
                </div>
                <div class="col-sm-6 col-md-4 col-lg-3 item">
                    <a href="assets/images/v/vg/v5 (6).jpeg" data-lightbox="photos">
                        <img class="img-fluid" src="assets/images/v/vg/v5 (6).jpeg">
                    </a>
                </div>
                <div class="col-sm-6 col-md-4 col-lg-3 item">
                    <a href="assets/images/v/vg/v7 (1).jpeg" data-lightbox="photos">
                        <img class="img-fluid" src="assets/images/v/vg/v7 (1).jpeg">
                    </a>
                </div>
                <div class="col-sm-6 col-md-4 col-lg-3 item">
                    <a href="assets/images/v/vg/v7 (2).jpeg" data-lightbox="photos">
                        <img class="img-fluid" src="assets/images/v/vg/v7 (2).jpeg">
                    </a>
                </div>
                <div class="col-sm-6 col-md-4 col-lg-3 item">
                    <a href="assets/images/v/vg/v7 (3).jpeg" data-lightbox="photos">
                        <img class="img-fluid" src="assets/images/v/vg/v7 (3).jpeg">
                    </a>
                </div>
                <div class="col-sm-6 col-md-4 col-lg-3 item">
                    <a href="assets/images/v/vg/v7 (4).jpeg" data-lightbox="photos">
                        <img class="img-fluid" src="assets/images/v/vg/v7 (4).jpeg">
                    </a>
                </div>
                <div class="col-sm-6 col-md-4 col-lg-3 item">
                    <a href="assets/images/v/vg/v7 (5).jpeg" data-lightbox="photos">
                        <img class="img-fluid" src="assets/images/v/vg/v7 (5).jpeg">
                    </a>
                </div>
                <div class="col-sm-6 col-md-4 col-lg-3 item">
                    <a href="assets/images/v/vg/v7 (6).jpeg" data-lightbox="photos">
                        <img class="img-fluid" src="assets/images/v/vg/v7 (6).jpeg">
                    </a>
                </div>
                <div class="col-sm-6 col-md-4 col-lg-3 item">
                    <a href="assets/images/v/vg/v7 (7).jpeg" data-lightbox="photos">
                        <img class="img-fluid" src="assets/images/v/vg/v7 (7).jpeg">
                    </a>
                </div>
            </div>
        </div>
    </div>


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