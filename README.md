                  Customer Review Insight System- NLP-Based Sentiment & Issue Detection for Food/Product Reviews


**1. Problem Statement**

    Businesses in the food delivery and packaged food industry receive thousands of customer reviews across platforms such as Amazon, Zomato, and Swiggy.
    While star ratings provide an overall satisfaction metric, they fail to identify:
    
        a) Why customers are dissatisfied
        
        b) What specific issues are affecting user experience
        
        c) Which operational areas need improvement (taste, delivery, pricing, packaging)
    
    Manual analysis of such unstructured textual feedback is time-consuming and not scalable.

    This project aims to build an NLP-based system that can automatically:

        a) Predict customer sentiment
        
        b) Quantify overall satisfaction levels
        
        c) Detect key drivers of dissatisfaction from textual reviews

**2. Datasets Description**


    The model was trained on the Amazon Fine Food Reviews Dataset, which contains over 5.6 lakh customer food product reviews.
    Key feature used - Rating (1-5) & Customer review (Text)
    Label engineering:
        a) 1-2 = Negative Sentiment
        b) 3   = Neutral Sentiment
        c) 4-5 = Postive Sentiment

    Neutral reviews were excluded to reduce classification ambiguity and improve detection of dissatisfied customers.

    Final dataset distribution:

        Positive Reviews ≈ 4.4 lakh
        
        Negative Reviews ≈ 0.82 lakh
    
    Class imbalance was addressed using: 'class_weight='balanced'


**3.  Text Preprocessing**


    Preprocessing pipeline included:
    
          a) Lowercasing
          
          b) Removal of punctuation
          
          c) Stopword removal
          
          d) Lemmatization
          
          e) Retention of negation words (e.g., not, never)
          
      Negation handling was critical to prevent polarity reversal in phrases such as: not good, not tasty etc.


**4.  Feature Engineering**

    Initial TF-IDF (unigram) representation failed to capture negation context, resulting in incorrect predictions 
    for phrases such as:The food was not good
    
    To address this, Bigram-based TF-IDF was incorporated: ngram_range = (1,2)
    This enabled the model to preserve contextual polarity by capturing phrase-level features 
    such as:not good, not tasty etc.

**5.  Model Selection & used**

    Tried multiple models such as Logistic, Naive Bayes, and Linear SVM. 
    But selected Logistic Regression model as it was giving better recall result than others.

**6.  Model Output**

    1. Single Review Analysis

        For a given review, the system returns:
        
            a) Predicted Sentiment (Positive / Negative)
            
            b) Confidence Score
            
            c) Detected Issue (Taste / Delivery / Packaging / Price) if any

    2. Bulk Review Analysis

        For uploaded CSV files containing customer reviews:

            a) Total Reviews Analysed
            
            b) Positive Reviews
            
            c) Negative Reviews
            
            d) Customer Satisfaction Score (%)
            
            e) Issue Breakdown: such as Delivery Issues: 40% , Taste Issues: 25%, Packaging Issues: 20%,  
               and Price Issues: 15%
    
**7.  Tech Stack**

      Python
      NLTK
      Scikit-Learn
      TF-IDF Vectorizer
      Logistic Regression
      Streamlit

**8.  Limitations**

      Since the model was trained on food/product review data, predictions may not generalise well to out-of-domain textual inputs 
      such as: Financial complaints , Movie reviews etc.


 **9.  Business use case**

    The deployed system enables product managers or restaurant owners to:
    
              a) Analyse customer sentiment at scale
              
              b) Identify operational issues impacting customer satisfaction
              
              c) Prioritise improvements in delivery, packaging, taste, or pricing
              
              d) Track monthly satisfaction trends for specific products/restaurants


  [Click Here to Use Live App]
  https://customer-review-insight-system-mwuqd2pjy7jehattabdrq4.streamlit.app/


Author
Mohit Kushwaha
LinkedIn: www.linkedin.com/in/mohit-kushwaha-024401112

