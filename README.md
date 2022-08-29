# Leaf Skateshop

### For rollerbladers, by rollerbladers. The Leaf Skateshop is the newest and fastest growing skateshop in the UK.

---

As a developer, I've been tasked with creating an ecommerse site for a skateshop.

This project has been made using Django / Python, HTML, CSS and JavaScript.

[Here is the live version of this project](https://leaf-skateshop.herokuapp.com/)

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

- The overall layout used was taken from [tooplate.com](https://www.tooplate.com/view/2114-pixie). This was done to speed up project completion in the given timeframe, with more time being allocated to site functionality and the backend. As with using any template, there was a lot of customisation required to wire up the pages using Django, and also tweaks to the html and css to suit the project. For example, the inclusion of a searchbar was included as a 'must have' feature in the userstories. The template also did not come with any account pages, so they were implimented via editing the allauth pages instead, making sure they fit the overall theme of the site. The banner image was changed to one more fitting for the site content, along with the colour scheme to fit with the 'leaf' name of the shop (colour choice is discussed further in the testing document).

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

- The homepage design was chosen to have a large strong image imediately on display to the user, working as a clear indication as to the site content, and what sort of products may be found on the store. The store logo 'Leaf Skateshop' was designed to stand strongly in the center of the page with plenty of spacing and a heavy font. The name would dictate the general colour scheme, using a lot of dark green and black for accessibility reasons as well as overall stlying. As discussed below, the page includes a brief 'who we are' statement along with a 'call to action' button. There are also a small selection of the latest added products viewable on the page, again working as an imediate indication as to the nature of the store.

### Pre navbar header

- Across the top of all pages, a header is displayed, detailing some strong incentives for users to purchase from the store. One feature that is repeated across the site is the incentive of hitting the 'free delivery' mark of £100. Obviously the larger the order the better for the store, but it also provides an incentive for the user, a potential reason for them to top up their shopping bag with an extra purchase to avoid paying shipping costs. The second incentive is the stores 'Expert knowledge and advice', this is included to communicate to customers that the store staff understand the products and are open to giving advice where required. This is important because rollerblading as a sport can seem fairly inaccessible to someone without previous knowledge, with the varying features of products hidden behind jargon and other industry terms. This knowledge is accessible for the customers within each product page, where they can ask a question about a specific product, and the admin can respond. The final incentive is a 'Free size swap'. This is something that various other skate shops offer and advertise so it's important for our store to match them. Within rollerblading, different brand's skates, or event models of skates within the same brand, have a very different fit on the foot. Because of this, offering a free size swap releives one of the main worries that someone may have when buying new skates.
- To avoid this head becoming overbearing on smaller screens with the long text, the choice was made to filter off the less important incentives one by one, maintaining the header's height at the top of the page. The highest importance was assigned to 'Free Delivery on all orders over £100', second priority to 'Expert knowledge and advice' with 'Free size swap' being placed last. The downside to this is that the latter two incentives would be hidden to customer who only view the site on a small display. One solution to this in a future iteration would be to include the incentives in an 'About Us' or 'FAQ' page, discussed in the future features section.

### Navbar

- As mentioned, one of the main goals with the navbar was to give space to the site name 'Leaf Skateshop'. The logo font was chosen because it was bold and angular, and because it looked stylish in full caps, rather than overbearing. The colour scheme of the logo was chosen to fit the leaf, nature theme, as well as being a colour that would work well in other areas of the site, and provide enough distinction to other text for accessibility. All of the links present in the nav were originally going to be spread across the top of the page (see wireframes), however when making the site, they looked good centered underneath the strong logo, as it really draws the eye on the page. To keep the navbar from becoming slightly bloated with too many links, it was split into two rows with the top row being the priority links to the available products, and the second row being further product filtering in the search bar, along with icons for Account, Admin and Basket. These icons were chosen as they fit standard ecommerce convention, and don't clutter the navbar with too much text. While mouseovering any of the icons and nav links, the colours will change to indicate that the item is a link that can be clicked and will take the user away from the current page. The navbar is also responsive in that as soon as the display falls below 992px, it will become a button which will provide a dropdown list of all links. The searchbar is excluded from this as it moves to the top of the page.
- With regards to the Account button, to make the user journey as smooth as possible, I was keen for the user not to have to select a page from a list of options if possible. So rather than include a drop down menu that would list 'Account', 'Log in', 'Sign Out' and 'Register' I included logic in the html template to display one link for users to either log in (which includes a link to registration), and if the user was already logged in, the original link would be hidden and instead an identical link would be displayed to take the user to the accounts page which includes a button to sign out.

### Searchbar

- The searchbar was an important must have feature within the user stories. On a xl display it sits alongside the lower nav icons neatly, using another font awesome icon as the submit button. I had a choice to make with the searchbar as soon as the display hits 992px, and the responsive navbar kicks in. One option was to include the searchbar in the dropdown with the other links however this felt a bit awkward to use and I quickly decided to keep it seperate and relocate it to the top of the page for easy access for the user. As this was not included in the original template, it meant a fair amount of tweaks to the css to implement. This is discussed in more detail in the [testing file.]((https://github.com/CMecrow/CM-Project-5/blob/main/docs/testing.md))

### Messages

- 

### Banner Image and Call to Action

- I included a large eye catching banner image to complement the site's content and purpose. The image is high quality so looks good on larger screens and isn't overly cluttered so still looks good on smaller devices, though the rollerblader may be cropped on small devices, the skatepark ramps are still present. The call to action overlayed on the image gives a brief introduction to the shop as well as the site's logo, letting the user know a bit about the business and where they're based. These features are accompanied by the call to action button 'Shop now!', providing an access point to the store products straight from the eye catching banner image. This button styling is replicated across the site, to make it clear to users when an element is interactable for them. They also include a hover effect to reinforce this.

### New Items

- The template included a 'Featured items' section towards the bottom of the home page. I changed this to be new items, and applied the view appropriatley, to keep the webpage dynamic and up to date without any extra work for the site admin. These products will be automatically updated as new items are added on the back or frontend by the site admin. These products have a grey small border to seperate them, along with an eye catching image, bold product name with accompanying price in the site colour.

### Sign Up Form

- The website's sign up form is included on every page of the website. It fits with the colour theme of the site with an eye catching background and stand out bold white text as a call to action. Rather than a formal 'Newsletter sign up' or 'Sign Up Form', I used the prompt 'Stay in touch', as it is more casual and inviting than formal and demanding. The paragraph beneath the call to action outlines the benefits that the customer can gain from signing up. Namely 'Keep up to date with our latest products and offers, as well as signing up to receive our monthly newsletter, covering everything rollerblading.' The form is clear and simple with no labels or required field notices, keeping it as hassle free and inviting for the customer to use. The form itself is a restyled Mailchimp sign up form, which means that email addresses successfuly entered receive a notice underneath the submit button of "Thank you for subscribing!" and are added onto the store's Mailchimp newsletter list.

![Ihttps://i.imgur.com/FFRJjuj](https://i.imgur.com/FFRJjuj.jpg "Email signup")
![https://i.imgur.com/mqjH9Qu](https://i.imgur.com/mqjH9Qu.jpg "Mailchimp success")

### Footer

- The footer again features the site's bold eye catching logo, sat centerally above links to the store's social media pages, all opening on a seperate tab, with attributes for screenreaders and also for search engines to disregard them when considering rankings. The links themselves are the individual page's icons / logos, all of which are so well embeded in popular culture, it's fine for them to be used instead of text links. The icons are monochrome to not clutter the footer with blues and reds. A small copyright notice is also included underneath a horizontal rule.

---

### Product Pages

### Product header and sort options

- The product list page looks the same whatever the chosen category, filter or search term. The page contains a heading to display to the user what they're currently browsing, this extends to a user's search, displaying 'Results for: (search term)'. The page will also always include a drop down menu to select how the products should be sorted. This includes all expected options of 'date', 'name' and 'price', in both ascending and descending order.
- The products themselves are displayed in the same manner as those in the 'new products' section on the home page, leading with a strong image, product name and price.
- To keep the site tidy I included pagination on all products pages, with the maximum amount of products displayed being 9 per page. This stops any product selection from becoming sprawling and unwieldly, especially on smaller devices. It also keeps the site wide sign up form and social links included in the footer, more relevant because they'll never fall too far down the page itself. The buttons to control the pagination did differ from the intial ideas included in the wireframes, and this is discussed in more detail in the testing document. In terms of function, they opperate in a similar manner to the other buttons across the site with a strong hover effect, and also fit website convention with the icons being greyed out, rather than the usual colour, when the option isn't available. For example, going back a page when the user is on the first page.
- To select an individual product, the user can click anywhere within the applied border.

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

    This is then displayed to the customer on the product page in a dropdown menu, detailing the choices. The user can then select the quantity of the product they'd like to add to their bag and click the 'Add to Bag' button when happy to do so.
- The product category is also displayed, with a clickable link should the user wish to see more products within that category.
- One feature that is only displayed to the site admin, is the links to edit or delete a product. The edit product link takes the user to a new page, pre populated with the product's information. Any of these fields can be updated to suit quick and easily via the 'Update Product' button. The delete button does not take the user to a new page, instead deleting the product from the store and redirecting to the products page. Both these links are hidden via logic in the html template and views.py.

### Customer Queries

- The customer queries feature was added late in development. On the left hand side on desktop, above the comments on mobile, there's a heading and a few paragraphs to explain to the customer what the feature is for, and why it's advantageous to them. This information reiterates the incentives listed in the top banner It provides the customer with the ability to ask a question about the product whose page they're on. This feature is hidden to users that are not logged in via the html template, instead linking them to the login page with a prompt 'Question about (product name)? Login here to ask us.' If the user is logged in, there's a clear input box below the prompt 'Question about (product name)? Let us know.

---

## Future Features

### About Us / FAQ

- Pre header information

### Product Information

- Break down into categories

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

When researching the above keywords, one factor in related searches that kept appearing was location. Specifically adding 'UK' or 'Newcastle' on to the end of searches. Here are some expansions on the above keywords. The first set when searching 'Rollerblades' were also frequently appearing when searching for any term in the left hand collumn.

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

As the current itteration of the Leaf Skateshop doesn't contain an 'About Us' page, it's difficult to include some of the more long tailed keywords into this project. An about us page would work well as it could offer reference to the store location, hitting the above mentioned factor of locale. Another way that these keywords could be included would be an expansion on the product categories. Instead of just 'parts' we could drill into that further with categories for 'liners', 'wheels', 'frames' etc. This could also be implemented for skates, potentially splitting out that category into 'mens skates', 'womens skates' and 'kids skates'.

We could also add more keywords to a brand categorisation. For example a customer may be looking for a specific skate brand's products, and potentially then for more information about that brand, which could be provided via an link on the page to an external site, which search engines may already consider a high quality result, boosting our own rankings. In the current itteration, all products have the brand and specific product name included. This was very important because there's a lot of variation in skate products, so those who have an interest in the sport are more likely to be specialised and search for a specific item. The included descriptions also include as much information as supplied by the companies, without them getting overly verbose.

The site design is deliberately very image driven so including keywords proved very difficult. One area where certain keywords were easily included was on the landing page, the text on the banner image includes 'rollerbladers', 'skateshop' and 'UK'. As well as giving the company a bit of identity and purpose. 

Product images were all named very literally with the brand and product included in the image name itself.

Finally in the head of base.html, the site description was written to include the keywords 'skateshop', 'skate' 'skate shop', 'Newcastle', 'UK', 'rollerblading', 'rollerblading products'. The remaining keywords were included in the keywords meta element, along with prominent rollerblading brands. 'rollerblades', 'inline skates', 'inline skating', 'aggressive skates', 'aggressive skating', 'freestyle skates', 'complete skates', 'skate parts', 'skate wheels', 'skate frames', 'skate liners,' 'skate components', 'rollerblading gifts'.

The project also contains a sitemap.xml file created [here](https://www.xml-sitemaps.com/), and a robots.txt file, which allows search engine spiders into all points of our site, with the exception of the /admin/ directory.

