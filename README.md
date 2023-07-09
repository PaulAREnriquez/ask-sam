Hello Sophia v.1

A simple conversational chatbot developed as a natural language processing personal project. Sophia is a customer assistant at Goldilocks, and will try to answer your questions based on the data she's been trained on.

Training data can be found in `intents.json`, which can be edited to fit any use case. Retraining is needed when done so. The current implementation is a simple collection of patterns and responses arranged according to topics called `tags`.

A simple neural network is developed using Pytorch, to train the model from the `patterns` from the data, and try to predict the `tag` or the topic as its target. The chatbot will then randomly select a `response` from the list of  `responses` according to the `tag` it has predicted.

Tkinter is used to create a graphical user interface for the conversation.

Install first the requirements using:

`pip install -r requirements.txt`

To run the app:

`python -m app`

Once data in intents.json is edited, we need to retrain the model and run the `train.py` file:

`python -m train`

The model parameters will be saved in a file called `data.pth`, along with all the necessary information which can be read in `train.py`.

Thanks!