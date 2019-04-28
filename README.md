# HomoglyphAttackPreventionService
A service for preventing homoglyph attacks.

## One Click Deployment

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/{}azuredeploy.json" target="_blank">
<img src="https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/1-CONTRIBUTION-GUIDE/images/deploytoazure.png"/>
</a>

## Docker Service 
```
docker run --rm -it  -p 5000:5000  -e 'region=westeurope' -e 'key=put azure cv key here' abornst/homoglyph_service
```
