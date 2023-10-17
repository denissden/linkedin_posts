How to use ChatGPT to analyze large amounts of data? 

Almost everybody who used ChatGPT api had a situation where all your data doesn't fit into model's content. You will sure need to reduce the prompt!

To reduce large amounts of plain text, there is one interesting solution on github called pdfGPT. Briefly, the text is split into parts that are sorted by their meaning. If you tinker with a bit, you can make it work not only with pdfs. Be sure to check it out: https://github.com/bhaskatripathi/pdfGPT

But what if you don't want to integrate a self-hosted ML model into your code? It all depends on your situation. On large scale you definitely can afford to have such models. But on small and medium scales you might want to have a lighter-weight backend that connects to external APIs. 

Article repo url: https://github.com/denissden/linkedin_posts/tree/main/1_jellyfish

### Problem

We all like travelling! So here is a database of 500 places to visit. But how do we choose one? Let's ask ChatGPT.

Oops! *This model's maximum context length is 4097 tokens. However, your messages resulted in 18983 tokens. Please reduce the length of the messages.*

What instead of all entries we were sending only a relevant part? We just need to come up with a way to sort the entries by relevance and take a couple from the start of the list.

### Tagging entries

We can handle a part of our recommendations on our side. A simple system like our one-file program can't be as powerful as ChatGPT, but it's still capable. 

How did recommendation systems work a some time ago, when servers were not capable of running huge models? Simple! Everything relied on tags. Why not tag our places?

Our tags will contain
 - emotions you may feel when visiting the place
 - location (city, country) 
 - type of place: a hotel, a restaurant, a park etc. 
 - anything else ChatGPT will think of

ChatGPT will be perfect for generating the tags. For example, here are the generated tags for Central Park: `central park, manhattan, new york city, urban jungle, vast green lawns, winding paths, serene ponds, strolls, picnics, oasis, respite, hustle and bustle`

The nature of ChatGPT will make our tags not exact. It will sometimes use a synonym, sometimes a different form of a word. 

### Searching tags

Remember, the tags are not exact. And user's question doesn't always contain tags. We will also need to retrieve a couple of tags from the question! 

To get question tags, we can use ChatGPT too. Here are the tags for "I want some coffee": `coffee, drink, morning, caffeine, hot beverage, energy, café, espresso, latte, cappuccino, mocha, aroma, dark roast, beans, barista, coffee shop, wake up, mug`

To match the question tags with places' tags we could use a string similarity comparison like [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance). This algorith will smooth out ChatGPT's inconsistent tags. Tags `activities` and `active` will be given a high match score. 

All is left is to rank our places by the amount of matching tags. Top 10 places will be included in the final request to ChatGPT.

### Economy

Above solution may require large amounts of requests to ChatGPT to get the tags for all your entries. It may seem quite expensive at first. But the price of each user's request will be lower since there is a room for reducing the list of entries sent per request. There is also a possibility to optimize the tag generation. In my example each request generates tags for 10 places at once. This method not only reduces token usage but also makes generation a lot quicker.

To reduce tokens while generating entry tags:
 - reduce prompt, but make it informative enough to give the right tags
 - process entries in batches

To reduce tokens per user request:
 - reduce prompt
 - include fewer entries in the prompt

### Final words

Repo url: https://github.com/denissden/linkedin_posts/tree/main/1_jellyfish

The task of preparing and searching through data is not as simple as it is in my example. To make the example easy to understand, many of necessary optimizations were missed. For example, the search time complexity is at best `O(n*m)` where `n = amount of entries` and `m = amount of tags per entry`. The Levenstein algorithm is also `O(n*m)` and there are faster alternatives.

If you are interested how the speed can be improved, please let me know.

Feel free to ask any question and discuss in the comments. Have a nice day!