<h1 align="center"> FacQA
</h1>

<p align="center">
 <a target="_blank" href="">Video Demo</a>
</p>

## About The Project
* FacQA is a Fake News Detection App build using python Flask and Question Answer Generation ML Model
* It is a Part of Debunkathon organised by shastra IIT Madras

## Working

The completion of the Model/Tool involved several steps in determining the authenticity of an article. The steps are as follows:
* Scraping articles: The first step involves collecting articles from various sources on the internet.
* Generating Question-Answer pairs: The next step is to generate a Question-Answer pair from the article to be tested for its authenticity. 
* Generating Answers: For the Questions generated for step 1, we generate answers from the scrapped articles. 
* Measuring Text Similarity: After the answers have been generated, the text similarity between the answers generated in steps 2 and 3 is measured using BERT. This helps to determine the authenticity of the article by comparing the answers generated with the answers in the article.
* Calculating Bleu Score: Along with the BERT score, the Bleu score is also calculated to measure the similarity between the answers generated and the actual answers in the article.
* Deploying a Website: The final step is to deploy a website where users can input articles and receive the results of the authenticity check. This makes the tool easily accessible to the general public.

## Architecture
<img src="https://github.com/baquer/FacQA/blob/master/Images/arch.png">

## Screenshot
<img src = "https://github.com/baquer/FacQA/blob/master/Images/ss.png">

## Limitations
* Too many requests while scraping data from the websites
* Deploying the website with pre-trained models makes the website slow
* Too many dependencies
* Limited to text Input only


## Future Works
* Allow URL as an Input to find the authenticity of the news
* Allow Image as an Input and use CNN for finding out the authencity of the shared Image using the Questions Answers Generation Model 
