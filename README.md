# WarmMolGen-Demo

This application demonstrates the generation capabilities of the models trained as part of the paper titled [*"Exploiting Pretrained Biochemical Language Models for Targeted Drug Design"*](https://github.com/boun-tabi/biochemical-lms-for-drug-design), which has been accepted for publication in Bioinformatics Published by Oxford University Press. The available models are:

* **WarmMolGen**
  - **WarmMolGenOne** (i.e. *EncDecBase*)
  
    A target specific molecule generator where warm-started (i.e. initialized from pretrained models) model trained with one-stage starategy on targeted drug design.
  - **WarmMolGenTwo** (i.e. *EncDecLM*)
  
    A target specific molecule generator where warm-started (i.e. initialized from pretrained models) model trained withtwo-stage strategy containing a pre-finetuning on molecular generation followed by target-specific training. 
* **ChemBERTaLM**

  A molecule generator model finetuned from ChemBERTa checkpoint. 

### Usage
* Install requirements via `pip` dependency manager. 
  ```
  pip install requirements.txt 
  ``` 
* Run application:
  ```
  streamlit run About.py
  ```
  
### Citation
```bibtex
@article{10.1093/bioinformatics/btac482,
    author = {Uludoğan, Gökçe and Ozkirimli, Elif and Ulgen, Kutlu O. and Karalı, Nilgün Lütfiye and Özgür, Arzucan},
    title = "{Exploiting Pretrained Biochemical Language Models for Targeted Drug Design}",
    journal = {Bioinformatics},
    year = {2022},
    doi = {10.1093/bioinformatics/btac482},
    url = {https://doi.org/10.1093/bioinformatics/btac482}
}
```
