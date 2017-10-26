import argparse


def parse_args():
    print("parsing arguments")
    parser = argparse.ArgumentParser(description='PyTorch TreeLSTM for Sentiment Analysis Trees')
    parser.add_argument('--use_gpu', default=False, action='store_true')

    parser.add_argument('--data_dir', default='RNN_Data_files/', metavar='PATH')
    parser.add_argument('--save_dir', default='/home/cse/dual/cs5130298/scratch/checkpoints2/', metavar='PATH')

    parser.add_argument('--rnn_class', choices=['lstm', 'gru', 'rnn', 'customgru'], default='lstm',
                        help='class of underlying RNN to use')
    parser.add_argument('--reload', default='', metavar='PATH',
                        help='path to checkpoint to load (default: none)')
    parser.add_argument('--test', default=False, action='store_true',
                        help='test model on test set (use with --reload)')

    parser.add_argument('--batch_size', type=int, default=1,
                        help='batchsize for optimizer updates')
    parser.add_argument('--epochs', type=int, default=1,
                        help='number of total epochs to run')

    parser.add_argument('--lr', type=float, default=0.1,
                        metavar='LR', help='initial learning rate')
    parser.add_argument('--step_size', type=int, default=10, metavar='N')
    parser.add_argument('--gamma', type=float, default=1)

    parser.add_argument('--seed', type=int, default=123,
                        help='random seed (default: 123)')

    args = parser.parse_args()
    return args
