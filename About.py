# Copyright 2018-2022 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="About WarmMolGen",
        page_icon="🚀",
        layout='wide'
    )

    st.write("## [Exploiting Pretrained Biochemical Language Models for Targeted Drug Design](https://doi.org/10.1093/bioinformatics/btac482)")
    #st.sidebar.title("Model Demos")
    st.sidebar.success("Select a model demo above.")

    st.markdown(
        """
        This application demonstrates the generation capabilities of the models trained as part of the study below published in *Bioinformatics*. The available models are: 
        * WarmMolGen
            - WarmMolGenOne (i.e. EncDecBase)
            - WarmMolGenTwo (i.e. EncDecLM)
        * ChemBERTaLM 

        👈 Select a model demo from the sidebar to generate molecules right away 🚀

        ### Abstract
        **Motivation:** The development of novel compounds targeting proteins of interest is one of the most important tasks in
        the pharmaceutical industry. Deep generative models have been applied to targeted molecular design and have shown
        promising results. Recently, target-specific molecule generation has been viewed as a translation between the protein
        language and the chemical language. However, such a model is limited by the availability of interacting protein–ligand
        pairs. On the other hand, large amounts of unlabelled protein sequences and chemical compounds are available and
        have been used to train language models that learn useful representations. In this study, we propose exploiting pretrained
        biochemical language models to initialize (i.e. warm start) targeted molecule generation models. We investigate
        two warm start strategies: (i) a one-stage strategy where the initialized model is trained on targeted molecule generation
        and (ii) a two-stage strategy containing a pre-finetuning on molecular generation followed by target-specific training. We
        also compare two decoding strategies to generate compounds: beamsearch and sampling.

        **Results:** The results show that the warm-started models perform better than a baseline model trained from scratch.
        The two proposed warm-start strategies achieve similar results to each other with respect to widely used metrics
        from benchmarks. However, docking evaluation of the generated compounds for a number of novel proteins suggests
        that the one-stage strategy generalizes better than the two-stage strategy. Additionally, we observe that
        beam search outperforms sampling in both docking evaluation and benchmark metrics for assessing compound
        quality.

        **Availability and implementation:** The source code is available at https://github.com/boun-tabi/biochemical-lms-for-drug-design and the materials (i.e., data, models, and outputs) are archived in Zenodo at https://doi.org/10.5281/zenodo.6832145. 
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
    """
    )
    # page_names_to_funcs = {
    #     "—": intro,
    #     "Plotting Demo": plotting_demo,
    #     "Mapping Demo": mapping_demo,
    #     "DataFrame Demo": data_frame_demo
    # }

    # demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
    # page_names_to_funcs[demo_name]()

if __name__ == "__main__":
    run()
