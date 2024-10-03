
# INTRO to R

```
ls() # function in R lists all the objects (e.g., variables, dataframes, functions) currently stored in env

x <- rnorm(50) # random numbers mean=0 sd=1
y <- x+rnorm(50,mean=50,sd=.1)

cor(x,y) # correlation

mean(x)

sd(x)

mm <- matrix(1:16,nrow=4,ncol=4) # creating a matrix

## subsetting/indexing etc # [row, column]
mm[2,] # row 2
mm[,2] # column 2

mm[,c(1,3)] # first and 3rd cols
mm[,-c(1,3)] # removes 1st and 3rd cols

mm[3:4, 1:2]

## reading CSV
college <- read.csv("../data/College.csv")

## overview of dataset
head(college) # shows frist 6 rows
dim(college)
summary(college)

names(college) # column names
str(college) # structure

## subset data
private <- df[df$Private=="Yes",] # rows where the Private col is Yes
private <- subset(df,Private=="Yes") # another way

## select columns
df2 <- df[,c("X","Private")]

df3 <- df[order(df$Private),]

```

## DPLYR: another tool for data manipulation

```
library(dplyr)
browseVignettes("dplyr")

## dplyr aims to provide a function for each basic verb of data manipulating:
## (1) filter() (and slice())
## (2) arrange()
## (3) select() (and rename())
## (4) distinct()
## (5) mutate() (and transmute())
## (6) summarise()
## sample_n() and sample_frac()

glimpse(college)
glimpse(df)
summary(df)

## (1) "filter rows with filter()"
## first parameter is the data frame, then the conditions
filter(df, Private=="Yes")
filter(df, Private=="Yes" & Grad.Rate > 70)
filter(df, Private=="Yes" & Grad.Rate >= 70)


## (2) "select columns with select()"
## first parameter is the data frame, the remaining are column names
select(df, X, Private, S.F.Ratio, Grad.Rate, Top10perc)


## (3) "arrange rows with arrange()"
## first parameter is the data frame
arrange(df, Private)
arrange(df, desc(Private))


x %>% f(y) turns into f(x, y)

## (4) "extract distinct (unique) rows"
select(df, S.F.Ratio)

distinct(select(df, S.F.Ratio))

dim(distinct(select(df, Agency.Name)))


## (5) "add new columns with mutate()"

mutate(df, cost=Personal+Books)

dfx <- select(df,Personal,Books)
dfx <- mutate(dfx, cost=Personal+Books)
dfx


## (6) "summarise values with summarise()" [minimizes output]
## summarise() "reduces" the size of the output
summarise(df, books=sum(Books))
summarise(df, mean.tuition=mean(Outstate))


## summarise() is really powerful when working in groups
dfx <- group_by(df, Private)
dfx <- summarise(dfx, mean.tuition=mean(Outstate))
dfx


dfx <- group_by(df, Private)
dfx <- summarise(dfx, mean.books=mean(Books))
dfx

dfx <- group_by(df, Private)
dfx <- summarise(dfx, count=n()) # counts the number of rows each group
dfx

```

## Histogram
- single feature
- displays the shape of the distribution

jitterbox plot


```
## ============================================================================
## BASE R
## ============================================================================

plot(college$S.F.Ratio, college$Grad.Rate)
title("College graduation rate vs. Student-faculty ratio")

hist(college$Grad.Rate)
hist(college$S.F.Ratio)


s1 <- college[,c(16:19)]
pairs(s1)
```

## Plot

```

## ============================================================================
## BASE R
## ============================================================================

plot(college$S.F.Ratio, college$Grad.Rate)
title("College graduation rate vs. Student-faculty ratio")

hist(college$Grad.Rate)
hist(college$S.F.Ratio)


s1 <- college[,c(16:19)]
pairs(s1)



## ============================================================================
## ggplot2: another tool for R graphics
## ============================================================================

## "ggplot2 is designed to work in a layered fashion, starting with a
## layer showing the raw data then adding layers of annotation and
## statistical summaries."

## examples: ../docs/ggplot2-samples.pdf


library(ggplot2)
college <- read.csv("../data/College.csv")

## BASIC PLOTS

## ggplot2:
qplot(college$S.F.Ratio, college$Grad.Rate)
qplot(S.F.Ratio, Grad.Rate, data = college)

qplot(S.F.Ratio, Grad.Rate, data = college, colour=Private)

## add layers with "+"
qplot(S.F.Ratio, Grad.Rate, data = college, colour=Private) +
    ggtitle("College graduation rate vs. Student-faculty ratio")


## histograms are univariate: one variable required
qplot(Grad.Rate, data = college, geom="histogram")
qplot(Grad.Rate, data = college, geom="histogram", binwidth = 2)


## USING ggplot() function and CUSTOMIZING PLOTS
## aes = aesthetics
p <- ggplot(college, aes(x=S.F.Ratio, y=Grad.Rate))

p + geom_point()
p + geom_point(aes(colour = Private))
##p + geom_point(colour = Private) 
p + geom_point(colour = "green")


## nice palette
p + geom_point(aes(colour = Private)) + scale_color_brewer()

p + geom_point(aes(colour = Private)) +
    scale_color_brewer(type="qual", palette=2)

## variations on histogram
ggplot(college) +
    geom_histogram(aes(x=S.F.Ratio))

p <- ggplot(college, aes(x=S.F.Ratio))

p + geom_histogram()
p + stat_bin(geom="area")
p + stat_bin(geom="point")
p + stat_bin(geom="line")


## OVERLAYS
## The box plot (a.k.a. box and whisker diagram) is a standardized way of displaying the distribution of 
## data based on the five number summary: minimum, first quartile, median, third quartile, and maximum.
## http://www.physics.csbsju.edu/stats/box2.html
qplot(Private, Grad.Rate, data = college)
qplot(Private, Grad.Rate, data = college, geom="jitter")
qplot(Private, Grad.Rate, data = college, geom=c("jitter", "boxplot"))
qplot(Private, Grad.Rate, data = college, geom=c("boxplot", "jitter"))

p <- ggplot(college, aes(x=Private, y=Grad.Rate))

## documentation example: http://docs.ggplot2.org/current/geom_boxplot.html
p + geom_point()
p + geom_boxplot() + geom_jitter()
p + geom_boxplot() + geom_jitter() + coord_flip()
p + geom_boxplot(notch = TRUE, notchwidth = .5) +
    geom_jitter(colour="sienna1")

## modifying theme
theme_set(theme_bw())
## theme_set(theme_gray())
p + geom_boxplot(notch = TRUE, notchwidth = .5) +
    geom_jitter(colour="sienna1")


## 'FACETS'
library(dplyr)                          #for next line:
college$Top10quartile <- ntile(college$Top10perc, 4)

p <- ggplot(college, aes(x=S.F.Ratio, y=Grad.Rate)) + geom_point()
p

p + facet_grid(. ~ Top10quartile)

## an outlier affects the visuals. have a good reason for removing it,
## and document it
college2 <- college[college$S.F.Ratio<39,]

## tip: don't need to iterate too much
ggplot(college2, aes(x=S.F.Ratio, y=Grad.Rate)) + geom_boxplot() +
    geom_point() + facet_grid(. ~ Top10quartile) +
    ggtitle("Graduation Rate vs. Student-Faculty Ratio, by Top 10 Quartiles")

## vs.
p <- ggplot(college2, aes(x=S.F.Ratio, y=Grad.Rate))
p <- p + geom_boxplot()
p <- p + geom_point()
p <- p + facet_grid(. ~ Top10quartile)
p <- p + ggtitle("Graduation Rate vs. Student-Faculty Ratio, by Top 10 Quartiles")

read 2 texts and create a word cloud
-compute the freq of each word, and plot the most freq word in the biggest font
```

python = both interpreted and compiled
google = 10^100

tuple = immutable, ordered, allow dupes


## Prime
```
def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))
```

args is a tuple of its unnamed arguments and kwargs is a dictionary of its named arguments
```
def magic(*args, **kwargs):
    print ("unnamed args: ", args)
    print ("keyword args: ", kwargs)
magic(1, 2, 3, 4, 5, 6, 'foo', key1 = 'NU', key2 = 'rocks!', key3 = 'really!')
```


covariant is not normalized 
correlation coefficient `.corr`
pearson = standard corr
poisson = takes a certain fixed amount of time

bernoullie = win/lose
gamma distribution
brownian motion = complete randomness