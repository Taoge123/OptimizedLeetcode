''''
-requirement:
users: who and how
scale(write and read): QPS, data size, spike?
performance what is expected write to read delay. expected latency
cost

Zookeeper: configuration service: know which shard is available
cluster proxy: distribute traffic
shard proxy: caching, deal with long url

DB:
Vitess (Youtube) is a Database solution for scaling and managing large clusters of mysql
cassandra: wide column based table: node talks to other node. No more than 3 nodes(gossip protocle)
- processing service uses round robin to chose coordinator node, and use consistent hashing to pick up the correct node
- quorum writes: only 2 out of 3 success, then it's successful
- read quorum use minial vote or version number
- eventual consitency, actually is tunable consistency
-fault tolerant, scalable, asychronic

mangoDB: domcument based, leader based replication
Hbase: column based table, master based

storage stor:
Hadoop / AWS Redshift/ AWS S3


Processing Apache Spark (streaming) / AWS Kinesis
-checking point: a queue saving event, and
-partioning: mutiple queues dealing with a subset of events. Parallization.

partition consumer (infinite loop to deserilize binary data from partition or shard
)
-> deduplicated cache -> aggragator (hash table) -> internal q -> data writer -> dead letter q

dead letter queue, RebbitMQ / AWS SQS: save messages failed to sent. down stream downgration

Patitioner service client
blocking vs nonblocking IO: single thread when do processing, socket will be blocked. slow. but easy to debug.
- Netty: nonblock IO framework

buffering and batching. compress many events to one request. easy to compress, faster, but increase complexity
timeouts: connection time out and request timeout
retries: exponential back off and jitter ( add randomness to retry intervals, seperate retries)
circuit breaker: failure exceeding a thrshold, stop processing. cons: more difficult to test and hardd to determine threshold
- Polly / Netflix Hystrix

Load balancer
-hardware lb: NetScaler
-software lb: NGINX
            AWS ELB, open source
- TCP lb: doesn't check the content of packets, fast, million of request per seconds
  HTTP lb: terminate the connection. based on the content
- round robin
  least connection: send request to the lowest number of active
  least response time: send  to fastest reponse time
  hash based
- DNS
- health checking periodically
- secondary lb to standby

partition service Apache Kafka / AWS Kinesis
- web service
- strategy
  hash based, large scale not work well: hot partition
        include event time
        split hot partition to two more

AWS CloudWatch monitor

Thrift Binary file type

Murmurhash hash function

(distribution message queue)
Frontend service
-request validation
-Athentication and authorization
-Serverside encryption
-caching of metadata
-rate limiting throttling
-request deduplication

Meta data server: facade, cache, load balance

Incluster-Manager vs OutClusterManager
one cluster with many nodes, a leader, many clusters with small set of nodes, no leaders
monitor heartbeats from host, monitor cluster health
deal with leader and follower failures, deal with overheated clusters
split big queue between nodes, clusters

consistent hashing:
drawback: domino effect ; unevenly distributed



requiement specification
-who will use the system
-how will the system be used

-qps
-size
-spikes

performance
-write to read delay

cost
-min development: use open source
-min cost of maintenance: cloud service


youtube total views
individual events: fast write, different cateria, recalculte if needed; slow read, costly for large scale
aggregate data: fast read, ready to go; require aggregation pipline, hard to recalcultae, change caterion

scale mysql:
processing service ->cluster proxy (knows about db) -> configuration service(zookeeper)\
    -> shard proxy (cache, time out queries) -> shard --> read replica

cassandra:
every node knows each other
processing service (round robin) -> coordinator node (use consistent hashing)->
        correct node and calls multiiple nodes for replica
query -> coordinator node -> calls replica , minumum checking on sychronization


front end service host

-> reverse proxy -> frontend service -> cache & local disk

notification sender

tempory storage (mysql, nosql, distributed cache kafka, distributed q)
-> message retriver (use token to control number of rea threa)
-> message sender client -> meta data service -> task creator and executor


Rate limiter
can have negative tokens
how to talk: fully connected, n2; gossip; distributed cache redis; coordinator with leaers

TCP guarantee we get all the packets in the same order, while udp not, but faster


AWS
relational db: RDS, simple to admin and scale, multiple availability zones
object store: s3, highly available and reliable
load b: ELB highly available
cdn: cloudFront
memory cache: Elasticache
nosql: dynamodb

'''