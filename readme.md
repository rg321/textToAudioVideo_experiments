Repo tries to produce talking face taking input from text file.

There are mainly two approaches viz. Non-Deep Learning and Deep Learning.

For Non-Deep Learning approach, following are the steps -:
1) first phonemes are created out of input text
2) then each phoneme is mapped to corresponding mouth image (generally called as viseme)
3) option is provided to give any face image as input, to make that face talking
4) for that face-swapping is used, where lips from Mouths_base are swapped with provided image

For Deep Learning approach, idea is based on **https://github.com/Rudrabha/Wav2Lip**
Refer readme file in **deep-learning-approach** folder to know exact steps 