from operator import ge
from thirdweb import ThirdwebSDK
import os
from thirdweb.types.nft import NFTMetadataInput
from dotenv import load_dotenv

# You can customize this to a supported network or your own RPC URL
network = "mumbai"


# Now we can create a new instance of the SDK
sdk = ThirdwebSDK(network)

# Load your env variables 
load_dotenv()
#Your metamask Private key 
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
#Yours cases data 
casos = os.getenv('CASOS')


sdk = ThirdwebSDK.from_private_key(PRIVATE_KEY, network)

# If you want to send transactions, you can instantiate the SDK with a private key instead:
contract = sdk.get_nft_collection("0xF1b3976AB13353A939DedAb7276F5C4a1ae55BcA")

# Data from cases

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