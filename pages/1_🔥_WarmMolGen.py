import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import mols2grid
import textwrap
import numpy as np
from transformers import EncoderDecoderModel, RobertaTokenizer

# @st.cache(allow_output_mutation=False, hash_funcs={Tokenizer: str})
@st.cache(suppress_st_warning=True)
def load_models():
    # protein_tokenizer = RobertaTokenizer.from_pretrained("gokceuludogan/WarmMolGenTwo")
    # mol_tokenizer = RobertaTokenizer.from_pretrained("seyonec/PubChem10M_SMILES_BPE_450k")
    model1 = EncoderDecoderModel.from_pretrained("gokceuludogan/WarmMolGenOne")
    model2 = EncoderDecoderModel.from_pretrained("gokceuludogan/WarmMolGenTwo")
    return model1, model2#, protein_tokenizer, mol_tokenizer    

st.set_page_config(page_title="WarmMolGen Demo", page_icon="🔥", layout='wide')
st.markdown("# WarmMolGen Demo")
st.sidebar.header("WarmMolGen Demo")
st.markdown(
    """
    This demo illustrates WarmMolGen models' generation capabilities. 


    Given a target sequence and a set of parameters, the models generate molecules targeting the given protein sequence.


    Please enter an input sequence below 👇  and configure parameters from the sidebar 👈 to generate molecules!


    See below for saving the output molecules and the code snippet generating them!
"""
)
protein_tokenizer = RobertaTokenizer.from_pretrained("gokceuludogan/WarmMolGenTwo")
mol_tokenizer = RobertaTokenizer.from_pretrained("seyonec/PubChem10M_SMILES_BPE_450k")
#model1, model2, protein_tokenizer, mol_tokenizer = load_models()
model1, model2 = load_models()

st.sidebar.subheader("Configurable parameters")

model_name = st.sidebar.selectbox(
    "Model Selector",
    options=[
        "WarmMolGenOne",
        "WarmMolGenTwo",
    ],
    index=0,
)

num_mols = st.sidebar.number_input(
    "Number of generated molecules",
    min_value=0,
    max_value=20,
    value=10,
    help="The number of molecules to be generated.",
)

max_new_tokens = st.sidebar.number_input(
    "Maximum length",
    min_value=0,
    max_value=1024,
    value=128,
    help="The maximum length of the sequence to be generated.",
)

do_sample = st.sidebar.selectbox(
    "Sampling?",
    (True, False),
    help="Whether or not to use sampling; use beam decoding otherwise.",
)

# num_beams = st.sidebar.number_input(
#     "Number of beams",
#     min_value=0,
#     max_value=20,
#     value=0,
#     help="The number of beams to use for beam search.",
# )
num_beams = None if do_sample is True else int(num_mols)

target = st.text_area(
    "Target Sequence",
    "MENTENSVDSKSIKNLEPKIIHGSESMDSGISLDNSYKMDYPEMGLCIIINNKNFHKSTG",
)
inputs = protein_tokenizer(target, return_tensors="pt")

model = model1 if model_name == 'WarmMolGenOne' else model2
outputs = model.generate(**inputs, decoder_start_token_id=mol_tokenizer.bos_token_id, 
                         eos_token_id=mol_tokenizer.eos_token_id, pad_token_id=mol_tokenizer.eos_token_id, 
                         max_length=int(max_new_tokens), num_return_sequences=int(num_mols), 
                         do_sample=do_sample, num_beams=num_beams)
output_smiles = mol_tokenizer.batch_decode(outputs, skip_special_tokens=True)
st.write("### Generated Molecules")
df_smiles = pd.DataFrame({'SMILES': output_smiles})
raw_html = mols2grid.display(df_smiles, mapping={"SMILES": "SMILES"})._repr_html_()
components.html(raw_html, width=900, height=450, scrolling=True)
st.markdown("## How to Generate")
generation_code = f"""
from transformers import EncoderDecoderModel, RobertaTokenizer

protein_tokenizer = RobertaTokenizer.from_pretrained("gokceuludogan/{model_name}") 
mol_tokenizer = RobertaTokenizer.from_pretrained("seyonec/PubChem10M_SMILES_BPE_450k")
model = EncoderDecoderModel.from_pretrained("gokceuludogan/{model_name}") 

inputs = protein_tokenizer("{target}", return_tensors="pt")
outputs = model.generate(**inputs, decoder_start_token_id=mol_tokenizer.bos_token_id, 
                         eos_token_id=mol_tokenizer.eos_token_id, pad_token_id=mol_tokenizer.eos_token_id, 
                         max_length={max_new_tokens}, num_return_sequences={num_mols}, do_sample={do_sample}, num_beams={num_beams})

mol_tokenizer.batch_decode(outputs, skip_special_tokens=True)
"""
st.code(textwrap.dedent(generation_code))
