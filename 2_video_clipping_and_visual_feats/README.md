# iLSU-T: automatic video-clipping and visual features extraction

This stage of data processing is composed of two stages:

1) Automatic video-clipping: with the script ```generate_videoclips.ipynb``` you can generate the videoclips in automatic process, by considering a random pre and post delays. <u>Note:</u> 
Please verify the path to the ```iLSU-T_video_IDs.csv```.

2) With the generated videoclips, compute I3D visual features using the method of these two GitHub repositories https://github.com/verashira/TSPNet and https://github.com/dxli94/WLASL/tree/master/code/I3D, with a window width of 8 frames, and a stride of 2 frames. 

    For reproduce iLSU-T baseline experiments, please use the following pretrained weights: 
    * the model on [this link](https://github.com/dxli94/WLASL) for I3D-ASL2k. <u>Note:</u> Please search for "WLASL pre-trained weights" link and use the model named ```nslt_2000_065538_0.514762.pt```.
    * the model on [this link](https://www.robots.ox.ac.uk/~vgg/research/bslattend/data/bsl5k.pth.tar) for I3D-BSL5k.


