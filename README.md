# Algorithmic-Bias

## Demonstrated Skills
- Computer Vision (CNN) - Deep Learning
- Data Visualization and Reporting
- Communication Skills
- Learning Skills (This was my introduction to Computer Vision and Deep Learning, in-depth)
- Research Skills
- Data Quality Assessment
- Model Production (Build a Streamlit App that embeds the models)

&nbsp;
## Part I - Problem Context

According to a 2019 study conducted by researchers at the National Institute of Standards and Technology (NIST), facial-recognition systems falsely identified African-Americans and Asian-Americans 10 to 100 times more than Caucasians. In another audit by MIT researcher Joy Buolamwini and Former Google researcher Timnit Gebru, facial-recognition systems at Microsoft and IBM positively identified males as compared to females.

The results found show that these systems exhibit biases in demographic characteristics such as race, gender, age, etc; even systems developed by leading companies in the field. Simply put, facial-recognition systems or software are machine learning algorithms trained to detect or recognize a persons’ race, gender, age, etc using a camera. While these systems have numerous applications, their intelligence and accuracy depend on the algorithms at heart, the data they are fed and the applications that use them.

Given the democratization of AI and the proliferation of facial-recognition systems, it is imperative that people who develop facial-recognition systems look into the problems (biases) that these systems face and how they can be fixed.

&nbsp;
## Part II - Project Objectives

As a AI Practitioner who had read about the bias in Facial-Recogniton System, I was intrigued by learning about how AI can be biased and how we can begin to think about making it fair and just, as we build solutions for the community.

Therefore, my objectives for this project were the following:

  - Understand Bias in AI and where it possibly comes from
  - Build image-classifiers that are biased and unbiased and study their accuracy and probabilities
  - Draw lessons from the image-classifiers about best practices in building these systems

&nbsp;
## Part III - Implementation

- Model Building
  
  The models (image-classifiers) were implemented using Deep Learning's CNN Models. The dataset that I used contained 10,000 Images (5,000 Black People & 5,000 White People). I then trained three models using this dataset:
  - Model A: This is the unbiased model. It was trained on a 50% balanced representation of black and white images.
  - Model B: This is a biased model. It was trained on a 75% to 25% representation of white to black images, respectively.
  - Model C: This is also a biased model. It was trained on a 25% to 75% representation of black to white images, respectively. 
  
- #### Add More Details...

&nbsp;
## Part IV - App Screenshots
  
  First Screen - Allow to upload Models
  ![alt text](https://github.com/Masupa/Algorithmic-Bias/blob/main/assets/app_img_one.png)
  
  Image Classifier
  ![alt text](https://github.com/Masupa/Algorithmic-Bias/blob/main/assets/app_img_two.png)
  
  Classification Results
  ![alt text](https://github.com/Masupa/Algorithmic-Bias/blob/main/assets/app_imgs_classification_report.png)
  
 &nbsp;
 ## Adding More Info...
