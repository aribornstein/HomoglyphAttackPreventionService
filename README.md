# Homoglyph Attack Prevention Service
Homoglyphic attacks can be used to attack State of the Art NLP models, this repo provides an open source service using Azure to preventing most homoglyphic attacks. For more information on Homoglyphic attacks check out [this post on the subject](https://medium.com/@aribornstein/homoglyph-attack-prevention-with-ocr-a6741ee7c9cd)

To use the service just send a URL encoded query string of up to 200 characters to the service perfect for validating tweets. Below is an example call using curl be sure to use your own service endpoint.

![Example call](https://cdn-images-1.medium.com/max/800/1*pyYdiHRBelu5YCBRGS2UrQ.png)

## One Click Deployment

<a href="https://portal.azure.com/?WT.mc_id=aiml-0000-abornst#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Faribornstein%2FHomoglyphAttackPreventionService%2Fmaster%2Fazuredeploy.json" target="_blank">
<img src="https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/1-CONTRIBUTION-GUIDE/images/deploytoazure.png"/>
</a>

If you need an azure account you can get a free one [here](https://azure.microsoft.com/offers/ms-azr-0044p/?WT.mc_id=aiml-0000-abornst)

## Docker Service 
```
docker run --rm -it  -p 5000:5000  -e 'region=westeurope' -e 'key=put azure cv key here' abornst/homoglyph_service
```
