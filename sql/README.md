# Unpivot in postgresql

Scenario:

You have a table with several columns like this:

id  | val1 | val2
----+------+-----
   1      1     2
   2      1     2

And you want to 'unpivot' it:

id key  val
 1 val1   1
 1 val2   2
 2 val1   1
 2 val2   2

Three methods mentioned here: https://stackoverflow.com/a/6360077/282024

* UNION ALL
* unnest
* hstore

