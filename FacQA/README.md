<h1 align="center"> FacQA
</h1>

<p align="center">
 <a target="_blank" href="https://drive.google.com/file/d/1eo1hMR7JJP-KcqNM6hg12eK5DMCdDSu-/view?usp=share_link">Video Demo</a>
</p>

<p align="center">
 <a target="_blank" href="https://facqa-production.up.railway.app/">FacQA Website</a>
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
* When scraping data from websites, we found that there is a limit to the number of requests that can be made before the website blocks further requests. This can hinder data collection and slow down the research process.
* Deploying websites with pre-trained models can make the website slow and less responsive. This is because these models can be quite large and computationally expensive, which can cause delays in processing and returning results to users.
* We also experienced issues with too many dependencies, which can make the project difficult to manage and maintain. Installing and updating multiple packages can be time-consuming and lead to compatibility issues, which can cause errors and bugs in the code.
* The approach is limited to text input only.


## Future Works
Some of the possible future work that could be done to improve upon the current approach are as follows:</br>
* Predicting news based on the article's URL rather than just the headlines and article text could be a valuable addition to the model. This would involve extracting data from the URL, such as the source or keywords, to gain further insight into the nature of the article and improve prediction accuracy.
* As visual media becomes increasingly prominent in news reporting, it is important to be able to distinguish between authentic and fake images. By training a CNN on image datasets, it could be possible to accurately identify images that are being used in a misleading or deceptive way.</br>
These potential areas of future work would involve expanding the scope of the research to include additional data sources and types of analysis. By doing so, we could improve the accuracy and comprehensiveness of our predictions, and contribute to the development of more robust and reliable news analysis models.
