# Any num as sum of three palindromes using ML

According to [this](https://arxiv.org/abs/1602.06208) research paper from arxiv -
***"Every positive integer is a sum of three palindromes"***
Now the research paper dives deep into it using some of lagrange's theorem and other techniques which you can check out yourself

But this has been already put into action by ***Lewix Baxter*** on [this amazing website](http://www.rnta.eu/cgi-bin/three_palindromes/pal3.py) 

## My Approach
I have always thought about using an overfitted model for something , There should be something it should be good for right
so my approach is to scrape data from that site above to make a huge dataset of number and its respective pallindromes and train some multi-output regression models specifically where I would want to overfit on the training set, as it has a mathematical formula behind it to solve as represented in the research paper, that's why I think a deep neural network can reproduce this same thing if we overfit it.

## Work in progress!!
This project is still currently work in progress, because the data scraping from that site is really slow and to make a huge dataset it will take more time
I am completing the dataset currently using a [script](https://github.com/biswaroop1547/Any_num_as_sum_of_three_palindromes_using_ML/blob/master/test.py) to scrape data from the website which I wrote in Python3 

Will complete this project soon to show that overfitting is not good for nothing :wink:
And to show how powerful ML can be and would surely reach an appropriate Conclusion! :smile:
