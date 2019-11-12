# Document Embedding Enhanced Event Detection with Hierarchical and Supervised Attention
- 提出的DEEB-RNN模型用于句子级别的事件检测。该模型先通过一个面向事件检测的基于双向RNN的层次化、有监督的注意力(attention)学习document embeddings，把单词级别的注意力放到事件触发词之上，把句子级别的注意力放到句子所包含的事件之上。然后，该模型使用学习到的document embeddings促使另一个双向RNN模型识别事件触发词以及句子中的事件类型。
- 注意力机制(attention mechanism)

# Economic Event Detection in Company-Specific News Text
- 提出了一个数据集
- 把经济事件检测作为句子级别的多标签分类任务来处理
- 对比了SVM和基于词向量的RNN-LSTM的实现效果

# Zero-Shot Transfer Learning for Event Extraction
- Zero-Shot Learning 一种迁移学习。在ZSL中，共享了语义空间的结果允许我们构建一个zero-shot分类器（即不需要附加的训练例子）来处理以前没有出现过的(unseen)情形。本文要解决的问题就是，克服传统event extraction方法因其严重依赖人工标注，从而不能很好地适应新的事件类型的弊端。因此ZSL提供了一个新的思路。
- 使用更丰富的结构来丰富每个event mention和event type的语义表示
- 使用抽象信息表示(AMR)来识别候选参数和构造event mention结构

# Self-regulation: Employing a Generative Adversarial Network to Improve Event Detection
- event mention = trigger + context
- challenge: 神经网络容易受到杂乱(spurious)特征的干扰
- solution: 使用*双通道自规范学习策略*来规范化学习过程。在自规范过程中，训练GAN用以产生最杂乱的特征，另一个具备记忆抑制特性的神经网络则会消除这些杂乱特征导致的fakes。
- task definition: multi-class classification problem
- channel 1 Cooperative Network: 句子中的每个token或者是trigger或者不是，如果是，那就计算x触发所有事件类型中的每一个的概率（也就是关于事件类型的概率分布），这个概率分布是discriminator预测的，训练的目标是最小化预测概率分布与真实概率分布的偏离。
- channel 2 GAN G_{hat}尽可能生成最杂乱的特征来对抗D_{hat}, D_{hat}要能够免疫G_{hat}的“捣乱”
- Regulation with Memory Suppressor(记忆抑制器)
suppressor对比G_{hat}和G生成的向量，如果两者区别较大，就记住G输出的特征，这样就将G_{hat}造成的记忆抹除，也就是“记住好的特征，忘记坏的特征”。训练目标：GAN会评估G和G_{hat}输出的相似度，如果相似度越低(即差异越大)，则损失越低，更有利于GAN记住好的特征，所以损失函数=最小化这个相似度L_{diff}(即最大化差异)
- Learning to Predict
D使用的隐特征来自G的输出，以及被净化后的G_{hat}的输出。因此使用D输出的预测结果(token x关于事件类型的概率分布)作为实验输出。
G和G_{hat}使用RNN实现；D和D_{hat}被实现为一个全连接层，后跟softmax层
SELF中的所有网络{G,G_{hat},D,D_{hat}}都是用相同的batches联合训练(trained jointly)。 训练策略：随机梯度下降with shuffled mini-batches和AdaDelta更新规则。梯度的计算使用反向传播(back propagation)，规范化的实现采用dropout(以一定概率丢弃神经元，之前在变分子编码贝叶斯中遇到过。之前“记住好的特征，忘记坏的特征”中，“忘记坏的特征”就是通过这种丢弃神经元的方法实现)