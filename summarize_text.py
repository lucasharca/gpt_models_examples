from openai import OpenAI

class TextSummarize:
    def __init__(self, client: OpenAI) -> None:
        self.client = client
    
    def text_summarizer(self, prompt):
        messages = [
            {
                    "role": "system",
                    "content": "You will be provided with a block of text, and your task is to extract a list of keywords from it."
            },
            {
                    "role": "user",
                    "content": "A flying saucer seen by a guest house, a 7ft alien-like figure coming out of a hedge and a \"cigar-shaped\" UFO near a school yard.\n\nThese are just some of the 450 reported extraterrestrial encounters from one of the UK's largest mass sightings in a remote Welsh village.\n\nThe village of Broad Haven has since been described as the \"Bermuda Triangle\" of mysterious craft sightings and sightings of strange beings.\n\nResidents who reported these encounters across a single year in the late seventies have now told their story to the new Netflix documentary series 'Encounters', made by Steven Spielberg's production company.\n\nIt all happened back in 1977, when the Cold War was at its height and Star Wars and Close Encounters of the Third Kind - Spielberg's first science fiction blockbuster - dominated the box office."
            },
            {
                    "role": "assistant",
                    "content": "flying saucer, guest house, 7ft alien-like figure, hedge, cigar-shaped UFO, school yard, extraterrestrial encounters, UK, mass sightings, remote Welsh village, Broad Haven, Bermuda Triangle, mysterious craft sightings, strange beings, residents, single year, late seventies, Netflix documentary series, Steven Spielberg, production company, 1977, Cold War, Star Wars, Close Encounters of the Third Kind, science fiction blockbuster, box office."
            },
            {
                    "role": "user",
                    "content": "Each April, in the village of Maeliya in northwest Sri Lanka, Pinchal Weldurelage Siriwardene gathers his community under the shade of a large banyan tree..."
            },
            {
                    "role": "assistant",
                    "content": "April, Maeliya, northwest Sri Lanka, Pinchal Weldurelage Siriwardene, banyan tree, wewa, reservoir, tank, Sinhala, rice paddies, agrarian committee, coconut milk, blessings, harvest, irrigation canals, farmers, village life, pagoda, temple."
            },
            {
                    "role": "user",
                    "content": prompt
            }
        ]

        response = self.client.responses.create(
            model="gpt-4.1-mini",
            input=messages,
            temperature=0.5,
            max_output_tokens=256
        )
        
        return response.output_text.strip()