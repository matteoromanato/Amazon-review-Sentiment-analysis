# Data analytics: Sentiment on Amazon reviews

The aim of the project is analyzing some Amazon reviwes to create a Machine Learning model to predict the review's polarity.
I compare different approach:
- Lexicon based
- Supervise Machine Learning (Random forest, Logistic regression)
- Unsupervised (K-means)
- AI approach using Google-news-embedded-300

## Code
The code is avaible [[here]](https://colab.research.google.com/drive/1bjU-lboFpcfqoZxYxUy5l1CsEtZdDZ_E#scrollTo=p0ADvJCuPJ1B).
## Prerequisites
The preferred way is to use Google Colab or a jupiter notebook.

## Installation
Use the package manager pip to install the requirements.

```bash
pip install requirements.txt
```

Requirements: 
* numpy
* pandas
* matplotlib
* sklearn
* searborn
* wordcloud
* nltk
* Afinn
* nlpaug
* gensim

## Usage
The code is executable but pay attention when the code import the dataset the path may be not correct, upload the dataset on your drive!.

If you are using your PC pay attention on the dataset path. On Colab the path was: 
```python
 '/content/...'
```

## Data
The dataset used was **amazon-fine-food-reviews** [[link]](https://www.kaggle.com/snap/amazon-fine-food-reviews).

In my project I had 2 dataset that I merge and I took only the instance of the left dataset.
All the data can provide from the link above don't worry. 



## Authors
Matteo Romanato - matteoromanato14@gmail.com 
<p>
  <a href="https://www.linkedin.com/in/matteo-romanato-b44414124/" rel="nofollow noreferrer">
    <img src="https://i.stack.imgur.com/gVE0j.png" alt="linkedin"> LinkedIn
  </a> &nbsp; 
  <a href="https://github.com/matteoromanato" rel="nofollow noreferrer">
    <img src="https://i.stack.imgur.com/tskMh.png" alt="github"> Github
  </a>
</p>
