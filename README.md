# NFT Hakapura

What is the impact that Hyperconnection has on the lives of young people? It is the question that motivated the creation of this collection that mixes science, art and technology to promote a social cause as important as the protection of children's digital awareness. On this occasion, the Kamanau Foundation interviewed 12 young people from Easter Island, to measure symptoms of addiction to digital devices and climate anxiety factors; data that was later processed by Artificial Intelligence to merge them with the works of two outstanding plastic artists from RapaNui. In this way, the first artistic and philanthropic collection of the Kamanau Foundation is born, which has a total issue of 30 NFTs.

## Smartcontract

Smartcontract developed with [thirdweb](https://thirdweb.com/) SDK.

```bash
pip install thirdweb-sdk
```

## Metadata

You need to allocate all your cases data to be parsed by this script, on a data.json file at root of the repo folder. This file, will contain a list of objects in the form of:

```bash
{
    "data": [
        {
            "name": "",
            "description": "",
            "image": "",
            "Gender": "",
            "Age": "",
            "Location": "",
            "Relationship of technology and climate change": "",
            "Responsible for climate change": "",
            "internet bandwidth": "",
            "Major connection hours": "",
            "Screen hours per week": "",
            "Screen hours per weekend": "",
            "Concern about climate change": "",
            "Feelings about climate change": "",
            "Thoughts about climate change": "",
            "DAST": "",
            "Climate anxiety index": "",
            "Technology intoxication index*": "",
            "Digital addiction level": ""
        },
        {
            "name": "",
            "description": "",
            "image": "",
            "Gender": "",
            "Age": "",
            "Location": "",
            "Relationship of technology and climate change": "",
            "Responsible for climate change": "",
            "internet bandwidth": "",
            "Major connection hours": "",
            "Screen hours per week": "",
            "Screen hours per weekend": "",
            "Concern about climate change": "",
            "Feelings about climate change": "",
            "Thoughts about climate change": "",
            "DAST": "",
            "Climate anxiety index": "",
            "Technology intoxication index*": "",
            "Digital addiction level": ""
        },
}
```

## Run the script

When you are ready, you can run the script to mint all your NFTs with this command:
    ```bash
    python3 script.py
    ```

This will load your cases data, parse it by the Case object class and build its treats, then will load each json metadata and mint it with your NFT Collection smartcontract. 
 
## License
[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/deed.es)