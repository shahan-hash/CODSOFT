import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical


def data_generator(
        mapping,
        features,
        tokenizer,
        max_length,
        vocab_size,
        batch_size):

    while True:

        X1, X2, y = [], [], []

        n = 0

        for image_id, captions in mapping.items():

            if image_id not in features:
                continue

            feature = features[image_id][0]

            for caption in captions:

                seq = tokenizer.texts_to_sequences(
                    [caption]
                )[0]

                for i in range(1, len(seq)):

                    in_seq = seq[:i]
                    out_seq = seq[i]

                    in_seq = pad_sequences(
                        [in_seq],
                        maxlen=max_length
                    )[0]

                    out_seq = to_categorical(
                        [out_seq],
                        num_classes=vocab_size
                    )[0]

                    X1.append(feature)
                    X2.append(in_seq)
                    y.append(out_seq)

                    n += 1

                    if n == batch_size:

                        yield (
                            (
                                np.array(X1),
                                np.array(X2)
                            ),
                            np.array(y)
                        )

                        X1, X2, y = [], [], []
                        n = 0