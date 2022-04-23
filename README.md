# Automatic-End-to-End-Speech-Recognition-using-pytorch [![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) [![](https://img.shields.io/badge/Prateek-Ralhan-brightgreen.svg?colorB=ff0000)](https://prateekralhan.github.io/)

## Dependencies:
1. [Pytorch](https://pytorch.org)
2. [Torchaudio](https://pypi.org/project/torchaudio/)
3. [Numpy](https://pypi.org/project/numpy/)
4. [CUDA Toolkit 10.1](https://developer.nvidia.com/cuda-10.1-download-archive-base)
5. [Nvidia cuDNN](https://developer.nvidia.com/rdp/cudnn-download)

### Note: 
  * You may need to create [Nvidia Developer account](https://developer.nvidia.com/developer-program) for downloading cuDNN for your appropriate CUDA version. Don't worry it's free !! :smile:
  * Also, ensure whether your GPU is CUDA compatible or not. You can check this [here](https://developer.nvidia.com/cuda-gpus).

## Hardware Config:
1. GPU - Nvidia Geforce GTX 1050Ti - Get latest Drivers for your GPU from [here](https://www.nvidia.in/Download/index.aspx?lang=en-in)
2. CPU - i7 7700 , processor speed - 3.8 GHz
3. RAM - 12 GB DDR4


## Dataset:
For handling the audio data, I am using torchaudio here which is a library built by the PyTorch team specifically for audio data. trained on a subset of LibriSpeech, which is a corpus of read English speech data derived from audiobooks, comprising 100 hours of transcribed audio data. THe dataset will be automatically downloaded when you execute the script. Each sample of the dataset contains the waveform, sample rate of audio, the utterance/label, and more metadata on the sample.

## Model:
The model built here inspired by Deep Speech 2 (Baidu's second revision of their now-famous model) with some personal improvements to the architecture. The model will have two main neural network modules - N layers of Residual Convolutional Neural Networks (ResCNN) to learn the relevant audio features, and a set of Bidirectional Recurrent Neural Networks (BiRNN) to leverage the learned ResCNN audio features. The model is topped off with a fully connected layer used to classify characters per time step.The output of the model will be a probability matrix of characters, and we'll use that probability matrix to decode the most likely characters spoken from the audio. 

## Streamlit Webapp
I also developed a lightweight streamlit based webapp for performing ASR which is using *wav2vec2-base-960h* huggingface 🤗 model provided by Facebook AI.

![1](https://user-images.githubusercontent.com/29462447/164911256-a5379696-0400-4e16-8d1e-430a9796ef57.png)
![2](https://user-images.githubusercontent.com/29462447/164911263-4b036119-ca45-474a-8ac5-bd75fba77dc4.png)

## Installation:
* Simply run the command ***pip install -r requirements.txt*** to install the dependencies.

## Usage:
1. Clone this repository and install the dependencies as mentioned above.
2. Make a directory within the directory `streamlit_app` with the name `.streamlit` *(Don't forget the dot !!)*.
3. Create a file `config.toml` in this directory *(Be aware of the file extension !!)*.
4. Copy-Paste the following contents in this file and save :
```
[theme]
base="dark"
primaryColor="#0fffcf"
textColor="#0dd2c8"
```
5. Navigate to the root directory of this repository and simply run the command: 
```
streamlit run app.py
```
6. Navigate to http://localhost:8501 in your web-browser.
7. By default, streamlit allows us to upload files of **max. 200MB**. If you want to have more size for uploading files, execute the command :
```
streamlit run app.py --server.maxUploadSize=1028
```

## Results:
1. Perform ASR on the fly!
![1](https://user-images.githubusercontent.com/29462447/164911256-a5379696-0400-4e16-8d1e-430a9796ef57.png)
![2](https://user-images.githubusercontent.com/29462447/164911263-4b036119-ca45-474a-8ac5-bd75fba77dc4.png)


### Running the Dockerized App
1. Ensure you have Docker Installed and Setup in your OS (Windows/Mac/Linux). For detailed Instructions, please refer [this.](https://docs.docker.com/engine/install/)
2. Navigate to the folder where you have cloned this repository ( where the ***Dockerfile*** is present ).
3. Build the Docker Image (don't forget the dot!! :smile: ): 
```
docker build -f Dockerfile -t app:latest .
```
4. Run the docker:
```
docker run -p 8501:8501 app:latest
```

This will launch the dockerized app. Navigate to ***http://localhost:8501/*** in your browser to have a look at your application. You can check the status of your all available running dockers by:
```
docker ps
```
