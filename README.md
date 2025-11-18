# DJANGO MART

This is an e-commerce website built using Django that allows users to browse products, add items to a shopping cart, place orders, and manage their account. The website also provides an admin interface for managing products, orders, and users.

## Features
- User Authentication: Users can sign up, log in, and manage their accounts.
    - sign_up: Users can sign up using email verification.
       ![fill up register page](r_images/account/profile/how_to_create_registerpage.PNG)

       ![after sending a registration request](r_images/account/profile/how_regester_request..PNG)

       ![example of token](r_images/account/profile/email_interfaze_for_register_request.PNG)
    
       ![after click token](r_images/account/profile/after_click_in_email_verification_code.PNG)
       
    - login: Users can login using register email and password
       ![login interface](r_images/account/profile/sing_in_page.PNG)

       ![login interface](r_images/account/profile/login.PNG)

    - forget password: If Users forget the password he/she change the password 
       ![forgot pass interface](r_images/account/profile/forgot_pass.PNG)


- Users profile management: Users can change their profile picture, change their address , update their personal information etc.
    - Profile for unregister User:
       ![alt text](r_images/account/profile/un_reg_profile.PNG)
       ![alt text](r_images/account/profile/un_reg_profile2.PNG)
    
    -Profile for register User:
        ![profile interface 1](<r_images/account/profile management/profile_management_for_valid_user.PNG>)
        ![profile interface 2](<r_images/account/profile management/profile_management_for_valid_user1.PNG>)
        ![profile interface 3](<r_images/account/profile management/profile_management_for_valid_user2.PNG>)
        ![update personal information](<r_images/account/profile management/update_personal_info.PNG>)
        ![update user address](<r_images/account/profile management/update_user_address.PNG>)

- Users Dashboard feature: Dashboard feature is only for register user.
  In Users dashboard severall functionality have exists such as:
    - Dashboard front page:
        ![dashboard front page](<r_images/account/dashboard/dashboard front.PNG>)

    - All product category:
        ![all product category feature](r_images/account/dashboard/all_category_or_selling_item.PNG)

    - make a prerequested order:
        ![prerequested order feature](r_images/account/dashboard/make_bulk_order.PNG)

    - recent Order feature:
         ![recent order functionality](r_images/account/dashboard/recent_order.PNG)

    - Seals statistics and report:
         ![seals statistics fucntionality](r_images/account/dashboard/seals_statics_and_report.PNG)

    - Top selling product:
         ![top selling product functionality](r_images/account/dashboard/top_selling_product.PNG)
         
    - all transactions features:
        ![all transactions features ](r_images/account/dashboard/transection.PNG)
    
- Shopping Cart: Users can add products to their shopping cart, update quantities, and remove items.
    - add to cart feature:
        ![add to cart functionality](<r_images/cart/add to cart/add_to_cart.PNG>)
    - increase and decrease feature:
        ![increase ](r_images/cart/increaseAndDecrease/increase.PNG)
        ![decrease](r_images/cart/increaseAndDecrease/decrease.PNG)
    - remove cart feature:
        ![remove cart item](<r_images/cart/remove from cart/Capture.PNG>)

- Order Management: Users can view their order history and track their current orders.
    - Order history:
      ![order history](r_images/order/order_history.PNG)

    - recent order:
      ![recent order](r_images/order/recent_order.PNG)
    
    - place order:
      ![place order function](r_images/order/place_order.PNG)

- Product Catalog: Users can browse products by categories, view product details, and search for products.
    - home page or store:
      ![alt text](r_images/product_catalog/Capture1.PNG)
    - store for un-register user:
      ![unregister user](r_images/product_catalog/store_for_unreg_user.PNG)

    - store for register user:
      ![store for register user](r_images/product_catalog/store_page_for_valid_user.PNG)

    - product detail for un-register user:
      ![detail for un-register user](r_images/product_catalog/product_detail_for_unreg_user.PNG)
    
    - product detail for register user:
      ![detail for register user](r_images/product_catalog/product_details_for_valid_user.PNG)

    - out of stock feature:
      ![out of stock](r_images/product_catalog/out_of_feature.PNG)

- Search and filtering feature: Users can view their product using Search and filtering feature:
    - search by keyword:
      ![search by keyword](r_images/search/search_by_keyword.PNG)

    - search by category:
      ![search by category](r_images/search/search_by_category.PNG) 
      ![search by category](r_images/search/search_by_category2.PNG) 

- pagination feature: Users can view their product using pagination feature:
    
    - overall pagination:
      ![overall pagination first page](<r_images/pagination/overall pagination.PNG>)
      ![overall pagination page2](<r_images/pagination/overall pagination2.PNG>)

    - category based pagination:
      ![category based pagination](r_images/pagination/pagenation_for_unreg_user_with_category_filtering.PNG)
      ![category based pagination ](r_images/pagination/pagenation_for_unreg_user_with_category_filtering2.PNG)

- Wish list feature: Users can add their product to wish list and purchase this product easily using this feature:
      - add to wish list:
        ![add to wish list](r_images/product_catalog/wish_list_product.PNG) 

- comment and review feature: Users can make their comment and give review using comment and review feature feature:
    - ![comment first part](r_images/commentAndReview/comment1.PNG)
    - ![comment second part](r_images/commentAndReview/comment2.PNG)


- Payment Integration: Integration with a payment gateway (e.g., sslcommerz) for handling online fake - - - payments.
    - pre step for make a paymet:
      ![pre step ](r_images/order/place_order.PNG)

    - make a fake payment:
      ![fake payment](r_images/payment/fake_payment_and_getway_implementation.PNG)
    
    - confirm a fake payment:
       ![confirm a fake payment](r_images/payment/action_for_payment_and_getway.PNG)
    
    - transaction report after a payment:
       ![transaction report](r_images/payment/success_payment_and_getway.PNG)


- Responsive Design: Optimized for desktops, tablets.


## Upcoming Features

- *Weather Alerts:* Receive weather alerts for severe conditions.
- *Widget Support:* Add weather information directly to your home screen.
- *Localization:* Support for multiple languages.
- *Dark Mode:* Supports system-wide dark theme.
- *Current Weather:* Displays real-time weather data, including temperature, humidity, wind speed, and more.
- *Hourly Forecast:* Provides weather forecast for the upcoming hours.
- *Multiple Locations:* Track weather for different locations by entering a city.
- *User-friendly Interface:* Simple and intuitive UI for a seamless user experience.
- *Offline support:* Store weather data for up to 24 hours for offline access for searched city.

## Limitations

- some simple dug has present.
- some spelling mistake has present.
- comparatively lower UI desing.
