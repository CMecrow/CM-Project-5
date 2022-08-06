# Testing

Testing on this project has been done both manually and through validators and linters. Detailed below are some of the test conducted, issues found and workarounds implimented.

---

## Homepage

### Searchbar

Because the searchbar was not included in the template, it was slightly more difficult to integrate with the responsive nav's design. Because I decided not to include the searchbar in the nav's responsive drop down menu, and to instead have it move to the top of the page, I had to find a way of fixing it place. My first attempt at this was using:

        position: fixed;

However, this had the unintended consiquence of having the searchbar appear at the top of the page when scrolling down. To stop this from happening the position was changed to:

        position: absolute;

The responsive resizing of the searchbar is not completed in as smoother a manner as I'd like in relation to the navbar below it, I simply used resizing via media queries. Ideally it should match the resizing of the logo and nav buttons, instead of over or underlapping. This is a small aesthetic issue and does not effect the functionality, however it may be revisited later in the project, should there be time.

### New Items

- The template did include some js and custom css to have a carousell feature to the featured items. This wasn't something that felt necessary for this project