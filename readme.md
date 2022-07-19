# To try out this repo:
1. Clone the repo to your local machine
2. Make sure you have python3, pip, and pipenv
3. Run **pipenv install** in the project root directory (to create a virtual env, and to install dependencies in it)
4. Type the text you want to be animated in sample.txt
5. To use predefined face image, run **python imageprototype.py** in the project root directory
6. To use own face image, first download **shape_predictor_68_face_landmarks.dat** file using command **wget http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2** followed by **bzip2 -d shape_predictor_68_face_landmarks.dat.bz2**
7. Then, run **python imageprototype.py <image_name>.jpg**

