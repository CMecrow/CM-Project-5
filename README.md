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
