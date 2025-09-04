# iLSU-T: an Open Dataset for Uruguayan Sign Language Translation (FG2025)

## 1. Introduction
This is the code and repository for the article ([link to the full paper]()): 
> Stassi, A., Boria, Y., Di Martino, M., & Randall, G. (2025). iLSU-T: an Open Dataset for Uruguayan Sign Language Translation. In Proceedings of the 19th IEEE International Conference on Automatic Face and Gesture Recoginition (pp. dddd-xxxx).

The main contributions of this work are:

* iLSU-T, the first dataset with multimodal video, audio, and text for LSU translation. iLSU-T comprises more than 185 hours of curated video from TV broadcasting in Uruguay.
* A preprocessing pipeline to derive the iLSU-T dataset.
* A theoretical discussion from the linguistic perspective about the problem of aligning and annotating interpreted sign language videos with text.
* The first recorded evaluation and benchmarking of state-of-the-art available methods for sign language translation (SLT) in the LSU context.

### 1.1. SLT datasets context

| Dataset      |   Source language    |   Target language    | #signers             |  #hours              |  #samples            |  Vocabulary          |  Video quality       |    Annotations       |   Source             |
| ------------ | -------------------- | -------------------- | -------------------- | -------------------- | -------------------- | -------------------- | -------------------- | -------------------- | -------------------- |
| Phoenix2014T |    DGS               |        German        |          9           |    10.5              |        8257          |       2k9            |     210x260@25,fps   |      text, gloss     |        TV            |
| LSA-T        |    LSA     |       Spanish       | 103          | 21.78             |    14880   | 14k2 |  1920x1080@30,fps |     text (SD)  | Web |
| CSL-Daily    | CSL | Chinese | 10 | 23 | 20654 | 2k5 | 1920x1080@30,fps | text, gloss | Lab
| KETI         |        KSL       |       Korean        |  14          | 28                |    14672 |  419 |  1920x1080@30,fps |    text        | Lab |
| AUSLAN-Daily |     Auslan                |  English                   |    67          |     45              |     25106    |  13k9 |       1280x720/1920x1080@25-30,fps         |      text          |   TV         |
| SIGNUM       |        DGS       |        German       |  25          |  55.3             |    33210   | N/A |  776x578@30,fps    |    text        | Lab |
| How2Sign     |     English                   |           ASL          |    11          |        79           |    35k2   |  16k   |    1280x720@30,fps                  |    text          |    Lab         |
| OpenASL          |   ASL          |    English          |  220  |   288             |  98417     | 33k5 | variable |   text          | Web |
| BOBSL            |   English              | BSL          |  37          |   1467           |  1M2     | 78k   | 444x444@25,fps   |   text          |  TV |
|**iLSU-T (ours)** |  **Spanish** |            **LSU**      |  **18**         |   **201.5**           | **86k5**      | **37k9** | **variable, 343x364@25-30,fps** |    **text (SD)**    |  **TV**    |

## 2. Repository structure
This repository is organized is several folders, one per each process. 
In the following, it is presented a list of the folders with a brief content description for each one:
* <u>preprocessing</u>: preprocessing methods to obtain iLSU-T episodes frow raw data, including text files.
* <u>data</u>: csv file with all the iLSU-T episodes and metadata. Please see section 3 for access the dataset. FYI, you might have to adjust paths to data (episodes and whisperx files) in .csv.
* <u>video_clipping_and_visual_feats</u>: a Jupyter notebook for exploring the iLSU-T episodes and generate video-clips. You will find the instructions to compute I3D visual features from video-clips.
* <u>split_and_package_datasets</u>: the scripts for splitting data into train, val and test sets for the whole dataset, and the three considered subsets in the paper.
* <u>slt_config_files</u>: config files for the three SOTA methods used in the paper.

## 3. iLSU-T dataset download
Please visit [this website](https://iie.fing.edu.uy/proyectos/lsu-ds/en/ilsu-t/) for download the iLSU-T dataset after accepting the License of Restricted Use.

Available data in the website: 
* iLSU-T episodes,
* [WhisperX](https://github.com/m-bain/whisperX) transcriptions, and
* 20 hours of manual aligned WhisperX transcriptions (work in progress...)

## 4. Tested methods on iLSU-T
* [SLT](https://github.com/neccam/slt) 
* [SCULT](https://github.com/avoskou/Stochastic-Transformer-Networks-with-Linear-Competing-Units-Application-to-end-to-end-SL-Translatio) 
* [GASLT](https://github.com/YinAoXiong/GASLT)

## Acknowledgements
iLSU-T was partially supported by a CAP--UdelaR scholarship, Uruguay. Some of the experiments were carried out using ClusterUY. We acknowledge DiNaTel Uruguay for providing us with the raw data, the NICA--UdelaR team for fruitful interdisciplinary discussions, and G. Gómez and F. Lecumberry for their website assistance.

If you use this code and/or data for your work, please do not forget to cite us: 

```
@inproceedings{stassi2025ilsut,
  title={iLSU-T: an Open Dataset for Uruguayan Sign Language Translation},
  author={Stassi, Ariel E and Boria, Yanina and Di Martino, J Mat{\'\i}as and Randall, Gregory},
  booktitle={2025 IEEE 19th International Conference on Automatic Face and Gesture Recognition (FG)},
  pages={1--10},
  year={2025},
  organization={IEEE}
}
```








