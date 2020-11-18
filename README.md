# Book Review App - Data centric development
 
****!Remove development server before deploying****
 
Book Review App
 
A book review app where users can read and write reviews on books, with 
links to buy these books.  If a book is not on the app a user can create
it.
 
* [Live link to site](https://book-review-kelvinhere.herokuapp.com/ 'Heroku live link to app')
* [This Repository](https://github.com/KelvinHere/book-review-app 'Github repository link')
 
## Contents
 
1. [**UX**](#ux)
   * [Project Purpose](#project-purpose)
   * [Wireframe Designs](#wireframe-designs)
   * [User Stories](#user-stories)
   * [Business Goals](#business-goals)
   * [Developer Goals](#developer-goals)
   * [Design Choices](#design-choices)   
       * [*General Design*](#general-design)
       * [*Colours and Fonts*](#colours-and-fonts)
2. [**Features**](#features)
   * [Existing Features](#existing-features)
       * [*Sorting*](#sorting)
       * [*Database*](#database)
       * [*Backend*](#backend)
       * [*Frontend*](#frontend)
   * [Future Features](#future-features)
       * [*Near Future*](#near-future)
       * [*Far Future*](#far-future)
3. * [**Changes during Development**](#changes-during-development)
4. * [**Testing**](#testing)
5. * [**Technologies Used**](#technologies-used)
6. * [**Deployment**](#deployment)
        * [Version Control](#version-control)
        * [Local Deployment](#local-deployment)
        * [Heroku Deployment](#heroku-deployment)
        * [Deployment with Gunicorn](#deployment-with-gunicorn)
7. * [**Credits**](#credits)
       * [Content](#content)
       * [Media](#media)
       * [Acknowledgements](#acknowledgements)
 
## UX
 
#### Project Purpose
 
The purpose of this project is to create an application where people can review books
they have read and find new books they might enjoy from a description and reviews.
 
#### Wireframe Designs
 
- The home page will responsively display book cards
![BookView](https://github.com/KelvinHere/book-review-app/blob/master/readme-files/wireframes/wireframe-home-s.jpg "Book view wireframe image")
- On clicking the book covers you will be shown a reveal with extra information
![RevealView](https://github.com/KelvinHere/book-review-app/blob/master/readme-files/wireframes/wireframe-reveal-s.jpg "Book view revealed wireframe image")
- Viewing reviews page
![ReviewsView](https://github.com/KelvinHere/book-review-app/blob/master/readme-files/wireframes/wireframe-reviews-s.jpg "View reviews wireframe image")
- All input forms will take the style below, this will cover adding or editing a book or review.
![FormView](https://github.com/KelvinHere/book-review-app/blob/master/readme-files/wireframes/wireframe-add-review-s.jpg "Form wireframe image")
 
#### User Stories
 
As a user I want
1. To find out more about a book quickly, because I don't have much time.
1. To read reviews on a book I think I may like, because I want opinions before I buy it.
1. To buy a book I just read reviews on, because it confirmed I will probably like it.
1. To find the highest rated book, because I want to see what 'is in'.
1. To buy a book with the worst overall rating, because I enjoy b-movies more than I should.
1. To view all of an author's books, because I will probably enjoy another book of the same author.
1. To view titles in alphabetical order, because I kind of know what a book is called and this could help.
1. To write a review on a book I have just read, because I want people to know how great/bad it was.
1. To edit a review I just wrote, because I changed my mind on how I feel about it.
1. To delete a review, because I don't want people knowing I have read this book.
1. To be able to create a book entry because it does not already exist and I want to review it.
1. I want to update some incorrect information in a book's details.
1. To delete a book I created.
 
#### Business Goals
 
The business purpose of this app is to engage the user with a list of books they can enjoy, 
the user can browse books, reviews and click affiliate links to buy books, earning the 
owner of the app money.
 
#### Developer Goals
 
Each feature must be well programmed, function properly and tested to be bug free.  This 
will display a professional use of the programming languages and test suite.
 
This project will display I have an understanding of how to integrate a database into an app
and perform CRUD operations on the database from a frontend.
 
To show an understanding of Flask, Python, MongoDB, Javascript, jQuery,
Materialize, HTML, CSS, Unittests and how they all interact to form a final product.
 
#### Design Choices
 
##### General Design
 
Materialize with cards was used to create an app that will be instantly familiar with anyone
who has used a google product, allowing a large amount of users to instantly begin browsing
the app.
 
The design was made minimal with a very clean look to avoid information overload on smaller
screens and allow the book covers to draw most attention.  The site is made mobile first and
to be responsive to screen size, allowing larger screens to show more books at once.
 
As the database of books grows, it will be harder to find a book you may be looking for, so
a search by title, rating and author was introduced.
 
Navigation and selection are consistent throughout the app.
 
##### Colours and Fonts
 
**Font 1** - The font 'Oswald' was used in busy areas where needed and the branding, as it is heavy enough 
to draw attention to itself even if there is a lot of other text on the screen, such as a synopsis.
 
**Font 2** - For sub text, such as reviews and descriptions I used the font 'Quicksand', this font is easy to read and
looks 'tidy' helping the app look professional.
 
**Colours** - For the main site colours I used Teal and White, I went two tone as I wanted the color focus to be on the
book covers and help the star ratings stand out.  The majority of the site is shadowed cards with Teal
for the header and most buttons.  The only exceptions to this are the edit button (yellow) and the delete
buttons (red), these stand out warning colours should give the user an idea they might want to think
before clicking.
 
## Features
 
### Existing Features
 
Using this app you will be able to  :-
- Create
    - A book
    - A review with a score
 
- Read 
    - A list of books and sort them by Title, Author and Rating
    - The average score from a book
    - A list of reviews and their scores
 
- Update
    - A books information
    - A review in a book
 
- Delete 
    - A book from the database
    - A review from a book
 
#### Sorting
* Sort feature allows book sorting ascending and descending by rating, author or title.
 
#### Database
* A book will be given an average score using its reviews.
* A book's average score only updates when a new review for that book is added.
* Add book button allows a user to create a new book entry into the database.
* Delete book button allows a user to delete a book and its reviews from the database.
* Write review button allows a review and star rating to be added to a book in the database.
* Edit review button allows a user to edit the contents and rating of a review.
* Delete review button allows a user to remove a review from a book.
* Book cards are automatically created via information from the database.
 
#### Backend
* The review score when adding a review is checked and capped between 0 and 10, if a user edits the form to give the book a score of 100 it will be reduced to 10, or -55 will be turned to 0, avoiding review score manipulation.
* The reviews button also displays how many reviews there are for a book example "15 Reviews".
* Book titles and author names are turned lower case for future proofing the app to avoid duplicate books and allow easier searches.
 
#### Frontend
* The website header title will always take you to the home page and keep your sort settings.
* The nav buttons at the top of the page will collapse into an icon on smaller screens.
* The book cards are 1 column wide on mobile, 2 columns on medium res tablets and 3 columns on high res desktops.
* Books will have a link to buy, which will take you to a specified external web page.
* Book cards have "Title", "Author", "Rating" as well as a cover to give users quick relevant information.
* Book cards have buttons that show the number of reviews, an option to write a review or buy for quick access.
* Clicking a book cover will reveal its synopsis and an extra button to edit the book.
* Sort feature is a collapsable menu which takes up little space when not used.
* If books are sorted by rating and have the same star rating they are sub sorted by how many reviews they have.
 
 
### Changes during development
 
During development a new useful feature was added:-
After sorting books by rating, also sub-sort them by number of reviews.
 
This would allow books that have a high rating and lots of reviews rank higher than books with just one high rating review.  But this feature
needed another field to be added to all the documents.  I wrote a small script that would update all documents of my book collection with the
new field **review_num**, after this all books in the books collection would be iterated over and have the length of the reviews array assigned
to the review_num field.
 
An extra method was created to increment or decrement the review_num each time a review is added or removed.
 
This was done after using mongodump.exe to create a backup of the database.
 
The app was changed from the default Flask server to use Gunicorn as it was recommended not to use the default Flask server during production 
by the Flask documentation.
 
### Future Features
 
##### Near Future
 
- Add sort by genre feature
- Add book and author search feature
 
##### Far Future
 
- Add login system so
    1. Users can only edit and delete their own reviews
    1. Only an administrator can delete a book
 
## Testing
 
[Testing Documentation](https://github.com/KelvinHere/book-review-app/blob/master/testing.md) - Documentation for testing
 
## Technologies Used
 
- **HTML5/CSS3**
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Web framework
- [MongoDB](www.mongodb.com) - NoSQL Database
- [Materialize](https://materializecss.com/) - Frontend framework
- [Unittest](https://docs.python.org/3/library/unittest.html) - Python unit testing framework
- [Python](https://www.python.org/) Programming language
- [Javascript](https://www.javascript.com/) Programming language
- [jQuery](https://jquery.com/) - JavaScript Library
- [Heroku](https://www.heroku.com/) - Cloud Application Platform
- [Gunicorn](https://gunicorn.org/) - Python WSGI HTTP Server
- [Gitpod](https://www.gitpod.com) - Development environment
- [Git](https://git-scm.com/) - Version control
- [Github](https://www.github.com) - Code hosting platform
- [Draw.io](https://www.draw.io/) -Prototyping wireframing tool
- [Photoshop CS](https://www.adobe.com/) - Image editing software
 
## Deployment
 
This project was created in [GitPod](https://gitpod.io/) with the [Code Institute template](https://github.com/Code-Institute-Org/gitpod-full-template) and version controlled through 'Git', the project was committed and pushed to [GitHub](https://github.com/).
The project was then deployed to [Heroku](https://www.heroku.com/).
 
### Version Control
* After files are created or modified they are committed to a GitHub repository using git by :-
    - adding the modified files locally using `git add .` or `git add filename.extension`
    - commiting the modified files with a message of changes using `git commit -m "changes here"`
    - pushing the new commit to the master branch on GitHub repository with `git push`
    - updating an out of date local branch with `git fetch origin` and pulling changes with `git pull origin`
 
### Local Deployment
 
* Requirements
    - An Atlas MongoDB account with a database called `book_app_db` which has the collections `books` and `genres`
    - An Atlas user profile called `root` with read/write access to the `book_app_db` database
    - Local computer with an IDE, Python 3.8.6, git and pip.
 
Clone this repository to your local workspace :-
 
1. Open the [Book Review App](https://github.com/KelvinHere/book-review-app) repository.
2. Click the 'Code' button and then copy the 'Clone with HTTPS' URL.
3. From your IDE open a terminal.
4. From inside the directory you want the clone, type `git clone` and paste the URL you copied from GitHub then press enter.  Example below.
 
- `git clone https://github.com/KelvinHere/book-review-app.git`
 
5. Cloning will be completed when your terminal is waiting for its next command.
6. More information or changes in the cloning procedure at this link [Git Clone](https://github.com/git-guides/git-clone).
7. Make sure pip is up to date `pip install --upgrade pip`
8. Install the app requirements `pip install -r requirements.txt`
9. Link the app to your Atlas MongoDb account through an environment variable
    - Login to Atlas MongoDb
    - Click Clusters > Overview > Connect
    - Click 'connect your application'
    - Select your driver and version ie 'Python' '3.6 or later'
    - Copy the given "Connection String"
    - Create env.py in the root of the book app workspace and add the code below
        - `import os`
        - `os.environ.setdefault()`
    - Paste the Connection String inside this and replace the <> markers with your Atlas details
    - The contents of env.py should look similar to the code below
        - `import os`
        - `os.environ.setdefault("MONGO_URI", "mongodb+srv://root:MYPASSWORD@firstcluster.er9ib.mongodb.net/book_app_db?retryWrites=true&w=majority")`
10. Run `python3 app.py` to start the app
11. Open the given link in your IDE and you will be connected to your Atlas book_app_db and can start adding books.
 
 
### Heroku Deployment
 
The deployed version of 'Book Review' is hosted on Heroku and was deployed with the following steps.
 
* Requirements
    - A locally deployed version of the Book Review App from the instructions above
    - A Heroku account
    - [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) installed locally, instructions in [this link](https://devcenter.heroku.com/articles/heroku-cli)
 
1. Create a Heroku account and login
2. Click New > App
3. Give the app a name, select a region and create the app
4. Setup enviromental variables in Heroku
    - Select your app in Heroku and click settings
    - Under Config Vars set up the key value pairs as below
    - IP = 0.0.0.0
    - PORT = 5000
    - MONGO_URI = The Atlas MongoDb Connection String as explained in [local deployment](#local-deployment) above
5. Login to Heroku from your terminal with `heroku login -i` then follow prompts
6. `pip freeze --local > requirements.txt` to update your requirements.txt in case of new requirements
7. `git init` if you have not initialised your git repo
8. `heroku git:remote -a YOUR_APP_NAME` to add remote
9. `git add .` and `git commit` your changes
10. `git push heroku master` to deploy to Heroku
11. From the Heroku website
12. You many need to click 'More' in the Heroku app and select 'Restart all dynos'
13. Click 'Open App' 
14. The App should now be running through Heroku
 
### Deployment with Gunicorn
 
As specified in the [Flask deployment](https://flask.palletsprojects.com/en/1.1.x/deploying/#deployment) documentation, Flasks built in server is not suitable for production as it does not scale well.
I decided to deploy to Heroku with Gunicorn as the server, deployment instructions on the Heroku website in [this link](https://devcenter.heroku.com/articles/python-gunicorn).
 
A quick summary of instructions with basic configuration below.
 
1. Install gunicorn with `pip install gunicorn`
2. `pip freeze --local > requirements.txt` to update your requirements.txt to include gunicorn
3. Create a point of entry for gunicorn, I created a file called [wsgi.py](https://github.com/KelvinHere/book-review-app/blob/master/wsgi.py) click to see its contents
4. Update the procfile to `web: gunicorn wsgi:app` so Heroku can launch the app through gunicorn
5. Log into heroku CLI and run `heroku config:set WEB_CONCURRENCY=3` to add an environmental variable into the app on heroku to take advantage of concurrency
6. Commit your changes as before
7. Push to heroku with `git push heroku master`
8. The app should now be on heroku running on gunicorn
 
## Credits
### Content
 
- This project was created by KelvinHere
 
### Media
 
- Book covers - From various authors
- Star images - KelvinHere
 
### Acknowledgements
 
* [Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/).
* [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04) - For deployment information on gunicorn
* [Code Institute](https://codeinstitute.net/).
* My mentor Spencer.

