# Testing

Testing on this project has been done both manually and through validators and linters. Detailed below are some of the test conducted, issues found and workarounds implimented.

---

## Colour Choice

The site originally used a colour that fitted the style and theme of the site, and was something I was happy with from the begining of the project until right at the end. However, whe running Lighthouse accessibility testing, it became clear that the chosen colour, which was implemented on the info bar at the top of the page, on all buttons as well as the sign up form, did not provide enough contrast with white text. Although I had used the colour through out the site, I had no option to keep it. I selected a darker green to provide more contrast with the white text, and when running this through Lighthouse testing, it was passed.

## Homepage

### Searchbar

Because the searchbar was not included in the template, it was slightly more difficult to integrate with the responsive nav's design. Because I decided not to include the searchbar in the nav's responsive drop down menu, and to instead have it move to the top of the page, I had to find a way of fixing it place. My first attempt at this was using:

        position: fixed;

However, this had the unintended consiquence of having the searchbar appear at the top of the page when scrolling down. To stop this from happening the position was changed to:

        position: absolute;

The responsive resizing of the searchbar is not completed in as smoother a manner as I'd like in relation to the navbar below it, I simply used resizing via media queries. Ideally it should match the resizing of the logo and nav buttons, instead of over or underlapping. This is a small aesthetic issue and does not effect the functionality, however it may be revisited later in the project, should there be time.

### New Items

- The template did include some js and custom css to have a carousell feature to the featured items. This wasn't something that felt necessary for this project

---

## Product Page

### Categories

While working with the product categories, in particular displaying certain categories, I ran into trouble when deviating from the walkthrough project code. I initially discarded

        .split(',')

from

        categories = request.GET['category'].split(',')

as the user would not be able to apply multiple categories in the same filter, so the split would not be required. However the unintended consiquence of this was that the variable then returned a string rather than a list. This caused a problem in the filtering on this line of code:

        products = full_products.filter(category__name__in=categories)

The work around was to search for the string rather than the list:

        products = full_products.filter(category__name=categories)

This workaround solved the immediate problem and products were successfuly displayed however it became an issue when trying to print the applied categories on the products page, as it was returning a blank queryset. At this point I reverted back to the walkthrough project code to return a list, despite there only being one category that could be displayed. Although not an ideal fix for the current itteration of the project, it does mean that should the ability to search via multiple criteria be added to the project at a later date, everything will still work as intended.

### Pagination

Site pagination was initially first accomplished in two steps across the site. The following is the code for the all products view, without any filtering applied:

        full_products = Product.objects.all()
        pagination = Paginator(full_products, 9)
        page_num = request.GET.get('page')
        products = pagination.get_page(page_num)

Any filters that were applied required slight adjustments to the initial product storing variable, to make sure that the filters were applied, for example:

        filtered_products = full_products.filter(category__name__in=categories).order_by('-date_added')
        pagination = Paginator(filtered_products, 9)

The second step was in the navigation of the paginated pages. The previous and next buttons at the bottom of the page. The initial href for these were:

        href="?page={{ products.previous_page_number }}" and href="?page={{ products.next_page_number }}"

This worked fine for the all products view but proved an issue when navigating with filters applied. For example, if the category of 'Skates' was selected, the filtering would apply along with the pagination and 9 products with the correct category would be displayed. However when the navigation to the next page was clicked, the filters were removed and instead page 2 of all products was displayed.

This was a really tricky fix. I eventually stumbled on [this document](https://simpleisbetterthancomplex.com/snippet/2016/08/22/dealing-with-querystring-parameters.html), along with [this youtube walkthrough](https://www.youtube.com/watch?v=dkJ3uqkdCcY) which provided the applied solution of creating a custom template tag to deconstruct the url, pass it through a function and return it as required.

Template tag:

        from django import template


        register = template.Library()

        @register.simple_tag
        def my_url(value, field_name, urlencode=None):
        url = '?{}={}'.format(field_name, value)

        if urlencode:
                querystring = urlencode.split('&')
                filtered_querystring = filter(lambda p: p.split('=')[0]!=field_name, querystring)
                encoded_querystring = '&'.join(filtered_querystring)
                url = '{}&{}'.format(url, encoded_querystring)

        
        return url

Restructured href on  navigation:

        href="{% my_url products.previous_page_number 'page' request.GET.urlencode %}"
        href="{% my_url products.next_page_number 'page' request.GET.urlencode %}"


One fallout from the above fix was that instead of using page selectors at the bottom of the products list, I instead ended up using buttons for previous page and next page. Although this wasn't the original design, because the store is unlikely to stock a very large amount of products, and also because filtering and searching products is an option, I didn't think it'd prove too much of an inconvenience to the user to click through page by page, rather than skipping multiple.

When writing the view for all_products, I built it in stages, for example first ensuring that all products were displayed with pagination applied, then filters could be applied and also paginated etc etc. Because of this approach, I ended up repeating the pagination in each section unnecessarily. This then caused issue when trying to impliment the Sort By dropdown menu, where sorting could be applied on All Products, but as soon as a filter or search query was applied, the sorting would not work. This tripped me up for a long time until I decided to simplify the code in the view and apply the pagination at the end of the view. This fixed the error and caused the sorting to work as expected.



