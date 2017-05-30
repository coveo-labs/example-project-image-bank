# example-project-image-bank
This project is an example regarding the format of publication in coveo-labs. It demonstrates how to extract images from powerpoint documents located in a google drive repository, then build an image bank with Rekognition and display it in an hosted search page on Coveo's Cloud Platform.

## Description
This repository shares examples of Coveo indexing pipeline extensions scripts, custom UI component, PushAPI scripts, etc. The entire code for a particular example resides in its project. When adding a project to coveo-labs, please use the same structure and guidelines as provided here.

## Available documentation
The code for the projects uses APIs, SDKs, and code from the Coveo Platform. You can use the following resources for more information and get started:
 
- Cloud Platform API general documentation: https://developers.coveo.com/display/public/CloudPlatform/Coveo+Cloud+V2+Home
- Cloud Platform Swagger: https://platform.cloud.coveo.com/docs?api=Platform (use the drop-down list to navigate the API categories, top-right of the page).
- PushAPI documentation: https://developers.coveo.com/display/public/CloudPlatform/Push+API+Usage+Overview
- Usage Analytics Swagger: https://usageanalytics.coveo.com/docs/ 
- Coveo Search UI Framework: https://github.com/coveo/search-ui 

## Contributing
Create a project in coveo-labs.
Make sure to comply with these guidelines:
- README.md file that contains the following sections: 
- Description 
- How-to build 
- How-to run 
- Dependencies 
- Link to live demo (when applicable).

Feel free to add more sections if you want, but have at least the one listed here.

Files in your project should have the following structure (when applicable):
- Project Root
- ---- README.md
- -------- /extensions # contains the indexing pipeline extensions
- -------- /indexing # contains the code to index through the PushAPI
- -------- /sources # contains the source configuration in json format
- -------- /ui # contains the ui for your project
- -------- /misc # everything that doesn’t fit in the other directories
 
The Coveo Team will look at your code and validate that :
- The guidelines are respected
- You didn’t forget any API key or password in it
- There is no malicious code

## How-to build 
This project do not require to build. However, you will need to integrate UI components, Indexing Pipeline Extensions, Sources into your Coveo organization.

## How-to run 
- If you don't have a Coveo organization, request a test one.
- In the Coveo Cloud Admin Console, create an API key with push permissions (and save it for later)
- Setup the extensions using the code provided in /extensions
- ---- Make sure you configure the extensions properly... 
- ---- ... "Images tagging with AWS Rekognition" will require AWS Secret/Key (you can get it under the free tier program)... 
- ---- ... "PPTX Image Extractor" will require the source id where you want to push, and also the API key you just created
- Create a google drive source named "PPTX Image Extraction"
- ---- Edit the source json and replace the mapping section by the json provided in /sources ("PPTXImageExtration.mappings.json")
- ---- Edit the source json and replace the Post-Conversion Extensions section by the json provided in /sources ("PPTXImageExtration.extensions.json"), making sure you replace the "extension_name_put_extension_id_here" by the proper extension id.
- Create a PUSH source named "PPTX Image Extraction Image Bank"
- ---- Edit the source json and replace the mapping section by the json provided in /sources ("PPTXImageExtrationImageBank.mappings.json")
- ---- Edit the source json and replace the Post-Conversion section by the json provided in /sources ("PPTXImageExtrationImageBank.extensions.json"), making sure you replace the "extension_name_put_extension_id_here" by the proper extension id.
- In the Fields section of the Coveo Cloud Admin Console, make sure that the field awsrekognition is set to "Multi-Value facet", is displayable in search results and can be used as a search operator.
- Note regarding the post-conversion extensions: as of today, extensions are limited to 5 seconds, so it could timeout with very large documents and only Coveo can increase that timeout limit for now. We are currently working on a way for clients/parters to increase the limit by themselves. Stay tuned!
- Trigger the initial build on PPTX Image Extraction
- In the Coveo Cloud Admin Console, create a new hosted search page, and replace the code by the one provided ("/ui/ImageBankBasicSearchPage.html")

## Dependencies 

## Authors
- Gauthier Robe (https://github.com/gforce81)
- Jérôme Devost (https://github.com/jdevost)
- Jean-François Cloutier (https://github.com/ancientwinds)
