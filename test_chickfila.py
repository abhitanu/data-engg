import requests
from bs4 import BeautifulSoup

# Define the target URL (replace with the actual URL you want to scrape)
#url = "https://www.w3schools.com/tags/"
#url = "https://www.chick-fil-a.com/menu"

# Send an HTTP GET request to the URL and store the response
#response = requests.get(url)

html_content = """<!DOCTYPE html>
<!--[if gt IE 9]><!-->
<html lang="en">
<!--<![endif]-->
<head>





	<script>
		window.dataLayer = window.dataLayer || [];
		dataLayer.push({ pageModel: null, userModel: null });  // Clear the previous attributes.
		dataLayer.push({
			event: 'page_view',
			pageModel: {
				language: 'en',
				page_id: 'BCA40B2350AF41BF868B7FEE34F2DEB8',
				page_location: 'http://www.chick-fil-a.com/menu',
				page_name: 'menu',
				page_referrer: '',
				page_title: 'Menu | Chick-fil-A',
				site_brand: 'CFACOM',
				site_country: 'fe80::da9d:e18:ff7e:12f7%7',
				site_region: ''
			}
		});
	</script>








<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="keywords" content="">
<meta name="description" content="Menu">


<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />
<meta name="server" content="I-064A84B5EA244" />
<meta name="serverzone" content="0.0" />
<meta name="site" content="CFACOM" />
<meta name='bsk' content='80dd234943647559a245be654346b81f'/>
<meta name='bskv' content=''/>
	<link rel="canonical" href="https://www.chick-fil-a.com/menu" />

<link rel="apple-touch-icon" sizes="180x180" href="/Assets/Theming/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="32x32" href="/Assets/Theming/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/Assets/Theming/favicon-16x16.png">
<link rel="manifest" href="/Assets/Theming/site.webmanifest">
<link rel="mask-icon" href="/Assets/Theming/safari-pinned-tab.svg" color="#dd1f37">
<meta name="msapplication-TileColor" content="#dd1f37">
<meta name="msapplication-config" content="/Assets/Theming/browserconfig.xml">
<meta name="theme-color" content="#dd1f37">


<title>Menu | Chick-fil-A</title>

		<link href="https://d2wl1kt18tqdum.cloudfront.net/v2.1.880-stageb/Assets/Theming/css/cfacom.css" rel="stylesheet" type="text/css" />

	



<!-- OneTrust Cookies Consent Notice start -->

<script src="https://cdn.cookielaw.org/scripttemplates/otSDKStub.js"  type="text/javascript" charset="UTF-8" data-domain-script="4eeb7bf7-e1e9-49fc-84fa-3395630bec87"></script>
<script type="text/javascript">
function OptanonWrapper() { }
</script>
<!-- OneTrust Cookies Consent Notice end -->

<!--Google Optimize Snippet start -->
<script type="text/plain" class="optanon-category-2" src="https://www.googleoptimize.com/optimize.js?id=OPT-TXZMM4N"></script>
<!--Google Optimize Snippet end -->


	<!-- Google Tag Manager -->
	<script>
		(function (w, d, s, l, i) {
			w[l] = w[l] || [];
			w[l].push({
				'gtm.start' :
					new Date().getTime(),
				event : 'gtm.js'
			});
			var f = d.getElementsByTagName(s)[0],
				j = d.createElement(s),
				dl = l != 'dataLayer' ? '&l=' + l : '';
			j.async = true;
			j.src =
				'//www.googletagmanager.com/gtm.js?id=' + i + dl;
			f.parentNode.insertBefore(j, f);
		})(window, document, 'script', 'dataLayer', 'GTM-NXDPGM');
	</script>
	<!-- End Google Tag Manager -->

    <script>
        function getExperienceType () {
            var experienceType = "Desktop";

            if (Number(document.documentElement.clientWidth) < 960) {
                experienceType = "Mobile";
            } else if (window.matchMedia("(orientation: landscape)") && (Number(document.documentElement.clientHeight) < 960)) {
                experienceType = "Mobile";
            }

            return experienceType;
        }

        window.digitalData =
        {
            'page' : {
                'category' : {
                    'pageType': 'LocationMenu'
                },
                'pageInfo' : {
                    'destinationURL' : 'http://www.chick-fil-a.com/menu',
                    'experienceType' : getExperienceType(),
                    'pageName' : 'Menu',
                    'sysEnv' : 'Prod'
                }
            },
            'user' : {
                'profile' : {
                    'profileInfo' : {
                        'loginStatus' : 'not-logged-in',
                        'profileID' : ''
                    }
                }
            }
        };
    </script>

            <!-- Schema.org markup for Google+ -->
            <meta itemprop="name" content="Menu">
            <meta itemprop="description" content="Menu">
            <meta itemprop="image" content="http://www.chick-fil-a.com/-/media/images/cfacom/default-images/chick-fil-a-logo-vector.gif">
            <!-- Twitter Card data -->
            <meta name="twitter:card" content="summary_large_image">
            <meta name="twitter:site" content="@ChickfilA">
            <meta name="twitter:title" content="Menu">
            <meta name="twitter:description" content="Menu">
            <meta name="twitter:creator" content="@ChickfilA">
            <meta name="twitter:image:src" content="http://www.chick-fil-a.com/-/media/images/cfacom/default-images/chick-fil-a-logo-vector.gif">
            <!-- Open Graph data -->
            <meta property="og:title" content="Menu"/>
            <meta property="og:type" content="article"/>
            <meta property="og:url" content="https://www.chick-fil-a.com/menu"/>
            <meta property="og:description" content="Menu"/>
            <meta property="og:site_name" content="Chick-fil-A"/>
            <meta property="article:tag" content=""/>
            <meta property="og:image" content="http://www.chick-fil-a.com/-/media/images/cfacom/default-images/chick-fil-a-logo-vector.gif"/>
                <meta property="og:image:secure_url" content="https://www.chick-fil-a.com/-/media/images/cfacom/default-images/chick-fil-a-logo-vector.gif"/>
                <meta property="og:image:width" content="693"/>
                <meta property="og:image:height" content="390"/>



		<link rel="alternate" hreflang="es" href="https://www.chick-fil-a.com/menu" />


	
</head>
<body>



	<!-- Google Tag Manager -->
	<noscript>
		<iframe src="//www.googletagmanager.com/ns.html?id=GTM-NXDPGM"
						height="0"
						width="0"
						style="display: none; visibility: hidden;"></iframe>
	</noscript>
	<!-- End Google Tag Manager -->


		<a class="visually-hidden skip-link" href="#LocationFrameId">Skip to main content</a>



	<div class="national-menu-page">
		

		




<div class="header-frame" data-sticky-position="true" data-sticky-priority="1">
	
	<header data-component="MainNav">
		<div class="nav-frame">
			<div class="header-components flex">
				<a href="/" class="icon-logo-desktop logo"><span>Chick-Fil-A</span></a>

				

<div class="location-tools"
		 data-component="locationTools"
		 data-modal-id="pwo-modal"
		 data-has-favorited-restaurants="false"
		 data-layer-identifier="BCA40B2350AF41BF868B7FEE34F2DEB8"
		 data-layer-name="/sitecore/content/CFACOM/Home/menu">
	<div class="current-location" data-populate="current-location-menu-id">
		<div class="icon-location-off"></div>
		<button data-element="findRestaurant" type="button">
			Find a restaurant
		</button>
	</div>
</div>


<a href="https://order.chick-fil-a.com/get-started" class="order-now" title="Order Now" >Order Now</a>


<div class="nav-toggle" data-component="NavToggle">
	<a data-action="toggle nav" href="#" class="icon-nav-toggle-off">
		<span>Close Main Nav</span>
	</a>
</div>


				<nav class="main-nav logged-out" role="navigation" aria-label="Main menu">

						<div class="cfa-one logged-out btn vis-white" id="navitem-cfaone">
<form action="/identity/externallogin?authenticationType=Crn&amp;ReturnUrl=%2fidentity%2fexternallogincallback%3fReturnUrl%3d%252f%26sc_site%3dCFACOM%26authenticationSource%3dDefault&amp;sc_site=CFACOM&amp;signup_redirect_uri=%2f" class="sign-in" id="main-menu-signin" method="post">									<button class="" type="submit">Sign In</button>
</form>						</div>

					<ul class="flex">
						



						


	<li id="navitem-menu"
			class="navitem-hoverable navitem-hoverable--menu">

<a href="/menu" >			<span>Menu</span>
				<span class="icon-arrow-down" aria-expanded="false"></span>
</a>
		
			<div class="subnav">

				
				<ul id="menusubcategoricalid"
						class="menusubcategories"
						aria-label="Menu subcategories'">

						<li>
<a href="/menu#breakfast" id="breakfast-id" data_component="clickData" data-layer-protocol="https" title="Breakfast" data-layer-category="PrimaryMenuList" data-layer-id="BCA40B2350AF41BF868B7FEE34F2DEB8" >Breakfast									<span class="visually-hidden">
										Selected
									</span>
</a>						</li>
						<li>
<a href="/menu#entrees" data_component="clickData" data-layer-id="BCA40B2350AF41BF868B7FEE34F2DEB8" data-layer-category="PrimaryMenuList" id="entrées-id" data-layer-protocol="https" >Entr&#233;es									<span class="visually-hidden">
										Selected
									</span>
</a>						</li>
						<li>
<a href="/menu#salads" data_component="clickData" data-layer-id="BCA40B2350AF41BF868B7FEE34F2DEB8" data-layer-category="PrimaryMenuList" id="salads-id" data-layer-protocol="https" >Salads									<span class="visually-hidden">
										Selected
									</span>
</a>						</li>
						<li>
<a href="/menu#sides" data_component="clickData" data-layer-id="BCA40B2350AF41BF868B7FEE34F2DEB8" data-layer-category="PrimaryMenuList" id="sides-id" data-layer-protocol="https" >Sides									<span class="visually-hidden">
										Selected
									</span>
</a>						</li>
						<li>
<a href="/menu#kidsmeals" data_component="clickData" data-layer-id="BCA40B2350AF41BF868B7FEE34F2DEB8" data-layer-category="PrimaryMenuList" id="kid's-meals-id" data-layer-protocol="https" >Kid&#39;s Meals									<span class="visually-hidden">
										Selected
									</span>
</a>						</li>
						<li>
<a href="/menu#treats" data_component="clickData" data-layer-id="BCA40B2350AF41BF868B7FEE34F2DEB8" data-layer-category="PrimaryMenuList" id="treats-id" data-layer-protocol="https" >Treats									<span class="visually-hidden">
										Selected
									</span>
</a>						</li>
						<li>
<a href="/menu#beverages" data_component="clickData" data-layer-id="BCA40B2350AF41BF868B7FEE34F2DEB8" data-layer-category="PrimaryMenuList" id="beverages-id" data-layer-protocol="https" >Beverages									<span class="visually-hidden">
										Selected
									</span>
</a>						</li>
						<li>
<a href="/menu#sauces" data_component="clickData" data-layer-id="BCA40B2350AF41BF868B7FEE34F2DEB8" data-layer-category="PrimaryMenuList" id="dipping-sauces-and-dressings-id" data-layer-protocol="https" >Dipping Sauces and Dressings									<span class="visually-hidden">
										Selected
									</span>
</a>						</li>
						<li>
								
									<a href="/catering" data-component="clickData" data-layer-category="PrimaryMenuList" data-layer-id="BCA40B2350AF41BF868B7FEE34F2DEB8" data-layer-protocol="https" >Catering</a>
								
						</li>
				</ul>
			</div>
	</li>



	<li id=""
			class="">

<a href="/stories" >			<span>Stories</span>
</a>
		
	</li>



	<li id="navitem-about"
			class="navitem-hoverable navitem-hoverable--about">

<a href="/about/who-we-are" >			<span>About</span>
				<span class="icon-arrow-down" aria-expanded="false"></span>
</a>
		
			<div class="subnav">

				
				<ul id="menusubcategoricalid"
						class="menusubcategories"
						aria-label="Menu subcategories'">

						<li>
								
									<a href="/about/who-we-are" data-component="clickData" data-layer-category="PrimaryMenuList" data-layer-id="BCA40B2350AF41BF868B7FEE34F2DEB8" data-layer-protocol="https" >Who We Are</a>
								
						</li>
						<li>
								
									<a href="/about/great-food" data-component="clickData" data-layer-category="PrimaryMenuList" data-layer-id="BCA40B2350AF41BF868B7FEE34F2DEB8" data-layer-protocol="https" >Great Food</a>
								
						</li>
						<li>
								
									<a href="/about/giving-back" data-component="clickData" data-layer-category="PrimaryMenuList" data-layer-id="BCA40B2350AF41BF868B7FEE34F2DEB8" data-layer-protocol="https" >Giving Back</a>
								
						</li>
						<li>
								
									<a href="/about/history" data-component="clickData" data-layer-category="PrimaryMenuList" data-layer-id="BCA40B2350AF41BF868B7FEE34F2DEB8" data-layer-protocol="https" >History</a>
								
						</li>
						<li>
								
									<a href="/about/s-truett-cathy-brand-restaurants" data-component="clickData" data-layer-category="PrimaryMenuList" title="S. Truett Cathy Brands" data-layer-id="BCA40B2350AF41BF868B7FEE34F2DEB8" data-layer-protocol="https" >S. Truett Cathy Brands</a>
								
						</li>
				</ul>
			</div>
	</li>



	<li id=""
			class="">

<a href="/careers" >			<span>Careers</span>
</a>
		
	</li>

					</ul>

					

<div class="location-tools"
		 data-component="locationTools"
		 data-modal-id="pwo-modal"
		 data-has-favorited-restaurants="false"
		 data-layer-identifier="BCA40B2350AF41BF868B7FEE34F2DEB8"
		 data-layer-name="/sitecore/content/CFACOM/Home/menu">
	<div class="current-location" data-populate="current-location-menu-id">
		<div class="icon-location-off"></div>
		<button data-element="findRestaurant" type="button">
			Find a restaurant
		</button>
	</div>
</div>


					




					

<div class="search" id="navitem-search">
	<form class="site-search">
		
<div id="search-form"
		 class="yext-search-form "
		 data-component="yextSearch"
		 data-api-key="71620ba70d81b48c7c72331e25462ebc"
		 data-business-id="2192285"
		 data-locale="en"
		 data-experience-key="cfa-answers"
		 data-experience-version="PRODUCTION"
		 data-placeholder-text="Try: Nutrition and allergens"
		 data-redirect-url="http://search.chick-fil-a.com/"
		 data-source-id="39335374-a80c-4a4e-bdc8-070135e262a4"></div>


		<button type="submit" class="icon-search-off">
			<span>Search</span>
		</button>
	</form>

	<span role="button"
				tabindex="0"
				aria-label="Click here to close the site search"
				class="icon-close"></span>
</div>


					<div class="order-button-group flex">
<a href="https://order.chick-fil-a.com/get-started" class="btn-round btn-round--red" >Order now</a>
<form action="/identity/externallogin?authenticationType=Crn&amp;ReturnUrl=%2fidentity%2fexternallogincallback%3fReturnUrl%3d%252f%26sc_site%3dCFACOM%26authenticationSource%3dDefault&amp;sc_site=CFACOM&amp;signup_redirect_uri=%2f" class="" id="toolbar-menu-signin" method="post">								<button class="btn-round btn-round--white" type="submit">Sign In</button>
</form>					</div>
				</nav>
				
			</div>
		</div>
	</header>
</div>

<div id="favorited-restaurants-yext"
		 data-source="ae7b2b27-b853-46d3-b9f7-b98e2dd1fbe9"
		 class="pwo-modal mfp-hide   ">
	<button class="mfp-close"></button>
	<div class="content">
<h2>
	Find a Restaurant
</h2>

	<form class="pwo-modal-search"
				data-component="pwoSearchForm"
				data-layer-identifier="ae7b2b27-b853-46d3-b9f7-b98e2dd1fbe9"
				data-layer-name="/sitecore/content/CFACOM/Home/menu"
				action="/locations"
				method="get">
		<div class="search-container" data-element="pwoSearchContainer">
			<div class="pwo-modals-form-error" data-element="formErrorMsg" role="alert">
				<p>
					Please enter an address
				</p>
			</div>
			<img src="/-/media/images/cfa/feature/page-content/defaultimages/pwo/pwo-modals/search-icon.svg?h=-1&amp;w=-1&amp;la=en&amp;hash=188E517FD3EE32A05D7899D47361FD1C" alt="Search Icon" />
			<input class="user-input"
						 type="text"
						 name="locationsearch"
						 placeholder="Enter address, city and state, or zip"
						 aria-label="Enter address, city and state, or zip"
						 data-element="pwoSearchInput"
						 data-pwo="false">
		</div>
		<input type="hidden" id="menuItem" name="menuItem" value="">
		<input class="btn-round"
					 type="submit"
					 value="Search"
					 aria-label="Search">
	</form>
		<form action="/locations"
					method="get"
					class="use-location use-location-form"
					data-component="geoLocation"
					data-layer-identifier="ae7b2b27-b853-46d3-b9f7-b98e2dd1fbe9"
					data-layer-name="/sitecore/content/CFACOM/Home/menu">
			<img src="/-/media/images/cfa/feature/page-content/defaultimages/pwo/pwo-modals/use-my-location-icon.svg?h=-1&amp;w=-1&amp;la=en&amp;hash=650EDAE81BDF8B8A4264317DEAB99BE0" alt="Use My Location Icon" />
			<a href="">
				Use my location
			</a>

			<input type="hidden" id="loclatitude" name="latitude" value="0">
			<input type="hidden" id="loclongitude" name="longitude" value="0">
			<input type="hidden" id="menuItem" name="menuItem" value="">
		</form>

	</div>
</div>

<div id="find-restaurants-modal"
		 data-source="0cc5ac81-a983-4001-a526-7129aecdaadf"
		 class="pwo-modal mfp-hide   ">
	<button class="mfp-close"></button>
	<div class="content">
<h2>
	Find a Restaurant
</h2>

	<form class="pwo-modal-search"
				data-component="pwoSearchForm"
				data-layer-identifier="0cc5ac81-a983-4001-a526-7129aecdaadf"
				data-layer-name="/sitecore/content/CFACOM/Home/menu"
				action="/locations"
				method="get">
		<div class="search-container" data-element="pwoSearchContainer">
			<div class="pwo-modals-form-error" data-element="formErrorMsg" role="alert">
				<p>
					Please enter an address
				</p>
			</div>
			<img src="/-/media/images/cfa/feature/page-content/defaultimages/pwo/pwo-modals/search-icon.svg?h=-1&amp;w=-1&amp;la=en&amp;hash=188E517FD3EE32A05D7899D47361FD1C" alt="Search Icon" />
			<input class="user-input"
						 type="text"
						 name="locationsearch"
						 placeholder="Enter address, city and state, or zip"
						 aria-label="Enter address, city and state, or zip"
						 data-element="pwoSearchInput"
						 data-pwo="false">
		</div>
		<input type="hidden" id="menuItem" name="menuItem" value="">
		<input class="btn-round"
					 type="submit"
					 value="Search"
					 aria-label="Search">
	</form>
		<form action="/locations"
					method="get"
					class="use-location use-location-form"
					data-component="geoLocation"
					data-layer-identifier="0cc5ac81-a983-4001-a526-7129aecdaadf"
					data-layer-name="/sitecore/content/CFACOM/Home/menu">
			<img src="/-/media/images/cfa/feature/page-content/defaultimages/pwo/pwo-modals/use-my-location-icon.svg?h=-1&amp;w=-1&amp;la=en&amp;hash=650EDAE81BDF8B8A4264317DEAB99BE0" alt="Use My Location Icon" />
			<a href="">
				Use my location
			</a>

			<input type="hidden" id="loclatitude" name="latitude" value="0">
			<input type="hidden" id="loclongitude" name="longitude" value="0">
			<input type="hidden" id="menuItem" name="menuItem" value="">
		</form>

	</div>
</div>


<!-- Page content -->
<div class="frame" id="LocationFrameId">

<div class="menu-order-ctas "
		 data-source="7243DE10669F41A4B4E96EF4CCC451E9"
		 tabindex="0">
	<h2>
		What kind of order can we get started for you?
	</h2>
	<ul>
			<li tabindex="0">
<a href="https://order.chick-fil-a.com/load-dot-com" ><img src="https://d1fd34dzzl09j.cloudfront.net/Images/CFACOM/Location%20Icons/drivethru_location_refactor.svg?h=33&amp;w=60&amp;la=en" loading="lazy" alt="Drive Thru Icon" />					<p>
						Order Pickup
					</p>
</a>			</li>

			<li tabindex="0">
<a href="https://order.chick-fil-a.com/delivery/address" ><img src="https://d1fd34dzzl09j.cloudfront.net/Images/CFACOM/Location%20Icons/delivery-icon-ways-you-can-order.svg?h=39&amp;w=59&amp;la=en" loading="lazy" alt="Delivery Icon Ways You Can Order" />					<p>
						Order Delivery
					</p>
</a>			</li>
					<li tabindex="0">
<a href="https://order.chick-fil-a.com/get-started/catering" ><img src="https://d1fd34dzzl09j.cloudfront.net/Images/CFACOM/Location%20Icons/catering-icon_location_refactor.svg?h=30&amp;w=52&amp;la=en" loading="lazy" alt="Catering Icon" />					<p>
						Order Catering
					</p>
</a>			</li>
	</ul>
</div>
<div class="home-menu "
     data-source="8cf1bc27-6fcf-4aec-b3f6-bc043e49cc33"
		 data-lang="en"
     data-component="menuNav"
     data-sticky-position="true"
     data-sticky-priority="2">
		<div class="subnav">
			<ul>
					<li data-element="subNavMenuCategory" data-source="64b0fb99-0012-48a5-88c6-fe897ea8e874">
<img src="https://d1fd34dzzl09j.cloudfront.net/Images/CFACOM/Menu%20Items/Mobile/Breakfast-Figma.png?h=80&amp;w=79&amp;la=en" loading="lazy" class="menu-icon" alt="Breakfast Icon" />
<a href="#breakfast" data-element="subNavMenuLink" data-layer-list-name="USNationalMenu Breakfast" data-layer-list-type="LocationMenuNavigation" data-layer-list-id="8CF1BC276FCF4AECB3F6BC043E49CC33" >Breakfast</a>					</li>
					<li data-element="subNavMenuCategory" data-source="1f65609c-4550-4856-ad61-8ceaa4e55398">
<img src="https://d1fd34dzzl09j.cloudfront.net/Images/CFACOM/Menu%20Items/Mobile/CFA-Spicy-Chicken-Entree-Figma.png?h=66&amp;w=65&amp;la=en" loading="lazy" class="menu-icon" alt="CFA Spicy Chicken Entree" />
<a href="#entrees" data-element="subNavMenuLink" data-layer-list-name="USNationalMenu Entrees" data-layer-list-type="LocationMenuNavigation" data-layer-list-id="8CF1BC276FCF4AECB3F6BC043E49CC33" >Entr&#233;es</a>					</li>
					<li data-element="subNavMenuCategory" data-source="55d5c6e4-8ad9-4dfd-9526-bf1d833e6a54">
<img src="https://d1fd34dzzl09j.cloudfront.net/Images/CFACOM/Menu%20Items/Mobile/Salad-Figma.png?h=61&amp;w=60&amp;la=en" loading="lazy" class="menu-icon" alt="Salad" />
<a href="#salads" data-element="subNavMenuLink" data-layer-list-name="USNationalMenu Salads" data-layer-list-type="LocationMenuNavigation" data-layer-list-id="8CF1BC276FCF4AECB3F6BC043E49CC33" >Salads</a>					</li>
					<li data-element="subNavMenuCategory" data-source="81c9c5d4-ee98-4518-9704-f3e9b06186f9">
<img src="https://d1fd34dzzl09j.cloudfront.net/Images/CFACOM/Menu%20Items/Mobile/Large-Fries-Sides-Figma.png?h=64&amp;w=64&amp;la=en" loading="lazy" class="menu-icon" alt="Large Fries Sides" />
<a href="#sides" data-element="subNavMenuLink" data-layer-list-name="USNationalMenu Sides" data-layer-list-type="LocationMenuNavigation" data-layer-list-id="8CF1BC276FCF4AECB3F6BC043E49CC33" >Sides</a>					</li>
					<li data-element="subNavMenuCategory" data-source="9c259e67-73cb-4722-b10d-fbb060f9f5c9">
<img src="https://d1fd34dzzl09j.cloudfront.net/Images/CFACOM/Menu%20Items/Mobile/Kids-Meal-Figma.png?h=64&amp;w=64&amp;la=en" loading="lazy" class="menu-icon" alt="Kids Meal" />
<a href="#kidsmeals" data-element="subNavMenuLink" data-layer-list-name="USNationalMenu Kids Meals" data-layer-list-type="LocationMenuNavigation" data-layer-list-id="8CF1BC276FCF4AECB3F6BC043E49CC33" >Kid&#39;s Meals</a>					</li>
					<li data-element="subNavMenuCategory" data-source="ccfeac71-916c-4d8c-b652-af7a755c79b2">
<img src="https://d1fd34dzzl09j.cloudfront.net/Images/CFACOM/Menu%20Items/Mobile/Milkshake-Treat-Figma.png?h=63&amp;w=50&amp;la=en" loading="lazy" class="menu-icon" alt="Milkshake Treat" />
<a href="#treats" data-element="subNavMenuLink" data-layer-list-name="USNationalMenu Treats" data-layer-list-type="LocationMenuNavigation" data-layer-list-id="8CF1BC276FCF4AECB3F6BC043E49CC33" >Treats</a>					</li>
					<li data-element="subNavMenuCategory" data-source="6bcd19cc-d2a0-44e6-9c98-dd2a2d8903cc">
<img src="https://d1fd34dzzl09j.cloudfront.net/Images/CFACOM/Menu%20Items/Mobile/Beverage-Figma.png?h=63&amp;w=50&amp;la=en" loading="lazy" class="menu-icon" alt="Beverage Icon" />
<a href="#beverages" data-element="subNavMenuLink" data-layer-list-name="USNationalMenu Drinks" data-layer-list-type="LocationMenuNavigation" data-layer-list-id="8CF1BC276FCF4AECB3F6BC043E49CC33" title="Beverages" >Beverages</a>					</li>
					<li data-element="subNavMenuCategory" data-source="19dea90f-4cd5-4c77-9e42-a827e7016da5">
<img src="/-/media/images/cfacom/menu-items/ws-menu-feed-images/new-sauces/cfa-sauce_00006.png?h=800&amp;w=800&amp;la=en&amp;hash=4D29730094B633C4D062F7130C89E8C9" loading="lazy" class="menu-icon" alt="" />
<a href="#sauces" data-element="subNavMenuLink" data-layer-list-name="USNationalMenu Dipping Sauces and Dressings" data-layer-list-type="LocationMenuNavigation" data-layer-list-id="8CF1BC276FCF4AECB3F6BC043E49CC33" >Dipping Sauces and Dressings</a>					</li>
					<li data-element="subNavMenuCategory" data-source="e7e9c761-2ed5-41a7-b814-c0a0c79d652b">
<img src="/-/media/images/cfacanada/default-images/olo-fpo-catering.jpg?h=200&amp;w=235&amp;la=en&amp;hash=ECCCBC5EC8B11E3EC40B050A393F4D5E" loading="lazy" class="menu-icon" alt="fpo" />
<a href="/catering" data-element="subNavMenuLink" data-layer-list-name="USNationalMenu Catering" data-layer-list-type="LocationMenuNavigation" data-layer-list-id="8CF1BC276FCF4AECB3F6BC043E49CC33" title="Catering" >Catering</a>					</li>
			</ul>
		</div>
</div>

<div id="menu"
		 class="location-menu "
		 data-clientkey="00000"
		 data-source="13467392CEAB4BE4B158207C7F20FECF"
		 data-component="menuNavMobile"
		 role="main">

		<div class="menu-availability-callout" role="alert" tabindex="0">
			<h1>
				Chick-fil-A® Menu
			</h1>
			<p>Availability may differ at different locations.</p>
		</div>
	
<div class="menu-group hidden "
		 data-source="64B0FB99001248A588C6FE897EA8E874"
		 data-is-initially-hidden="true">
	<div class="title-container">
<img src="https://d1fd34dzzl09j.cloudfront.net/Images/CFACOM/Menu%20Items/Mobile/Breakfast-Figma.png?h=-1&amp;w=-1&amp;la=en" class="menu-icon" alt="Menu Item" />		<h2 id="breakfast">
			Breakfast
		</h2>
	</div>



	<div class="menu-items ">
	<div class="flex" style="">
		






<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="BISCUIT_CHICKEN"
     data-categorytag="MOBILE_BREAKFAST"
     data-id="5BEA8EBA96F740B9BB8D5CCDE6037123">
<a href="/menu/chick-fil-a-chicken-biscuit" data-layer-list-type="MenuItemCard" aria-label="Chick-fil-A® Chicken Biscuit" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="5BEA8EBA96F740B9BB8D5CCDE6037123" data-layer-list-id="5BEA8EBA96F740B9BB8D5CCDE6037123" data-layer-list-name="BISCUIT_CHICKEN" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/COM/Menu_Refresh/Breakfast/Breakfast%20PDP/_0000s_0000_Stack620_0000_CFA_1605_60_Biscuit_Chicken_PROD_2155_1240px.png" alt="Chick-fil-A&#174; Chicken Biscuit" loading="lazy" />
				</span>
				<span class="item-title">
Chick-fil-A<sup>®</sup> Chicken Biscuit				</span>
				<p>
					<span>
							
								460&nbsp;Cal&nbsp;per Biscuit
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="BISCUIT_CHICKEN">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="BISCUIT_SPICY_CHICKEN"
     data-categorytag="MOBILE_BREAKFAST"
     data-id="8DF65F950F9044CE99E87BE3EB221B89">
<a href="/menu/breakfast/spicy-chicken-biscuit" data-layer-list-type="MenuItemCard" aria-label="Spicy Chicken Biscuit" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="8DF65F950F9044CE99E87BE3EB221B89" data-layer-list-id="8DF65F950F9044CE99E87BE3EB221B89" data-layer-list-name="BISCUIT_SPICY_CHICKEN" >			<div class="item-details">
				<span class="product food">
<img src="/-/media/images/cfacom/plps/spicy-biscuit/spicybisc_hero.png?h=580&amp;w=710&amp;la=en&amp;hash=CBB670DF5272F9D2014F9D51FF7010E8" loading="lazy" alt="Spicy Chicken Biscuit" title="Breakfast bold" />				</span>
				<span class="item-title">
Spicy Chicken Biscuit				</span>
				<p>
					<span>
							
								430&nbsp;Cal&nbsp;per Biscuit 
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="BISCUIT_SPICY_CHICKEN">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="CHICK_N_MINIS"
     data-categorytag="MOBILE_BREAKFAST"
     data-id="042801420D6546AD868FB5F539403E0A">
<a href="/menu/chick-n-minis" data-layer-list-type="MenuItemCard" aria-label="Chick-fil-A Chick-n-Minis™" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="042801420D6546AD868FB5F539403E0A" data-layer-list-id="042801420D6546AD868FB5F539403E0A" data-layer-list-name="CHICK_N_MINIS" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/COM/Menu_Refresh/Breakfast/Breakfast%20PDP/_0000s_0014_%5BFeed%5D_0000s_0024_Breakfast_Chicken-Mini-4ct.png" alt="Chick-fil-A Chick-n-Minis™" loading="lazy" />
				</span>
				<span class="item-title">
Chick-fil-A Chick-n-Minis™				</span>
				<p>
					<span>
							
								360&nbsp;Cal&nbsp;per 4 Chick-n-Minis
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="CHICK_N_MINIS">
					Order now
				</a>
</div>

	</div>
</div>
<div class="menu-items ">
	<div class="flex" style="">
		






<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="EGG_WHITE_GRILL"
     data-categorytag="MOBILE_BREAKFAST"
     data-id="90E16401A9F644708A42D38A55AF4838">
<a href="/menu/egg-white-grill" data-layer-list-type="MenuItemCard" aria-label="Egg White Grill" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="90E16401A9F644708A42D38A55AF4838" data-layer-list-id="90E16401A9F644708A42D38A55AF4838" data-layer-list-name="EGG_WHITE_GRILL" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/COM/Menu_Refresh/Breakfast/Breakfast%20PDP/_0000s_0039_Stack620_0011_35592_eggWHTchk_p1_trg_42016_1240px.png" alt="Egg White Grill" loading="lazy" />
				</span>
				<span class="item-title">
Egg White Grill				</span>
				<p>
					<span>
							
								300&nbsp;Cal&nbsp;per Sandwich
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="EGG_WHITE_GRILL">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="HBS_BURRITO"
     data-categorytag="MOBILE_BREAKFAST"
     data-id="173A3A64B1E64733B46BB75479289FF1">
<a href="/menu/hash-brown-scramble-burrito" data-layer-list-type="MenuItemCard" aria-label="Hash Brown Scramble Burrito" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="173A3A64B1E64733B46BB75479289FF1" data-layer-list-id="173A3A64B1E64733B46BB75479289FF1" data-layer-list-name="HBS_BURRITO" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/COM/Menu_Refresh/Breakfast/Breakfast%20PDP/_0000s_0004_ChickenSausageBurrito-pdp_1797v2_2880px_resize2.png" alt="Hash Brown Scramble Burrito" loading="lazy" />
				</span>
				<span class="item-title">
Hash Brown Scramble Burrito				</span>
				<p>
					<span>
							
								700&nbsp;Cal&nbsp;per Burrito
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="HBS_BURRITO">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="HASHBROWN_BOWL"
     data-categorytag="MOBILE_BREAKFAST"
     data-id="0D8B9204693042FF8F1153E0BC3D9342">
<a href="/menu/hash-brown-scramble-bowl" data-layer-list-type="MenuItemCard" aria-label="Hash Brown Scramble Bowl" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="0D8B9204693042FF8F1153E0BC3D9342" data-layer-list-id="0D8B9204693042FF8F1153E0BC3D9342" data-layer-list-name="HASHBROWN_BOWL" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/COM/Menu_Refresh/Breakfast/Breakfast%20PDP/_0000s_0005_ChickenHashbrownBreakfastBowl-pdp_Hearty-Breakfast-Bowl_resize2.png" alt="Hash Brown Scramble Bowl" loading="lazy" />
				</span>
				<span class="item-title">
Hash Brown Scramble Bowl				</span>
				<p>
					<span>
							
								470&nbsp;Cal&nbsp;per Bowl
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="HASHBROWN_BOWL">
					Order now
				</a>
</div>

	</div>
</div>
<div class="menu-items ">
	<div class="flex" style="">
		






<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="CEC_BISCUIT"
     data-categorytag="MOBILE_BREAKFAST"
     data-id="569F3CC306F54C8CB64623B5F5B3051D">
<a href="/menu/chicken-egg-cheese-biscuit" data-layer-list-type="MenuItemCard" aria-label="Chicken, Egg & Cheese Biscuit" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="569F3CC306F54C8CB64623B5F5B3051D" data-layer-list-id="569F3CC306F54C8CB64623B5F5B3051D" data-layer-list-name="CEC_BISCUIT" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Breakfast/Biscuit_ChickenEggCheese_PROD_2182_rev17_RGB_1080px.png" alt="Chicken, Egg &amp; Cheese Biscuit" loading="lazy" />
				</span>
				<span class="item-title">
Chicken, Egg & Cheese Biscuit				</span>
				<p>
					<span>
							
								550&nbsp;Cal&nbsp;per Biscuit
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="CEC_BISCUIT">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="BEC_BISCUIT"
     data-categorytag="MOBILE_BREAKFAST"
     data-id="9F56F3BF1A954F8F845A76FC6F7288A4">
<a href="/menu/bacon-egg-cheese-biscuit" data-layer-list-type="MenuItemCard" aria-label="Bacon, Egg & Cheese Biscuit" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="9F56F3BF1A954F8F845A76FC6F7288A4" data-layer-list-id="9F56F3BF1A954F8F845A76FC6F7288A4" data-layer-list-name="BEC_BISCUIT" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/COM/Menu_Refresh/Breakfast/Breakfast%20PDP/_0000s_0008_Bacon-Egg-Cheese-Biscuit_620_PDP.png" alt="Bacon, Egg &amp; Cheese Biscuit" loading="lazy" />
				</span>
				<span class="item-title">
Bacon, Egg & Cheese Biscuit				</span>
				<p>
					<span>
							
								420&nbsp;Cal&nbsp;per Biscuit
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="BEC_BISCUIT">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="SEC_BISCUIT"
     data-categorytag="MOBILE_BREAKFAST"
     data-id="DBB8E424478947A5BB91816A6EB7BBF9">
<a href="/menu/sausage-egg-cheese-biscuit" data-layer-list-type="MenuItemCard" aria-label="Sausage, Egg & Cheese Biscuit" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="DBB8E424478947A5BB91816A6EB7BBF9" data-layer-list-id="DBB8E424478947A5BB91816A6EB7BBF9" data-layer-list-name="SEC_BISCUIT" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/COM/Menu_Refresh/Breakfast/Breakfast%20PDP/_0000s_0026_%5BFeed%5D_0000s_0012_Breakfast_Sausage-Egg-Cheese-Biscuit.png" alt="Sausage, Egg &amp; Cheese Biscuit" loading="lazy" />
				</span>
				<span class="item-title">
Sausage, Egg & Cheese Biscuit				</span>
				<p>
					<span>
							
								620&nbsp;Cal&nbsp;per Biscuit
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="SEC_BISCUIT">
					Order now
				</a>
</div>

	</div>
</div>
<div class="menu-items ">
	<div class="flex" style="">
		






<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="CEC_MUFFIN"
     data-categorytag="MOBILE_BREAKFAST"
     data-id="437FBE0526E742A89A7833C2FC14BED8">
<a href="/menu/chicken-egg-cheese-muffin" data-layer-list-type="MenuItemCard" aria-label="Chicken, Egg & Cheese Muffin" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="437FBE0526E742A89A7833C2FC14BED8" data-layer-list-id="437FBE0526E742A89A7833C2FC14BED8" data-layer-list-name="CEC_MUFFIN" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Breakfast/CECMuffin_1080px.png" alt="Chicken, Egg &amp; Cheese Muffin" loading="lazy" />
				</span>
				<span class="item-title">
Chicken, Egg & Cheese Muffin				</span>
				<p>
					<span>
							
								420&nbsp;Cal&nbsp;per Sandwich
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="CEC_MUFFIN">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="BEC_MUFFIN"
     data-categorytag="MOBILE_BREAKFAST"
     data-id="0715C8F4A25841A8ADB370D0D357C845">
<a href="/menu/bacon-egg-cheese-muffin" data-layer-list-type="MenuItemCard" aria-label="Bacon, Egg & Cheese Muffin" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="0715C8F4A25841A8ADB370D0D357C845" data-layer-list-id="0715C8F4A25841A8ADB370D0D357C845" data-layer-list-name="BEC_MUFFIN" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/COM/Menu_Refresh/Breakfast/Breakfast%20PDP/_0000s_0007_BaconEggCheeseMuffin-Feed_0001s_0008_CFA_1605_59_EnglishMuffin_BaconEggCheese_PROD_2121_1240px.png" alt="Bacon, Egg &amp; Cheese Muffin" loading="lazy" />
				</span>
				<span class="item-title">
Bacon, Egg & Cheese Muffin				</span>
				<p>
					<span>
							
								310&nbsp;Cal&nbsp;per Sandwich
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="BEC_MUFFIN">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="SEC_MUFFIN"
     data-categorytag="MOBILE_BREAKFAST"
     data-id="178FCB499F6D40AE9BDDD5A86B6CE5A1">
<a href="/menu/sausage-egg-cheese-muffin" data-layer-list-type="MenuItemCard" aria-label="Sausage, Egg & Cheese Muffin" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="178FCB499F6D40AE9BDDD5A86B6CE5A1" data-layer-list-id="178FCB499F6D40AE9BDDD5A86B6CE5A1" data-layer-list-name="SEC_MUFFIN" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/COM/Menu_Refresh/Breakfast/Breakfast%20PDP/_0000s_0036_%5BFeed%5D_0000s_0002_Breakfast_Sausage-Egg-Cheese-Muffin.png" alt="Sausage, Egg &amp; Cheese Muffin" loading="lazy" />
				</span>
				<span class="item-title">
Sausage, Egg & Cheese Muffin				</span>
				<p>
					<span>
							
								500&nbsp;Cal&nbsp;per Sandwich
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="SEC_MUFFIN">
					Order now
				</a>
</div>

	</div>
</div>
<div class="menu-items ">
	<div class="flex" style="">
		






<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="HASH_BROWN_GROUP"
     data-categorytag="MOBILE_BREAKFAST"
     data-id="912C53BF2FF54E0CB21E3A32BF6AF934">
<a href="/menu/hash-browns" data-layer-list-type="MenuItemCard" aria-label="Hash Browns" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="912C53BF2FF54E0CB21E3A32BF6AF934" data-layer-list-id="912C53BF2FF54E0CB21E3A32BF6AF934" data-layer-list-name="HASH_BROWN_GROUP" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/COM/Menu_Refresh/Breakfast/Breakfast%20PDP/_0000s_0009_%5BFeed%5D_0000s_0028_Breakfast_Hashbrowns_2.png" alt="Hash Browns" loading="lazy" />
				</span>
				<span class="item-title">
Hash Browns				</span>
				<p>
					<span>
							
								270&nbsp;Cal&nbsp;per Serving
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="HASH_BROWN_GROUP">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="YOGURT_GREEK_PARFAIT"
     data-categorytag="MOBILE_BREAKFAST"
     data-id="B93416693397437E9CEC1E83174D3476">
<a href="/menu/greek-yogurt-parfait" data-layer-list-type="MenuItemCard" aria-label="Greek Yogurt Parfait" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="B93416693397437E9CEC1E83174D3476" data-layer-list-id="B93416693397437E9CEC1E83174D3476" data-layer-list-name="YOGURT_GREEK_PARFAIT" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Sides%26treats/Jul19_OrganicAussieGreekYogurtParfaitCupGranola_pdp.png" alt="Greek Yogurt Parfait" loading="lazy" />
				</span>
				<span class="item-title">
Greek Yogurt Parfait				</span>
				<p>
					<span>
							
								270&nbsp;Cal&nbsp;per Serving
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="YOGURT_GREEK_PARFAIT">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="FRUIT_CUP"
     data-categorytag="MOBILE_BREAKFAST"
     data-id="B0AC07B87CBB4017B59F61CBFE7E1765">
<a href="/menu/fruit-cup" data-layer-list-type="MenuItemCard" aria-label="Fruit Cup" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="B0AC07B87CBB4017B59F61CBFE7E1765" data-layer-list-id="B0AC07B87CBB4017B59F61CBFE7E1765" data-layer-list-name="FRUIT_CUP" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/COM/Menu_Refresh/Sides/Sides%20PDP/_0000s_0010_%5BFeed%5D_0003s_0002_Sides_Fruit-Cup.png" alt="Fruit Cup" loading="lazy" />
				</span>
				<span class="item-title">
Fruit Cup				</span>
				<p>
					<span>
							
								70&nbsp;Cal&nbsp;per Serving
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="FRUIT_CUP">
					Order now
				</a>
</div>

	</div>
</div>
<div class="menu-items ">
	<div class="flex" style="">
		
	</div>
</div>

	
</div>

<div class="menu-group  "
		 data-source="1F65609C45504856AD618CEAA4E55398"
		 data-is-initially-hidden="false">
	<div class="title-container">
<img src="https://d1fd34dzzl09j.cloudfront.net/Images/CFACOM/Menu%20Items/Mobile/CFA-Spicy-Chicken-Entree-Figma.png?h=-1&amp;w=-1&amp;la=en" class="menu-icon" alt="Menu Item" />		<h2 id="entrees">
			Entr&#233;es
		</h2>
	</div>



	<div class="menu-items ">
	<div class="flex" style="">
		






<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="SANDWICH_CFA_CHICKEN"
     data-categorytag="MOBILE_ENTREES"
     data-id="987DE4AC8940403CA2ABFBFE72A4B7B0">
<a href="/menu/entrees/chick-fil-a-chicken-sandwich" data-layer-list-type="MenuItemCard" aria-label="Chick-fil-A® Chicken Sandwich" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="987DE4AC8940403CA2ABFBFE72A4B7B0" data-layer-list-id="987DE4AC8940403CA2ABFBFE72A4B7B0" data-layer-list-name="SANDWICH_CFA_CHICKEN" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Entrees/Jul19_CFASandwich_pdp.png" alt="Chick-fil-A&#174; Chicken Sandwich" loading="lazy" />
				</span>
				<span class="item-title">
Chick-fil-A<sup>®</sup> Chicken Sandwich				</span>
				<p>
					<span>
							
								420&nbsp;Cal&nbsp;per Sandwich
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="SANDWICH_CFA_CHICKEN">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="CFA_DELUXE_SANDWICH"
     data-categorytag="MOBILE_ENTREES"
     data-id="99E310C018594DDE94BE2BFF3441F9D2">
<a href="/menu/chick-fil-a-deluxe-sandwich" data-layer-list-type="MenuItemCard" aria-label="Chick-fil-A® Deluxe Sandwich" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="99E310C018594DDE94BE2BFF3441F9D2" data-layer-list-id="99E310C018594DDE94BE2BFF3441F9D2" data-layer-list-name="CFA_DELUXE_SANDWICH" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/COM/Menu_Refresh/Entree/Entree%20PDP/_0000s_0004_NEWStack6200001CFAPDPDeluxeSandwich1085png.png" alt="Chick-fil-A&#174; Deluxe Sandwich" loading="lazy" />
				</span>
				<span class="item-title">
Chick-fil-A<sup>®</sup> Deluxe Sandwich				</span>
				<p>
					<span>
							
								490&nbsp;Cal&nbsp;per Sandwich
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="CFA_DELUXE_SANDWICH">
					Order now
				</a>
</div>





	</div>
</div>
<div class="menu-items ">
	<div class="flex" style="">
		






<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="SPICY_DELUXE_SANDWICH"
     data-categorytag="MOBILE_ENTREES"
     data-id="4E89208B17C44B748ACCBD0143680239">
<a href="/menu/entrees/spicy-deluxe-sandwich" data-layer-list-type="MenuItemCard" aria-label="Spicy Deluxe Sandwich" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="4E89208B17C44B748ACCBD0143680239" data-layer-list-id="4E89208B17C44B748ACCBD0143680239" data-layer-list-name="SPICY_DELUXE_SANDWICH" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/COM/Menu_Refresh/Entree/Entree%20Desktop/_0003s_0012_%5BFeed%5D_0001s_0023_Entrees_Spicy-Deluxe-Sandwich.png" alt="Spicy Deluxe Sandwich" loading="lazy" />
				</span>
				<span class="item-title">
Spicy Deluxe Sandwich				</span>
				<p>
					<span>
							
								520&nbsp;Cal&nbsp;per Sandwich
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="SPICY_DELUXE_SANDWICH">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="GRILLED_CHICKEN_SANDWICH"
     data-categorytag="MOBILE_ENTREES"
     data-id="301B46BCA48242E187B08A89A4D6221A">
<a href="/menu/grilled-chicken-sandwich" data-layer-list-type="MenuItemCard" aria-label="Grilled Chicken Sandwich" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="301B46BCA48242E187B08A89A4D6221A" data-layer-list-id="301B46BCA48242E187B08A89A4D6221A" data-layer-list-name="GRILLED_CHICKEN_SANDWICH" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/COM/Menu_Refresh/Entree/Entree%20PDP/_0000s_0009_Final__0026_CFA_PDP_Grilled-Deluxe-Sandwich_1085.png" alt="Grilled Chicken Sandwich" loading="lazy" />
				</span>
				<span class="item-title">
Grilled Chicken Sandwich				</span>
				<p>
					<span>
							
								390&nbsp;Cal&nbsp;per Sandwich
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="GRILLED_CHICKEN_SANDWICH">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="SPICY_CHICKEN_CFA_SANDWICH"
     data-categorytag="MOBILE_ENTREES"
     data-id="3E831FE0CDF044059191E351F7FD3494">
<a href="/menu/spicy-chicken-sandwich" data-layer-list-type="MenuItemCard" aria-label="Spicy Chicken Sandwich" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="3E831FE0CDF044059191E351F7FD3494" data-layer-list-id="3E831FE0CDF044059191E351F7FD3494" data-layer-list-name="SPICY_CHICKEN_CFA_SANDWICH" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Entrees/CFASpicySandwich_1080.png" alt="Spicy Chicken Sandwich" loading="lazy" />
				</span>
				<span class="item-title">
Spicy Chicken Sandwich				</span>
				<p>
					<span>
							
								450&nbsp;Cal&nbsp;per Sandwich
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="SPICY_CHICKEN_CFA_SANDWICH">
					Order now
				</a>
</div>

	</div>
</div>
<div class="menu-items ">
	<div class="flex" style="">
		






<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="NUGGETS_CFA"
     data-categorytag="MOBILE_ENTREES"
     data-id="CB446760AE9B4036853DB50367EB3EC9">
<a href="/menu/entrees/chick-fil-a-nuggets" data-layer-list-type="MenuItemCard" aria-label="Chick-fil-A® Nuggets" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="CB446760AE9B4036853DB50367EB3EC9" data-layer-list-id="CB446760AE9B4036853DB50367EB3EC9" data-layer-list-name="NUGGETS_CFA" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Entrees/nuggets_8ct_PDP.png" alt="Chick-fil-A&#174; Nuggets" loading="lazy" />
				</span>
				<span class="item-title">
Chick-fil-A<sup>®</sup> Nuggets				</span>
				<p>
					<span>
							
								250&nbsp;Cal&nbsp;per Entree
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="NUGGETS_CFA">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="GRILLED_NUGGETS"
     data-categorytag="MOBILE_ENTREES"
     data-id="282E7F72980746A2B19BDADF1A17CB54">
<a href="/menu/grilled-nuggets" data-layer-list-type="MenuItemCard" aria-label="Grilled Nuggets" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="282E7F72980746A2B19BDADF1A17CB54" data-layer-list-id="282E7F72980746A2B19BDADF1A17CB54" data-layer-list-name="GRILLED_NUGGETS" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Entrees/grilledNuggets_8ct_PDP.png" alt="Grilled Nuggets" loading="lazy" />
				</span>
				<span class="item-title">
Grilled Nuggets				</span>
				<p>
					<span>
							
								130&nbsp;Cal&nbsp;per Entree
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="GRILLED_NUGGETS">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="GRILLED_CHICKEN_CLUB"
     data-categorytag="MOBILE_ENTREES"
     data-id="231842FBD255423FBD88440726EE7896">
<a href="/menu/chick-fil-a-grilled-chicken-club-sandwich" data-layer-list-type="MenuItemCard" aria-label="Chick-fil-A® Grilled Chicken Club Sandwich" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="231842FBD255423FBD88440726EE7896" data-layer-list-id="231842FBD255423FBD88440726EE7896" data-layer-list-name="GRILLED_CHICKEN_CLUB" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Entrees/grilledClub_colbyJack_PDP.png" alt="Chick-fil-A&#174; Grilled Chicken Club Sandwich" loading="lazy" />
				</span>
				<span class="item-title">
Chick-fil-A<sup>®</sup> Grilled Chicken Club Sandwich				</span>
				<p>
					<span>
							
								520&nbsp;Cal&nbsp;per Sandwich
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="GRILLED_CHICKEN_CLUB">
					Order now
				</a>
</div>

	</div>
</div>
<div class="menu-items ">
	<div class="flex" style="">
		






<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="COOL_WRAP_GRILLED"
     data-categorytag="MOBILE_ENTREES"
     data-id="75029E36C8C74DEEA88C2B615C38CECF">
<a href="/menu/chick-fil-a-cool-wrap" data-layer-list-type="MenuItemCard" aria-label="Chick-fil-A® Cool Wrap" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="75029E36C8C74DEEA88C2B615C38CECF" data-layer-list-id="75029E36C8C74DEEA88C2B615C38CECF" data-layer-list-name="COOL_WRAP_GRILLED" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Entrees/wrap_pdp.png" alt="Chick-fil-A&#174; Cool Wrap" loading="lazy" />
				</span>
				<span class="item-title">
Chick-fil-A<sup>®</sup> Cool Wrap				</span>
				<p>
					<span>
							
								660&nbsp;Cal&nbsp;per Entree
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="COOL_WRAP_GRILLED">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="CHICK_N_STRIPS"
     data-categorytag="MOBILE_ENTREES"
     data-id="5AA38FEB23BC4B3399DF59D20CF7B8ED">
<a href="/menu/chick-n-strips" data-layer-list-type="MenuItemCard" aria-label="Chick-fil-A Chick-n-Strips®" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="5AA38FEB23BC4B3399DF59D20CF7B8ED" data-layer-list-id="5AA38FEB23BC4B3399DF59D20CF7B8ED" data-layer-list-name="CHICK_N_STRIPS" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Entrees/strips_3ct_PDP.png" alt="Chick-fil-A Chick-n-Strips&#174;" loading="lazy" />
				</span>
				<span class="item-title">
Chick-fil-A Chick-n-Strips<sup>®</sup>				</span>
				<p>
					<span>
							
								310&nbsp;Cal&nbsp;per Entree
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="CHICK_N_STRIPS">
					Order now
				</a>
</div>

	</div>
</div>

	
</div>

<div class="menu-group hidden "
		 data-source="55D5C6E48AD94DFD9526BF1D833E6A54"
		 data-is-initially-hidden="true">
	<div class="title-container">
<img src="https://d1fd34dzzl09j.cloudfront.net/Images/CFACOM/Menu%20Items/Mobile/Salad-Figma.png?h=-1&amp;w=-1&amp;la=en" class="menu-icon" alt="Menu Item" />		<h2 id="salads">
			Salads
		</h2>
	</div>



	<div class="menu-items ">
	<div class="flex" style="">
		






<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="COBB_SALAD"
     data-categorytag="MOBILE_SALADS"
     data-id="CFD947B5FAF2420E82C97FD91B6C1780">
<a href="/menu/cobb-salad" data-layer-list-type="MenuItemCard" aria-label="Cobb Salad" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="CFD947B5FAF2420E82C97FD91B6C1780" data-layer-list-id="CFD947B5FAF2420E82C97FD91B6C1780" data-layer-list-name="COBB_SALAD" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Salads%26wraps/cobbSalad_nug_pdp.png" alt="Cobb Salad" loading="lazy" />
				</span>
				<span class="item-title">
Cobb Salad				</span>
				<p>
					<span>
							
								830&nbsp;Cal&nbsp;per Salad (includes toppings and dressing)
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="COBB_SALAD">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="SALAD_SPICY_SOUTHWEST"
     data-categorytag="MOBILE_SALADS"
     data-id="ADC578E833854A90926927279A0D2DCC">
<a href="/menu/spicy-southwest-salad" data-layer-list-type="MenuItemCard" aria-label="Spicy Southwest Salad" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="ADC578E833854A90926927279A0D2DCC" data-layer-list-id="ADC578E833854A90926927279A0D2DCC" data-layer-list-name="SALAD_SPICY_SOUTHWEST" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Salads%26wraps/sswSalad_spicyGrilled_pdp.png" alt="Spicy Southwest Salad" loading="lazy" />
				</span>
				<span class="item-title">
Spicy Southwest Salad				</span>
				<p>
					<span>
							
								680&nbsp;Cal&nbsp;per Salad (includes toppings and dressing)
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="SALAD_SPICY_SOUTHWEST">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="SALAD_MARKET"
     data-categorytag="MOBILE_SALADS"
     data-id="4CDA55EDC8FF44DE9F3A93F6822D8774">
<a href="/menu/market-salad" data-layer-list-type="MenuItemCard" aria-label="Market Salad" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="4CDA55EDC8FF44DE9F3A93F6822D8774" data-layer-list-id="4CDA55EDC8FF44DE9F3A93F6822D8774" data-layer-list-name="SALAD_MARKET" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Salads%26wraps/marketSalad_grilled_pdp.png" alt="Market Salad" loading="lazy" />
				</span>
				<span class="item-title">
Market Salad				</span>
				<p>
					<span>
							
								550&nbsp;Cal&nbsp;per Salad (includes toppings and dressing)
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="SALAD_MARKET">
					Order now
				</a>
</div>

	</div>
</div>

	
</div>

<div class="menu-group hidden "
		 data-source="81C9C5D4EE9845189704F3E9B06186F9"
		 data-is-initially-hidden="true">
	<div class="title-container">
<img src="https://d1fd34dzzl09j.cloudfront.net/Images/CFACOM/Menu%20Items/Mobile/Large-Fries-Sides-Figma.png?h=-1&amp;w=-1&amp;la=en" class="menu-icon" alt="Menu Item" />		<h2 id="sides">
			Sides
		</h2>
	</div>



	<div class="menu-items ">
	<div class="flex" style="">
		






<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="WAFFLE_POTATO_FRIES"
     data-categorytag="MOBILE_SIDES"
     data-id="1C386EF04BF44E61B8D579EF2890B696">
<a href="/menu/sides/chick-fil-a-waffle-potato-fries" data-layer-list-type="MenuItemCard" aria-label="Chick-fil-A Waffle Potato Fries®" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="1C386EF04BF44E61B8D579EF2890B696" data-layer-list-id="1C386EF04BF44E61B8D579EF2890B696" data-layer-list-name="WAFFLE_POTATO_FRIES" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Sides%26treats/Medium_Lowered_1217shoot_1080x1080.png" alt="Chick-fil-A Waffle Potato Fries&#174;" loading="lazy" />
				</span>
				<span class="item-title">
Chick-fil-A Waffle Potato Fries<sup>®</sup>				</span>
				<p>
					<span>
							
								420&nbsp;Cal&nbsp;per Serving
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="WAFFLE_POTATO_FRIES">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="FRUIT_CUP"
     data-categorytag="MOBILE_SIDES"
     data-id="C48D803BE56C4CC599AA432A0440CB5B">
<a href="/menu/fruit-cup" data-layer-list-type="MenuItemCard" aria-label="Fruit Cup" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="C48D803BE56C4CC599AA432A0440CB5B" data-layer-list-id="C48D803BE56C4CC599AA432A0440CB5B" data-layer-list-name="FRUIT_CUP" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/COM/Menu_Refresh/Sides/Sides%20PDP/_0000s_0010_%5BFeed%5D_0003s_0002_Sides_Fruit-Cup.png" alt="Fruit Cup" loading="lazy" />
				</span>
				<span class="item-title">
Fruit Cup				</span>
				<p>
					<span>
							
								70&nbsp;Cal&nbsp;per Serving
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="FRUIT_CUP">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="SALAD_SIDE"
     data-categorytag="MOBILE_SIDES"
     data-id="77DE48DD00364296B61D707D27A9D051">
<a href="/menu/side-salad" data-layer-list-type="MenuItemCard" aria-label="Side Salad" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="77DE48DD00364296B61D707D27A9D051" data-layer-list-id="77DE48DD00364296B61D707D27A9D051" data-layer-list-name="SALAD_SIDE" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Sides%26treats/sideSalad_pdp.png" alt="Side Salad" loading="lazy" />
				</span>
				<span class="item-title">
Side Salad				</span>
				<p>
					<span>
							
								530&nbsp;Cal&nbsp;per Serving
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="SALAD_SIDE">
					Order now
				</a>
</div>

	</div>
</div>
<div class="menu-items ">
	<div class="flex" style="">
		






<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="MACNCHEESE"
     data-categorytag="MOBILE_SIDES"
     data-id="1B99E1AE02F04620AC1B5FBEAFAB0D0D">
<a href="/menu/mac-cheese" data-layer-list-type="MenuItemCard" aria-label="Mac & Cheese" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="1B99E1AE02F04620AC1B5FBEAFAB0D0D" data-layer-list-id="1B99E1AE02F04620AC1B5FBEAFAB0D0D" data-layer-list-name="MACNCHEESE" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/COM/Menu_Refresh/Sides/Sides%20PDP/MacnCheese_5oz_pdp.png" alt="Mac &amp; Cheese" loading="lazy" />
				</span>
				<span class="item-title">
Mac & Cheese				</span>
				<p>
					<span>
							
								450&nbsp;Cal&nbsp;per Serving
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="MACNCHEESE">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="CHICKEN_SOUP"
     data-categorytag="MOBILE_SIDES"
     data-id="DA4CC46DF1C64705BEA781F4C5336788">
<a href="/menu/chicken-noodle-soup" data-layer-list-type="MenuItemCard" aria-label="Chicken Noodle Soup" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="DA4CC46DF1C64705BEA781F4C5336788" data-layer-list-id="DA4CC46DF1C64705BEA781F4C5336788" data-layer-list-name="CHICKEN_SOUP" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Sides%26treats/Chicken-Noodle-Soup_Small_PDP.png" alt="Chicken Noodle Soup" loading="lazy" />
				</span>
				<span class="item-title">
Chicken Noodle Soup				</span>
				<p>
					<span>
							
								170&nbsp;Cal&nbsp;per Serving
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="CHICKEN_SOUP">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="CHICKEN_TORTILLA_SOUP"
     data-categorytag="MOBILE_SIDES"
     data-id="4FE600C452F04E2881F2B9E4D5BBC411">
<a href="/menu/sides/chicken-tortilla-soup" data-layer-list-type="MenuItemCard" aria-label="Chicken Tortilla Soup" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="4FE600C452F04E2881F2B9E4D5BBC411" data-layer-list-id="4FE600C452F04E2881F2B9E4D5BBC411" data-layer-list-name="CHICKEN_TORTILLA_SOUP" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/COM/Menu_Refresh/Sides/Sides%20Desktop/_0006s_0005_%5BFeed%5D_0003s_0007_Sides_Chicken-Tortilla-Soup.png" alt="Chicken Tortilla Soup" loading="lazy" />
				</span>
				<span class="item-title">
Chicken Tortilla Soup				</span>
				<p>
					<span>
							
								340&nbsp;Cal&nbsp;per Serving
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="CHICKEN_TORTILLA_SOUP">
					Order now
				</a>
</div>

	</div>
</div>
<div class="menu-items ">
	<div class="flex" style="">
		






<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="KALE_CRUNCH_SIDE"
     data-categorytag="MOBILE_SIDES"
     data-id="CFFB9852F21A4E5185C5EC9D90213ABC">
<a href="/menu/sides/kale-crunch-side" data-layer-list-type="MenuItemCard" aria-label="Kale Crunch Side" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="CFFB9852F21A4E5185C5EC9D90213ABC" data-layer-list-id="CFFB9852F21A4E5185C5EC9D90213ABC" data-layer-list-name="KALE_CRUNCH_SIDE" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Sides%26treats/kaleCrunch_lg_pdp.png" alt="Kale Crunch Side" loading="lazy" />
				</span>
				<span class="item-title">
Kale Crunch Side				</span>
				<p>
					<span>
							
								170&nbsp;Cal&nbsp;
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="KALE_CRUNCH_SIDE">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="YOGURT_GREEK_PARFAIT"
     data-categorytag="MOBILE_SIDES"
     data-id="53E2291F912B488286BA482875D97100">
<a href="/menu/greek-yogurt-parfait" data-layer-list-type="MenuItemCard" aria-label="Greek Yogurt Parfait" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="53E2291F912B488286BA482875D97100" data-layer-list-id="53E2291F912B488286BA482875D97100" data-layer-list-name="YOGURT_GREEK_PARFAIT" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Sides%26treats/Jul19_OrganicAussieGreekYogurtParfaitCupGranola_pdp.png" alt="Greek Yogurt Parfait" loading="lazy" />
				</span>
				<span class="item-title">
Greek Yogurt Parfait				</span>
				<p>
					<span>
							
								270&nbsp;Cal&nbsp;per Serving
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="YOGURT_GREEK_PARFAIT">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="CHIPS_WAFFLE"
     data-categorytag="MOBILE_SIDES"
     data-id="48F846A33BDA4F639D31B5F12AAC1C69">
<a href="/menu/waffle-potato-chips" data-layer-list-type="MenuItemCard" aria-label="Waffle Potato Chips" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="48F846A33BDA4F639D31B5F12AAC1C69" data-layer-list-id="48F846A33BDA4F639D31B5F12AAC1C69" data-layer-list-name="CHIPS_WAFFLE" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Drinks/chips_1080.png" alt="Waffle Potato Chips" loading="lazy" />
				</span>
				<span class="item-title">
Waffle Potato Chips				</span>
				<p>
					<span>
							
								220&nbsp;Cal&nbsp;per Serving
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="CHIPS_WAFFLE">
					Order now
				</a>
</div>

	</div>
</div>
<div class="menu-items ">
	<div class="flex" style="">
		






<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="APPLE_SAUCE"
     data-categorytag="MOBILE_SIDES"
     data-id="52CE1933E3FE4DB182D7DF25F9CBCD15">
<a href="/menu/buddy-fruits-apple-sauce" data-layer-list-type="MenuItemCard" aria-label="Buddy Fruits® Apple Sauce" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="52CE1933E3FE4DB182D7DF25F9CBCD15" data-layer-list-id="52CE1933E3FE4DB182D7DF25F9CBCD15" data-layer-list-name="APPLE_SAUCE" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Sides%26treats/Buddy_Fruits_PDP.png" alt="Buddy Fruits&#174; Apple Sauce" loading="lazy" />
				</span>
				<span class="item-title">
Buddy Fruits<sup>®</sup> Apple Sauce				</span>
				<p>
					<span>
							
								45&nbsp;Cal&nbsp;per Container
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="APPLE_SAUCE">
					Order now
				</a>
</div>

	</div>
</div>

	
</div>

<div class="menu-group hidden "
		 data-source="9C259E6773CB4722B10DFBB060F9F5C9"
		 data-is-initially-hidden="true">
	<div class="title-container">
<img src="https://d1fd34dzzl09j.cloudfront.net/Images/CFACOM/Menu%20Items/Mobile/Kids-Meal-Figma.png?h=-1&amp;w=-1&amp;la=en" class="menu-icon" alt="Menu Item" />		<h2 id="kidsmeals">
			Kid&#39;s Meals
		</h2>
	</div>



	<div class="menu-items ">
	<div class="flex" style="">
		






<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="KD_MEAL_NUG_5CT"
     data-categorytag="MOBILE_KIDSMEALS"
     data-id="2AC4A32921C2484B840AE4CE3763158A">
<a href="/menu/nuggets-kids-meal" data-layer-list-type="MenuItemCard" aria-label="5 Ct Nuggets Kid's Meal" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="2AC4A32921C2484B840AE4CE3763158A" data-layer-list-id="2AC4A32921C2484B840AE4CE3763158A" data-layer-list-name="KD_MEAL_NUG_5CT" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Entrees/Dec2019_CFANuggets_5ct_pdp.png" alt="5 Ct Nuggets Kid&#39;s Meal" loading="lazy" />
				</span>
				<span class="item-title">
5 Ct Nuggets Kid's Meal				</span>
				<p>
					<span>
							
								160&nbsp;Cal&nbsp;per Entree
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="KD_MEAL_NUG_5CT">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="KD_MEAL_STRIPS_2"
     data-categorytag="MOBILE_KIDSMEALS"
     data-id="FE38540EE1E14A1FA59778704631BA54">
<a href="/menu/chicknstrips-kids-meal" data-layer-list-type="MenuItemCard" aria-label="2 Ct Chick-n-Strips® Kid's Meal" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="FE38540EE1E14A1FA59778704631BA54" data-layer-list-id="FE38540EE1E14A1FA59778704631BA54" data-layer-list-name="KD_MEAL_STRIPS_2" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Entrees/strips_2ct_PDP.png" alt="2 Ct Chick-n-Strips&#174; Kid&#39;s Meal" loading="lazy" />
				</span>
				<span class="item-title">
2 Ct Chick-n-Strips<sup>®</sup> Kid's Meal				</span>
				<p>
					<span>
							
								200&nbsp;Cal&nbsp;per Entree
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="KD_MEAL_STRIPS_2">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="KD_MEAL_GRILLED_NUGGETS_5"
     data-categorytag="MOBILE_KIDSMEALS"
     data-id="A54165142D394FF38EAFEB335EECA895">
<a href="/menu/grilled-nuggets-kids-meal" data-layer-list-type="MenuItemCard" aria-label="5 Ct Grilled Nuggets Kid's Meal" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="A54165142D394FF38EAFEB335EECA895" data-layer-list-id="A54165142D394FF38EAFEB335EECA895" data-layer-list-name="KD_MEAL_GRILLED_NUGGETS_5" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Entrees/Dec2019_GrilledNuggets_5ct_pdp.png" alt="5 Ct Grilled Nuggets Kid&#39;s Meal" loading="lazy" />
				</span>
				<span class="item-title">
5 Ct Grilled Nuggets Kid's Meal				</span>
				<p>
					<span>
							
								80&nbsp;Cal&nbsp;per Entree
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="KD_MEAL_GRILLED_NUGGETS_5">
					Order now
				</a>
</div>

	</div>
</div>

	
	<div class="co-item ">
		<div class="wrapper flex">
			<div class="image">
<img src="https://d1fd34dzzl09j.cloudfront.net/Images/CFACOM/Kids/3-U%20March%2024%20book_11zon.jpg?h=682&amp;w=1053&amp;la=en" alt="" />				<div class="item-title">
					
					
				</div>
			</div>
			<div class="content" >
					<h2 class="title"><p style="text-align: left;">Ages 3 and under </p>
<p style="text-align: left;">On the Go</p></h2>
				<p>Embark on a thrilling journey through the world of vehicles. From the iconic work of Richard Scarry, this collection of board books invites young readers to take the wheel and immerse themselves in exciting adventures. Collect all four titles: Boats, Cars, Planes, and Trucks.</p>				<p>
				</p>
			</div><!--/content -->
		</div>
	</div>

	<div class="co-item ">
		<div class="wrapper flex">
			<div class="image">
<img src="https://d1fd34dzzl09j.cloudfront.net/Images/CFACOM/Kids/4-U%20March%202024%20book_11zon.jpg?h=690&amp;w=1028&amp;la=en" alt="" />				<div class="item-title">
					
					
				</div>
			</div>
			<div class="content" >
					<h2 class="title"><p style="text-align: left;">Ages 4 and up </p>
<p style="text-align: left;">Shine A Light Program</p></h2>
				<p>Uncover fascinating mysteries such as what is inside, under, or beyond the obvious. Kids love discovering what&rsquo;s &ldquo;behind the scenes.&rdquo; Let them investigate hidden wonders big and small. Collect all five books: On the Space Station, Secrets of Our Earth, Secrets of the Apple Tree, Secrets of the Rain Forest, and Secrets of the Seashore.</p>				<p>
				</p>
			</div><!--/content -->
		</div>
	</div>

</div>

<div class="menu-group hidden "
		 data-source="CCFEAC71916C4D8CB652AF7A755C79B2"
		 data-is-initially-hidden="true">
	<div class="title-container">
<img src="https://d1fd34dzzl09j.cloudfront.net/Images/CFACOM/Menu%20Items/Mobile/Milkshake-Treat-Figma.png?h=-1&amp;w=-1&amp;la=en" class="menu-icon" alt="Menu Item" />		<h2 id="treats">
			Treats
		</h2>
	</div>



	<div class="menu-items ">
	<div class="flex" style="">
		






<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="FROSTED_LEMONADE"
     data-categorytag="MOBILE_TREATS"
     data-id="11F16CFD0A184D97B53EA3EBDFFBC3A0">
<a href="/menu/frosted-lemonade" data-layer-list-type="MenuItemCard" aria-label="Frosted Lemonade" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="11F16CFD0A184D97B53EA3EBDFFBC3A0" data-layer-list-id="11F16CFD0A184D97B53EA3EBDFFBC3A0" data-layer-list-name="FROSTED_LEMONADE" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/COM/Menu_Refresh/Treats/Treats%20PDP/_0000s_0003_%5BFeed%5D_0005s_0001_Treats_Frosted-Lemonade.png" alt="Frosted Lemonade" loading="lazy" />
				</span>
				<span class="item-title">
Frosted Lemonade				</span>
				<p>
					<span>
							
								320&nbsp;Cal&nbsp;per Serving
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="FROSTED_LEMONADE">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="SM_FROSTED_COFFEE"
     data-categorytag="MOBILE_TREATS"
     data-id="EDFBF04E3EED464187398FD2439793C5">
<a href="/menu/frosted-coffee" data-layer-list-type="MenuItemCard" aria-label="Frosted Coffee" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="EDFBF04E3EED464187398FD2439793C5" data-layer-list-id="EDFBF04E3EED464187398FD2439793C5" data-layer-list-name="SM_FROSTED_COFFEE" >			<div class="item-details">
				<span class="product food">
<img src="https://d1fd34dzzl09j.cloudfront.net/Images/CFACOM/PLP%20updates/Treats_Frosted-Coffee.png?h=1000&amp;w=800&amp;la=en" loading="lazy" alt="Frosted Coffee" />				</span>
				<span class="item-title">
Frosted Coffee				</span>
				<p>
					<span>
							
								250&nbsp;Cal&nbsp;per Serving
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="SM_FROSTED_COFFEE">
					Order now
				</a>
</div>

	</div>
</div>
<div class="menu-items ">
	<div class="flex" style="">
		






<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="COOKIE_CHOCOLATE_CHUNK"
     data-categorytag="MOBILE_TREATS"
     data-id="A4DDC0AC1973486AB9351AA941F0ED36">
<a href="/menu/chocolate-chunk-cookie" data-layer-list-type="MenuItemCard" aria-label="Chocolate Chunk Cookie" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="A4DDC0AC1973486AB9351AA941F0ED36" data-layer-list-id="A4DDC0AC1973486AB9351AA941F0ED36" data-layer-list-name="COOKIE_CHOCOLATE_CHUNK" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Sides%26treats/PDP_CCCookie.png" alt="Chocolate Chunk Cookie" loading="lazy" />
				</span>
				<span class="item-title">
Chocolate Chunk Cookie				</span>
				<p>
					<span>
							
								370&nbsp;Cal&nbsp;per Cookie
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="COOKIE_CHOCOLATE_CHUNK">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="BROWNIE_GROUP"
     data-categorytag="MOBILE_TREATS"
     data-id="196C011F16664F2195FB751CA72247B7">
<a href="/menu/chocolate-fudge-brownie" data-layer-list-type="MenuItemCard" aria-label="Chocolate Fudge Brownie" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="196C011F16664F2195FB751CA72247B7" data-layer-list-id="196C011F16664F2195FB751CA72247B7" data-layer-list-name="BROWNIE_GROUP" >			<div class="item-details">
				<span class="product food">
						<img src="" alt="Chocolate Fudge Brownie" loading="lazy" />
				</span>
				<span class="item-title">
Chocolate Fudge Brownie				</span>
				<p>
					<span>
							
								0&nbsp;Cal&nbsp;
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="BROWNIE_GROUP">
					Order now
				</a>
</div>

	</div>
</div>
<div class="menu-items ">
	<div class="flex" style="">
		






<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="SM_COOKIES_CREAM_MILKSHAKE"
     data-categorytag="MOBILE_TREATS"
     data-id="71E810D2146F436597AAC44034EAB686">
<a href="/menu/cookies-cream-milkshake" data-layer-list-type="MenuItemCard" aria-label="Cookies & Cream Milkshake" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="71E810D2146F436597AAC44034EAB686" data-layer-list-id="71E810D2146F436597AAC44034EAB686" data-layer-list-name="SM_COOKIES_CREAM_MILKSHAKE" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Mobile/Desserts/Menu%20Item/16oz_C%26C_Milkshake-1080.png" alt="Cookies &amp; Cream Milkshake" loading="lazy" />
				</span>
				<span class="item-title">
Cookies & Cream Milkshake				</span>
				<p>
					<span>
							
								630&nbsp;Cal&nbsp;per Milkshake
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="SM_COOKIES_CREAM_MILKSHAKE">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="SM_CHOCOLATE_MILKSHAKE"
     data-categorytag="MOBILE_TREATS"
     data-id="4A17BCC54697406FB5732711FCA3D087">
<a href="/menu/chocolate-milkshake" data-layer-list-type="MenuItemCard" aria-label="Chocolate Milkshake" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="4A17BCC54697406FB5732711FCA3D087" data-layer-list-id="4A17BCC54697406FB5732711FCA3D087" data-layer-list-name="SM_CHOCOLATE_MILKSHAKE" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Mobile/Desserts/Menu%20Item/16oz_ChocolateMilkshake-1080.png" alt="Chocolate Milkshake" loading="lazy" />
				</span>
				<span class="item-title">
Chocolate Milkshake				</span>
				<p>
					<span>
							
								590&nbsp;Cal&nbsp;per Milkshake
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="SM_CHOCOLATE_MILKSHAKE">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="SM_STRAWBERRY_MILKSHAKE"
     data-categorytag="MOBILE_TREATS"
     data-id="F84E1C690A2C44C089B915DA02A75015">
<a href="/menu/strawberry-milkshake" data-layer-list-type="MenuItemCard" aria-label="Strawberry Milkshake" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="F84E1C690A2C44C089B915DA02A75015" data-layer-list-id="F84E1C690A2C44C089B915DA02A75015" data-layer-list-name="SM_STRAWBERRY_MILKSHAKE" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Mobile/Desserts/Menu%20Item/16oz_StrawberryMilkshake-1080.png" alt="Strawberry Milkshake" loading="lazy" />
				</span>
				<span class="item-title">
Strawberry Milkshake				</span>
				<p>
					<span>
							
								590&nbsp;Cal&nbsp;per Milkshake
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="SM_STRAWBERRY_MILKSHAKE">
					Order now
				</a>
</div>

	</div>
</div>
<div class="menu-items ">
	<div class="flex" style="">
		






<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="SM_VANILLA_MILKSHAKE"
     data-categorytag="MOBILE_TREATS"
     data-id="910518B3B97C4AB58FE7601FB8968116">
<a href="/menu/vanilla-milkshake" data-layer-list-type="MenuItemCard" aria-label="Vanilla Milkshake" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="910518B3B97C4AB58FE7601FB8968116" data-layer-list-id="910518B3B97C4AB58FE7601FB8968116" data-layer-list-name="SM_VANILLA_MILKSHAKE" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Mobile/Desserts/Menu%20Item/16oz_VanillaMilkshake-1080.png" alt="Vanilla Milkshake" loading="lazy" />
				</span>
				<span class="item-title">
Vanilla Milkshake				</span>
				<p>
					<span>
							
								580&nbsp;Cal&nbsp;per Milkshake
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="SM_VANILLA_MILKSHAKE">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="SM_ICEDREAM_CONE"
     data-categorytag="MOBILE_TREATS"
     data-id="63DE847879F24C56845A97005B691C77">
<a href="/menu/icedream-cone" data-layer-list-type="MenuItemCard" aria-label="Chick-fil-A® Icedream® Cone" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="63DE847879F24C56845A97005B691C77" data-layer-list-id="63DE847879F24C56845A97005B691C77" data-layer-list-name="SM_ICEDREAM_CONE" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/COM/Menu_Refresh/Drinks/Drinks%20PDP/_0000s_0027_%5BFeed%5D_0006s_0013_Drinks_Ice-Dream.png" alt="Chick-fil-A&#174; Icedream&#174; Cone" loading="lazy" />
				</span>
				<span class="item-title">
Chick-fil-A<sup>®</sup> Icedream<sup>®</sup> Cone				</span>
				<p>
					<span>
							
								180&nbsp;Cal&nbsp;per Cone
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="SM_ICEDREAM_CONE">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="KD_ICEDREAM_CUP"
     data-categorytag="MOBILE_TREATS"
     data-id="191B6D46B18F48899476F2FED7ABF799">
<a href="/menu/icedream-cup" data-layer-list-type="MenuItemCard" aria-label="Chick-fil-A® Icedream® Cup" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="191B6D46B18F48899476F2FED7ABF799" data-layer-list-id="191B6D46B18F48899476F2FED7ABF799" data-layer-list-name="KD_ICEDREAM_CUP" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Sides%26treats/IceDream_RedCup_1080x1080.png" alt="Chick-fil-A&#174; Icedream&#174; Cup" loading="lazy" />
				</span>
				<span class="item-title">
Chick-fil-A<sup>®</sup> Icedream<sup>®</sup> Cup				</span>
				<p>
					<span>
							
								140&nbsp;Cal&nbsp;per Cup
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="KD_ICEDREAM_CUP">
					Order now
				</a>
</div>

	</div>
</div>

	
</div>

<div class="menu-group hidden "
		 data-source="6BCD19CCD2A044E69C98DD2A2D8903CC"
		 data-is-initially-hidden="true">
	<div class="title-container">
<img src="https://d1fd34dzzl09j.cloudfront.net/Images/CFACOM/Menu%20Items/Mobile/Beverage-Figma.png?h=-1&amp;w=-1&amp;la=en" class="menu-icon" alt="Menu Item" />		<h2 id="beverages">
			Beverages
		</h2>
	</div>



	<div class="menu-items ">
	<div class="flex" style="">
		






<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="MANGO_PASSION_SUNJOY_GROUP"
     data-categorytag="MOBILE_BEVERAGES"
     data-id="87C8487373A5453F9D2D6B8582B1C199">
<a href="/menu/mango-passion" data-layer-list-type="MenuItemCard" aria-label="Seasonal Mango Passion Sunjoy Beverages" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="87C8487373A5453F9D2D6B8582B1C199" data-layer-list-id="87C8487373A5453F9D2D6B8582B1C199" data-layer-list-name="MANGO_PASSION_SUNJOY_GROUP" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Mobile/Beverages/Menu%20Item/MangoPassionSunjoy_1080x1080.png" alt="Seasonal Mango Passion Sunjoy Beverages" loading="lazy" />
				</span>
				<span class="item-title">
Seasonal Mango Passion Sunjoy Beverages				</span>
				<p>
					<span>
							
								160&nbsp;Cal&nbsp;per Container
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="MANGO_PASSION_SUNJOY_GROUP">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="SWEET_TEA_INDIVIDUAL"
     data-categorytag="MOBILE_BEVERAGES"
     data-id="F7505C91782B4B2AA4EEA7154B5741E9">
<a href="/menu/freshly-brewed-iced-tea-sweetened" data-layer-list-type="MenuItemCard" aria-label="Freshly-Brewed Iced Tea Sweetened" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="F7505C91782B4B2AA4EEA7154B5741E9" data-layer-list-id="F7505C91782B4B2AA4EEA7154B5741E9" data-layer-list-name="SWEET_TEA_INDIVIDUAL" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Drinks/tea_pdp.png" alt="Freshly-Brewed Iced Tea Sweetened" loading="lazy" />
				</span>
				<span class="item-title">
Freshly-Brewed Iced Tea Sweetened				</span>
				<p>
					<span>
							
								100&nbsp;Cal&nbsp;per Container
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="SWEET_TEA_INDIVIDUAL">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="MEAL_UNSWEET_TEA"
     data-categorytag="MOBILE_BEVERAGES"
     data-id="2BE37AB3CFDE4D1FA44DA568AF633183">
<a href="/menu/freshly-brewed-iced-tea-unsweetened" data-layer-list-type="MenuItemCard" aria-label="Freshly-Brewed Iced Tea Unsweetened" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="2BE37AB3CFDE4D1FA44DA568AF633183" data-layer-list-id="2BE37AB3CFDE4D1FA44DA568AF633183" data-layer-list-name="MEAL_UNSWEET_TEA" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Drinks/tea_pdp.png" alt="Freshly-Brewed Iced Tea Unsweetened" loading="lazy" />
				</span>
				<span class="item-title">
Freshly-Brewed Iced Tea Unsweetened				</span>
				<p>
					<span>
							
								0&nbsp;Cal&nbsp;per Container
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="MEAL_UNSWEET_TEA">
					Order now
				</a>
</div>

	</div>
</div>
<div class="menu-items ">
	<div class="flex" style="">
		






<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="LEMONADE"
     data-categorytag="MOBILE_BEVERAGES"
     data-id="6408FDDB473B463485CDFCE7DAD293D1">
<a href="/menu/chick-fil-a-lemonade" data-layer-list-type="MenuItemCard" aria-label="Chick-fil-A® Lemonade" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="6408FDDB473B463485CDFCE7DAD293D1" data-layer-list-id="6408FDDB473B463485CDFCE7DAD293D1" data-layer-list-name="LEMONADE" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Drinks/lemonade_pdp.png" alt="Chick-fil-A&#174; Lemonade" loading="lazy" />
				</span>
				<span class="item-title">
Chick-fil-A<sup>®</sup> Lemonade				</span>
				<p>
					<span>
							
								270&nbsp;Cal&nbsp;per Container
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="LEMONADE">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="DIET_LEMONADE"
     data-categorytag="MOBILE_BEVERAGES"
     data-id="7FC5049A5D224E18B03CBEAA95E5D8FD">
<a href="/menu/chick-fil-a-diet-lemonade" data-layer-list-type="MenuItemCard" aria-label="Chick-fil-A® Diet Lemonade" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="7FC5049A5D224E18B03CBEAA95E5D8FD" data-layer-list-id="7FC5049A5D224E18B03CBEAA95E5D8FD" data-layer-list-name="DIET_LEMONADE" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Drinks/lemonade_pdp.png" alt="Chick-fil-A&#174; Diet Lemonade" loading="lazy" />
				</span>
				<span class="item-title">
Chick-fil-A<sup>®</sup> Diet Lemonade				</span>
				<p>
					<span>
							
								60&nbsp;Cal&nbsp;per Container
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="DIET_LEMONADE">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="SWEET_TEA_LEMONADE"
     data-categorytag="MOBILE_BEVERAGES"
     data-id="FC2A105B035C4700958072023A8F4719">
<a href="/menu/sunjoy-w-12-sweet-tea-12-lemonade" data-layer-list-type="MenuItemCard" aria-label="Sunjoy® (1/2 Sweet Tea, 1/2 Lemonade)" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="FC2A105B035C4700958072023A8F4719" data-layer-list-id="FC2A105B035C4700958072023A8F4719" data-layer-list-name="SWEET_TEA_LEMONADE" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Mobile/Beverages/Menu%20Item/Sunjoy_SIMP_1080x1080.png" alt="Sunjoy&#174; (1/2 Sweet Tea, 1/2 Lemonade)" loading="lazy" />
				</span>
				<span class="item-title">
Sunjoy<sup>®</sup> (1/2 Sweet Tea, 1/2 Lemonade)				</span>
				<p>
					<span>
							
								180&nbsp;Cal&nbsp;per Container
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="SWEET_TEA_LEMONADE">
					Order now
				</a>
</div>

	</div>
</div>
<div class="menu-items ">
	<div class="flex" style="">
		






<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="SWEET_TEA_DIET_LEMONADE"
     data-categorytag="MOBILE_BEVERAGES"
     data-id="FCEA971BC3164FC7A9CC341BBEBE2472">
<a href="/menu/sunjoy-w-12-sweet-tea-12-diet-lemonade" data-layer-list-type="MenuItemCard" aria-label="Sunjoy® (1/2 Sweet Tea, 1/2 Diet Lemonade)" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="FCEA971BC3164FC7A9CC341BBEBE2472" data-layer-list-id="FCEA971BC3164FC7A9CC341BBEBE2472" data-layer-list-name="SWEET_TEA_DIET_LEMONADE" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Mobile/Beverages/Menu%20Item/Sunjoy_SIMP_1080x1080.png" alt="Sunjoy&#174; (1/2 Sweet Tea, 1/2 Diet Lemonade)" loading="lazy" />
				</span>
				<span class="item-title">
Sunjoy<sup>®</sup> (1/2 Sweet Tea, 1/2 Diet Lemonade)				</span>
				<p>
					<span>
							
								100&nbsp;Cal&nbsp;per Container
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="SWEET_TEA_DIET_LEMONADE">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="UNSWEET_TEA_LEMOMADE"
     data-categorytag="MOBILE_BEVERAGES"
     data-id="4B7F0725BE324F04804217E091E60351">
<a href="/menu/sunjoy-w-12-unsweet-tea-12-lemonade" data-layer-list-type="MenuItemCard" aria-label="Sunjoy® (1/2 Unsweet Tea, 1/2 Lemonade)" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="4B7F0725BE324F04804217E091E60351" data-layer-list-id="4B7F0725BE324F04804217E091E60351" data-layer-list-name="UNSWEET_TEA_LEMOMADE" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Mobile/Beverages/Menu%20Item/Sunjoy_SIMP_1080x1080.png" alt="Sunjoy&#174; (1/2 Unsweet Tea, 1/2 Lemonade)" loading="lazy" />
				</span>
				<span class="item-title">
Sunjoy<sup>®</sup> (1/2 Unsweet Tea, 1/2 Lemonade)				</span>
				<p>
					<span>
							
								90&nbsp;Cal&nbsp;per Container
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="UNSWEET_TEA_LEMOMADE">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="UNSWEET_TEA_DIET_LEMONADE"
     data-categorytag="MOBILE_BEVERAGES"
     data-id="308E299B16B4434ABACCF34C7CF8CAE6">
<a href="/menu/sunjoy-w-12-unsweet-tea-12-diet-lemonade" data-layer-list-type="MenuItemCard" aria-label="Sunjoy® (1/2 Unsweet Tea, 1/2 Diet Lemonade)" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="308E299B16B4434ABACCF34C7CF8CAE6" data-layer-list-id="308E299B16B4434ABACCF34C7CF8CAE6" data-layer-list-name="UNSWEET_TEA_DIET_LEMONADE" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Mobile/Beverages/Menu%20Item/Sunjoy_SIMP_1080x1080.png" alt="Sunjoy&#174; (1/2 Unsweet Tea, 1/2 Diet Lemonade)" loading="lazy" />
				</span>
				<span class="item-title">
Sunjoy<sup>®</sup> (1/2 Unsweet Tea, 1/2 Diet Lemonade)				</span>
				<p>
					<span>
							
								20&nbsp;Cal&nbsp;per Container
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="UNSWEET_TEA_DIET_LEMONADE">
					Order now
				</a>
</div>

	</div>
</div>
<div class="menu-items ">
	<div class="flex" style="">
		






<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="ICED_COFFEE"
     data-categorytag="MOBILE_BEVERAGES"
     data-id="1CAC58B2D88C4EC088C579902E8F00A5">
<a href="/menu/iced-coffee" data-layer-list-type="MenuItemCard" aria-label="Iced Coffee" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="1CAC58B2D88C4EC088C579902E8F00A5" data-layer-list-id="1CAC58B2D88C4EC088C579902E8F00A5" data-layer-list-name="ICED_COFFEE" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Drinks/2022IcedCoffee_1080x1080.png" alt="Iced Coffee" loading="lazy" />
				</span>
				<span class="item-title">
Iced Coffee				</span>
				<p>
					<span>
							
								130&nbsp;Cal&nbsp;per Container
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="ICED_COFFEE">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="COCA_COLA"
     data-categorytag="MOBILE_BEVERAGES"
     data-id="9B113277EBDB4C7596AF3CB645437669">
<a href="/menu/coca-cola" data-layer-list-type="MenuItemCard" aria-label="Coca-Cola®" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="9B113277EBDB4C7596AF3CB645437669" data-layer-list-id="9B113277EBDB4C7596AF3CB645437669" data-layer-list-name="COCA_COLA" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/COM/Menu_Refresh/Drinks/Drinks%20PDP/_0000s_0022_Feed_Menu_0000_Drinks_Coca-cola.png" alt="Coca-Cola&#174;" loading="lazy" />
				</span>
				<span class="item-title">
Coca-Cola<sup>®</sup>				</span>
				<p>
					<span>
							
								140&nbsp;Cal&nbsp;per Container
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="COCA_COLA">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="DRPEPPER"
     data-categorytag="MOBILE_BEVERAGES"
     data-id="C1417EF3DC9D4370AB7E4DB807F2D988">
<a href="/menu/dr-pepper" data-layer-list-type="MenuItemCard" aria-label="Dr Pepper®" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="C1417EF3DC9D4370AB7E4DB807F2D988" data-layer-list-id="C1417EF3DC9D4370AB7E4DB807F2D988" data-layer-list-name="DRPEPPER" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Mobile/Beverages/Parent/DrPepper_PaperCup_straight_wet_1200x1200.png" alt="Dr Pepper&#174;" loading="lazy" />
				</span>
				<span class="item-title">
Dr Pepper<sup>®</sup>				</span>
				<p>
					<span>
							
								180&nbsp;Cal&nbsp;per Container
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="DRPEPPER">
					Order now
				</a>
</div>

	</div>
</div>
<div class="menu-items ">
	<div class="flex" style="">
		






<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="BOTTLED_WATER"
     data-categorytag="MOBILE_BEVERAGES"
     data-id="879C865EBB7445A79FD70F20FCBB79A6">
<a href="/menu/dasani-bottled-water" data-layer-list-type="MenuItemCard" aria-label="DASANI® Bottled Water" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="879C865EBB7445A79FD70F20FCBB79A6" data-layer-list-id="879C865EBB7445A79FD70F20FCBB79A6" data-layer-list-name="BOTTLED_WATER" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Mobile/Beverages/Menu%20Item/Dasani_1080x1080.png" alt="DASANI&#174; Bottled Water" loading="lazy" />
				</span>
				<span class="item-title">
DASANI<sup>®</sup> Bottled Water				</span>
				<p>
					<span>
							
								0&nbsp;Cal&nbsp;per Bottle
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="BOTTLED_WATER">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="JUICE_MINUTE_MAID_APPLE"
     data-categorytag="MOBILE_BEVERAGES"
     data-id="55904D288D034A4E83057F7B0673F599">
<a href="/menu/honest-kids-apple-juice" data-layer-list-type="MenuItemCard" aria-label="Honest Kids® Apple Juice" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="55904D288D034A4E83057F7B0673F599" data-layer-list-id="55904D288D034A4E83057F7B0673F599" data-layer-list-name="JUICE_MINUTE_MAID_APPLE" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/COM/Menu_Refresh/Drinks/Drinks%20PDP/_0000s_0017_%5BFeed%5D_appley_620_tiny.png" alt="Honest Kids&#174; Apple Juice" loading="lazy" />
				</span>
				<span class="item-title">
Honest Kids<sup>®</sup> Apple Juice				</span>
				<p>
					<span>
							
								35&nbsp;Cal&nbsp;per Container
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="JUICE_MINUTE_MAID_APPLE">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="JUICE_SIMPLY_ORANGE"
     data-categorytag="MOBILE_BEVERAGES"
     data-id="FB896B6AE42A426E961DA0491B7EDCE1">
<a href="/menu/simply-orange" data-layer-list-type="MenuItemCard" aria-label="Simply Orange®" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="FB896B6AE42A426E961DA0491B7EDCE1" data-layer-list-id="FB896B6AE42A426E961DA0491B7EDCE1" data-layer-list-name="JUICE_SIMPLY_ORANGE" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Drinks/SimplyOJ_Oct19_PDP.png" alt="Simply Orange&#174;" loading="lazy" />
				</span>
				<span class="item-title">
Simply Orange<sup>®</sup>				</span>
				<p>
					<span>
							
								160&nbsp;Cal&nbsp;per Container
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="JUICE_SIMPLY_ORANGE">
					Order now
				</a>
</div>

	</div>
</div>
<div class="menu-items ">
	<div class="flex" style="">
		






<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="MILK_CHOCOLATE_1_PERCENT"
     data-categorytag="MOBILE_BEVERAGES"
     data-id="8B423E25F77B4CEF88212819E89BC6CF">
<a href="/menu/1-chocolate-milk" data-layer-list-type="MenuItemCard" aria-label="1% Chocolate Milk" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="8B423E25F77B4CEF88212819E89BC6CF" data-layer-list-id="8B423E25F77B4CEF88212819E89BC6CF" data-layer-list-name="MILK_CHOCOLATE_1_PERCENT" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Mobile/Kids%20Meals/Parent/220121_Milk_Choc_0009_1080x1080.png" alt="1% Chocolate Milk" loading="lazy" />
				</span>
				<span class="item-title">
1% Chocolate Milk				</span>
				<p>
					<span>
							
								140&nbsp;Cal&nbsp;per Container
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="MILK_CHOCOLATE_1_PERCENT">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="MILK_WHITE_1_PERCENT"
     data-categorytag="MOBILE_BEVERAGES"
     data-id="2EE540B82B5F45819252BE2783FE0DE1">
<a href="/menu/1-white-milk" data-layer-list-type="MenuItemCard" aria-label="1% Milk" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="2EE540B82B5F45819252BE2783FE0DE1" data-layer-list-id="2EE540B82B5F45819252BE2783FE0DE1" data-layer-list-name="MILK_WHITE_1_PERCENT" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Mobile/Kids%20Meals/Parent/220121_Milk_Reg_0009_1080x1080.png" alt="1% Milk" loading="lazy" />
				</span>
				<span class="item-title">
1% Milk				</span>
				<p>
					<span>
							
								90&nbsp;Cal&nbsp;per Container
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="MILK_WHITE_1_PERCENT">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="COFFEE"
     data-categorytag="MOBILE_BEVERAGES"
     data-id="7B216D28C2FD43459E3DCBAF78A5680F">
<a href="/menu/coffee" data-layer-list-type="MenuItemCard" aria-label="Coffee" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="7B216D28C2FD43459E3DCBAF78A5680F" data-layer-list-id="7B216D28C2FD43459E3DCBAF78A5680F" data-layer-list-name="COFFEE" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Drinks/Dec19_Coffee_pdp.png" alt="Coffee" loading="lazy" />
				</span>
				<span class="item-title">
Coffee				</span>
				<p>
					<span>
							
								0&nbsp;Cal&nbsp;per Container
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="COFFEE">
					Order now
				</a>
</div>

	</div>
</div>
<div class="menu-items ">
	<div class="flex" style="">
		






<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="GALLONS"
     data-categorytag="MOBILE_BEVERAGES"
     data-id="A10AF76BFB8B40DD810741811D5F914A">
<a href="/menu/gallon-beverages" data-layer-list-type="MenuItemCard" aria-label="Gallon Beverages" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="A10AF76BFB8B40DD810741811D5F914A" data-layer-list-id="A10AF76BFB8B40DD810741811D5F914A" data-layer-list-name="GALLONS" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Drinks/lemonadeGallon_PDP2.png" alt="Gallon Beverages" loading="lazy" />
				</span>
				<span class="item-title">
Gallon Beverages				</span>
				<p>
					<span>
							
								2090&nbsp;Cal&nbsp;per Gallon
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="GALLONS">
					Order now
				</a>
</div>

	</div>
</div>

	
</div>

<div class="menu-group hidden "
		 data-source="19DEA90F4CD54C779E42A827E7016DA5"
		 data-is-initially-hidden="true">
	<div class="title-container">
<img src="/-/media/images/cfacom/menu-items/ws-menu-feed-images/new-sauces/cfa-sauce_00006.png?h=-1&amp;w=-1&amp;la=en&amp;hash=5048FE1366157481834778FCF01CB15A" class="menu-icon" alt="Menu Item" />		<h2 id="sauces">
			Dipping Sauces and Dressings
		</h2>
	</div>



	<div class="menu-items ">
	<div class="flex" style="">
		






<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="BBQ_ALLACART"
     data-categorytag="SAUCES_SUBMENU|DRESSINGS_SUBMENU"
     data-id="D24CA26AE006484C87002288BE9C9181">
<a href="/menu/barbecue-sauce" data-layer-list-type="MenuItemCard" aria-label="Barbeque Sauce" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="D24CA26AE006484C87002288BE9C9181" data-layer-list-id="D24CA26AE006484C87002288BE9C9181" data-layer-list-name="BBQ_ALLACART" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Modifiers/Sauces/sauces_1ozPDP/Sauce_Barbeque_PDP.png" alt="Barbeque Sauce" loading="lazy" />
				</span>
				<span class="item-title">
Barbeque Sauce				</span>
				<p>
					<span>
							
								45&nbsp;Cal&nbsp;per Container
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="BBQ_ALLACART">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="CFA_SAUCE_ALLACART"
     data-categorytag="SAUCES_SUBMENU|DRESSINGS_SUBMENU"
     data-id="E9D21B07BCA84980AED6618E6A566640">
<a href="/menu/chick-fil-a-sauce" data-layer-list-type="MenuItemCard" aria-label="Chick-fil-A® Sauce" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="E9D21B07BCA84980AED6618E6A566640" data-layer-list-id="E9D21B07BCA84980AED6618E6A566640" data-layer-list-name="CFA_SAUCE_ALLACART" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Modifiers/Sauces/sauces_1ozPDP/Sauce_CFA-Sauce_PDP.png" alt="Chick-fil-A&#174; Sauce" loading="lazy" />
				</span>
				<span class="item-title">
Chick-fil-A<sup>®</sup> Sauce				</span>
				<p>
					<span>
							
								140&nbsp;Cal&nbsp;per Container
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="CFA_SAUCE_ALLACART">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="RANCH_ALLACART"
     data-categorytag="SAUCES_SUBMENU|DRESSINGS_SUBMENU"
     data-id="4A1D2BC64C67455EB66653E748C57F16">
<a href="/menu/garden-herb-ranch-sauce" data-layer-list-type="MenuItemCard" aria-label="Garden Herb Ranch Sauce" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="4A1D2BC64C67455EB66653E748C57F16" data-layer-list-id="4A1D2BC64C67455EB66653E748C57F16" data-layer-list-name="RANCH_ALLACART" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Modifiers/Sauces/sauces_1ozPDP/Sauce_Garden-Herb-Ranch_PDP.png" alt="Garden Herb Ranch Sauce" loading="lazy" />
				</span>
				<span class="item-title">
Garden Herb Ranch Sauce				</span>
				<p>
					<span>
							
								140&nbsp;Cal&nbsp;per Container
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="RANCH_ALLACART">
					Order now
				</a>
</div>

	</div>
</div>
<div class="menu-items ">
	<div class="flex" style="">
		






<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="HONEY_MUS_ALLACART"
     data-categorytag="SAUCES_SUBMENU|DRESSINGS_SUBMENU"
     data-id="B14B3C8D9AFB491D800483A3C2517FCE">
<a href="/menu/honey-mustard-sauce" data-layer-list-type="MenuItemCard" aria-label="Honey Mustard Sauce" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="B14B3C8D9AFB491D800483A3C2517FCE" data-layer-list-id="B14B3C8D9AFB491D800483A3C2517FCE" data-layer-list-name="HONEY_MUS_ALLACART" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Modifiers/Sauces/sauces_1ozPDP/Sauce_Honey-Mustard_PDP.png" alt="Honey Mustard Sauce" loading="lazy" />
				</span>
				<span class="item-title">
Honey Mustard Sauce				</span>
				<p>
					<span>
							
								50&nbsp;Cal&nbsp;per Container
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="HONEY_MUS_ALLACART">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="POLYNESIAN_ALLACART"
     data-categorytag="SAUCES_SUBMENU|DRESSINGS_SUBMENU"
     data-id="669930A085D746918AF3C5F96FDC92EA">
<a href="/menu/polynesian-sauce" data-layer-list-type="MenuItemCard" aria-label="Polynesian Sauce" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="669930A085D746918AF3C5F96FDC92EA" data-layer-list-id="669930A085D746918AF3C5F96FDC92EA" data-layer-list-name="POLYNESIAN_ALLACART" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Modifiers/Sauces/sauces_1ozPDP/Sauce_Polynesian_PDP.png" alt="Polynesian Sauce" loading="lazy" />
				</span>
				<span class="item-title">
Polynesian Sauce				</span>
				<p>
					<span>
							
								110&nbsp;Cal&nbsp;per Container
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="POLYNESIAN_ALLACART">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="SRIRACHA_ALLACART"
     data-categorytag="SAUCES_SUBMENU|DRESSINGS_SUBMENU"
     data-id="D68BC1EBB1B14E29932E1E84BC012A9C">
<a href="/menu/sweet-and-spicy-sriracha-sauce" data-layer-list-type="MenuItemCard" aria-label="Sweet and Spicy Sriracha Sauce" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="D68BC1EBB1B14E29932E1E84BC012A9C" data-layer-list-id="D68BC1EBB1B14E29932E1E84BC012A9C" data-layer-list-name="SRIRACHA_ALLACART" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Modifiers/Sauces/sauces_1ozPDP/Sauce_Sweet-and-Spicy-Sriracha_PDP.png" alt="Sweet and Spicy Sriracha Sauce" loading="lazy" />
				</span>
				<span class="item-title">
Sweet and Spicy Sriracha Sauce				</span>
				<p>
					<span>
							
								45&nbsp;Cal&nbsp;per Container
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="SRIRACHA_ALLACART">
					Order now
				</a>
</div>

	</div>
</div>
<div class="menu-items ">
	<div class="flex" style="">
		






<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="BUFFALO_ALLACART"
     data-categorytag="SAUCES_SUBMENU|DRESSINGS_SUBMENU"
     data-id="418E4664572643C383C6E31A08B304B2">
<a href="/menu/zesty-buffalo-sauce" data-layer-list-type="MenuItemCard" aria-label="Zesty Buffalo Sauce" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="418E4664572643C383C6E31A08B304B2" data-layer-list-id="418E4664572643C383C6E31A08B304B2" data-layer-list-name="BUFFALO_ALLACART" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Modifiers/Sauces/sauces_1ozPDP/PDP_1oz-Sauce_Buffalo.png" alt="Zesty Buffalo Sauce" loading="lazy" />
				</span>
				<span class="item-title">
Zesty Buffalo Sauce				</span>
				<p>
					<span>
							
								25&nbsp;Cal&nbsp;per Container
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="BUFFALO_ALLACART">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="HONEY_BBQ_ALLACART"
     data-categorytag="SAUCES_SUBMENU|DRESSINGS_SUBMENU"
     data-id="B43D49B45A2047D3AD196575FF742E52">
<a href="/menu/honey-roasted-bbq-sauce" data-layer-list-type="MenuItemCard" aria-label="Honey Roasted BBQ Sauce" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="B43D49B45A2047D3AD196575FF742E52" data-layer-list-id="B43D49B45A2047D3AD196575FF742E52" data-layer-list-name="HONEY_BBQ_ALLACART" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Modifiers/Condiments_full-res_Honey-Roasted-BBQ_PDP.png" alt="Honey Roasted BBQ Sauce" loading="lazy" />
				</span>
				<span class="item-title">
Honey Roasted BBQ Sauce				</span>
				<p>
					<span>
							
								60&nbsp;Cal&nbsp;per Packet
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="HONEY_BBQ_ALLACART">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="AVACADO_RAN_ALLACART"
     data-categorytag="SAUCES_SUBMENU|DRESSINGS_SUBMENU"
     data-id="E1EFBE19487E4380A5352EFEF65F405D">
<a href="/menu/avocado-lime-ranch-dressing" data-layer-list-type="MenuItemCard" aria-label="Avocado Lime Ranch Dressing" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="E1EFBE19487E4380A5352EFEF65F405D" data-layer-list-id="E1EFBE19487E4380A5352EFEF65F405D" data-layer-list-name="AVACADO_RAN_ALLACART" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Modifiers/Dressing/2ozPDP/2oz-Dressing_full-res_Avocado-Lime-Ranch_PDP.png" alt="Avocado Lime Ranch Dressing" loading="lazy" />
				</span>
				<span class="item-title">
Avocado Lime Ranch Dressing				</span>
				<p>
					<span>
							
								310&nbsp;Cal&nbsp;per Packet
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="AVACADO_RAN_ALLACART">
					Order now
				</a>
</div>

	</div>
</div>
<div class="menu-items ">
	<div class="flex" style="">
		






<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="CREAMY_SALSA_ALLACART"
     data-categorytag="SAUCES_SUBMENU|DRESSINGS_SUBMENU"
     data-id="F2B5F52E3CAF40ED95EEE59D363ADA7E">
<a href="/menu/creamy-salsa-dressing" data-layer-list-type="MenuItemCard" aria-label="Creamy Salsa Dressing" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="F2B5F52E3CAF40ED95EEE59D363ADA7E" data-layer-list-id="F2B5F52E3CAF40ED95EEE59D363ADA7E" data-layer-list-name="CREAMY_SALSA_ALLACART" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Modifiers/Dressing/2ozPDP/2oz-Dressing_full-res_Creamy-Salsa_PDP.png" alt="Creamy Salsa Dressing" loading="lazy" />
				</span>
				<span class="item-title">
Creamy Salsa Dressing				</span>
				<p>
					<span>
							
								290&nbsp;Cal&nbsp;per Packet
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="CREAMY_SALSA_ALLACART">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="HONEY_MUST_ALLACART"
     data-categorytag="SAUCES_SUBMENU|DRESSINGS_SUBMENU"
     data-id="C533E4987C8A480FBCC4F45A80F49BAF">
<a href="/menu/fat-free-honey-mustard-dressing" data-layer-list-type="MenuItemCard" aria-label="Fat Free Honey Mustard Dressing" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="C533E4987C8A480FBCC4F45A80F49BAF" data-layer-list-id="C533E4987C8A480FBCC4F45A80F49BAF" data-layer-list-name="HONEY_MUST_ALLACART" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Modifiers/Dressing/2ozPDP/2oz-Dressing_full-res_Fat-Free-Honey-Mustard_PDP.png" alt="Fat Free Honey Mustard Dressing" loading="lazy" />
				</span>
				<span class="item-title">
Fat Free Honey Mustard Dressing				</span>
				<p>
					<span>
							
								90&nbsp;Cal&nbsp;per Packet
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="HONEY_MUST_ALLACART">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="GARLIC_HERB_ALLACART"
     data-categorytag="SAUCES_SUBMENU|DRESSINGS_SUBMENU"
     data-id="83544C2472A040C9B94186ED592B0E7D">
<a href="/menu/garden-herb-ranch-dressing-1" data-layer-list-type="MenuItemCard" aria-label="Garden Herb Ranch Dressing" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="83544C2472A040C9B94186ED592B0E7D" data-layer-list-id="83544C2472A040C9B94186ED592B0E7D" data-layer-list-name="GARLIC_HERB_ALLACART" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Modifiers/Dressing/2ozPDP/2oz-Dressing_full-res_Garden-Herb-Ranch_PDP.png" alt="Garden Herb Ranch Dressing" loading="lazy" />
				</span>
				<span class="item-title">
Garden Herb Ranch Dressing				</span>
				<p>
					<span>
							
								280&nbsp;Cal&nbsp;per Packet
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="GARLIC_HERB_ALLACART">
					Order now
				</a>
</div>

	</div>
</div>
<div class="menu-items ">
	<div class="flex" style="">
		






<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="LITE_BALSAM_ALLACART"
     data-categorytag="SAUCES_SUBMENU|DRESSINGS_SUBMENU"
     data-id="4DBAF3B46A8F41BA8F8FEE2E0F97BB9C">
<a href="/menu/light-balsamic-vinaigrette-dressing" data-layer-list-type="MenuItemCard" aria-label="Light Balsamic Vinaigrette Dressing" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="4DBAF3B46A8F41BA8F8FEE2E0F97BB9C" data-layer-list-id="4DBAF3B46A8F41BA8F8FEE2E0F97BB9C" data-layer-list-name="LITE_BALSAM_ALLACART" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Modifiers/Dressing/2ozPDP/2oz-Dressing_full-res_Light-Balsamic-Vinaigrette_PDP.png" alt="Light Balsamic Vinaigrette Dressing" loading="lazy" />
				</span>
				<span class="item-title">
Light Balsamic Vinaigrette Dressing				</span>
				<p>
					<span>
							
								80&nbsp;Cal&nbsp;per Packet
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="LITE_BALSAM_ALLACART">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="ITALIAN_LITE_ALLACART"
     data-categorytag="SAUCES_SUBMENU|DRESSINGS_SUBMENU"
     data-id="67E3DFF9C12A460CB07057100C322D36">
<a href="/menu/light-italian-dressing" data-layer-list-type="MenuItemCard" aria-label="Light Italian Dressing" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="67E3DFF9C12A460CB07057100C322D36" data-layer-list-id="67E3DFF9C12A460CB07057100C322D36" data-layer-list-name="ITALIAN_LITE_ALLACART" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Modifiers/Dressing/2ozPDP/2oz-Dressing_full-res_Light-Italian_PDP.png" alt="Light Italian Dressing" loading="lazy" />
				</span>
				<span class="item-title">
Light Italian Dressing				</span>
				<p>
					<span>
							
								25&nbsp;Cal&nbsp;per Packet
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="ITALIAN_LITE_ALLACART">
					Order now
				</a>
</div>







<div class="location-menu-card item"
     data-component="locationMenuCard"
     data-tag="VIN_APPLE_ALLACART"
     data-categorytag="SAUCES_SUBMENU|DRESSINGS_SUBMENU"
     data-id="3B384A9C5F3947FFA6C807F9CB2E6288">
<a href="/menu/zesty-apple-cider-vinaigrette-dressing" data-layer-list-type="MenuItemCard" aria-label="Zesty Apple Cider Vinaigrette Dressing" data-layer-protocol="https" data-element="menuItemLink" data-component="clickData" data-layer-category="MenuCategory" data-layer-id="3B384A9C5F3947FFA6C807F9CB2E6288" data-layer-list-id="3B384A9C5F3947FFA6C807F9CB2E6288" data-layer-list-name="VIN_APPLE_ALLACART" >			<div class="item-details">
				<span class="product food">
						<img src="https://www.cfacdn.com/img/order/menu/Online/Modifiers/Dressing/2ozPDP/2oz-Dressing_full-res_Zesty-Apple-Cider_PDP.png" alt="Zesty Apple Cider Vinaigrette Dressing" loading="lazy" />
				</span>
				<span class="item-title">
Zesty Apple Cider Vinaigrette Dressing				</span>
				<p>
					<span>
							
								230&nbsp;Cal&nbsp;per Packet
							
					</span>
				</p>
			</div>
</a>				<a class="btn-round btn-round--red lb-modal"
				   aria-label="Order now"
				   data-element="modalCta"
				   data-location-number=""
				   data-item-tag="VIN_APPLE_ALLACART">
					Order now
				</a>
</div>

	</div>
</div>

	
</div>

</div>

<div id="operator-sites-sign-in-modal"
		 class="base-modal operator-sites-sign-in-modal operator-sites-modal mfp-hide "
		 role="dialog"
		 tabindex="0">
<form action="/identity/externallogin?authenticationType=Crn&amp;ReturnUrl=%2fidentity%2fexternallogincallback%3fReturnUrl%3d%252fmenu%26sc_site%3dCFACOM%26authenticationSource%3dDefault&amp;sc_site=CFACOM&amp;signup_redirect_uri=%2fmenu" class="inner" method="post">		<button aria-label="Close" class="mfp-close" type="button"></button>
		<h4>
			Sign in with Chick-fil-A One™ to favorite this location
		</h4>
<p>Earn points, redeem rewards and reach new tiers with increasing benefits. Access your order history to make quick reorders and edits to existing orders.</p>		<button id="favorite-restaurant"
						class="btn-round btn-round--red"
						type="submit"
						aria-label="Sign in with Chick-fil-A One™">
			Sign in with Chick-fil-A One™
		</button>
</form></div>

<div id="location-order-now-modal" class="location-order-now-modal mfp-hide " tabindex="0">
	<button class="mfp-close"></button>
	<div class="content">
		<div class="header">
			<h3>
				What type of order can we get started for you?
			</h3>
			<p>Order ahead for pickup or let us deliver to your location</p>
		</div>
		<a data-element="pickupBtn"
			 href=""
			 class="pickup-btn"
			 data-layer-event="conversion_pickupBtn_click"
			 data-redirect-url="https://order.chick-fil-a.com/load-dot-com">
			<img src="/-/media/images/cfacom/pdps/pickup-stand-alone.svg?la=en&amp;hash=CC253BD91969B2BEF0DF6E3DF9D328E3" loading="lazy" alt="Order Pickup" />
			<p>Order Pickup</p>
		</a>

			<a data-element="deliveryBtn"
				 href=""
				 class="delivery-btn"
				 data-layer-event="conversion_deliveryBtn_click"
				 data-redirect-url="https://order.chick-fil-a.com/delivery/address">
				<img src="/-/media/images/cfacom/pdps/delivery-van.svg?la=en&amp;hash=6AEBCE5E2C2CBD8F24F78AC7C32200C5" loading="lazy" alt="van" />
				<p>Order Delivery</p>
			</a>
	</div>
</div>
	
	<div class="footer">
		<footer>





<div class="cfa-one-footer grid-layout  " data-source="BA98D497B43747BAAEEE1761F7201323">
	<div class="img-container">
<img src="https://d1fd34dzzl09j.cloudfront.net/Images/CFACOM/Home%20Page%20Refresh/Home%20Page%20Refresh%20V2/March%202024%20update/CFA_one_footer_mobile.jpeg?h=296&amp;w=574&amp;la=en" loading="lazy" class="mobile-img" alt="" />
		<img src="https://d1fd34dzzl09j.cloudfront.net/Images/CFACOM/Home%20Page%20Refresh/Home%20Page%20Refresh%20V2/March%202024%20update/CFA_one_footer_desktop.jpg?h=637&amp;w=692&amp;la=en" loading="lazy" class="desktop-img" alt="" />
	</div>
	<div class="background-img mobile-img"
	     style="background-image: url(https://d1fd34dzzl09j.cloudfront.net/Images/CFACOM/Home%20Page%20Refresh/Home%20Page%20Refresh%20V2/March%202024%20update/CFA_one_footer_mobile.jpeg);
	            background-size: cover;
	            background-position: center center;">
	</div>
	<div class="background-img desktop-img"
	     style="background-image: url(https://d1fd34dzzl09j.cloudfront.net/Images/CFACOM/Home%20Page%20Refresh/Home%20Page%20Refresh%20V2/March%202024%20update/CFA_one_footer_desktop.jpg);
	            background-size: cover;
	            background-position: center center;">
	</div>
	<div class="content" >
		<div class="icon-container">
			<img src="https://d1fd34dzzl09j.cloudfront.net/Images/CFACOM/PLP%20updates/Fall%202023%20PLPs/CFA%20App.png?h=35&amp;w=21&amp;la=en" loading="lazy" alt="" />
			<p>Make your meals more rewarding</p>
		</div>
		<div class="title">
			<h2>
			Sign up for Chick-fil-A One<sup>®</sup>
			</h2>
			<p><style>
    .lrg-app-banner { display: none; }
    .cfa-one.logged-out.vis-white { background: white; }
</style>
Receive points with every qualifying purchase. Redeem for available rewards of your choice.&nbsp;<a href="https://www.chick-fil-a.com/one">Learn more about our loyalty program</a>.
<div class="  ">
<a href="https://itunes.apple.com/us/app/chick-fil-a/id488818252" class="apple cfa-one-app-goal" rel="noopener noreferrer" target="_blank">Download on the App Store</a>
<a href="https://play.google.com/store/apps/details?id=com.chickfila.cfaflagship" class="google cfa-one-app-goal" rel="noopener noreferrer" target="_blank">Get it on Google Play</a>
</div></p>
		</div>

	</div>
</div>

			
			<div class="footer-modules wrapper">
				<nav class="footer-nav" aria-label="footer">
						<ul aria-label="">

        <li>
<a href="/nutrition-allergens" data-layer-list-type="LinkList" data-component="contentLink" data-layer-content-type="LinkList" title="Click here to view Chick-fil-A&#39;s Nutrition and Allergens information" data-layer-name="Footer Menu" data-layer-index="1" data-layer-identifier="9E75ADB167294B9587607FD08785A576" >Nutrition &amp; Allergens</a>        </li>
        <li>
<a href="/customer-support" data-layer-list-type="LinkList" data-component="contentLink" data-layer-content-type="LinkList" data-layer-name="Footer Menu" data-layer-index="2" data-layer-identifier="9E75ADB167294B9587607FD08785A576" >Customer Support</a>        </li>
        <li>
<a href="/legal" data-layer-list-type="LinkList" data-component="contentLink" data-layer-content-type="LinkList" data-layer-name="Footer Menu" data-layer-index="3" data-layer-identifier="9E75ADB167294B9587607FD08785A576" >Legal</a>        </li>
        <li>
<a href="/franchising" data-layer-list-type="LinkList" data-component="contentLink" data-layer-content-type="LinkList" data-layer-name="Footer Menu" data-layer-index="4" data-layer-identifier="9E75ADB167294B9587607FD08785A576" >Franchising</a>        </li>
        <li>
<a href="https://shop.chick-fil-a.com/" data-layer-list-type="LinkList" data-component="contentLink" data-layer-content-type="LinkList" data-layer-name="Footer Menu" data-layer-index="5" data-layer-identifier="9E75ADB167294B9587607FD08785A576" >Merchandise</a>        </li>
        <li>
<a href="/press-room" data-layer-list-type="LinkList" data-component="contentLink" data-layer-content-type="LinkList" data-layer-name="Footer Menu" data-layer-index="6" data-layer-identifier="9E75ADB167294B9587607FD08785A576" >Press Room</a>        </li>


			<li>
				<ul>

        <li>
<a href="/do-business-with-us" data-layer-list-type="LinkList" data-component="contentLink" data-layer-content-type="LinkList" data-layer-name="Footer Menu secondary" data-layer-index="1" data-layer-identifier="9E75ADB167294B9587607FD08785A576" >Do business with us</a>        </li>
        <li>
<a href="/legal/terms-conditions" data-layer-list-type="LinkList" data-component="contentLink" data-layer-content-type="LinkList" data-layer-name="Footer Menu secondary" data-layer-index="2" data-layer-identifier="9E75ADB167294B9587607FD08785A576" >Terms and Conditions of Use</a>        </li>
        <li>
<a href="/legal/privacy/chick-fil-a-privacy-policy" data-layer-list-type="LinkList" data-component="contentLink" data-layer-content-type="LinkList" data-layer-name="Footer Menu secondary" data-layer-index="3" data-layer-identifier="9E75ADB167294B9587607FD08785A576" >Privacy Policy</a>        </li>
        <li>
<a href="/legal/privacy/california-privacy-policy" data-layer-list-type="LinkList" data-component="contentLink" data-layer-content-type="LinkList" data-layer-name="Footer Menu secondary" data-layer-index="4" data-layer-identifier="9E75ADB167294B9587607FD08785A576" >California Privacy Notice</a>        </li>
        <li>
<a href="/legal/privacy/cookie-interest-based-advertising-policy" data-layer-list-type="LinkList" data-component="contentLink" data-layer-content-type="LinkList" data-layer-name="Footer Menu secondary" data-layer-index="5" data-layer-identifier="9E75ADB167294B9587607FD08785A576" >Cookie and Internet-Based Advertising Policy</a>        </li>
        <li>
<a href="#ot-sdk-show-settings" data-layer-list-type="LinkList" data-component="contentLink" data-layer-content-type="LinkList" title="Do Not Sell Or Share My Personal Information" data-layer-name="Footer Menu secondary" class="optanon-toggle-display" data-layer-index="6" data-layer-identifier="9E75ADB167294B9587607FD08785A576" >Do Not Sell Or Share My Personal Information</a>        </li>
        <li>
<a href="javascript:onclick=&quot;try{ah.optOut()}catch(e){}" data-layer-list-type="LinkList" data-component="contentLink" data-layer-content-type="LinkList" title="Cookie Preference Center" data-layer-name="Footer Menu secondary" class="optanon-toggle-display" data-layer-index="7" data-layer-identifier="9E75ADB167294B9587607FD08785A576" >Cookie Preference Center</a>        </li>
        <li>
<a href="/legal/accessibility" data-layer-list-type="LinkList" data-component="contentLink" data-layer-content-type="LinkList" data-layer-name="Footer Menu secondary" data-layer-index="8" data-layer-identifier="9E75ADB167294B9587607FD08785A576" >Accessibility</a>        </li>
        <li>
<a href="/locations/browse" data-layer-list-type="LinkList" data-component="contentLink" data-layer-content-type="LinkList" data-layer-name="Footer Menu secondary" data-layer-index="9" data-layer-identifier="9E75ADB167294B9587607FD08785A576" >Locations listing</a>        </li>
        <li>
<a href="/careers" data-layer-list-type="LinkList" data-component="contentLink" data-layer-content-type="LinkList" data-layer-name="Footer Menu secondary" data-layer-index="10" data-layer-identifier="9E75ADB167294B9587607FD08785A576" >Careers</a>        </li>
        <li>
<a href="/legal/supply-chain" data-layer-list-type="LinkList" data-component="contentLink" data-layer-content-type="LinkList" data-layer-name="Footer Menu secondary" data-layer-index="11" data-layer-identifier="9E75ADB167294B9587607FD08785A576" >Supply Chain</a>        </li>
        <li>
&#169; 2024 CFA Properties, Inc. All rights reserved.        </li>

				</ul>
			</li>
	</ul>



				</nav><!-- /footer-nav -->
				<div class="social">
						<ul class="social-icons" aria-label="">

        <li>
<a href="https://www.facebook.com/ChickfilA/" data-layer-list-type="LinkList" target="_blank" data-component="contentLink" data-layer-content-type="LinkList" data-layer-name="Social Menu" class="icon-facebook-over" rel="noopener noreferrer" data-layer-index="1" data-layer-identifier="6D9735F1CC27465A85120B0BEF1C976F" >                        <span>Facebook</span>
</a>        </li>
        <li>
<a href="https://www.instagram.com/chickfila/" data-layer-list-type="LinkList" target="_blank" data-component="contentLink" data-layer-content-type="LinkList" data-layer-name="Social Menu" class="icon-instagram-over" rel="noopener noreferrer" data-layer-index="2" data-layer-identifier="6D9735F1CC27465A85120B0BEF1C976F" >                        <span>Instagram</span>
</a>        </li>
        <li>
<a href="https://www.youtube.com/user/chickfila" data-layer-list-type="LinkList" target="_blank" data-component="contentLink" data-layer-content-type="LinkList" data-layer-name="Social Menu" class="icon-youtube-over" rel="noopener noreferrer" data-layer-index="3" data-layer-identifier="6D9735F1CC27465A85120B0BEF1C976F" >                        <span>YouTube</span>
</a>        </li>


	</ul>



				</div><!-- /social-->
			</div><!-- /footer-modules -->
		</footer>
	</div>


</div>

	</div>
	<!-- /Page content -->


<div class="print-footer">
    <div class="icon-logo-desktop"></div>
    
</div><!-- /print-footer -->

<script
	src="https://code.jquery.com/jquery-3.4.1.min.js"
	integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo="
	crossorigin="anonymous"></script>

<script>
	window.jQuery || document.write('<script src="https://d2wl1kt18tqdum.cloudfront.net/v2.1.880-stageb/Assets/Theming/js/lib/jquery.js"><\/script>');
</script>

<script src="https://d2wl1kt18tqdum.cloudfront.net/v2.1.880-stageb/Assets/Theming/js/vendor-js.js"></script>
<script src="https://d2wl1kt18tqdum.cloudfront.net/v2.1.880-stageb/Assets/Theming/js/CFACom.js"></script>
<script src="https://d2wl1kt18tqdum.cloudfront.net/v2.1.880-stageb/Assets/Theming/js/menu-js.js"></script>


	

	

	<div id="defaultsiteoverlay" class="lightbox mfp-hide"></div>

	


	

	<span data-component="scrollMilestone"></span>
</body>
</html>
"""

# Check if the request was successful
#if response.status_code == 200:
  # Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all product elements (replace with the appropriate class or tag for products on the target website)
#product_elements = soup.find_all('div', class_='location-menu-card item')  
product_elements = soup.find_all('div', class_='location-menu-card item')
num_products = len(product_elements)
print(f"Number of products: {num_products}")

# Extract product data
for product in product_elements:
# Find the element containing the product name (replace with the appropriate tag or class)

#span_element = product.find('span', class_='item-title').text.strip()
    span_element = product.find('span', class_='item-title')

    if span_element:
        sandwich_name = span_element.text.strip()
        print(f"Sandwich Name: {sandwich_name}")
    else:
        print("Span element with class 'item-title' not found.")

    span_calorie = product.find('span', text=lambda text: text and "Cal" in text)

    if span_calorie:
        calorie = span_calorie.text.strip()
        print(f"Calories: {calorie}")
    else:
        print("Span element with class 'item-title' not found.")

    # Find the element containing the product price (replace with the appropriate tag or class)
    #span_element = product.find('span', class_='prc-food-new')

    #if span_element:
    #    value = span_element.text.strip()
    #else:
    #    print("Span element not found.\n")

    # Print the extracted data

    #print("-" * 30)  # Optional separator between products
