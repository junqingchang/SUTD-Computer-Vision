import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
    """
    Softmax loss function, naive implementation (with loops)
    
    Inputs have dimension D, there are C classes, and we operate on minibatches
    of N examples.
    
    Inputs:
    - W: A numpy array of shape (D, C) containing weights.
    - X: A numpy array of shape (N, D) containing a minibatch of data.
    - y: A numpy array of shape (N,) containing training labels; y[i] = c means
      that X[i] has label c, where 0 <= c < C.
    - reg: (float) regularization strength
    
    Returns a tuple of:
    - loss as single float
    - gradient with respect to weights W; an array of same shape as W
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using explicit loops.     #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    num_train_data = X.shape[0]
    num_dimension = W.shape[0]
    num_classes = W.shape[1]
    for i in range(num_train_data):
        exps = np.exp(np.dot(X[i,:],W))
        sum_of_exps = np.sum(exps)
        softmax_output = [j/sum_of_exps for j in exps]
        for class_type in range(num_classes):
            if class_type == y[i]:
                dW[:, class_type] += X.T[:, i] * (softmax_output[class_type]-1)
            else:
                dW[:, class_type] += X.T[:, i] * softmax_output[class_type]
        loss += -np.log(softmax_output[y[i]])
        
        
    loss /= num_train_data
    loss += 0.5 * reg * np.sum(W**2)
    
    dW /= num_train_data
    dW += reg * W

    #############################################################################
    #                          END OF YOUR CODE                                 #
    #############################################################################
    
    return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
    """
    Softmax loss function, vectorized version.
    
    Inputs and outputs are the same as softmax_loss_naive.
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)
    
    #############################################################################
    # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    
    
    num_train_data = X.shape[0]
    num_dimension = W.shape[0]
    num_classes = W.shape[1]
    
    f = X.dot(W)
    exp_scores = np.exp(f)
    softmax_output = exp_scores/np.sum(exp_scores, axis=1, keepdims=True)
    log_probs = -np.log(softmax_output[range(num_train_data), y])
    
    loss = np.sum(log_probs)/num_train_data
    loss += 0.5 * reg * np.sum(W **2)
    
    dscores = softmax_output
    dscores[range(num_train_data), y] -= 1
    dW = X.T.dot(dscores)
    dW /= num_train_data
    dW += reg*W
    #############################################################################
    #                          END OF YOUR CODE                                 #
    #############################################################################
    
    return loss, dW

