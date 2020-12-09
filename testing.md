# Testing the Book Review app
 
1. [**Automated Tests**](#automated-tests)
   * [Code Validation](#code-validation)
   * [Unit Testing](#unit-testing)
   * [Writing your own unittests](#writing-your-own-unittests)
2. [**Manual Testing**](#manual-testing)
   * [Database Testing](#database-testing)
   * [Navigation testing](#navigation-testing)
   * [Incorrect Form Submissions](#incorrect-form-submissions)
   * [Scoring Tests](#scoring-tests)
   * [UI Testing](#ui-testing)
3. [**User Story Testing**](#user-story-testing)
 
## Automated Tests
 
### Code Validation
 
This projects code has been validated through various services
 
- W3C Markup
    - [viewbooks.html](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbook-review-kelvinhere.herokuapp.com%2Fview_books)
    - [addbook.html](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbook-review-kelvinhere.herokuapp.com%2Fadd_book)
    - [editbook.html](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbook-review-kelvinhere.herokuapp.com%2Fedit_book%2F5f96bdb414d4ef7e4c5b27e6)
    - [addreview.html](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbook-review-kelvinhere.herokuapp.com%2Fadd_review%2F5f96bdb414d4ef7e4c5b27e6)
    - [editreview.html](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbook-review-kelvinhere.herokuapp.com%2Fedit_review%2F5f96bdb414d4ef7e4c5b27e6%2F5f9d6c01ff0a9a6af0953ebb)
    - [viewreviews.html](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbook-review-kelvinhere.herokuapp.com%2Fview_reviews%2F5f96bdb414d4ef7e4c5b27e6)
- W3C CSS
    - [style.css](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fbook-review-kelvinhere.herokuapp.com%2Fstatic%2Fcss%2Fstyle.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
    * ![CSS3](https://www.w3.org/Icons/valid-css)
    * ![SVG](https://www.w3.org/Icons/valid-css-blue)
 
- W3C Spell Checker
    - All pages checked through W3C Spell Checker
 
### Unit Testing
 
Unit testing was used on this project to quickly and efficiently test changes to code.  These tests in [testbookapp.py](https://github.com/KelvinHere/book-review-app/blob/master/testbookapp.py)
check that :-
- All of the apps CRUD operations can be carried out on a database.
- All routes take the user to the correct webpages and contain the required information from the database.
- All functions in [app.py](https://github.com/KelvinHere/book-review-app/blob/master/app.py) return the correct values.
- All tests were initially made to fail as to avoid false negatives.
 
On running the unittests in [testbookapp.py](https://github.com/KelvinHere/book-review-app/blob/master/testbookapp.py) the database is switched to an empty local database, some
setup is required if running locally, as explained below in [Writing your own unittests](#writing-your-own-unittests).  This allows
the app to be tested end to end and stops the risk of the tests corrupting the live database.
 
An example of this end to end testing would be, testing the view that adds a book to the database.  The unittest posts imitation form data to the 'insert_book' view, the 'viewbooks' 
view is then called to render the viewbooks.html page where the form information added should be read from the database and be displayed.  The test asserts that all the book 
information that should be read from the database is present on the viewbooks.html output page.
 
The result of my unittests
From gitpod unit tests can be run by starting the local database `mongod --dbpath testdb`
Then running the tests `python3 -m unittest testbookapp.py -v`
- ![unittests](https://github.com/KelvinHere/book-review-app/blob/master/readme-files/testing/unittests.jpg "result of unit tests")
 
### Writing your own unittests
 
1. Follow the local deployment instructions in the ['Local Deployment' section of readme.md](https://github.com/KelvinHere/book-review-app/blob/master/README.md#deployment)
 
2. [Install MongoDB Community Edition](https://www.mongodb.com/try/download/community?tck=docs_server), binaries only dont worry about setting it as a service
 
3. Add the following enviromental variables to env&#46;py
    - `os.environ.setdefault("IP", "0.0.0.0")`
    - `os.environ.setdefault("PORT", 5000)`
 
3. From your IDE load the Book Review App
 
4. Start the test database from the terminal in your deployed app directory.  Run `mongod` with the following arguments `--dbpath testdb` for example
    * `C:\MongoDB\Server\4.4\bin\mongod.exe --dbpath testdb`
    * Documentation to help running mongod [link here](https://docs.mongodb.com/manual/reference/program/mongod.exe/)
 
5. Add your new tests to [testbookapp.py](https://github.com/KelvinHere/book-review-app/blob/master/testbookapp.py)
 
6. Run the unit tests from the terminal with `python3 -m unittest testbookapp.py` (use `py` instead of `python3` if you are using windows 10)
 
7. Optionally add the verbose argument `-v` to the command above to display more information on the tests running
 
## Manual Testing
 
### Database Testing
Each feature of the apps CRUD operations have been tested manually
- A book can be added
- A book can be deleted
- A book can be edited
- Books display on the home page
* A review can be added
* A review can be deleted
* A review can be edited
* Reviews can be viewed by book
- Books can be sorted by Title, ascending or descending
- Books can be sorted by Author, ascending or descending
- Books can be sorted by rating, ascending or descending
 
### Navigation Testing
- Every route and button has been checked and it takes you to the correct destination.
 
### Incorrect Form Submissions
For each of the forms in this app an attempt was made to submit an incomplete  or incorrect form each time missing
or using an incorrect type in each field.  Each time a field was missing the correct error message was displayed to
inform the user to complete the field.  Each time an incorrect type was entered into a field the correct error message
was displayed. 
 
This test was performed on :-
- Add book
- Edit book
- Add review
- Edit review
 
### Scoring Tests
Manual tests were carried out on the scoring system to make sure the scores were being calculated
correctly.  Tests below, each test was carried out on a newly input book.
 
- **Test initial score** - Passed
    - Book added
        - Score 0
 
- **Test add review** - Passed
    - Add book
    - Add 5 Star review
        - Book score 5
        - Review score 5
 
- **Test add multiple reviews** - Passed
    - Add book
    - Add 0 star review
    - Add 5 star review
        - Review score 0
        - Review score 5
        - Book score 2.5
 
- **Test update review** - Passed
    - Add book
    - Add 4 star review
        - Review score 4
        - Book score 4
            - Update review to 2 star
                - Review score 2
                - Book score 2
 
- **Test delete review** - Passed
    - Add book
    - Add review 2 star
    - Add review 4 star
        - Review score 2
        - Review score 4
        - Book score 3
            - Delete 4 star review
                - Review score 2
                - Book score 2
 
### UI Testing
The app has been tested to display correctly on :-
 
- Mobile
    - Firefox
    - Chrome
- Desktop
    - Firefox
    - Chrome
    - Opera
    - Edge
 
For each of these, all the functionality of the app was tested to work as shown in
the manual testing sections above.
 
The app was tested on different resolution devices to check its responsiveness.
 
- Small - 1 column of books
- Medium - 2 columns of books
- Large - 3 columns of books
 
Regarding mobile
- The UI was tested in Chrome Inspection tools, using each of its in built device emulators.
- I checked that mobile landscape and portrait responsiveness works changing column width if necessary.
- That all text was comfortable to read on smaller screens.
 
The app was user tested by friends and family on mobile and desktop, unusual situations can usually be 
found under these testing circumstances.
 
## User Story Testing
Answered user stories from the [User Stories](https://github.com/KelvinHere/book-review-app/blob/master/README.md#user-stories) section of [readme.md](https://github.com/KelvinHere/book-review-app/blob/master/README.md)
 
As a user I want
1. **To find out more about a book quickly, because I don't have much time.**
- A user can instantly see an average review score of a book and how many reviews have been written about it from
its un-revealed card.  If they want to know more or see a description they can click the cover to reveal that
information.
 
2. **To read reviews on a book I think I may like, because I want opinions before I buy it.**
- A user can click read reviews from a books card to see each review and its rating.
 
3. **To buy a book I just read reviews on, because it confirmed I will probably like it.**
- A user can click an affiliate link to buy the book from its card revealed or unrevealed.
 
4. **To find the highest rated book, because I want to see what 'is in'.**
- A user can use the sort bar at the top of the home page to sort by rating high to low.
 
5. **To buy a book with the worst overall rating, because I enjoy b-movies more than I should.**
- A user can use the sort bar at the top of the home page to sort by rating low to high.
 
6. **To view all of an author's books, because I will probably enjoy another book of the same author.**
- A user can sort books by author in ascending or descending order to group books by author.
 
7. **To view titles in alphabetical order, because I kind of know what a book is called and this could help.**
- A user can sort books by title in ascending or descending order.
 
8. **To write a review on a book I have just read, because I want people to know how great/bad it was.**
- A user can click on a write review button on a books card (revealed or unrevealed) to write a review.
 
9. **To edit a review I just wrote, because I changed my mind on how I feel about it.**
- A user can find their review and click the edit button to update their review.
 
10. **To delete a review, because I don't want people knowing I have read this book.**
- A user can find their review and click the delete button to remove their review.
 
11. **To be able to create a book entry because it does not already exist and I want to review it.**
- A user can click the add book button on the top menu bar / dropdown menu or bottom of the view books
page.
 
12. **I want to update some incorrect information in a book's details.**
- A user can click the edit book button of a books card  to update any information about that book.
 
13. **To delete a book I created.**
- If a user wants to delete a book they created, they can do it from the edit book page with the delete book button.
 

