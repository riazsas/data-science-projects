# EMPLOYEE PERFORMANCE ANALYSIS
## PROJECT SUMMARY
REQUIREMENT

NX Future Inc , (referred as INX ) , is one of the leading data analytics and automation solutions provider with over 15 years of global business presence.

Recent years, the employee performance indexes are not healthy and this is becoming a growing concerns among the top management. There has been increased escalations on service delivery and client satisfaction levels came down by 8 percentage points.

CEO, Mr. Brain, knows the issues but concerned to take any actions in penalizing non-performing employees as this would affect the employee morale of all the employees in general and may further reduce the performance.

Mr. Brain decided to initiate a data science project , which analyses the current employee data and find the core underlying causes of this performance issues. Mr. Brain, being a data scientist himself, expects the findings of this project will help him to take right course of actions. He also expects a clear indicators of non performing employees, so that any penalization of non-performing employee, if required, may not significantly affect other employee morals.

The following insights are expected from this project.

    Department wise performances
    Top 3 Important Factors effecting employee performance
    A trained model which can predict the employee performance based on factors as inputs. This will be used to hire employees
    Recommendations to improve the employee performance based on insights from analysis.

SUMMARY

The project was conducted to be able to bring to light the factors affecting employee performance , training a model which is able to predict the Performance Rating of an employee, analyzing the data to provide recommendations to improve the performance and gain insights from analysis. The project was executed in the following steps:

    Importing the data provided, finding out the predictor & target variables and cleaning the data for null values.
    Analyzing the performance of each department and other features to gain insights.
    Label Encoding the ordinal columns.
    The most important features for analysis was selected using the following feature selection techniques: Univarite Analysis Feature Analysis using ExtraTreesClassifier Correlation Score
    Standardizing the data and splitting the data into test and train data points.
    Training the data using algorithms such as Support Vector Machines, Random Forest,XGBoost Classifier and Artificial Neural Networks and comparing the accuracy score to find out the most accurate model.
    PCA factorization was also used to select the features but as the accuracy was comparitvely lower than the above feature selection techniques. Therefore, PCA was not implemented into training the model

Classification alogrithms were chosen to train the model, as the target variable falls under discrete data type and specifically classification alogrithms which are able to classify non-linearly seperable data such as - Random Forest,Support Vector Machines, Naive Bayes, XGBoost Classifier and Artificial Neural Networks were used in order to develop a model that was able to predict employee performance based on the input variables, it was observed that Random Forest with GridSearchCV gives the maximum accuracy of 93.8%. Therefore Random Forest with GridSearchCV can be chosen to fit the bussiness case
FEATURE SELECTION/ENGINEERING

The most important features for analysis was selected using the following feature selection techniques:

Univarite Analysis
Feature Analysis using ExtraTreesClassifier
Correlation Score

Based on the above, the following features were selected for Analysis:

Emp Last Salary Hike Perecent
Emp Environment Satisfaction
Years Since Last Promotion
Emp Department
Experience Years in Current Role
Emp Work Life Balance
Emp Job Role
Years with Current Manager
Experience Years at this Company
Emp Hourly Rate

Standard scaler was used to transform the features so as to control the difference of magnitude within the units of the selected features

It was observed that using these features for training the model yielded a fair accuracy score.

PCA factorization was also used to select the features but as the accuracy was comparitvely lower than the above feature selection techniques. Therefore, PCA was not implemented into training the model.
Results, Analysis and Insights
Query 1: Department wise performances.

    The department wise performances are ranked in the following order:

        Development

        Data Science

        Human Resources

        Research and Development

        Sales

        Finance

        Note:Ranked by comparing the Overall Percentage of Excellent and Outstanding Employees in a given Department

Query 2: The Top 3 important features affecting the employee performance

    The top 3 Factors affecting employee performance are
        Last Salary Hike Percentage
        Employee Environment Satisfaction and
        Years since last promotion

Query 3: A Trained model which can predict the employee performance

    It was observed that Random Forest with GridSearchCV which gives the highest accuracy of 93.8% was chosen to fit the bussiness case,after comparing the accuracy scores of the classification alogrithms. The following algorithms were chosen to train the model:
    Random Forest Classifier with Grid Search - 93.8% Accuracy Score
    Support Vector Machine (Classifier) -88.3% Accuracy Score
    XGBOOST Classifier: 93.08% Accuracy Score
    Artitficial Neural Network: 85.5% Accuracy Score

    Additional Insights:
        The Candidates with a Marketing Background underperform when compared to other Educational Backgrounds
        Age does not play a factor in employee performance.
        It is observed that candidates with over 5 years of experience in their current roles underperformed when compared to candidates with less than 5 years of experience.

RECOMMENDATIONS

    Looking at the data it is inferred that creating a work environment based around the necessities of the employee correlates to a better performing employee.
    It is observed from the data that the employees that recieve a high salary hike tend to outperform employees that recieve a comparitively lower salary hike.
    Promoting employee retreats and similar events also tend to improve employee performance,as work life balance is a key parameter contributing to employee performance.
    Rotating the reporting manager frequently will also boost employee performances.
    It is also recommended that employees be given the chance to apply for a promotion every 2 years, so as to increase their performance
    Additional Insight: Employees working in the Development department have shown the best performance according to the given data, which suggests that their best practices be implemented to other departments

