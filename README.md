# Capstone
Final DS 222 Capstone

# Object detection with neural network classification
### Contrastive language image processing with threatening photographs

## The Problem
Nueral network and object detection is a promenient and emergent area of study. With cameras and photographs avaialble in abundance all around the world, many wish to be able to interpret and in my case reduce threats around the world. This project pushes the limits of classification to analyze image data and make a compelling prediction on whether a person is holding a weapon. 

## Background
### Threat reduction and image interpretation
In order to have a reliable outcome the image data must be aquired from multiple resources. Without access to survielance camera company data, most of the images must be scraped from public domains on the internet. Without surprise, it is difficult to find high quality images of people holding firearms from a 3rd person point of view. However, I was able to find what would be highly probably image folders to contain a person holding a gun. 

After ammassing photos it next became the challenge of orienting them and both manually and programatically processign them to achieve the cleanest dataset possible. There is quite a bit of noise in the real world especially with photographs so my next step was to use the flexible and adapable image processor known as CLIP. 

## Data Formatting and Modeling
### Data Source, Formatting, and Cleaning
Photos were gathered from a Github repo known as OD weapon detection master set( URL ), otherwise images were webscraped from reddit and google. Second to last, I provided a unique dataset of my own photographs replicated in similar scenarios and classifified into two distinct groups (human with gun and without). Finally, I supplied an adversarial dataset with images desgined to confuse the model (humans holding packages, guitars, and golf clubs).

At first, 

In all versions, newlines were preserved in the data. This was done in an effort to allow the model to learn where to insert a newline on its own. In versions where the punctuation was removed, newlines were replaced with the word "newline", which was not part of the original vocabulary. In processing of the model output, "newline" was replaced with a newline.

The words in each line were later divided, using a moving window technique. Data was reformatted to include a single word, its preceding word, and the word coming after it. This was done for two, three, and four word windows. Although more words would allow for more context, this would go beyond the typical length of a sonnet line.

### Modeling
Initially, the input for the models were transformed into binary arrays with one-hot encoding. This was then used to train a neural network with LSTM and Dense layers. These models were trained with two and three word starter phrases and their following words. In all cases, these models did not produce meaningful results. In one case, the only word a model would predict was "wardrobe".

This led to a revamping of how modeling had been approached. Rather than preprocessing the data with a one-hot encoder, the data was preprocessed using Keras's Sequential tool, and an embedding layer was added to the model. This model was then trained on four-word sequences and their following word. The results of this were much more cogent and meaningful.  

## Observations
There were a few hurdles in this project, most of which focused on the data formatting and what the model would be trained on. These challenges were deciding how many words should be included in the starter text, what format the data should be in to train the model on, deciding to include an embedding layer, and other such difficulties. From the modeling (and remodeling) process it is gleamed that it is much better to preprocess the input text by sequencing rather than one-hot encoding, since one-hot encoding is best meant for categorical data. While a case can be made that natural language generation is categorical since it is about determining what word in the present vocabulary *should* come next, it is also about the relationship between words and the context they are placed in. Sequencing words and using an embedding layer allow for word relationships and context to be taken into account.

This resulted in a neural network that produced this, among other, generated poetry samples:
(this generated sample has not be reformatted other than to replace "newline" with an actual newline)
>rose whose beauty yea i
i least wilt
and
hear that trees makest seek
i do of your desire

The results from this model are cogent and have some meaning to a human. This generated text could be expressing a desire for someone so strong it is crushing, causing the person to wilt. It could be touching on how in the search for someone's affections hope springs eternal.

As thought-inpsiring as the output from this model may be, it does not abide by the strict structure of Shakespearean sonnets. There is no rhyming, and the syllable count for each line is varied. This means that unregulated output from a NLG model will not naturally abide by the strict structure of a Shakespearean sonnet.

## Next Steps
From here there are a few different avenues to pursue. In the interest of generating consistent sonnets that fit the Shakespearean structure, restrictions can be placed on what generated word will be part of the final product. With these restrictions controls can be put in place for both rhyme and metrics. 