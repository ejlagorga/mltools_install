To install the following packages:

numpy==1.14.5
Keras==2.1.5
tensorflow==1.8.0
matplotlib==2.2.2
pandas==0.23.1
seaborn==0.8.1
setuptools==39.2.0
scikit_learn==0.19.1

run the following commands:

cat pyinstall_lockheed_tf.parta* > pyinstall_lockheed_tf.tar.gz
tar -zxf dist/pyinstall_lockheed_tf.tar.gz
pip install -r requirements.txt --use-wheel --no-index --find-links wheelhouse
