from pad_sequences import pad_sequences_sparse


def test1():
    # expected
    expected = []
    expected.append([(1, 0), (2, 0), (3, 1)])
    expected.append([(0, 2), (2, 1)])

    # sequence
    sequences = []
    sequences.append([(1, 0), (2, 0), (3, 1)])
    sequences.append([(1, 3), (0, 2), (2, 1)])

    # matrix dimsion
    seqlen = [4, 4]

    padded = pad_sequences_sparse(
        sequences=sequences, seqlen=seqlen,
        maxlen=3, truncating='post')

    # compare
    assert padded == expected


def test2():
    # expected
    expected = []
    expected.append([(3, 0)])
    expected.append([(1, 2), (0, 1), (2, 0)])

    # sequence
    sequences = []
    sequences.append([(1, 0), (2, 0), (3, 1)])
    sequences.append([(1, 3), (0, 2), (2, 1)])

    # matrix dimsion
    seqlen = [4, 4]

    padded = pad_sequences_sparse(
        sequences=sequences, seqlen=seqlen,
        maxlen=3, truncating='pre')

    # compare
    assert padded == expected


def test3():
    # expected
    expected = []
    expected.append([(1, 1), (2, 1), (3, 2)])
    expected.append([(1, 4), (0, 3), (2, 2)])

    # sequence
    sequences = []
    sequences.append([(1, 0), (2, 0), (3, 1)])
    sequences.append([(1, 3), (0, 2), (2, 1)])

    # matrix dimsion
    seqlen = [4, 4]

    padded = pad_sequences_sparse(
        sequences=sequences, seqlen=seqlen,
        maxlen=5, padding='pre')

    # compare
    assert padded == expected


def test4():
    # expected
    expected = []
    expected.append([(1, 0), (2, 0), (3, 1)])
    expected.append([(1, 3), (0, 2), (2, 1)])

    # sequence
    sequences = []
    sequences.append([(1, 0), (2, 0), (3, 1)])
    sequences.append([(1, 3), (0, 2), (2, 1)])

    # matrix dimsion
    seqlen = [4, 4]

    padded = pad_sequences_sparse(
        sequences=sequences, seqlen=seqlen,
        maxlen=5, padding='post')

    # compare
    assert padded == expected
