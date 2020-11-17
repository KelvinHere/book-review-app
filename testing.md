# Testing the Book Review app

## Automated Tests

### Code Validation

This projects code has been validated through various services

- W3C Markup
- W3C CSS
- W3C Spellchecker



### Unit Testing

Unit testing was used on this project to quickly and efficently test changes to code.  These tests in [testbookapp.py](https://github.com/KelvinHere/book-review-app/blob/master/testbookapp.py)
check that :-
- All CRUD operations can be carried out on a database and that that database information makes it to the webpages it needs to get to. 
- All routes take the user to the correct webpages and contain the required information from the database
- All functions in app.py return the correct values

On running the unittests in [testbookapp.py](https://github.com/KelvinHere/book-review-app/blob/master/testbookapp.py) the database is switched to an empty local database, some
setup is required if running locally, as explained below in [Writing your own unittests on a local deployment](#writing-your-own-unittests-on-a-local-deployment).  This allows
the app to be tested end to end and stops the risk of the tests corrupting the live database.

An example of this end to end testing would be, testing the view that adds a book to the database.  The unittest posts immitation form data to the insert_book view, the viewbooks view 
is then called to render the viewbooks.html page where this information should now be displayed and the test asserts that all the book information that should be pulled from the 
database is displayed on the output page.

### Writing your own unittests on a local deployment

1. Follow the local deployment instructions in the ['Local Deployment' section of readme.md](https://github.com/KelvinHere/book-review-app/blob/master/README.md#deployment)

2. [Install MongoDB Community Edition](https://www.mongodb.com/try/download/community?tck=docs_server) binaries only dont worry about setting it as a service

3. Add the following enviromental varialbes to env.py
    - `os.environ.setdefault("IP", "0.0.0.0")`
    - `os.environ.setdefault("PORT", 5000)`

3. Start your locally deployed book review application

4. Start the test database from the terminal in your deployed app directory.  Run `mongod` with the following arguments `--dbpath testdb` for example
* `C:\MongoDB\Server\4.4\bin\mongod.exe --dbpath testdb`
* Documentation to help running mongod [link here](https://docs.mongodb.com/manual/reference/program/mongod.exe/`)

5. Add your new tests to testbookapp.py in the deployed app directory

6. Run the unit tests from the terminal in your app directory with the following command `python3 -m unittest testbookapp.py` (use `py` instead of `python3` if you are using windows 10)

7. Optionally add the verbose argument `-v` to the command above to display more information on the tests running

## Manual Testing

Manual testing of all CRUD operations have been tested
    - 

## User Story Testing

As a user I want
1. To find out more about a book quickly, because I don't have much time.
A user can instantly see an average review score of a book and how many reviews have been written about it from
its un-reavealed card.  If they want to know more or see a description they can click the cover to reveal that
information.

1. To read reviews on a book I think I may like, because I want opinions before I buy it.
A user can click read reviews from a books card to see each review and its rating.

1. To buy a book I just read reviews on, because it confirmed I will probably like it.
A user can click an affiliate link to buy the book from its card revealed or unrevealed.

1. To find the highest rated book, because I want to see what 'is in'.
A user can use the sort bar at the top of the home page to sort by rating high to low.

1. To buy a book with the worst overall rating, because I enjoy b-movies more than I should.
A user can use the sort bar at the top of the home page to sort by rating low to high.

1. To view all of an authors books, because I will probably enjoy another book of the same author.
A user can sort books by author in ascending or descending order to group books by author.

1. To view titles in alphabetical order, becuase I kind of know what a book is called and this could help.
A user can sort books by title in ascending or descending order.

1. To write a review on a book I have just read, because I want people to know how great/bad it was.
A user can click on a write review button on a books card (revealed or unrevealed) to write a review.

1. To edit a review I just wrote, because I changed my mind on how I feel about it.
A user can find their review and click the edit button to update their review.

1. To delete a review, because I don't want people knowing I have read this book.
A user can find their review and click the delete button to remove their review.

1. To be able to create a book entry because it does not already exist and I want to review it.
A user can click the add book button on the top menu bar / dropdown menu or bottom of the view books
page.

1. I want to update some incorrect information in a books details.
A user can click the edit book button of a books card  to update any information about that book.

1. To delete a book I created.
If a user wants to delete a book they created, they can do it from the edit book page with the delete book button.