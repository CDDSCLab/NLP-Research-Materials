# Improving Event Coreference Resolution by Learning Argument Compatibility from Unlabeled Data
- 通过从无标签数据中学习参数兼容性来改进事件共指消解

# Adversarial Training for Weakly Supervised Event Detection
- 基于对抗训练的弱监督事件监测
- 构建一个具有良好覆盖率的大型事件相关候选集，利用对抗训练机制迭代地从候选集中识别信息实例，同时滤去噪声
- 假设：如果一个给定的单词在已知的事件实例中充当trigger，那么所有提到这个单词的事件实例表达的都是同一个事件。基于该假设，本文提出了一种简单的基于trigger的潜藏（事件）实例发现策略
- Figure 1 总体架构：将数据集分为可靠和不可靠两个部分，然后设计一个鉴别器(discriminator)和生成器(generator)。discriminator用于判断一个给定的实例是否具有信息性以及是否被正确标注，generator用于从原始数据中选择最confusing的实例来欺骗discriminator。我们使用可靠数据作为正面数据以及generator选择的数据作为负面数据来训练discriminator。同时，我们训练generator让其选择用于欺骗discriminator的数据。在训练过程中，generator能提供大量的潜藏噪声来增强disciminator，disciminator也可以影响generator选择信息更加丰富的数据。因为噪声对于优化generator和discriminator没有影响，所以当generator和discriminator达到平衡时，discriminator的抗噪能力会得到增强，从而更好地进行事件分类；generator能够有效地选择信息实例到discriminator。

系统架构包括三部分:

- instance encoder 使用CNN和BERT
- adversarial training 包括discriminator和generator. discriminator用来检测event triggers，识别数据集中的每个实例的时间类型。generator用来从不可靠数据集中选择实例，尽可能欺骗discriminator
- adaption for weakly supervised scenarios(对弱监督场景的适应)

# Biomedical Event Extraction Based on Knowledge-driven Tree-LSTM
- 为了有效地从复杂的上下文获取专业知识，本文使用树型LSTM
- 为了更好地获取专业知识，进一步使用外部知识库(KB)

# Document-Level Event Factuality Identification via Adversarial Neural Network
- 基于对抗神经网络的文档级事件真实性识别
- Figure 2
> 为了从文档视图中抽取事件的特征表示，我们考虑依赖路径和句子的序列内和序列间的attention。另外，由于DLEF语料库内文档内容的多样性，我们使用对抗训练来确保模型的健壮性。

# Geolocating Political Events in Text
- 从给定的句子中找出某一事件的发生地点
- 使用两个神经网络(RNN->LSTM)进行event-location linking任务；描述了基于规则的基线模型，以文献中的现有模型作为比较

# A Framework for Decoding Event-Related Potentials from Text
- 提出了一个新的框架，用于建模在阅读过程中收集的*事件相关电位（ERPs）*，该框架将预先训练好的卷积解码器与语言模型结合在一起。

# Sub-Event Detection from Twitter Streams as a Sequence Labeling Problem
- 针对检测子事件存在与否的binary classification问题，提出了一个新的神经基线模型
- 在检测子事件的类型上，提出了一个更合理的基线
- 考虑了连续tweets之间的时间顺序关系，将子事件检测界定为序列标记问题

# SEDTWik: Segmentation-based Event Detection from Tweets using Wikipedia