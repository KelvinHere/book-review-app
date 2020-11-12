Directory for test MongoDB

To run unittests in testbookapp.py correctly you must start MongoDb in this directory

1.  Start mongod using "mongod --dbpath testdb" in the root directory
2.  Run unittests with "python 3 -m unittest testbookapp.py -v" in the root directory

See link to more testing information in the readdme.md of this repo.
