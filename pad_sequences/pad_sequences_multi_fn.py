def pad_sequences_multi(sequences: list,
                        padding: str = 'pre',
                        truncating: str = 'pre',
                        maxlen: int = None,
                        value: list = None) -> list:
    # use the len of the longest sequence
    if maxlen is None:
        maxlen = max([len(seq) for seq in sequences])

    # impute, e.g. (0, 0, 0), as padding value
    if value is None:
        value = [0 for _ in range(len(sequences[0][0]))]
    if not isinstance(value, (list, tuple)):
        value = [value for _ in range(len(sequences[0][0]))]

    # loop over all sequences
    padded = []
    for seq in sequences:
        # ensure that 1 single observation is processed as list
        if not isinstance(seq[0], (list, tuple)):
            seq = [seq]

        # convert tuple to list
        seq = list(seq)

        # Padding
        if padding == 'pre':
            seq.reverse()
        while len(seq) < maxlen:
            seq.append(value)
        if padding == 'pre':
            seq.reverse()

        # Trucation (not implemented)
        if len(seq) > maxlen:
            if truncating == 'pre':
                seq = seq[(len(seq) - maxlen):]
            if truncating == 'post':
                seq = seq[:maxlen]

        # sequence is done
        padded.append(seq)

    # dataset is done
    return padded
