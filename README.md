# Two-stage-vote ensemble framework
 
Identifying driver genes, exactly from massive genes with mutations, promotes accurate diagnosis and treatment of cancer. In recent years, a lot of works about uncovering driver genes based on integration of mutation data and gene interaction networks, is gaining more attention. However, it is in suspense if it is more effective for prioritizing driver genes when integrating various types of mutation information (frequency and functional impact) and gene networks. Hence, we build a two-stage-vote ensemble framework based on somatic mutations and mutual interactions. Specifically, we first represent and combine various kinds of mutation information, which are propagated through networks by an improved iterative framework. Then, the first vote is conducted on iteration results by voting methods and the second vote is performed to ensemble results of the first poll for the final driver gene list. Compared with four excellent previous approaches, our method has better performance in identifying driver genes on $33$ types of cancer from TCGA. Meanwhile, we also conduct a comparative analysis about two kinds of mutation information, five gene interaction networks and four voting strategies. Our framework offers a new view for data integration and promotes more latent cancer genes to be admitted. 

![image](https://github.com/gritheart/Two-stage-vote-ensemble-framework/master/1-flowchart.jpg)
