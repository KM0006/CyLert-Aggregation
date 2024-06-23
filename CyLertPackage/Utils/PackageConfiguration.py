
CySecBERTModelName = "markusbayer/CySecBERT"

from transformers import AutoModel, AutoTokenizer

CySecBertTokenizer = AutoTokenizer.from_pretrained(CySecBERTModelName)
CySecBertModel = AutoModel.from_pretrained(CySecBERTModelName)

