# Advertisement Sales Prediction
This project is used to predict sales based on many different types of advertisement such as:
    - Tv
    - Radio
    - Newspaper
1) cleaning and organizing data:
    From this step there are no changes since the data is already clean and does not need any cleaning
2) data visualization using matplotlib:
    From the plot we conclude that:
    1- The dominant feature in this dataset is TV
    2- Newspaper has a very weak correlation to sales so we can drop it from testing
    3- Radio has a decent correlation to sales, but we need to do some feature engineering to make it a useable feature.
3) feature engineering:
    Adding a basic TV-Radio interaction feature creates a beautiful correlation to the dataset, making an almost straight line with 100% corelation.
4) training + testing:
    Since our data is almost linear, its better to use a simple linear regression model for this task
    After fitting and testing, we are left with an MSE of 0.812 and an R2 of 0.974 which means that our model has 97.4% accuracy