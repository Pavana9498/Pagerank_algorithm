This project is a python implementation of page rank.
PageRank is an algorithm used by Google Search to rank web pages in their search engine results. PageRank is a way of measuring the importance of website pages. According to Google:
PageRank works by counting the number and quality of links to a page to determine a rough estimate of how important the website is. The underlying assumption is that more important websites are likely to receive more links from other websites.
A PageRank results from a mathematical algorithm based on
the webgraph, created by all web pages as nodes and hyperlinks as edges(E). The page rank score of page ‘i’ , P(i) is defined as:
P(i) = Ʃ P(j)/O(j) (i,j E E)
We can write the n equations of Page rank as: P = At P where A is the adjacency matrix of our graph. And Power iteration algorithm is used to find P. We use Markov chain framework which models web surfing as a stochastic process and make web graph to meet Markov chain conditions by converting the adjacency matrix into stochastic, irreducible
And aperiodic matrix.
