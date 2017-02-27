#CPEG 657 - Search & Data Mining ............. 2/22

###Indexing
	* Relevance Modeling
	* 

###Vector Spaced Model Searching
* Using keywords and assign wheits to each term
	1. (TF) Term Frequency - less weight to common term
	2. (IDF) Inverse Document Frequency
	3. (LN) Document Length Normalization
* Search engines were based on "keyword" matching<br>
  Spammers took advantage of this

###Automatic Feedback
* Lawyers trying to find all documents related to a particular case
* Is Documents return good or need query to be updated?
* Machine Learning problem [Training Data]->[Model]->[testing data]->prediction

###Rocchio Feedback
* $$q_m = 𝛂q + \frac{𝞫}{|D_r|} \sum_{∀d}$$
  $$Similarity(D,Q) = \sum_{i=1}^n$$
  
###Similarity (Pivoted Normaliation Formula)
* Give priority to first occurrance and less to repeated
  $$S(D,Q) = \sum_{t=Q,D} \frac{1+ln(1+ln(c(t,D)}{(1-s)+s \frac{|D|}{avdl}}*c(t,Q)*ln \frac{N+1}{df(t)}$$