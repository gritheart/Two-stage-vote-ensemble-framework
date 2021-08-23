# Two-stage-vote ensemble framework
 
Identifying driver genes, exactly from massive genes with mutations, promotes accurate diagnosis and treatment of cancer. In recent years, a lot of works about uncovering driver genes based on integration of mutation data and gene interaction networks, is gaining more attention. However, it is in suspense if it is more effective for prioritizing driver genes when integrating various types of mutation information (frequency and functional impact) and gene networks. Hence, we build a two-stage-vote ensemble framework based on somatic mutations and mutual interactions. Specifically, we first represent and combine various kinds of mutation information, which are propagated through networks by an improved iterative framework. Then, the first vote is conducted on iteration results by voting methods and the second vote is performed to ensemble results of the first poll for the final driver gene list. Compared with four excellent previous approaches, our method has better performance in identifying driver genes on $33$ types of cancer from TCGA. Meanwhile, we also conduct a comparative analysis about two kinds of mutation information, five gene interaction networks and four voting strategies. Our framework offers a new view for data integration and promotes more latent cancer genes to be admitted. 

![image](https://github.com/gritheart/Two-stage-vote-ensemble-framework/blob/main/1-flowchart.jpg)

%**********************************************************************************************************************************************************************************

1. example：There are example data of Adenoid cystic carcino (ACC). It includes Functional Impact vectors (ACC_PPH2.mat and ACC_SIFT.mat), Frequency vector (ACC.mat) and five gene interaction networks handled by mutated coding genes in the experimental dataset of ACC (dawnrank_handled.mat, hint_hi2012_handled.mat, irefindex_handled.mat, multinet_handled.mat and wu_handled.mat). 

2. iterative_model.m: We combine Frequency, PolyPhen and SIFT scores in pair, which generates three feature combinations, i.e., Frequency_PolyPhen, Frequency_SIFT and PolyPhen_SIFT. Two elements in a combination are regarded as A0 and H0 of iterative model, respectively. Undirected graph M is provided by reconstructed networks mentioned above. In a word, there are 15 diverse inputs produced by three feature combinations and five undirected graphs and updated Ak and Hk are two outputs for each input.

3. voting_methods: We build a two-stage voting pipeline. First, we integrate corresponding iteration outcomes for Frequency_PolyPhen, Frequency_SIFT and PolyPhen_SIFT by the first vote, respectively, and produce three integrated ranked gene lists to study which feature combination is effective. Then, we integrate these three rankings by the second vote in order to get the final selection and detect novel driver genes. Here, we offer four various voting methods: Borda voting, Geometric mean, HPA and SetExpan, in order to explore whether voting methods influence results or not, if so, which ones perform well. 



