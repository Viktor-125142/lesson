from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
# mname = "facebook/wmt19-ru-en"
mname = "Helsinki-NLP/opus-mt-ru-en"
tokenizer = AutoTokenizer.from_pretrained(mname)
model = AutoModelForSeq2SeqLM.from_pretrained(mname)

input = "Это твоя первая программа?"
input_ids = tokenizer.encode(input, return_tensors="pt")
outputs = model.generate(input_ids)
decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(decoded)
