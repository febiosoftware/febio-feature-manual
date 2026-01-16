# febio-feature-manual
This repo is used to generate the FEBio Feature Manual. 

## Prerequisites
In order to generate the manual, you must install `mkdocs` and the `material` theme.

```
pip install mkdocs mkdocs-material
```

## Building the manual
To build the manual, first run the `build.py` Python script. 

```
py build.py
```

This will populate the docs folder (and subfolders) with markdown (md) files. 

Then, use mkdocs to build the manual. To test the manual locally, you can use:

```
mkdocs serve
```

Mkdocs will let you know when the site is ready and where to view it. 

To build the actual site, use

```
mkdocs build
```
This will create a new folder called `site` where the files are located. You can view the site by pointing a browser to the index.html file. 

## Extending the manual
To update the manual, all you need to do is update the `febio_feature.json` file. It is best not to hand-edit this file. Instead, use FEBio Studio (3.1 and above) to generate the file as follows:
* Open FEBioStudio and select the menu FEBio --> FEBio Info.
* In the dialog that appears, click the _Export_ button and overwrite the `febio_feature.json` file.

Note that FEBioStudio will include any features from active plugins that are loaded. If you only want the features from the plain-vanilla FEBio version, make sure to first disable all plugins! 

Then, rebuild the site as described above. 

By default, new features get a bare minimum webpage. To expand that page, you can create a markdown file for the feature in the /meta folder. Make sure to give it the exact same name as the webpage name (but with the .md extension). The contents of the md file will be added to the _Description_ section of the webpage.

