# Automatic-End-to-End-Speech-Recognition-using-pytorch

*******************************************************
#### Disclaimer: 
***This is a work in Progress***
*******************************************************

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

## Next Steps:
1. Use Transformers !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! :smile:
2. I used my Laptop's GPU for training a subset of the dataset as such models require loads of computation and it is not practical to leave my lappy running for days :( but I plan to train on the entire dataset. For this I plan to use the Nvidia Tesla P100 GPUs using GCP for better and faster computation.
