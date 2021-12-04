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

## Milestone 1

The files of milestone 1 (M1) are about simply reading tweets from the Twitter API or a file and writting them to a file on disk, which is considered as our “data lake” in this project.

The detailed running code instruction is as follows:

  * In **server.py**: Type "python server.py". Then we can type "ls" to see all files in the project and get the **tweets.txt**.

  * In **word_count.py**: Type "python word_count.py -w -word" // Type 'python word_count.py -w "your phrase"'

    ("-word" is for a word and "--phrase phrase" is for a phrase)".

  * In **vocabulary_size.py**: Type "python vocabulary_size.py".

## Milestone 2

Then, milestone 2 (M2) mainly consists of transitioning our code to use a PostgreSQL database instead of a data lake, continuing to read tweets from the Twitter API and writting them to our database using Python.

  * To use **server_postgres.sql**:
    Type "git clone git@github.com:DAL2611/GB-760-Project.git" to clone our project.
    Type "psql" to get into the postgresSQL environment.
    Type "\c tweets" to connect the database.
...

  * In **word_count_postgres.py**: Type "python word_count_postgres.py -like ("-word" is for a word and "--phrase phrase" is for a phrase)".

## Milestone 3

Finally, the files of milestone 3 (M3) are about upgrading our code to use Kafka as a streaming message queue.

  * sudo systemctl start kafka -> sudo systemctl status kafka (for checking)
  * Create Topics in your terminal: ~/kafka/bin/kafka-topics.sh --create --topic gb760 --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
  * Run **server_to_kafka.py**
  * Run **server_from_kafka.py**
  * Run **trendiness_kafka.py -w -word** : As long as this code runs, at each new minute, it should print the most up-to-date trendiness score
