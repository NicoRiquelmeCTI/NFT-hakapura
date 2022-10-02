from operator import ge
from thirdweb import ThirdwebSDK
import os
from thirdweb.types.nft import NFTMetadataInput
from dotenv import load_dotenv

# You can customize this to a supported network or your own RPC URL
network = "mumbai"


# Now we can create a new instance of the SDK
sdk = ThirdwebSDK(network)

# If you want to send transactions, you can instantiate the SDK with a private key instead:
load_dotenv()
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
sdk = ThirdwebSDK.from_private_key(PRIVATE_KEY, network)

contract = sdk.get_nft_collection("0xF1b3976AB13353A939DedAb7276F5C4a1ae55BcA")

# Data from cases
casos = [
        {
            "name": "#1 Healthy girl user of digital devices",
            "description": "Healthy user of digital devices young girl. I feel moderately concerned about climate change: Fear, Anxiety, guilt",
            "image": "fs.readFileSync(\"hakapura-images/1.jpg\")",
            "Gender": "Woman",
            "Age": "19",
            "Location": "Easter Island",
            "Relationship of technology and climate change": "ambivalent",
            "Responsible for climate change": "People",
            "internet bandwidth": "21.71",
            "Major connection hours": "18:00 - 00:00",
            "Screen hours per week": "3",
            "Screen hours per weekend": "5",
            "Concern about climate change": "Moderately concerned about climate change",
            "Feelings about climate change": "Fear, Anxiety, Guilt, Shame, Despair, Optimism (I have faith that climate change can be tackled)",
            "Thoughts about climate change": "The things I value will be destroyed, Our safety is threatened, I will do my best to do my bit",
            "DAST": "17",
            "Climate anxiety index": "10",
            "Technology intoxication index*": "31.02",
            "Digital addiction level": "Healthy user of digital devices young"
        },
        {
            "name": "#2 Excessive girl user of digital devices",
            "description": "Excessive user of digital devices young girl. I feel moderately concerned about climate change: guilt, Shame, Despair",
            "image": "fs.readFileSync(\"hakapura-images/2.jpg\")",
            "Gender": "Woman",
            "Age": "18",
            "Location": "Easter Island",
            "Relationship of technology and climate change": "ambivalent",
            "Responsible for climate change": "Unidentified",
            "internet bandwidth": "289",
            "Major connection hours": "18:00 - 00:00",
            "Screen hours per week": "7",
            "Screen hours per weekend": "10",
            "Concern about climate change": "Moderately concerned about climate change",
            "Feelings about climate change": "Guilt, Shame, Despair",
            "Thoughts about climate change": "I have doubts about having children for their future",
            "DAST": "21",
            "Climate anxiety index": "6",
            "Technology intoxication index*": "34.21",
            "Digital addiction level": "Excessive user of digital devices"
        },
        {
            "name": "#3 Healthy girl user of digital devices",
            "description": "Healthy users of digital devices young girl. I feel very concerned about climate change: Sadness, guilt, Optimism (I have faith that climate change can be tackled)",
            "image": "fs.readFileSync(\"hakapura-images/3.jpg\")",
            "Gender": "Woman",
            "Age": "21",
            "Location": "Easter Island",
            "Relationship of technology and climate change": "ambivalent",
            "Responsible for climate change": "People",
            "internet bandwidth": "543.27",
            "Major connection hours": "18:00 - 00:00",
            "Screen hours per week": "3",
            "Screen hours per weekend": "3",
            "Concern about climate change": "Very concerned about climate change",
            "Feelings about climate change": "Sadness, Guilt, Optimism (I have faith that climate change can be faced)",
            "Thoughts about climate change": "I have doubts about having children for their future, Future generations will not be able to enjoy the beauty that I enjoyed",
            "DAST": "23",
            "Climate anxiety index": "6.5",
            "Technology intoxication index*": "35.66",
            "Digital addiction level": "Healthy users of digital devices young"
        },
        {
            "name": "#4 Boy in danger of addiction to digital devices",
            "description": "Digital addiction endangered young boy. I feel a little worried about climate change: Optimism (I have faith that climate change can be tackled)",
            "image": "fs.readFileSync(\"hakapura-images/4.jpg\")",
            "Gender": "Men",
            "Age": "19",
            "Location": "Easter Island",
            "Relationship of technology and climate change": "Negative",
            "Responsible for climate change": "Technology",
            "internet bandwidth": "3",
            "Major connection hours": "12:00 - 18:00",
            "Screen hours per week": "3",
            "Screen hours per weekend": "5",
            "Concern about climate change": "A little worried about climate change",
            "Feelings about climate change": "Optimism (I have faith that climate change can be tackled)",
            "Thoughts about climate change": "The things I value will be destroyed",
            "DAST": "25",
            "Climate anxiety index": "1",
            "Technology intoxication index*": "35.89",
            "Digital addiction level": "Digital addiction endangered young"
        },
        {
            "name": "#5 Boy in danger of addiction to digital devices",
            "description": "Digital addiction endangered young boy. I feel Moderately concerned about climate change: Impotence",
            "image": "fs.readFileSync(\"hakapura-images/5.jpg\")",
            "Gender": "Men",
            "Age": "19",
            "Location": "Easter Island",
            "Relationship of technology and climate change": "Positive",
            "Responsible for climate change": "People",
            "internet bandwidth": "19.48",
            "Major connection hours": "12:00 - 18:00",
            "Screen hours per week": "5",
            "Screen hours per weekend": "7",
            "Concern about climate change": "Moderately concerned about climate change",
            "Feelings about climate change": "Impotence",
            "Thoughts about climate change": "I still don't lose hope in humanity",
            "DAST": "24",
            "Climate anxiety index": "4",
            "Technology intoxication index*": "37.45",
            "Digital addiction level": "Digital addiction endangered young"
        },
        {
            "name": "#6 Boy in danger of addiction to digital devices",
            "description": "Digital addiction endangered young boy. I feel a little worried about climate change: Anxiety",
            "image": "fs.readFileSync(\"hakapura-images/6.jpg\")",
            "Gender": "Men",
            "Age": "22",
            "Location": "Easter Island",
            "Relationship of technology and climate change": "Positive",
            "Responsible for climate change": "People",
            "internet bandwidth": "10",
            "Major connection hours": "12:00 - 18:00",
            "Screen hours per week": "7",
            "Screen hours per weekend": "5",
            "Concern about climate change": "A little worried about climate change",
            "Feelings about climate change": "Anxiety",
            "Thoughts about climate change": "I'll do my best to make my contribution",
            "DAST": "18",
            "Climate anxiety index": "8",
            "Technology intoxication index*": "41.36",
            "Digital addiction level": "Digital addiction endangered young"
        },
        {
            "name": "#7 Excessive girl user of digital devices",
            "description": "Excessive user of digital devices girl. I feel very concerned about climate change: Sadness, Fear, Anxiety",
            "image": "fs.readFileSync(\"hakapura-images/7.jpg\")",
            "Gender": "Woman",
            "Age": "19",
            "Location": "Easter Island",
            "Relationship of technology and climate change": "Impartial",
            "Responsible for climate change": "Unidentified",
            "internet bandwidth": "9",
            "Major connection hours": "12:00 - 18:00",
            "Screen hours per week": "5",
            "Screen hours per weekend": "7",
            "Concern about climate change": "Muy preocupada/o",
            "Feelings about climate change": "Sadness, Fear, Anxiety, Helplessness, Shame",
            "Thoughts about climate change": "People have failed, The future is terrifying, Humanity is doomed, The things I value will be destroyed, I hesitate to have children for their future, I still have not lost hope in humanity, I will do everything I can to do my input",
            "DAST": "33",
            "Climate anxiety index": "7",
            "Technology intoxication index*": "47.52",
            "Digital addiction level": "Excessive user of digital devices"
        },
        {
            "name": "#8 Excessive boy user of digital devices",
            "description": "Excessive user of digital devices boy. I feel extremely concerned about climate change: Sadness, Fear, Impotence",
            "image": "fs.readFileSync(\"hakapura-images/8.jpg\")",
            "Gender": "Hombre",
            "Age": "23",
            "Location": "Easter Island",
            "Relationship of technology and climate change": "Positive",
            "Responsible for climate change": "People",
            "internet bandwidth": "7.25",
            "Major connection hours": "12:00 - 18:00",
            "Screen hours per week": "7",
            "Screen hours per weekend": "7",
            "Concern about climate change": "Extremely concerned about climate change",
            "Feelings about climate change": "Sadness, Fear, Helplessness, Vulnerability, Optimism (I have faith that climate change can be faced)",
            "Thoughts about climate change": "People have failed, The future is terrifying, Things I hold dear will be destroyed, Our safety is threatened, I am hesitant to have children for their future, I still do not lose hope in humanity, I will do all I can to make my input",
            "DAST": "33",
            "Climate anxiety index": "15",
            "Technology intoxication index*": "50.57",
            "Digital addiction level": "Excessive user of digital devices"
        },
        {
            "name": "#9 Girl in danger of addiction to digital devices",
            "description": "Digital addiction endangered young girl. I feel very concerned about climate change: Sadness, Fear, Anxiety",
            "image": "fs.readFileSync(\"hakapura-images/9.jpg\")",
            "Gender": "Woman",
            "Age": "26",
            "Location": "Easter Island",
            "Relationship of technology and climate change": "Negative",
            "Responsible for climate change": "Unidentified",
            "internet bandwidth": "40",
            "Major connection hours": "18:00 - 00:00",
            "Screen hours per week": "3",
            "Screen hours per weekend": "7",
            "Concern about climate change": "Very concerned about climate change",
            "Feelings about climate change": "Sadness, Fear, Anxiety, Helplessness, Vulnerability, Guilt, Shame, Despair, Hurt",
            "Thoughts about climate change": "People have failed, Humanity is doomed, I have doubts about having children for their future",
            "DAST": "28",
            "Climate anxiety index": "21",
            "Technology intoxication index*": "54.43",
            "Digital addiction level": "Digital addiction endangered young"
        },
        {
            "name": "#10 Digitally addicted young boy",
            "description": "Digitally addicted young boy. I feel extremely concerned about climate change: Sadness, Impotence, Vulnerability",
            "image": "fs.readFileSync(\"hakapura-images/10.jpg\")",
            "Gender": "Men",
            "Age": "26",
            "Location": "Easter Island",
            "Relationship of technology and climate change": "Impartial",
            "Responsible for climate change": "People",
            "internet bandwidth": "360",
            "Major connection hours": "18:00 - 00:00",
            "Screen hours per week": "3",
            "Screen hours per weekend": "7",
            "Concern about climate change": "Extremely concerned about climate change",
            "Feelings about climate change": "Sadness, Helplessness, Vulnerability, Guilt, Despair",
            "Thoughts about climate change": "People have failed, The future is terrifying, Humanity is doomed, I will have fewer opportunities than my parents, Things I value will be destroyed, I have doubts about having children for their future, I still do not lose hope in humanity, I will everything I can to make my contribution",
            "DAST": "47",
            "Climate anxiety index": "18",
            "Technology intoxication index*": "81.94",
            "Digital addiction level": "Digitally addicted young"
        },
        {
            "name": "#11 Digitally addicted young girl",
            "description": "Digitally addicted young girl. I feel very concerned about climate change: Sadness, Anxiety, Impotence",
            "image": "fs.readFileSync(\"hakapura-images/11.jpg\")",
            "Gender": "Woman",
            "Age": "25",
            "Location": "Easter Island",
            "Relationship of technology and climate change": "Negative",
            "Responsible for climate change": "People",
            "internet bandwidth": "270",
            "Major connection hours": "18:00 - 00:00",
            "Screen hours per week": "3",
            "Screen hours per weekend": "5",
            "Concern about climate change": "Very concerned about climate change",
            "Feelings about climate change": "Sadness, Anxiety, Helplessness, Guilt",
            "Thoughts about climate change": "People have failed, The future is terrifying, Humanity is doomed, I hesitate to have children for their future, I will do my best to contribute",
            "DAST": "51",
            "Climate anxiety index": "12",
            "Technology intoxication index*": "76.98",
            "Digital addiction level": "Digitally addicted young"
        },
        {
            "name": "#12 Digitally addicted young girl",
            "description": "Digitally addicted young girl. I feel extremely concerned about climate change: Fear, Vulnerability, guilt",
            "image": "fs.readFileSync(\"hakapura-images/12.jpg\")",
            "Gender": "Woman",
            "Age": "25",
            "Location": "Easter Island",
            "Relationship of technology and climate change": "Negative",
            "Responsible for climate change": "People, companies and governments",
            "internet bandwidth": "190",
            "Major connection hours": "18:00 - 00:00",
            "Screen hours per week": "5",
            "Screen hours per weekend": "7",
            "Concern about climate change": "Extremely concerned about climate change",
            "Feelings about climate change": "Fear, Vulnerability, Guilt, Despair",
            "Thoughts about climate change": "People have failed, The future is terrifying, Humanity is doomed, Things I value will be destroyed, I hesitate to have children for their future, I will do my best to contribute",
            "DAST": "57",
            "Climate anxiety index": "17",
            "Technology intoxication index*": "86.52",
            "Digital addiction level": "Digitally addicted young"
        }
    ]

class Caso:
    def __init__(self, data):
        self.name = data["name"]
        self.number = self.name.split("#")[1].split(" ")[0]
        self.description = data["description"]
        self.image = data["image"]
        self.gender = data["Gender"]
        self.age = data["Age"]
        self.location = data["Location"]
        self.rel_t_cc = data["Relationship of technology and climate change"]
        self.responsible = data["Responsible for climate change"]
        self.bandwidth = float(data["internet bandwidth"])
        self.con_hours = data["Major connection hours"]
        self.hpw = int(data["Screen hours per week"])
        self.hpwk = int(data["Screen hours per weekend"])
        self.concern = data["Concern about climate change"]
        self.feelings = data["Feelings about climate change"]
        self.thoughts = data["Thoughts about climate change"]
        self.dast = float(data["DAST"])
        self.climate_anxiety = float(data["Climate anxiety index"])
        self.tech_intoxication = float(data["Technology intoxication index*"])
        self.da_level = data["Digital addiction level"]
        self.metadata = {
            "name": self.name,
            "description": f"""This NFT represents the testimony of a young {self.gender} from Easter Island about their perception of the impact that hyperconnection has on their life. From the data collected on their symptoms of addiction to digital devices and climate anxiety, an AI model was used to interpret and encode them in the work painted by the artist from Easter, Tauroa, thus generating the image you see. The input used was:
                {self.description}.  
                This work is part of the Hakapura collection, a project promoted by the Chilean Kamanau Foundation in order to make visible the vulnerabilities of children's digital awareness. In this sense, for this collection a new smart contract format was innovated to promote the use of NFTs in philanthropic and social campaigns, so that by purchasing this digital object, its owner will be donating 90% of its profit to the cause. Funds will be distributed among the artists, a youth organization on the island and the foundation.
                If you buy this NFT, you will become a Mataroa (navigator in the Easter language) and you will be invited to participate in our community to contribute to the co-creation of recommendations for the proper use of new technologies. In addition, if you help us continue to raise funds for the cause by reselling your NFT, you will receive a second NFT to be part of our community of ambassadors for life. 
                So, how important to you is the protection of children's digital awareness? It's time to put your cryptocurrencies into action!""",
            "date": "14-09-2022",
            "external_link": "https://kamanau.org/coleccion-nft/",
            "developer github": "@nicoriquelmecti",
            "developer address": "0x2D4De773c3Dfb579bebB958c2Ff6c34b864f0022",
            "image": open(f"hakapura-images/{self.number}.jpg", "rb"),
            "attributes": [
                {
                "trait_type": "Location", 
                "value": self.location
                },
                {
                "trait_type": "Category", 
                "value": "Ahí" 
                },
                
                {
                "trait_type": "Gender", 
                "value": self.gender
                }, 
                {
                "trait_type": "Digital addiction level", 
                "value": self.da_level
                }, 
                {
                "trait_type": "Concern about climate change", 
                "value": self.concern
                },
                {
                "trait_type": "Relationship of technology and climate change", 
                "value": self.rel_t_cc
                }, 
                 
                {
                "trait_type": "Responsible for climate change", 
                "value": self.responsible
                },
                
                {
                "display_type": "number",
                "trait_type": "internet bandwidth", 
                "value": self.bandwidth
                }, 
                {
                "trait_type": "Major connection hours", 
                "value": self.con_hours
                }, 
                {
                "display_type": "number",
                "trait_type": "Screen hours per week", 
                "value": self.hpw
                },
                {
                "display_type": "number",
                "trait_type": "Screen hours per weekend", 
                "value": self.hpwk
                },
                {
                "display_type": "number",
                "trait_type": "DAST", 
                "value": self.dast
                },
                {
                "display_type": "number",
                "trait_type": "Climate anxiety index", 
                "value": self.climate_anxiety
                },
                {
                "display_type": "number",
                "trait_type": "Technology intoxication index*", 
                "value": self.tech_intoxication
                },
                {
                "display_type": "number", 
                "trait_type": "Edition", 
                "value": 1
                }
            ]
        }

    def build_traits(self):
        for feeling in self.feelings.split(", "):

            self.metadata["attributes"].append(
                {
                "trait_type": "Feelings about climate change", 
                "value": feeling
                }
            )

        for thought in self.thoughts.split(", "):
            self.metadata["attributes"].append(
                {
                "trait_type": "Thoughts about climate change", 
                "value": thought
                }
            )
            

#Build case instances

for case in casos[5:]:
    case_object = Caso(case)
    case_object.build_traits()
    #print(case_object.metadata)
    #case_list.append(case_object)

    # Build metadata
    metadata = NFTMetadataInput.from_json(case_object.metadata)

    # Mint NFT
    tx = contract.mint_to("0x985044bf9b17099820D2Af079FD14D55Ddaf53F3", metadata)
    receipt = tx.receipt
    token_id = tx.id
    nft = tx.data()
    print(nft)