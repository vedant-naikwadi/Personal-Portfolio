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
    <title>Services</title>
    <!-- google font -->
    <link href="//fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;400;500;600;700;800;900&display=swap"
        rel="stylesheet">
    <!-- Template CSS Style link -->
    <link rel="stylesheet" href="assets/css/style-starter.css">
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
                            <a class="nav-link" aria-current="page" href="index.py">Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="about.py">About Me</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link " href="project.py">Projects</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link active" href="services.py">Services</a>
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
                <h4 class="inner-text-title font-weight-bold pt-sm-5 pt-4">Services</h4>
                <ul class="breadcrumbs-custom-path">
                    <li><a href="index.py">Home</a></li>
                    <li class="active"><i class="fas fa-angle-right mx-2"></i>Services</li>
                </ul>
            </div>
        </div>
    </section>
    <!-- //inner banner -->

    <!-- grids section -->
    <section class="w3l-bottom-grids-6 py-5" id="features">
        <div class="container py-md-5 py-4">
            <div class="title-heading-w3 text-center mb-sm-5 mb-4">
                <h5 class="title-small mb-1">specialized In</h5>
                <h3 class="title-style">What I Offer</h3>
            </div>
            <div class="row">
                <div class="col-lg-3 col-md-6 grids-feature">
                    <div class="area-box active">
                        <div class="icon-style">
                            <i class="fas fa-lightbulb"></i>
                        </div>
                        <h4><a href="#feature" class="title-head">Creative Design</a></h4>
                        <a href="about.py" class="btn more p-0">Explore More<i
                                class="fas fa-long-arrow-alt-right ms-1"></i></a>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6 grids-feature mt-md-0 mt-4">
                    <div class="area-box">
                        <div class="icon-style">
                            <i class="fas fa-laptop-code"></i>
                        </div>
                        <h4><a href="#feature" class="title-head">Web Design</a></h4>
                        <a href="about.py" class="btn more p-0">Explore More<i
                                class="fas fa-long-arrow-alt-right ms-1"></i></a>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6 grids-feature mt-lg-0 mt-4">
                    <div class="area-box">
                        <div class="icon-style">
                            <i class="fas fa-layer-group"></i>
                        </div>
                        <h4><a href="#feature" class="title-head">Brand Identity</a></h4>
                        <a href="about.py" class="btn more p-0">Explore More<i
                                class="fas fa-long-arrow-alt-right ms-1"></i></a>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6 grids-feature mt-lg-0 mt-4">
                    <div class="area-box">
                        <div class="icon-style">
                            <i class="fas fa-chart-pie"></i>
                        </div>
                        <h4><a href="#feature" class="title-head">Graphic Design</a></h4>
                        <a href="about.py" class="btn more p-0">Explore More<i
                                class="fas fa-long-arrow-alt-right ms-1"></i></a>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- //grids section -->

    <!-- service section -->
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
    <!-- //service section -->

    <!-- pricing section -->
    <section class="w3l-pricing py-5">
        <div class="container py-md-5 py-4">
            <div class="title-heading-w3 text-center mb-sm-5 mb-4">
                <h5 class="title-small mb-1">Contact Now</h5>
                <h3 class="title-style">Let's achieve greatness together</h3>
            </div>
            <div class="row t-in justify-content-center">
                <div class="col-lg-4 col-md-6 price-main-info">
                    <!-- <div class="price-inner card box-shadow">

                        <div class="card-body">
                            <h4 class="text-uppercase text-center mb-3">Basic Plan</h4>
                            <h5 class="card-title pricing-card-title">
                                Free
                            </h5>
                            <ul class="list-unstyled mt-3 mb-4">
                                <li> <span class="fa fa-check"></span> Ui Design</li>
                                <li> <span class="fa fa-check"></span> Web Development</li>
                                <li class="disable"> <span class="fa fa-check"></span> Logo design</li>
                                <li class="disable"> <span class="fa fa-check"></span> SEO optimization</li>
                                <li class="disable"> <span class="fa fa-check"></span> Wordpress integration</li>
                            </ul>
                            <div class="read-more mt-4 pt-lg-2 text-center">
                                <a href="contact.html" class="btn btn-style"> Order Now</a>
                            </div>
                        </div>
                    </div> -->
                </div>
                <div class="col-lg-4 col-md-6 price-main-info mt-lg-0 mt-4">
                    <div class="price-inner card box-shadow active">

                        <div class="card-body">
                            <h4 class="text-uppercase text-center mb-3">Skills</h4>
                            <h5 class="card-title pricing-card-title">
                                <i class='far fa-smile'></i>
                            </h5>
                            <ul class="list-unstyled mt-3 mb-4">
                                <li> <span class="fa fa-check"></span> UI Design</li>
                                <li> <span class="fa fa-check"></span> Web Development</li>
                                <li> <span class="fa fa-check"></span> Logo design</li>
                                <li> <span class="fa fa-check"></span> PHP web-development</li>
                                <li> <span class="fa fa-check"></span> Graphic designing</li>
                            </ul>
                            <div class="read-more mt-4 pt-lg-2 text-center">
                                <a href="contact.py" class="btn btn-style">Contact Now</a>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-lg-4 col-md-6 price-main-info mt-md-0 mt-4">
                    <!-- <div class="price-inner card box-shadow active">

                        <div class="card-body">
                            <label class="price-label">Recommended</label>
                            <h4 class="text-uppercase text-center mb-3">Pro Plan</h4>
                            <h5 class="card-title pricing-card-title">
                                <span class="align-top">$</span>59

                            </h5>
                            <ul class="list-unstyled mt-3 mb-4">
                                <li> <span class="fa fa-check"></span> Ui Design</li>
                                <li> <span class="fa fa-check"></span> Web Development</li>
                                <li> <span class="fa fa-check"></span> Logo design</li>
                                <li class="disable"> <span class="fa fa-check"></span> SEO optimization</li>
                                <li class="disable"> <span class="fa fa-check"></span> Wordpress integration</li>
                            </ul>
                            <div class="read-more mt-4 pt-lg-2 text-center">
                                <a href="contact.html" class="btn btn-style"> Order Now</a>
                            </div>
                        </div>
                    </div> -->
                </div>
                
            </div>
        </div>
    </section>
    <!-- //pricing section -->
    

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