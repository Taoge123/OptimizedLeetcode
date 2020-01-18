'''
30*24*3600 = 2 M
24*3600 = 0.1 M
2**31 = 2 billion

1 requirement:
functional
1) given a link, our system should give a unique shortened url.
2) when a user access the short link, our server should redirect it to the original link
3) users should be able to create customized link
4) The link should expire after a default period. User can specify

non functional
1) high availability. Server down, all the urls redirection will fail
2) redirecting happen in real time with lower latency
3) short links should not be guessable.

2 capacity estimation and contraints
traffic estimate:
heavy read. assume 100:1 read to write
assuming we have 30M / month,  1M new urls created / day, we expect 1M * 100=100M redirections per day
read QPS = 100 M / 0.1 M = 1000 URLs/ s
write QPS = 1000 / 100 = 10 URLs/ s

storage estimate:
total files: 30M * 5 * 12 = 2B urls for 5 years.
total storage: every url is 500 Bytes, 2B * 500 Bytes = 1TB

brandwidth estimate:
read 1000 * 500 bytes = 500 mb /s
write 5 mb / s

memery estimates:
2-8 rule, 20% url generates 80% traffic.
read 1000 urls / s * 0.2 * 3600 * 24 * 500 bytes = 1 GB per day
Since there will be duplicates request. actual memery should be less than it


3. system api
createURL(api_developer_key, original_url, custom_key, username, expiration_date)

deleteURL(api_dveloper_key, shortened_url)

api_developer_key is to set up limit on each user, to prevent abuse.

4. database design
we need to store billions of records
each object is small
no relations
read - heavy
'''