# Parts-of-Speech Tagger

The purpose of this project was to learn how to implement RNNs and compare different types of RNNs on the task of Parts-of-Speech tagging using a part of the CoNLL-2012 dataset with 42 possible tags. This repository contains:
1. my implementation of the GRU cell.
2. a custom implementation of RNN architecture that may be configured to be used as an LSTM, GRU or Vanilla RNN.
3. a Parts-of-Speech tagger that can be configured to use any of the above custom RNN implementations.

## Structure
The code in the repository are organised as follows:
- gru.py: custom GRU
- rnn.py: custom RNN
- model.py: POS Tagger Model
- train.py: training/validation/testing code
- main.py: driver code

For dataloader, I used torchtext library.

## Usage
```sh
usage: postagger.py [-h] [--use_gpu] [--data_dir PATH] [--save_dir PATH]
                    [--rnn_class RNN_CLASS] [--reload PATH] [--test]
                    [--batch_size BATCH_SIZE] [--epochs EPOCHS] [--lr LR]
                    [--step_size N] [--gamma GAMMA] [--seed SEED]

PyTorch Parts-of-Speech Tagger

optional arguments:
  -h, --help            show this help message and exit
  --use_gpu
  --data_dir PATH
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
