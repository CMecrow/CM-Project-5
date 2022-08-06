# Leaf Skateshop

### For rollerbladers, by rollerbladers. The Leaf Skateshop is the newest and fastest growing skateshop in the UK.

---

As a developer, I've been tasked with creating an ecommerse site for a skateshop.

This project has been made using Django / Python, HTML, CSS and JavaScript.

[Here is the live version of this project]()

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
    - Store customer details
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

These user stories were added to a kanabn board created in Projects in Github. The kanban board contains four columns:
- Backlog: This is where user stories that may not be added in this iteration of the project are kept. Refering to the MoSCoW prioritization categories, these can be considered 'could have'.
- Todo: Where all essential user stories that have not yet been worked on are stored, these can be considered 'must have'.
- In Progress: Where all user stories that are currently being worked on are located.
- Done: All completed user stories.

--- 

### Site Theme

- The overall layout used was taken from [tooplate.com](https://www.tooplate.com/view/2114-pixie). This was done to speed up project completion in the given timeframe, with more time being allocated to site functionality and the backend. As with using any template, there was a lot of customisation required to wire up the pages using Django, and also tweaks to the html and css to suit the project. For example, the inclusion of a searchbar was included as a 'must have' feature in the userstories. The template also did not come with any account pages, so they were implimented via editing the allauth pages instead, making sure they fit the overall theme of the site. The banner image was changed to one more fitting for the site content, along with the colour scheme to fit with the 'leaf' name of the shop.

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

### Homepage

- The homepage design was chosen to have a large strong image imediately on display to the user, working as a clear indication as to the site content, and what sort of products may be found on the store. The store logo 'Leaf Skateshop' was designed to stand strongly in the center of the page with plenty of spacing and a heavy font. The name would dictate the general colour scheme, using a lot of dark green and black for accessibility reasons as well as overall stlying. As discussed below, the page includes a brief 'who we are' statement along with a 'call to action' button. There are also a small selection of the latest added products viewable on the page, again working as an imediate indication as to the nature of the store.

### Navbar

- As mentioned, one of the main goals with the navbar was to give space to the site name 'Leaf Skateshop'. The logo font was chosen because it was bold and angular, and because it looked stylish in full caps, rather than overbearing. The colour scheme of the logo was chosen to fit the leaf, nature theme, as well as being a colour that would work well in other areas of the site, and provide enough distinction to other text for accessibility. All of the links present in the nav were originally going to be spread across the top of the page (see wireframes), however when making the site, they looked good centered underneath the strong logo, as it really draws the eye on the page. To keep the navbar from becoming slightly bloated with too many links, it was split into two rows with the top row being the priority links to the available products, and the second row being further product filtering in the search bar, along with icons for Account and Basket. These icons were chosen as they fit standard ecommerce convention, and don't clutter the navbar with too much text. While mouseovering any of the icons and nav links, the colours will change to indicate that the item is a link that can be clicked and will take the user away from the current page. The navbar is also responsive in that as soon as the display falls below 992px, it will become a button which will provide a dropdown list of all links. The searchbar is excluded from this as it moves to the top of the page.

### Searchbar

- The searchbar was an important must have feature within the user stories. On a xl display it sits alongside the lower nav icons neatly, using another font awesome icon as the submit button. I had a choice to make with the searchbar as soon as the display hits 992px, and the responsive navbar kicks in. One option was to include the searchbar in the dropdown with the other links however this felt a bit awkward to use and I quickly decided to keep it seperate and relocate it to the top of the page for easy access for the user. As this was not included in the original template, it meant a fair amount of tweaks to the css to implement. This is discussed in more detail in the [testing file.]((https://github.com/CMecrow/CM-Project-5/blob/main/docs/testing.md))

### Banner Image and Call to Action

- I included a large eye catching banner image to complement the site's content and purpose. The image is high quality so looks good on larger screens and isn't overly cluttered so still looks good on smaller devices, though the rollerblader may be cropped on small devices, the skatepark ramps are still present. The call to action overlayed on the image gives a brief introduction to the shop as well as the site's logo, letting the user know a bit about the business and where they're based. These features are accompanied by the call to action button 'Shop now!', providing an access point to the store products straight from the eye catching banner image.

### New Items

- The template included a 'Featured items' section towards the bottom of the home page. I changed this to be new items, and applied the view appropriatley, to keep the webpage dynamic and up to date without any extra work for the site admin. These products will be automatically updated as new items are added on the backend. 