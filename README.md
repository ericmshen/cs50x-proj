#In your Best Interest

is a simple web calculator, which, as the title suggests, performs interest-related calculations.
Currently it offers four options for calculation: simple interest, compound interest, annuities
(wherein money is deposited and compounded periodically), and a loan calculator (with the option
to specify any percentage down, to simulate a mortgage).

The website uses Flask as a web server and uses Bootstrap elements in its user interface.Clicking
on each of the four options—simple and compound interest, annuity, and loan/mortgage—via a navbar
brings the viewer to a form where they can specify the details of their calculation. If the
calculate button is pressed and the values are confirmed to be valid, the form's values are fed
into a function in application.py that gives out the results and formats them as currency. The
formulae for compound interest, annuities and mortgages is well-documented. These results are
presented in a new page.

The extra "touch" that distinguishes this calculator from any other is that it also provides a
chart graphic where users can make sense of the data. This is done using some Flask trickery and
the Chartist.js library. For instance, in calculating an annuity, the number of total deposits is
calculated. For each deposit, one list stores how much money has been totally deposited, while
another stores the total interest at that point. These lists are then passed as arguments when
the HTML is rendered into the JS function that creates the chart. The result is a scrollable bar
chart, where each bar displays the total balance of the annuity at a certain deposit time, as well
as how much of that balance is money from deposits and money from interest. The same idea applies
to the other calculation options—e.g. for the "loan/mortgage" option, the chart displays how much
of each payment goes toward paying off interest and paying off the principal for each payment.
Some jQuery also displays a tooltip that shows the value of each bar when the mouse hovers over it.

Creating this project helped me get moreo comfortable with Bootstrap and also JS (especially with
using libraries), ultimately helping me brighten up a run-of-the-mill calculator with responsive
and dynamically-generated charts that help illustrate numbers in a graphical and interactive
format.
