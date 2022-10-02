from operator import ge
from thirdweb import ThirdwebSDK
import os
from thirdweb.types.nft import NFTMetadataInput
from dotenv import load_dotenv

# You can customize this to a supported network or your own RPC URL
network = "polygon"

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
            "name": "#25 Hakapura",
            "number": "25"
        }
    ]
class Caso:
    def __init__(self, data):
        self.name = data["name"]
        self.number = data["number"]
        
        self.metadata = {
            "name": self.name,
            "description": f"""
                Work of the Easter Island artist Taku, in which the traditional Moai of Easter Island can be seen in an environment full of diversity. In this case, reference is made to the close relationship of the island's habitants with nature and, therefore, to the importance of preserving it for future generations.
                This work is part of the Hakapura collection, at the Mori category, a project promoted by the Chilean Kamanau Foundation in order to make visible the vulnerabilities of children's digital awareness. In this sense, for this collection a new smart contract format was innovated to promote the use of NFTs in philanthropic and social campaigns, so that by purchasing this digital object, its owner will be donating 90% of its profit to the cause. Funds will be distributed among the artists, a youth organization on the island and the foundation. If you buy this NFT, you will become a Mataroa (navigator in the Easter language) and you will be invited to participate in our community to contribute to the co-creation of recommendations for the proper use of new technologies. In addition, if you help us continue to raise funds for the cause by reselling your NFT, you will receive a second NFT to be part of our community of ambassadors for life. So, how important to you is the protection of children's digital awareness? It's time to put your cryptocurrencies into action!""",
            "date": "14-09-2022",
            "external_link": "https://kamanau.org/coleccion-nft/",
            "developer github": "@nicoriquelmecti",
            "developer address": "0x2D4De773c3Dfb579bebB958c2Ff6c34b864f0022",
            "image": open(f"Mori/{self.number}.jpg", "rb"),
            "attributes": [
               
                {
                "display_type": "number", 
                "trait_type": "Edition", 
                "value": 1
                },
                {
             
                "trait_type": "Category", 
                "value": "Mori"
                }
            ]
        }

            
#case_list = []

#Build case instances

for case in casos:
    case_object = Caso(case)


    # Build metadata
    metadata = NFTMetadataInput.from_json(case_object.metadata)

    # Mint NFT
    tx = contract.mint_to("0x985044bf9b17099820D2Af079FD14D55Ddaf53F3", metadata)
    receipt = tx.receipt
    token_id = tx.id
    nft = tx.data()
    print(nft)