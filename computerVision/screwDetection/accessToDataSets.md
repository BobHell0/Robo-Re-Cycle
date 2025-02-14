Google Drive Link:


NOTE: The reason there is no v5.0 data set is because:
When I created the v4.0 model I only used the images from my desk (white background). I was trying to do a technique called data augmentation, where you increase the size of a dataset artificially by editing the photos (cropping, changing colour scale, rotation, reflection, blurring, etc). However, the resulting model was not able to detect any screws, mainly because the initial data set for v4.0 was so small (~ 40 images). So rather than creating a separate v5.0 dataset, I just added extra images to the v4.0 dataset and used the resulting dataset to train the v5.0 model.