# Parts-of-Speech Tagger

The purpose of this project was to learn how to implement RNNs and compare different types of RNNs on the task of **Parts-of-Speech tagging** using a part of the **CoNLL-2012 dataset** with 42 possible tags. This repository contains:
1. a custom implementation of the *GRU cell*.
2. a custom implementation of the RNN architecture that may be configured to be used as an *LSTM*, *GRU* or *Vanilla RNN*.
3. a Parts-of-Speech tagger that can be configured to use any of the above custom RNN implementations.

## Requirements
- python 3.5
- [pytorch](http://pytorch.org/)
- [torchtext](https://github.com/pytorch/text)

## Organisation
The code in the repository are organised as follows:
- [gru.py](https://github.com/Shivanshu-Gupta/Pytorch-POS-Tagger/blob/master/gru.py): custom GRU
- [rnn.py](https://github.com/Shivanshu-Gupta/Pytorch-POS-Tagger/blob/master/rnn.py): custom RNN
- [model.py](https://github.com/Shivanshu-Gupta/Pytorch-POS-Tagger/blob/master/model.py): POS Tagger Model
- [train.py](https://github.com/Shivanshu-Gupta/Pytorch-POS-Tagger/blob/master/train.py): training/validation/testing code
- [main.py](https://github.com/Shivanshu-Gupta/Pytorch-POS-Tagger/blob/master/main.py): driver code

The raw dataset is in [RNN_Data_files/].

## Usage
### Preprocessing datasets
Use [preprocess.sh](https://github.com/Shivanshu-Gupta/Pytorch-POS-Tagger/blob/master/preprocess.sh) to generate tsv datasets containing sentences and POS tags in the intended *data_dir* (*RNN_Data_files/* here).
```sh
$ ./preprocess.sh RNN_Data_files/train/sentences.tsv RNN_Data_files/train/tags.tsv RNN_Data_files/train_data.tsv
$ ./preprocess.sh RNN_Data_files/val/sentences.tsv RNN_Data_files/val/tags.tsv RNN_Data_files/val_data.tsv
```
### Training/Testing
```sh
usage: main.py [-h] [--use_gpu] [--data_dir PATH] [--save_dir PATH]
                    [--rnn_class RNN_CLASS] [--reload PATH] [--test]
                    [--batch_size BATCH_SIZE] [--epochs EPOCHS] [--lr LR]
                    [--step_size N] [--gamma GAMMA] [--seed SEED]

PyTorch Parts-of-Speech Tagger

optional arguments:
  -h, --help            show this help message and exit
  --use_gpu
  --data_dir PATH       directory containing train_data.tsv and val_data.tsv (default=RNN_Data_files/)
  --save_dir PATH
  --rnn_class RNN_CLASS
                        class of underlying RNN to use
  --reload PATH         path to checkpoint to load (default: none)
  --test                test model on test set (use with --reload)
  --batch_size BATCH_SIZE
                        batchsize for optimizer updates
  --epochs EPOCHS       number of total epochs to run
  --lr LR               initial learning rate
  --step_size N
  --gamma GAMMA
  --seed SEED           random seed (default: 123)
```
## Results
[Results.pdf] compares the results for LSTM, GRU and Vanilla RNN based POS Taggers on various metrics. The best accuracy of 96.12% was obtained using LSTM-based POS Tagger. The pretrained model can be downloaded from [here](https://drive.google.com/open?id=0By07sE0zY59RRnhVd1VjUURlSWs).

[RNN_Data_files/]: https://github.com/Shivanshu-Gupta/Pytorch-POS-Tagger/tree/master/RNN_Data_files
[Results.pdf]: https://github.com/Shivanshu-Gupta/Pytorch-POS-Tagger/blob/master/Results.pdf
