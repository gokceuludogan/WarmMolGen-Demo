import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import mols2grid
import textwrap
from transformers import RobertaForCausalLM, RobertaTokenizer, pipeline

# @st.cache(allow_output_mutation=False, hash_funcs={Tokenizer: str})
@st.cache(suppress_st_warning=True)
def load_models():
    model = RobertaForCausalLM.from_pretrained("gokceuludogan/ChemBERTaLM")
    return model

    
st.set_page_config(page_title="ChemBERTaLM Demo", page_icon="✨", layout='wide')
st.markdown("# ChemBERTaLM Demo")
st.sidebar.header("ChemBERTaLM Demo")
st.markdown(
    """
    This demo illustrates ChemBERTaLM models' generation capabilities. 


    Given a set of parameters, ChemBERTaLM generates a collection of molecules.


    Please configure parameters from the sidebar 👈 to generate molecules!


    See below for saving the output molecules and the code snippet generating them!
"""
)

tokenizer = RobertaTokenizer.from_pretrained("gokceuludogan/ChemBERTaLM")
model = load_models()
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

st.sidebar.subheader("Configurable parameters")

num_mols = st.sidebar.number_input(
    "Number of generated molecules",
    min_value=0,
    max_value=200,
    value=20,
    help="The number of molecules to be generated.",
)

max_new_tokens = st.sidebar.number_input(
    "Maximum length",
    min_value=0,
    max_value=1024,
    value=128,
    help="The maximum length of the sequence to be generated.",
)

do_sample = True 

# target = st.text_input(
#     "Input Sequence",
#     "",
# )
target = ""
params = {'do_sample': do_sample, 'num_return_sequences': num_mols, 'max_length': max_new_tokens}
outputs = generator(target, **params)
output_smiles = [output["generated_text"] for output in outputs]
st.write("### Generated Molecules")
df_smiles = pd.DataFrame({'SMILES': output_smiles})
raw_html = mols2grid.display(df_smiles, mapping={"SMILES": "SMILES"})._repr_html_()
components.html(raw_html, width=900, height=450, scrolling=True)
st.markdown("## How to Generate")
generation_code = f"""
from transformers import RobertaForCausalLM, RobertaTokenizer, pipeline

tokenizer = RobertaTokenizer.from_pretrained("gokceuludogan/ChemBERTaLM")
model = RobertaForCausalLM.from_pretrained("gokceuludogan/ChemBERTaLM")
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

params = {params}
outputs = generator("{target}", **params)
output_smiles = [output["generated_text"] for output in outputs]
"""
st.code(textwrap.dedent(generation_code)) 

