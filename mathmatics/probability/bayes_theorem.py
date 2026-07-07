class bayes_theorem:
    # updates a prior belief P(H) using new evidence:
    # P(H|E) = P(E|H) * P(H) / P(E)
    # where P(E) (the evidence) is the weighted sum of the likelihood
    # under every hypothesis: sum(P(E|H_i) * P(H_i))
    # time complexity O(K) for K hypotheses, space O(1)
    def calculate(self,likelihood:float,prior:float,priors:list,likelihoods:list)->float:
        if len(priors) != len(likelihoods):
            return None
        evidence = sum(priors[i] * likelihoods[i] for i in range(len(priors)))
        if evidence == 0:
            return None
        return (likelihood * prior) / evidence

# classic "disease test" example:
# prior P(disease) = 0.01, P(positive|disease) = 0.99, P(positive|no disease) = 0.05
priors = [0.01, 0.99]
likelihoods = [0.99, 0.05]
result = bayes_theorem().calculate(likelihoods[0], priors[0], priors, likelihoods)
print(result)
