# Baby_Names_Visualization :

## Project Goal <hr/>

The goal of the project is to visualize the most popular names in the USA (by state or per year) from 1980 to 2018.

## Work Process <hr/>

#### ETL: EXTRACT - TRANSFORM - LOAD

* Extraction:
  We extracted our first tables from the social security webside as text files. The tables were diapached by state since we chose to work with the popula name by state, we had rougthly 52 tables in total. Our second table is the USA latitude and longitude for state that we got on Kaggle.


    + Sources:
  
        https://www.kaggle.com/washimahmed/usa-latlong-for-state-abbreviations

        https://www.ssa.gov/oact/babynames/decades/century.html

* Transform:
  
Our data was a report of the US babies names by state from 1910 to 2018 and hopefully we didn't have empty rows. The  work consisted of cleaning the data by converting the text files to csv, removing unnecessary columns, combining the table, and selecting the desired data to work with.

* Load:
we used postgresql as our database

### Heroku-Postgres <hr/>

This step consisted of uploading our data in the cloud through the connection of heroku  with postgres 


### Working with Python and Flash-Sqlalchemy 


Sections
Headers
Quotes
Emphasis
Horizontal Rule
Lists
Links
Images
Code
Tables
Custom HTML
Custom CSS
Additional Resources
Headers
Headers are defined by the '#'symbol. One '#' for H1, two for H2, etc.

TODO. Create an H1

TODO. Create an H2

TODO. Create an H3

TODO. Create an H4

Quotes
Quotes are defined by the '>' symbol

TODO. Create a quote

You can combine a header with a quote.

TODO. Create an H2 Quote

Emphasis
Add emphasis with asterisks '*' and underscores '_' Two before and after (no spaces) a section of texts makes it bold

One before and after (no spaces) a section of texts makes it bold

You can also put Bold and Italicized text inline by surrounding a group of words.

TODO. Create a bold sentence, an italicized sentence, and a sentence with both bold and italicized text inline

Horizontal Rule
A horizontal rule gives a visible line break. You can create one by putting three or more hypens, asterisks, or underscores (-, *, _).

For what it's worth, I prefer dashes...

TODO Create a horizontal rule

Lists
Create unordered lists using '-', '*', '+,

You can create sublists by indenting

Create ordered lists using a number prefix

TODO Create an unordered list of your 5 favorite TV Shows

TODO Create an ordered list of your top 5 Movies

Links
Create a link by surrounding it with angle bracket

Create a link with text by surrounding text with brackets, [], and link immediately following with parenthesis ()

TODO Create a link to your website, twitter, or github. with no text

TODO Create a link with text to your website, twitter, or github

What if you needed to reuse a link several times? Well, you could copy and paste that link each time. That means, if you need to update the link, you will have to do it each time its used. There's a better way!

Create reference style links by defining your link with the a 'key' inside of brackets, colon, space, and the link

Then use the reference style link by using your text inside of brackets followed by the link 'key' inside of bracket.

TODO Create a reference link to your website and reference it three times

You can also link to other locations on your markdown page. Remember, your MarkDown will get converted to HTML, so you can, in theory, use a anchor tag to link to an element with a specific ID. You can find an example of this in the list of sections at the top of this document.

When we create a header tag for example, it implicitly creates an id property.

Ex '# Header' becomes <h1 id="header">Header</h1>

Names will be converted to ids by replacing spaces with hyphens and uppercase letters with lowercase letters (think css naming convention).

Ex 'Header Info' becomes header-info

TODO Create a link to another part of your page.

Images
Defining an image is similar to defining a link, except you prefix it with '!'

Just like links, you can define images by reference in the same format.

Define the reference

Use the reference

TODO Create a reference link to your profile picture and then reference it.

Code
You can do inline code with backticks (``)

TODO Display a line of text with inline code

You can do blocks of code by surroung it with 3 backticks ( )

TODO Display a block of code from your favorite language

The above does not give language specific highlighting. You can specify the programming language immediately following the opening 3 backticks. You Should see a difference in highliting!

TODO Display a block of code from your favorite language while specifying the language

Tables
Tables are useful for displaying rows and columns of data. Column headers can be defined in between pipes (|). Headers are separated from table content with a row of dashes (-) (still separated by pipes), and there must be at least 3 dashes between each header. The row data follows beneath (still separated by pipes).

The column definitions and row definitions do not have to have the exact same width sizes, but it would be much more readable. Notice the output of the following two tables are the same, but the second (the raw markdown) is much more readable.

TODO Create a table with three columns and two rows

You can also align (Center, left, right) the text in a column by using colons (:) in the line breaks between headers and rows. No colon means the default left alignment. Colons on each side signifies center alignment. And a trailing colon means right alignment.

TODO Create a table with three columns, one aligned left, one aligned center, and one aligned right

Custom HTML
Since MarkDown gets automatically converted to HTML, you can add raw HTML directly to your MarkDown.

<p>Sample HTML Div</p>
Creates this

Sample HTML Div

TODO If you are comfortable with HTML, add some raw HTML.

Custom CSS
You can also add custom CSS to your MarkDown to add additional styling to your document. You can also include CSS by including a style tag.

    <style>
        body {
            color:red;
        }
    </style>
TODO If you are comfortable with CSS, give your page some style.

Additional Resources
Markdown Cheat Sheet - Adam P on Github
Daring Fireball Markdown Syntax
MarkDown in Visual Studio Code
The main goal of MarkDown is to be easily written and easily read. It uses "plain text" formatting and can be converted to HTML. The most common use case I've come across to use Markdown is for ReadMe files, used, for example, for Github repos. Markdown can also be used to create email.

Markdown, in comparison to HTML, is much simpler to read and write. The average person can typically understand markdown and would be able to learn and write it much quicker than HTML.

Specifically, Visual Studio Code uses the CommonMark Markdown specification.

Sections
Headers
Quotes
Emphasis
Horizontal Rule
Lists
Links
Images
Code
Tables
Custom HTML
Custom CSS
Additional Resources
Headers
Headers are defined by the '#'symbol. One '#' for H1, two for H2, etc.

TODO. Create an H1

TODO. Create an H2

TODO. Create an H3

TODO. Create an H4

Quotes
Quotes are defined by the '>' symbol

TODO. Create a quote

You can combine a header with a quote.

TODO. Create an H2 Quote

Emphasis
Add emphasis with asterisks '*' and underscores '_' Two before and after (no spaces) a section of texts makes it bold

One before and after (no spaces) a section of texts makes it bold

You can also put Bold and Italicized text inline by surrounding a group of words.

TODO. Create a bold sentence, an italicized sentence, and a sentence with both bold and italicized text inline

Horizontal Rule
A horizontal rule gives a visible line break. You can create one by putting three or more hypens, asterisks, or underscores (-, *, _).

For what it's worth, I prefer dashes...

TODO Create a horizontal rule

Lists
Create unordered lists using '-', '*', '+,

You can create sublists by indenting

Create ordered lists using a number prefix

TODO Create an unordered list of your 5 favorite TV Shows

TODO Create an ordered list of your top 5 Movies

Links
Create a link by surrounding it with angle bracket

Create a link with text by surrounding text with brackets, [], and link immediately following with parenthesis ()

TODO Create a link to your website, twitter, or github. with no text

TODO Create a link with text to your website, twitter, or github

What if you needed to reuse a link several times? Well, you could copy and paste that link each time. That means, if you need to update the link, you will have to do it each time its used. There's a better way!

Create reference style links by defining your link with the a 'key' inside of brackets, colon, space, and the link

Then use the reference style link by using your text inside of brackets followed by the link 'key' inside of bracket.

TODO Create a reference link to your website and reference it three times

You can also link to other locations on your markdown page. Remember, your MarkDown will get converted to HTML, so you can, in theory, use a anchor tag to link to an element with a specific ID. You can find an example of this in the list of sections at the top of this document.

When we create a header tag for example, it implicitly creates an id property.

Ex '# Header' becomes <h1 id="header">Header</h1>

Names will be converted to ids by replacing spaces with hyphens and uppercase letters with lowercase letters (think css naming convention).

Ex 'Header Info' becomes header-info

TODO Create a link to another part of your page.

Images
Defining an image is similar to defining a link, except you prefix it with '!'

Just like links, you can define images by reference in the same format.

Define the reference

Use the reference

TODO Create a reference link to your profile picture and then reference it.

Code
You can do inline code with backticks (``)

TODO Display a line of text with inline code

You can do blocks of code by surroung it with 3 backticks ( )

TODO Display a block of code from your favorite language

The above does not give language specific highlighting. You can specify the programming language immediately following the opening 3 backticks. You Should see a difference in highliting!

TODO Display a block of code from your favorite language while specifying the language

Tables
Tables are useful for displaying rows and columns of data. Column headers can be defined in between pipes (|). Headers are separated from table content with a row of dashes (-) (still separated by pipes), and there must be at least 3 dashes between each header. The row data follows beneath (still separated by pipes).

The column definitions and row definitions do not have to have the exact same width sizes, but it would be much more readable. Notice the output of the following two tables are the same, but the second (the raw markdown) is much more readable.

TODO Create a table with three columns and two rows

You can also align (Center, left, right) the text in a column by using colons (:) in the line breaks between headers and rows. No colon means the default left alignment. Colons on each side signifies center alignment. And a trailing colon means right alignment.

TODO Create a table with three columns, one aligned left, one aligned center, and one aligned right

Custom HTML
Since MarkDown gets automatically converted to HTML, you can add raw HTML directly to your MarkDown.

<p>Sample HTML Div</p>
Creates this

Sample HTML Div

TODO If you are comfortable with HTML, add some raw HTML.

Custom CSS
You can also add custom CSS to your MarkDown to add additional styling to your document. You can also include CSS by including a style tag.

    <style>
        body {
            color:red;
        }
    </style>
TODO If you are comfortable with CSS, give your page some style.

Additional Resources
Markdown Cheat Sheet - Adam P on Github
Daring Fireball Markdown Syntax
MarkDown in Visual Studio Code