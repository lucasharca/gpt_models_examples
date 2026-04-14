from openai import OpenAI
from config import api_key
from text_generator import TextGenerator
from summarize_text import TextSummarize
from simple_chatbot import SimpleChatbot

client = OpenAI(api_key=api_key)


#### Text Generator ####
# text_generator = TextGenerator(client)
# prompt = "Once upon a time"
# generated_text = text_generator.generate_text(prompt=prompt)
# print(generated_text)

#### Text Summarize ####
# text_summarize = TextSummarize(client)
# prompt = "Master Reef Guide Kirsty Whitman didn't need to tell me twice. Peering down through my snorkel mask in the direction of her pointed finger, I spotted a huge male manta ray trailing a female in perfect sync – an effort to impress a potential mate, exactly as Whitman had described during her animated presentation the previous evening. Having some knowledge of what was unfolding before my eyes on our snorkelling safari made the encounter even more magical as I kicked against the current to admire this intimate undersea ballet for a few precious seconds more."
# summarized_text = text_summarize.text_summarizer(prompt)
# print(summarized_text)
# response: Master Reef Guide, Kirsty Whitman, snorkel mask, male manta ray, female manta ray, mating behavior, snorkelling safari, undersea ballet, marine life, ocean, wildlife observation, reef, marine biology, animal behavior, underwater experience.

### Chatbot example ###
chatbot = SimpleChatbot(client)
prompt = "When was cheese first made?"
# prompt = "What is the next course to be uploaded to 365DataScience?"
chatbot_response = chatbot.poetic_chatbot(prompt)
print(chatbot_response)