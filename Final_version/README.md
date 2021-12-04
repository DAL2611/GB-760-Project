# GB-760-Project Group Members
**Yuyang Xie** yxie222@wisc.edu

**Calvin Chen** chen2328@wisc.edu

**Daniel Hom** dhom@wisc.edu

**Lucius Liu** fliu239@wisc.edu

**Wanpeng Meng** wmeng24@wisc.edu

**Vitchuda Poonyakanok (PINK)** poonyakanok@wisc.edu

**DUC LE** dale5@wisc.edu


# How to read the code

We uploaded each file in each part of each milestone in this Final_version folder. Every file can be indexed by its commitment information. Please follow this README.md to read code in order.

The files of milestone 1 (M1) are about simply reading tweets from the Twitter API or a file and writting them to a file on disk, which is considered as our “data lake” in this project.

Then, milestone 2 (M2) mainly consists of transitioning our code to use a PostgreSQL database instead of a data lake, continuing to read tweets from the Twitter API and writting them to our database using Python.

Finally, the files of milestone 3 (M3) are about upgrading our code to use Kafka as a streaming message queue.

The detailed running code instruction is as follows:

In **word_count.py**, we need to type "python word_count.py -like ("-word" is for a word and "--phrase phrase" is for a phrase)".

In **word_count_postgres.py**, we also need to input "python word_count_postgres.py -like ("-word" is for a word and "--phrase phrase" is for a phrase)".
