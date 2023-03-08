# Data validation workshop
This is the repository containing all files used during the MipWise Data 
Validation Workshop.

## Repository guide

* The file `schemas.py` contains the schemas. This includes setting data types, 
foreign keys, and row predicates.

* The file `utils.py` contains a handful of functions related to read, check 
  and write data.

* The file `main.py` contains functions performing simple computations on the 
input data. This file also runs the data validation to see ticdat in action.

* The data is in the file `data.xlsx`.

* The `docs` directory contains the slide deck used in the workshop.

## Additional resources
Here are some useful resources that you can leverage to start building 
reliable solutions to support decision-making. If you have any question, 
don't hesitate to reach out to us: https://mipwise.com/contact

### Mip Go
The material we use to provide initial consulting and development training 
to our collaborators.

Link to the repository: https://github.com/mipwise/mip-go

This particular session shows how to implement data schemas using `ticdat`:
https://github.com/mipwise/mip-go/tree/main/5_develop/4_data_schema

### Mip Template
We typically use this template as a starting point for new projects. This is 
a complete Python package and a bit more involving.
Link to the repository: https://github.com/mipwise/mip_template

This particular file is a template schema that anyone can use as a starting 
point:
https://github.com/mipwise/mip_template/blob/master/mip_template/schemas.py
