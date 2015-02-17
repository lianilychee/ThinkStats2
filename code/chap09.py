import thinkstats2

class CoinTest(thinkstats2.HypothesisTest):

	def TestStatistic(self, data):
		heads, tails = data
		test_stat = abs(heads - tails)
		return test_stat

	def RunModel(self):
		heads, tails = self.data
		n = heads + tails
		sample = [random.choice('HT') for _ in range (n)]
		hist = thinkstats2.Hist(sample)
		data = hist['H'], hist['T']
		return data

ct = CoinTest((140, 110))
pvalue = ct.PValue()