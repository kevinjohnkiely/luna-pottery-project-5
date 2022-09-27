# Luna Pottery - Project 5

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/lunapottery.jpg">

Live link to Application: (https://luna-pottery.herokuapp.com/)

Luna Pottery is an e-commerce online store application built with Django and Python. It allows users to create their own accounts, and experience a full online shopping experience whereby they can purchase items of ceramics and pottery. The application is intended as a template for all small-to-medium arts and crafts people to use to drive sales of their products and to better market their output using a modern, functional web storefront. The application also provides customer engagement by allowing the user to rate or review the products they have purchased.

# UX (User Experience)

## Target Audience
The target audience for this application are lovers of arts and crafts, in particular people who love ceramics and pottery. This target persona will also engage with the application by providing feedback on the ceramic products on offer. This audience may also include those who wish to learn how to create their own pottery by way of the pottery classes that can be booked using the web storefront. These requirements informed the UX strategy for the application, thus needing to display the 2 options of either buying pottery or taking classes clearly on the homepage. This is seen in both the wireframes and final design of the app, with respect to the landing/home page of the site.

## User Stories
There are 2 classifications of user that can use this site, the Customer and the Administrator. The Customer can carry out all expected tasks of a modern web storefront such as purchashing, adding items to cart, reviewing items and placing them on a wishlist. The Administrator is concerned with adding the store products to the store, with all the required details and data. The Admin may also edit or delete the products. The user stories for both user classes are as follows:

### User Stories for Admin User

+ [[#18](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/18)] Add A Product: The Admin user can use the front end form to add a new product with all relevant product details.
+ [[#19](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/19)] Edit A Product: The Admin user can navigate to the individual product page [[#2](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/2)], and click on the Edit button to be directed to a form page where updating can be completed
+ [[#20](https://github.com/kevinjohnkiely/luna-pottery-project-5/issues/20)] Delete A Product: The Admin user can follow same path as previous user story, and choose to click the Delete button. A modal popup appears to confirm that the deletion of the product will take place.

## Wireframes
The following images show wireframes of the 2 primary designs of the application. These wireframes were created using Balsamiq Wireframes.

### Wireframe of Home Page of Application
This wireframe details the homepage of the site, showing the layout of a welcoming slideshow image of some pottery products, some welcome information text, and a couple of call-to-action panels allowing the customer to either view the products or book a pottery class.

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/Homepage.png">

### Wireframe of the Product List Page
This wireframe shows how the list of products will appear, with various utilities to sort the display of products in specific orders.

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/Products.png">

### Wireframe of the Product Detail Page
This wireframe shows how an individual product page will look after selecting from previous list.

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/IndividualProduct.png">

<hr>

# System Design
Once the system requirements from the Site Users perspective was finalized, a design of information flow was completed to demonstrate how the required data models were needed for the backend of this application. The following entity relationship (ER) diagram displays the relationship between the various data models.

<img src="https://github.com/kevinjohnkiely/luna-pottery-project-5/blob/main/screenshotsWireframes/LunaPotteryERDiagram.png">