# Leaf Skateshop

### For rollerbladers, by rollerbladers. The Leaf Skateshop is the newest and fastest growing skateshop in the UK.

---

As a developer, I've been tasked with creating an ecommerce site for a skateshop.

This project has been made using Django / Python, HTML, CSS and JavaScript.

~~[Here is the live version of this project](https://leaf-skateshop.herokuapp.com/)~~

The project was redeployed via Render because of the changes to free Heroku hosting. [Link here.](https://cm-project-5.onrender.com/)

## Test Purchases

- Should you wish to put through a test purchase, please enter the following in the Stripe payment element at checkout.

![https://i.imgur.com/zcfkB4A](https://i.imgur.com/zcfkB4A.jpg "Payment details for a test purchase")

## Project Goals

## User Stories

The created user stories can be organised into the following epics:

- User & Admin accounts
- Admin product management
- Product display and filtering
- Shopping basket and payment system
- User engagement points, social media / newsletter
- User questions

These epics can then be broken down further into individual user stories:

- User & Admin accounts
    - Account registration
    - Store user details
    - Edit and update my saved information
    - View order history

- Admin product management
    - Add a new product
    - Edit an existing product
    - Remove a product from the store

- Product display and filtering
    - Site pagination
    - Selecting a category of product
    - Searchbar
    - Viewing an individual product
    - Selecting a size of product

- Shopping basket and payment system
    - Adding a product to the basket
    - Edit quantity and remove products in the basket
    - View a checkout page
    - Complete payment
    - Order confirmation

- User engagement points, social media / newsletter
    - Find the company's social media accounts
    - Sign up to a newsletter

- User questions
    - Post a question about a specific product
    - Answer user questions

These user stories were added to a kanban board created in Projects in Github [here](https://github.com/users/CMecrow/projects/2). The kanban board contains four columns:
- Backlog: This is where user stories that may not be added in this iteration of the project are kept. Referring to the MoSCoW prioritization categories, these can be considered 'could have'.
- Todo: Where all essential user stories that have not yet been worked on are stored, these can be considered 'must have'.
- In Progress: Where all user stories that are currently being worked on are located.
- Done: All completed user stories.

- Please note that User stories have been reviewed upon completion of the project with notes added to each.

## Site Development Schedule

- First planning this project, I realised that I would mainly have time to work over the weekends. Because of the size of the project, I applied an agile methodology to plan out the user stories and epics described above, to try and manage my time and calculate what features were must haves and which were could haves. With my working structure, I tried to work in one or two weekend sprints, to try and achieve at least basic functionality of the chosen epics over these periods. This helped me get my head around the task at hand, as I could focus on specific user stories to work towards epics, ensuring the basic functionality at least was there before moving on. The structure of the Code Institute walk through project, Boutique Ado, did also assist here as it could work as real boost to refer back to videos when I was slowed down by any bugs. I was very keen to try and implement as many features as I could and may have bitten off more than I could chew with the final implementation of the 'User questions' epic. Because of this the feature is not as well rounded as I would have liked, this is discussed further in the future features section.

---

## Leaf Skateshop business model / Site role

- This project is creating an ecommerce website for a skate shop called Leaf Skateshop. The shop and site will be business to consumer and the site will sell products directly to consumers. Leaf Skateshop as a whole would be classified as a small business, and they have requested this ecommerce site be built for them so they don't need to sell through any online intermediaries. This is beneficial to them as they can therefore have more control over the site, as well as make more profit from each sale as there's no partner to split with. The business to consumer model will also go on to suit them in the future, as more features are added to the site to increase user engagement. Features like an about us, FAQs, contact us and product wish lists would all deepen the relationships between the business and it's customers, as well as providing extra knowledge to the business as to which products are sought after, which aren't, as well as identifying customer questions and issues to tailor the website to answer them.
- The overall structure between business, website and consumer on a transactional basis will run as below:

    ![https://i.imgur.com/Yx2KNuQ](https://i.imgur.com/Yx2KNuQ.jpg "Leaf Skateshop business structure")

- As you can see in the above, the business passes information through the website about available products to the customer. The customer turns the available products into orders on the website. These orders are then picked up from the website by the business who then ship the ordered products to the customer.
- Though at this stage the above process is purely transactional, as mentioned above, the relationships between business and customer can be developed through further content on the website, meaning it's a place users visit not only to make purchases, but to learn more about the subject at hand a whole, namely rollerblading.

--- 

### Site Theme

- The overall layout used was taken from [tooplate.com](https://www.tooplate.com/view/2114-pixie). This was done to speed up project completion in the given time frame, with more time being allocated to site functionality and the backend. As with using any template, there was a lot of customisation required to wire up the pages using Django, and also tweaks to the html and css to suit the project. For example, the inclusion of a searchbar was included as a 'must have' feature in the user stories. The template also did not come with any account pages, so they were implemented via editing the allauth pages instead, making sure they fit the overall theme of the site. The banner image was changed to one more fitting for the site content, along with the colour scheme to fit with the 'leaf' name of the shop (colour choice is discussed further in the testing document).

---

## Wireframes

#### Desktop Homepage
![https://i.imgur.com/Ll4mx1L](https://i.imgur.com/Ll4mx1L.jpg "Desktop Homepage Wireframe")

#### Desktop Products Page
![https://i.imgur.com/FC1jq19](https://i.imgur.com/FC1jq19.jpg "Desktop Products Page")

#### Mobile Wireframes
![https://i.imgur.com/11KdD5p](https://i.imgur.com/11KdD5p.jpg "Mobile Wireframes")

---

## Features

### Existing Features

---

### Homepage and across site features

- The homepage design was chosen to have a large strong image immediately on display to the user, working as a clear indication as to the site content, and what sort of products may be found on the store. The store logo 'Leaf Skateshop' was designed to stand strongly in the center of the page with plenty of spacing and a heavy font. The name would dictate the general colour scheme, using a lot of dark green and black for accessibility reasons as well as overall styling. As discussed below, the page includes a brief 'who we are' statement along with a 'call to action' button. There are also a small selection of the latest added products viewable on the page, again working as an immediate indication as to the nature of the store.

### Pre navbar header

- Across the top of all pages, a header is displayed, detailing some strong incentives for users to purchase from the store. One feature that is repeated across the site is the incentive of hitting the 'free delivery' mark of £100. Obviously the larger the order the better for the store, but it also provides an incentive for the user, a potential reason for them to top up their shopping bag with an extra purchase to avoid paying shipping costs. The second incentive is the stores 'Expert knowledge and advice', this is included to communicate to users that the store staff understand the products and are open to giving advice where required. This is important because rollerblading as a sport can seem fairly inaccessible to someone without previous knowledge, with the varying features of products hidden behind jargon and other industry terms. This knowledge is accessible for the users within each product page, where they can ask a question about a specific product, and the admin can respond. The final incentive is a 'Free size swap'. This is something that various other skate shops offer and advertise so it's important for our store to match them. Within rollerblading, different brand's skates, or event models of skates within the same brand, have a very different fit on the foot. Because of this, offering a free size swap relieves one of the main worries that someone may have when buying new skates.
- To avoid this head becoming overbearing on smaller screens with the long text, the choice was made to filter off the less important incentives one by one, maintaining the header's height at the top of the page. The highest importance was assigned to 'Free Delivery on all orders over £100', second priority to 'Expert knowledge and advice' with 'Free size swap' being placed last. The downside to this is that the latter two incentives would be hidden to user who only view the site on a small display. One solution to this in a future iteration would be to include the incentives in an 'About Us' or 'FAQ' page, discussed in the future features section.

    ![https://i.imgur.com/DSpIQ5u](https://i.imgur.com/DSpIQ5u.jpg "Pre nav header")

### Navbar

- As mentioned, one of the main goals with the navbar was to give space to the site name 'Leaf Skateshop'. The logo font was chosen because it was bold and angular, and because it looked stylish in full caps, rather than overbearing. The colour scheme of the logo was chosen to fit the leaf, nature theme, as well as being a colour that would work well in other areas of the site, and provide enough distinction to other text for accessibility. All of the links present in the nav were originally going to be spread across the top of the page (see wireframes), however when making the site, they looked good centered underneath the strong logo, as it really draws the eye on the page. To keep the navbar from becoming slightly bloated with too many links, it was split into two rows with the top row being the priority links to the available products, and the second row being further product filtering in the search bar, along with icons for Account, Admin and Basket. These icons were chosen as they fit standard ecommerce convention, and don't clutter the navbar with too much text. While hovering any of the icons and nav links, the colours will change to indicate that the item is a link that can be clicked and will take the user away from the current page. The navbar is also responsive in that as soon as the display falls below 992px, it will become a button which will provide a drop down list of all links. The searchbar is excluded from this as it moves to the top of the page.
- The shopping bag icon will also display the amount of items in the bag, a useful feature for that purpose but also for indicating to the user, on top of the displayed message, that an item has been added.
- With regards to the Account button, to make the user journey as smooth as possible, I was keen for the user not to have to select a page from a list of options if possible. So rather than include a drop down menu that would list 'Account', 'Log in', 'Sign Out' and 'Register' I included logic in the html template to display one link for users to either log in (which includes a link to registration), and if the user was already logged in, the original link would be hidden and instead an almost identical link would be displayed to take the user to the accounts page which includes a button to sign out. This differs slightly on mobile because of the implementation of the drop down menu. One consideration I had was how to display to the user that they are logged in already. To remedy this, for mobile if the user is already logged in, the nav link will read 'My Account', if they aren't logged in, it'll read 'Log in / Register'. For desktop, when the user is logged in, the account icon would be displayed in the site green, leaning on the convention that green indicates 'success' or 'active'. When logged out it'd be displayed black.

    ![https://i.imgur.com/N9m9b1d](https://i.imgur.com/N9m9b1d.jpg "Navbar")

    ![https://i.imgur.com/1sjIIDK](https://i.imgur.com/1sjIIDK.jpg "Mobile Nav")

### Searchbar

- The searchbar was an important must have feature within the user stories. On a xl display it sits alongside the lower nav icons neatly, using another font awesome icon as the submit button. I had a choice to make with the searchbar as soon as the display hits 992px, and the responsive navbar kicks in. One option was to include the searchbar in the drop down with the other links however this felt a bit awkward to use and I quickly decided to keep it separate and relocate it to the top of the page for easy access for the user. As this was not included in the original template, it meant a fair amount of tweaks to the css to implement. This is discussed in more detail in the [testing file.]((https://github.com/CMecrow/CM-Project-5/blob/main/docs/testing.md))

### Messages

- Messages are employed throughout the site to give instant feedback to the user as to whether their action has succeeded or failed. It is also used as a display of an alert in some rare cases, for example to the admin to display which product they're currently editing. The most in depth message on the site is the message sent for a successful action.
- This message contains an extra feature of displaying to the user all the items in their shopping bag, along with some select information about the product, namely its image, name, size if applicable and quantity. This information extends further should the customer's bag be under the free delivery threshold of £100. If this is the case then an extra banner is shown indicating how much they'd have to spend to qualify. All of this is accompanied by the total cost of the items in the bag, and a link to take them to the checkout. All of this information however, feels a bit redundant on certain pages:
    - If the user is on the account page, updating their information, a large message would get in the way and not aid their current goals.
    - If the user is on the checkout or shopping bag page, they already have the items listed on the page so an extra display is redundant.
    - If a site admin is adding a product to the store, it's unlikely they'd have items in their basket, but it still feels unnecessary.
- The final unique feature of the success alerts is that they automatically hide after six seconds. This was not included on other messages such as alerts as they may be more unexpected, so require greater attention.

    ![https://i.imgur.com/mBpakXh](https://i.imgur.com/mBpakXh.jpg "Success message with bag notification")

### Confirmation emails

- Confirmation or verification emails are sent to users either when they're verifying their email when registering and also upon a successful purchase.
- The email verification is simple and sent when the registration form is completed with a link for the user to follow to authenticate their email address.
- The order confirmation email is more complex and is triggered upon receiving a successful webhook back from Stripe when the order has been found in the database or when the order itself has been created by the webhook when the order could not be found.

### Banner Image and Call to Action

- I included a large eye catching banner image to complement the site's content and purpose. The image is high quality so looks good on larger screens and isn't overly cluttered so still looks good on smaller devices, though the rollerblader may be cropped on small devices, the skatepark ramps are still present. The call to action overlayed on the image gives a brief introduction to the shop as well as the site's logo, letting the user know a bit about the business and where they're based. These features are accompanied by the call to action button 'Shop now!', providing an access point to the store products straight from the eye catching banner image. This button styling is replicated across the site, to make it clear to users when an element is interactable for them. They also include a hover effect to reinforce this.

    ![https://i.imgur.com/zQWI8sP](https://i.imgur.com/zQWI8sP.jpg "Banner image with call to action")

### New Items

- The template included a 'Featured items' section towards the bottom of the home page. I changed this to be new items, and applied the view appropriately, to keep the webpage dynamic and up to date without any extra work for the site admin. These products will be automatically updated as new items are added on the back or frontend by the site admin. These products have a grey small border to separate them, along with an eye catching image, bold product name with accompanying price in the site colour.

    ![https://i.imgur.com/WnKY1ab](https://i.imgur.com/WnKY1ab.jpg "New Items")

### Sign Up Form

- The website's sign up form is included on every page of the website. It fits with the colour theme of the site with an eye catching background and stand out bold white text as a call to action. Rather than a formal 'Newsletter sign up' or 'Sign Up Form', I used the prompt 'Stay in touch', as it is more casual and inviting than formal and demanding. The paragraph beneath the call to action outlines the benefits that the user can gain from signing up. Namely 'Keep up to date with our latest products and offers, as well as signing up to receive our monthly newsletter, covering everything rollerblading.' The form is clear and simple with no labels or required field notices, keeping it as hassle free and inviting for the user to use. The form itself is a restyled Mailchimp sign up form, which means that email addresses successfully entered receive a notice underneath the submit button of "Thank you for subscribing!" and are added onto the store's Mailchimp newsletter list.

    ![Ihttps://i.imgur.com/FFRJjuj](https://i.imgur.com/FFRJjuj.jpg "Email signup")
    ![https://i.imgur.com/mqjH9Qu](https://i.imgur.com/mqjH9Qu.jpg "Mailchimp success")

### Footer

- The footer again features the site's bold eye catching logo, sat centerally above links to the store's social media pages, all opening on a separate tab, with attributes for screen readers and also for search engines to disregard them when considering rankings. The links themselves are the individual page's icons / logos, all of which are so well embedded in popular culture, it's fine for them to be used instead of text links. The icons are monochrome to not clutter the footer with blues and reds. A small copyright notice is also included underneath a horizontal rule.

    ![https://i.imgur.com/uhhD4ih](https://i.imgur.com/uhhD4ih.jpg "Footer")

---

### Product Pages

### Product header and sort options

- The product list page looks the same whatever the chosen category, filter or search term. The page contains a heading to display to the user what they're currently browsing, this extends to a user's search, displaying 'Results for: (search term)'. The page will also always include a drop down menu to select how the products should be sorted. This includes all expected options of 'date', 'name' and 'price', in both ascending and descending order.
- The products themselves are displayed in the same manner as those in the 'new products' section on the home page, leading with a strong image, product name and price.
- To keep the site tidy I included pagination on all products pages, with the maximum amount of products displayed being 9 per page. This stops any product selection from becoming sprawling and unwieldy, especially on smaller devices. It also keeps the site wide sign up form and social links included in the footer, more relevant because they'll never fall too far down the page itself. The buttons to control the pagination did differ from the initial ideas included in the wireframes, and this is discussed in more detail in the testing document. In terms of function, they operate in a similar manner to the other buttons across the site with a strong hover effect, and also fit website convention with the icons being greyed out, rather than the usual colour, when the option isn't available. For example, going back a page when the user is on the first page.
- To select an individual product, the user can click anywhere within the applied border.

    ![https://i.imgur.com/ZOPuuoo](https://i.imgur.com/ZOPuuoo.jpg "All Products")

---

### Individual Product Pages

### Product Information and Editing

- The individual product page carries the product name as a header in the same style as other headers across the site, such as 'New items' or 'All Products'. This consistency is better visually for the user and builds into an overall style for the website. The main information about the product is displayed, the image, product name, price, description and sizing. The product descriptions are taken directly from the company's own description or website and could in future be broken down into smaller categories. This is discussed in the future features section. When added to the database via frontend or backend of the website, all products can be allocated a 'Clothes sizes' category:

    - S
    - M 
    - L 
    - XL
    
    or a 'Skate sizes' category:

    - UK6 / EU40
    - UK7 / EU41
    - UK8 / EU42
    - UK9 / EU43
    - UK10 / EU45
    - UK11 / EU46

    This is then displayed to the user on the product page in a drop down menu, detailing the choices. The user can then select the quantity of the product they'd like to add to their bag and click the 'Add to Bag' button when happy to do so.
- The product category is also displayed, with a clickable link should the user wish to see more products within that category.
- One feature that is only displayed to the site admin, is the links to edit or delete a product. The edit product link takes the user to a new page, pre populated with the product's information. Any of these fields can be updated to suit quick and easily via the 'Update Product' button. The delete button does not take the user to a new page, instead deleting the product from the store and redirecting to the products page. Both these links are hidden via logic in the html template and views.py.

    ![https://i.imgur.com/MLq2MV5](https://i.imgur.com/MLq2MV5.jpg "Individual product page")

### User Queries

- The user queries feature was added late in development. On the left hand side on desktop, above the comments on mobile, there's a heading and a few paragraphs to explain to the user what the feature is for, and why it's advantageous to them. This information reiterates the incentives listed in the top banner It provides the user with the ability to ask a question about the product whose page they're on, as well as providing an additional contact email, should it be more suitable for their query. Next to this info box, any comments already left on the product are displayed in order of date created with the author's username, comment and date and time of posting. For clarity's sake the comments are separated by a horizontal rule. Beneath this is the input box. The ability to leave these questions is hidden to users that are not logged in via the html template, instead linking them to the login page with a prompt 'Question about (product name)? Login here to ask us.' If the user is logged in, there's a clear input box below the prompt 'Question about (product name)? Let us know.
- Development of this feature is discussed further in the future features section of the readme.
- A negative of the current iteration of this feature is that admins can only moderate comments from the admin interface rather than having easily accessibly links to delete or hide comments on the front end, similar to those present to edit or delete products.

    ![https://i.imgur.com/hvs2nOV](https://i.imgur.com/hvs2nOV.jpg "Customer queries")

### Related Products

- The related products section uses the same layout as the 'new products' section on the home page. This time however it displays a random selection of 4 products from the same category of product already being shown. A key element to this is that the currently viewed product is excluded from this list, as it would unintuitive to advertise the same product again to the user, as well as being useless for the user themselves!

--- 

### Shopping Bag

- The shopping bag page contains logic to check whether the user has anything in their shopping bag. If they don't, they're told as much and given a link to return to the store.
- The shopping bag page is quite simple in design as this is when the user wants to be clear about their purchase. All elements on the page before the sign up form contain information about that particular order. Firstly the product details for the products in the basket. Then, displayed in a table, we have the image, name, size if applicable and sku number. We also have columns for individual price, an quantity selector which shows how many of that product are in the bag, and this can be adjusted as required, and finally a subtotal. This is calculated from the product price multiplied by it's quantity. Underneath the table we have the total costs, broken down into bag total, delivery if applicable and grand total.
- The user has the option at this point of 'Continue browsing' as it's feasible that they want to double check the total cost of their basket before going on to make more purchases, and also 'Checkout' should they wish to proceed to payment.
- One difference to the shopping bag page from those discussed previously is that the 'bag' section of any success messages will not be displayed while on it. This is because the user already has a clear breakdown of their bag on this page, so the extra notification wouldn't serve a purpose and would be annoying for the user, were they to prompt the message by adjusting quantities.

    ![https://i.imgur.com/JlEIDzc](https://i.imgur.com/JlEIDzc.jpg "Shopping bag")

---

### Checkout

- The checkout page is split in to three sections, 'Delivery', 'Order Summary' and 'Payment'.
- Delivery contains a form where the user is prompted to enter their delivery details, with a drop down selector for 'Country' to help navigate around the payment system, Stripe's tricky country verification. If the user is not logged in at this stage, there is a prompt with links underneath the form for them to create an account or log in, should they wish for a quicker checkout next time around by saving their delivery information. If the user is already logged in, in the prompts place there is a checkbox to save their details.
- The Order Summary section displays the products that are being purchased in a compact display, accompanied by a 'Return to Shopping Bag' link should any changes need to made. Underneath the products, again there's a breakdown of costs displayed to the user so they can confirm the total one last time before payment. The 'Complete Purchase' button is also located here as I thought it was beneficial to locate it right next to the total payment.
- Payment contains an element created by Stripe which will provide the users errors should the entered details be incorrect. Please see 'Test Purchases' at the top of the readme should you wish to test a purchase.
- Another feature of the checkout page is when details have been added successfully and the user has clicked 'Complete Purchase' the below overlay appears to indicate to the user that their order is being processed. Not only are they told 'Placing Order...' on the overlay itself, the triple dot indicate that there's a process happening, and the included rotating dots underneath, code taken from [here](https://loading.io/css/), also work to tell the user to wait. This is important as if they user were to refresh the page as they were not aware the order was going through, they could re-enter their details and be charged twice.

    ![https://i.imgur.com/lRCNif3](https://i.imgur.com/lRCNif3.jpg "Placing Order overlay")

    ![https://i.imgur.com/YmFD7uj](https://i.imgur.com/YmFD7uj.jpg "Checkout page")

### Checkout Success

- If the order goes through successfully, the user is taken to a separate 'checkout success' page, this page acts as confirmation for the user that the order has been successful, as well as giving them a table to view their order details. There is a link to return to the store underneath the table. I chose for this link to be slightly more muted than the large buttons elsewhere on the site, as it seemed more respectful to the user who's already made a purchase, rather than a button with capital letters saying 'back to the store!'

    ![https://i.imgur.com/Q4coVOm](https://i.imgur.com/Q4coVOm.jpg "Checkout Success")

---

### Account Pages

### Login

- The account process has been designed to contain as few pages as possible. Using all-auth meant the initial set up was very quick but the pages themselves do not contain any content so don't hold a huge amount of value for the site outside of their main purpose. The main login page contains the header 'Already Registered?' and the prompt 'If you have an account with us, please log in', with the form to do so below. Below the sign in button there's a muted link for resetting a password as well. 
- I decided to include a link to register in the login page to reduce the amount of pages used, and also to help the nav be as uncluttered and clean as possible. The header and prompt of 'New Here?' and 'Registration is quick and easy' mirror those of the log in form above, and act as an incentive for the unregistered user, describing the process as quick and easy. 

    ![https://i.imgur.com/3SmaHGY](https://i.imgur.com/3SmaHGY.jpg "Login")

### Create an Account

- The previous incentive didn't lie. The process for creating an account is quick and easy! All that's required is an email, username and password. Any further details would be unnecessary at this point as they can be completed at a later date in the account page or copied over from a checkout form. Just in case the user has clicked the wrong button on the previous login page, there's another prompt underneath the header containing a link back to the login page, ensuring the customer always has multiple options of exiting the page they're on should they have found their way there by mistake. Upon submitting their registration, the user is redirected to an email verification page alerting them that they will be emailed over a link they need to follow to verify their email before they can log in. This link takes the user to a page asking them to verify the address and if that's submitted they're redirected back to the login page. 

    ![https://i.imgur.com/h8lrYKK](https://i.imgur.com/h8lrYKK.jpg "Register")

### My Account / Logout

- The account page is split into two sections.
- The 'My Details' section, which contains the user's username, followed by a form for their delivery details. It's worth noting that should the user have already completed an order while logged in and ticked the option to save their details to their profile, the form will already be completed. If the user wants to make any changes to their delivery details, they can do so via adjusting the form and clicking 'Update My Details'. Floated to the right of this section at the bottom is also a 'Logout' button. This was included to help achieve the goal of having as few account pages as possible, and it seemed a logical place the customer may go to to log out of their account. To give the customer a chance to remain logged in, should they have got this far by accident, they're taken to a confirmation screen which includes a link head back to the store, as well as log out.
- The 'My Orders' section containers brief order summaries for any completed orders they've made while logged in. The order number is shrank as it's not as immediately useful for the user, with more room given to the date the order was placed, the products contained in the order, and the total charged. Should the user wish to see an order in more detail, they can do so via clicking on the order number to take them to the order confirmation page, as they would have seen when the order was confirmed.

    ![https://i.imgur.com/fOqOj25](https://i.imgur.com/fOqOj25.jpg "My Account")

    ![https://i.imgur.com/qeGKNaR](https://i.imgur.com/qeGKNaR.jpg "Logout")

---

### 404 Page

- A 404 page has been included should the user follow a link for a product that is no longer available, or should they lose their way elsewhere. The page is similar to the landing page in that it's dominated by a large image with a text box placed on top. The image itself was chosen because the skater is upside down / somewhere unexpected, much like the user has been to find the page. Not only is it eye catching but it also contained a large amount of blank colour on the left hand side where the text box could sit nicely. (This may not be the case on the smallest of displays). The text itself contains a clear message of "Error 404: the page you're looking for isn't available", a nice blame free explanation for the customer that everything is under control but whatever they're trying to access isn't currently accessible. This is accompanied by a large 'Return to the store' button to redirect the customer.

    ![https://i.imgur.com/7eQwCL0.](https://i.imgur.com/7eQwCL0.jpg "404 page")

---

## Future Features

### About Us / FAQ

- As mentioned in the business model / site role section, the Leaf Skateshop site can grow to be more than just transactional. It can develop in stages to be a bigger resource for the business to share information about themselves and rollerblading, deepening their relationships with users which would be beneficial for both parties. One way of sharing more information would be the inclusion of an 'About Us' page. This would give the business a more personal feel and give them room to tell their start-up story as a small business. From a customer point of view, it would be a resource to learn more about the business, to see if they're people they'd like to interact with and purchase from. From a business point of view an about us page would be a point to sell themselves, promote their staff and emphasise the mentioned incentive of 'expert knowledge'. If this came across to the customers, they may be more likely to query products, increasing the likelihood of them making a purchase, or reaching out via another future feature, a 'Contact Us' page.
Another perk for the business is that this sort of page would provide them with a good platform for including more keywords into the site in an appropriate manner.

- An FAQ page could be created easily through an existing feature on the site, the customer comments that can be left on products. If the business collected data on the common questions asked about products for a month or two, they could use that data to come up with the top 10 most common questions, and provide concise solutions for them. Were this to be implemented, it'd be well worth linking to it through base.html but also in the customer comment info section on the individual product pages.

- A final benefit of the FAQ page would be to double down on the incentives promised in the pre nav header. This information may not be visible on the smallest of screens, so it'd be important to have a point where all users can access it. A described perk of 'Free size swap' may sound great but it doesn't answer the question of how it works, how is shipping handled etc. A FAQ page would fill this requirement.

- While the above points are undoubtedly useful, they were not achievable in this iteration of the project due to time constraints. In general, they build on some of the 'must have' features or information already present on the site, rather than offering anything new so had to be considered a low priority.

### Product Information

- One considered development of the product model / displayed options would be adding further categories to products to help with keywords, for example, having a wheels category easily accessible on the site, may increase the rankings of our site for the search 'Rollerblade wheels'. Keywords as a concept are discussed in detail later in the readme. Rather than having a category of 'Parts' we could go further and have categories for 'wheels', 'frames' and 'liners', making it easier for users to find the product they're looking for. Another additional category could be 'brand', which could prove useful for users who are particularly loyal to a certain company, or are looking for a product that they know will work well with their current skates.
- While this would diversify the model and provide more options going forward, it wasn't considered a needed feature because of the inclusion of the search bar. The searchbar is a feature that aids customers find a specific product or brand, and does so while searching through product descriptions as well, widening the net. Though this can admittedly be more effort for the user.

### Customer Queries

- The included feature that currently requires the most work to live up to it's potential is the customer queries section. The feature would ideally have the function for site admins to specifically reply to customer questions, with their response being displayed beneath the question and highlighted. This could then be developed further and have the customer who asked the question sent an email notification that their question has been responded to, and for the admin, a notification that a question has been left, and where to find it. From both an admin and customer perspective the feature needs some work. For admins, the only moderation that can be carried out is within the admin page, built in to django, and as previously mentioned, any moderation should be achievable from the front end. For customers there should be the option to edit their submitted comments. Though the information present about the feature on the page does advise this isn't possible.
- All in all I decided that the skeleton version of this feature was still worth implementing, and it would provide a starting block for further expansion of the site.

---

## Data Model

- The data models use share a lot of the same data. For example 'User' in the User Profile model, will be the same that's used as 'Author' in the Comment data model and 'User Profile' in the Order data model. These links are required to be able to attach the pieces of data together. For example, for orders to be attributed to the correct user, or comments to the correct product. Some of the data is purely for the backend, for example in the checkout app, a user would interact with the Order data model, rather than the Order Line Item model. Some data is purely for the business, the 'Sku' in product is an example of this. Though it is displayed to the customer at various points in the user journey, it is primarily for the store to identify the correct product. There are some data points that are not currently used, but are included to aid the development of the site with extra features in the future. The Comment model includes an 'Updated on' field, though not currently in use, this will be necessary when the user is given the ability to edit their own comments / questions on the products page in the future.

    ![https://i.imgur.com/mqCvnrw](https://i.imgur.com/mqCvnrw.jpg "Data Model for Leaf Skateshop ecommerce site")

---

## SEO Considerations

The table below contains keywords considered for the Leaf Skateshop website.

|         Skates        |    Rollerblading   |    Skate Parts   | Gifts for a rollerblader       |
|:---------------------:|:------------------:|:----------------:|--------------------------------|
| Rollerblades          | _Skating_          | Skate wheels     | Things to buy a rollerblader   |
| Inline skates         | Inline skating     | Skate frames     | _Things to buy a skater_       |
| Aggressive skates     | Aggressive skating | Skate liners     | Rollerblader birthday present  |
| Complete skates       | _Extreme sports_   | Skate components | _Skater birthday present_      |
| _Recreational skates_ | Skate park sports  | _Wheels_         | Rollerblader christmas present |
| _Skate park skates_   |                    | _Frames_         |                                |
| Freestyle skates      |                    | _Liners_         |                                |

The headings worked as starter points for related keywords, listed below them. The entries in italics were then discounted for the following reasons:

- Leaf skateshop will not sell 'recreational skates'
- The term 'skater' was too generic and drew too many searches from the more popular sport of skateboarding. This discounted 'Skating', 'Things to buy a skater', 'Skater birthday' with 'Extreme sports' and 'Skate park sports' being discounted for the same reason.
- Some terms were too generic, 'Wheels', 'Frames' and 'Liners'
- The term 'Skate park skates' was too infrequently used, only being searched 38 times when entered on [wordtracker.com](https://www.wordtracker.com/)

When researching the above keywords, one factor in related searches that kept appearing was location. Specifically adding 'UK' or 'Newcastle' on to the end of searches. Here are some expansions on the above keywords. The first set when searching 'Rollerblades' were also frequently appearing when searching for any term in the left hand column.

Rollerblades:

- Rollerblades for men
- Rollerblades for women
- Rollerblades near me
- Rollerblades kids
- Rollerblades adults
- Rollerblades Newcastle
- Rollerblades UK
- What's the difference between roller skates and rollerblades?
- Where to buy rollerblades
- Which is the best rollerblades

Skate Parts:

- Skate parts UK
- inline skate wheels
- Skate laces
- Inline skate wheels UK
- What are the parts of a skate called?
- Pro skates

As the current iteration of the Leaf Skateshop doesn't contain an 'About Us' page, it's difficult to include some of the more long tailed keywords into this project. An about us page would work well as it could offer reference to the store location, hitting the above mentioned factor of locale. Another way that these keywords could be included would be an expansion on the product categories. Instead of just 'parts' we could drill into that further with categories for 'liners', 'wheels', 'frames' etc. This could also be implemented for skates, potentially splitting out that category into 'men's skates', 'women's skates' and 'kid's skates'.

We could also add more keywords to a brand categorisation. For example a user may be looking for a specific skate brand's products, and potentially then for more information about that brand, which could be provided via an link on the page to an external site, which search engines may already consider a high quality result, boosting our own rankings. In the current iteration, all products have the brand and specific product name included. This was very important because there's a lot of variation in skate products, so those who have an interest in the sport are more likely to be specialised and search for a specific item. The included descriptions also include as much information as supplied by the companies, without them getting overly verbose.

The site design is deliberately very image driven so including keywords proved very difficult. One area where certain keywords were easily included was on the landing page, the text on the banner image includes 'rollerbladers', 'skateshop' and 'UK'. As well as giving the company a bit of identity and purpose. 

Product images were all named very literally with the brand and product included in the image name itself.

Finally in the head of base.html, the site description was written to include the keywords 'skateshop', 'skate' 'skate shop', 'Newcastle', 'UK', 'rollerblading', 'rollerblading products'. The remaining keywords were included in the keywords meta element, along with prominent rollerblading brands. 'rollerblades', 'inline skates', 'inline skating', 'aggressive skates', 'aggressive skating', 'freestyle skates', 'complete skates', 'skate parts', 'skate wheels', 'skate frames', 'skate liners,' 'skate components', 'rollerblading gifts'.

The project also contains a sitemap.xml file created [here](https://www.xml-sitemaps.com/), and a robots.txt file, which allows search engine spiders into all points of our site, with the exception of the /admin/ directory.

---

## Leaf Skateshop Facebook account

- A Facebook Business page was created for Leaf Skateshop. Key elements included were:
    - Use of logo as profile picture to reinforce the brand name
    - Reuse of the strong banner image to give Facebook users a clear indication as to the purpose of the site and the nature of the products sold
    - Inclusion of keywords in the short bio section: 'Skateshop', 'UK'
    - Added location 'Newcastle' as that was a query that appeared a lot in the keyword research above
    - Included an email address for any enquiries. (If this were a real business you'd not want to include the email as a gmail account, instead you'd want to use a domain name to seem more professional and inspire customer confidence)
    - A direct link to the shop site, along with the use of the 'Call To Action' button being a 'Shop Now' linking to the site.
    - A positive first post linking to the site, prompting users to sign up with all the incentives.

- I have deactivated the page to avoid it being taken down or any misuse. Please see screenshot below

    ![https://i.imgur.com/R3Z8aQU](https://i.imgur.com/R3Z8aQU.jpg "Leaf Skateshop Facebook page")

---

## Deployment procedure

- Created an app on Heroku named leaf-skateshop.
- Added a postgres database to the app in Heroku.
- I downloaded my current product database into a json file as shown [here](https://code-institute-room.slack.com/archives/C01C4AU8ULA/p1641488400004200)
- Installed dj-database-url in GitPod (Problem encountered: Installing dj-database-url, updated my installation of django. I reinstalled django 3.2 and installed an earlier version of dj-database-url to work around this issue).
- Installed psycopg2-binary in GitPod.
- Made sure they were then included in my requirements.txt.
- Imported dj_database_url into my settings.py.
- Altered the DATABASES variable to use the database url from postgres in Heroku.
- Attempted to makemigrations and migrate over the data models to postgres.
- Now that I was connected to the postgres database, I uploaded my products.json file again as shown [here](https://code-institute-room.slack.com/archives/C01C4AU8ULA/p1641488400004200) to avoid the slow task of manually updating via admin.
- Then created a new superuser for the postgres database.
- As I was wanting to ensure the new database was uploaded correctly, I created an env.py file containing the new postgres database url so it could still be accessed by GitPod without being commited. This also meant I could authenticate my new superuser.
- Then installed guinicorn on GitPod and updated my requirements.txt.
- Procfile created to tell Heroku to create a web Dyno, explained [here.](https://www.heroku.com/dynos)
- As all static filed would be passed over via S3, I added DISABLE_COLLECTSTATIC 1 to Heroku's config vars.
- Updated the new Heroku link to allowed_hosts in settings.py.
- Attempted to push to Heroku (Problem encountered: ERROR: Failed building wheel for backports.zoneinfo, the resolution to this was to specify which version of Python I wanted to use in a file named runetime.txt, and also to add the following code to my requirements.txt 'backports.zoneinfo;python_version<"3.9"' this fix was detailed [here](https://stackoverflow.com/questions/71712258/error-could-not-build-wheels-for-backports-zoneinfo-which-is-required-to-insta) as well as digging through the Heroku documentation [here](https://devcenter.heroku.com/articles/python-support)).
- Enabled automatic deployment on Heroku, linking to GitHub.
- Generated a new secret key to add to Heroku config vars.
- Updated settings.py to retrieve secret key from env.py file, for DEBUG to only be true should there be a variable named 'DEVELOPMENT' (again located in env.py but not on Heroku).
- Created a new public bucket on S3 to store static files, enabled static website hosting, applied a CORS configuration to grant our Heroku app access and generated a security policy for the bucket, all in permissions. Detailed walk through of these steps available [here.](https://codeinstitute.s3.amazonaws.com/fullstack/AWS%20changes%20sheet.pdf)
- Still within AWS, I navigated to IAM to create a user to access the newly created bucket. This required a group for the user, coupled with a suitable access policy. Again walk through followed [here.](https://codeinstitute.s3.amazonaws.com/fullstack/AWS%20changes%20sheet.pdf).
- Once the above step was complete, I had access to the newly created user's access key and secret access key, both of which were then added as config vars on Heroku, along with 'USE_AWS', which would be used in the next step.
- Back in GitPod, I installed boto3 and django-storages, updating my requirements.txt. Django-storages was added to my installed apps in settings.py. Still in settings, I added an if statement to check if the variable 'USE_AWS' was present, ensuring it wouldn't be in GitPod, but was in Heroku. Within the if statement, I added details of the S3 bucket, along with a way of the access key and secret access keys being reached on Heroku.
- Since the static files are almost ready to be used on the deployed Heroku site, I removed the DISABLE_COLLECTSTATIC variable.
- Because of the previous step, I needed to let Django know that we now wanted to use S3 to store any static files either when they're uploaded or requested via get static. The steps to achieve this involved making a new file of custom_storages.py, importing settings into it, as well as the S3 storage class within previously mentioned boto3 / django-storages packages.
- Within custom_storages.py I created a custom class called StaticStorage, inheriting from the imported packages, then passing the information that we want static files installed to a newly created variable in settings.py. This was then repeated for a class named MediaStorage, which would accomplish the same goal but for media files.
- Within settings.py, I set the static file storage to use the newly created StaticStorage class, and created the variable that would be past into that class, saving static files into a folder named 'static'. This was then repeated for media files.
- The urls for static and media files within S3 were then set using the previously created domain and location variables.
- Now upon deployment, Heroku will run collect static through python which will pull all static files from the project and use the created location and url variables to save the files within the S3 bucket.
- For the media files however, I uploaded these manually into the bucket within a folder named 'media', and granted public read access to the uploaded images.
- The variable AWS_S3_OBJECT_PARAMETERS was added to settings, the role of which is to communicate to the browser that static files can be cached for a long period of time, improving the user experience on future visits as loading speeds will be quicker.
- The first step to get Stripe up and running with the new deployed site was to ensure both the public and secret API keys were stored as config vars on Heroku.
- Then a new webhook was created to link up with the Heroku page, identical to the original, just with a new endpoint URL. The signing secret attached to the webhook was then also stored as a config var on Heroku.
- The new webhook was then tested on the deployed site, which were successful (issues arose at a later point when confirmation emails were introduced to the webhook handler, detailed in the testing document.)
- Success! Deployment complete.

- As mentioned I have kept my GitPod workspace using the postgres database as I was keen to manage the feature that was added late in development, the customer queries, with ease from GitPod. This will not be the case for anyone else using GitPod as the required variables are stored in an env.py which is separate to version control as it's listed in .gitignore.

---

## Credits

- The project took its roots and structure from Code Institute's Boutique Ado walk through project.
- The Comments model present in Products/models.py was taken and adjusted from my 4th Project, link [here.](https://github.com/CMecrow/CM-Project-4)
- The banner and 404 images used were taken from [here.](https://www.adamkola.com/rollerblading/) Ideally I'd use royalty free open source images, but due to the niche nature of the subject matter, high quality photos are extremely hard to come by.
- The product images and descriptions were taken from [here.](https://www.thisissoul.com/)
- The [site template](https://www.tooplate.com/templates/2114_pixie/) used.
- Stackoverflow on how to edit bootstrap's input glow [here.](https://stackoverflow.com/questions/14820952/change-bootstrap-input-focus-blue-glow)
- Django pagination documentation available [here](https://docs.djangoproject.com/en/4.0/topics/pagination/), with assisting youtube video [here](https://www.youtube.com/watch?v=dkJ3uqkdCcY).
- Related product youtube video [here](https://www.youtube.com/watch?v=fqIBA2Vpws0&t=136s).
- A useful document on QueryStrings [here](https://simpleisbetterthancomplex.com/snippet/2016/08/22/dealing-with-querystring-parameters.html).
- The Placing Order CSS loader taken from [here](https://loading.io/css/).
- The walk through for creating a json file containing my product database [here](https://code-institute-room.slack.com/archives/C01C4AU8ULA/p1641488400004200).
- Stackoverflow for issues during deployment to Heroku [here](https://stackoverflow.com/questions/71712258/error-could-not-build-wheels-for-backports-zoneinfo-which-is-required-to-insta#:~:text=Avoid%20installing%20backports.zoneinfo%20when%20using%20python%20%3E%3D%203.9).
- CodeInstitute deployment walk through [here.](https://codeinstitute.s3.amazonaws.com/fullstack/AWS%20changes%20sheet.pdf)

