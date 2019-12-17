import numpy as np
import random


def f_score(predict, golden, mode='f'):
    assert len(predict) == len(golden)
    TP = 0
    FP = 0
    FN = 0
    TN = 0
    for i in range(len(predict)):
        if predict[i] == golden[i] and predict[i] != 0:
            TP += 1
        elif predict[i] != golden[i]:
            if predict[i] == 0:
                FN += 1
            elif golden[i] == 0:
                FP += 1
            else:
                FN += 1
                FP += 1
        else:
            TN += 1
    try:
        P = TP / (TP + FP)
        R = TP / (TP + FN)
        F = 2 * P * R / (P + R)
    except:
        P = R = F = 0

    if mode == 'f':
        return P, R, F
    else:
        return TP, FN, FP, TN


def get_batch(data, batch_size, shuffle=True):
    assert len(list(set([np.shape(d)[0] for d in data]))) == 1
    num_data = np.shape(data[0])[0]
    indices = list(np.arange(0, num_data))
    if shuffle:
        random.shuffle(indices)
    for i in range((num_data // batch_size) + 1):
        select_indices = indices[i * batch_size:(i + 1) * batch_size]
        yield [np.take(d, select_indices, axis=0) for d in data]


def get_trigger_feeddict(model, batch, is_train=True):
    posis, sents, maskls, maskrs, event_types, lexical = batch
    return {model.posis: posis, model.sents: sents, model.maskls: maskls, model.maskrs: maskrs,
            model._labels: event_types, model.lexical: lexical, model.is_train: is_train}


def get_argument_feeddict(model, batch, is_train=True, stage='trigger'):
    sents, event_types, roles, maskl, maskm, maskr, \
    trigger_lexical, argument_lexical, trigger_maskl, trigger_maskr, trigger_posis, argument_posis = batch

    if stage == 'trigger':
        return get_trigger_feeddict(model,
                                    (trigger_posis, sents, trigger_maskl, trigger_maskr, event_types, trigger_lexical),
                                    False)
    elif stage == "argument":
        return {model.sents: sents, model.trigger_posis: trigger_posis, model.argument_posis: argument_posis,
                model.maskls: maskl, model.maskms: maskm, model.maskrs: maskr,
                model.trigger_lexical: trigger_lexical, model.argument_lexical: argument_lexical,
                model._labels: roles, model.is_train: is_train, model.event_types: event_types}
    else:
        raise ValueError("stage could only be trigger or argument")
