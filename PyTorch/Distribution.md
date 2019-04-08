# Distribution

## Probability Distributions
- https://pytorch.org/docs/stable/distributions.html?highlight=distribution#
- Flows the design of TensorFlow Distributions package:
	- Joshua V. Dillon, Ian Langmore, Dustin Tran, Eugene Brevdo, Srinivas Vasudevan, Dave Moore, Brian Patton, Alex Alemi, Matt Hoffman, Rif A. Saurous. TensorFlow Distributions
	- https://arxiv.org/pdf/1711.10604.pdf
- Common usage:
```python
probs = policy_network(state)
# Note that this is equivalent to what used to be called multinomial
m = Categorical(probs)
action = m.sample()
next_state, reward = env.step(action)
loss = -m.log_prob(action) * reward
loss.backward()
```

## The class:
```python
class torch.distributions.distribution.Distribution(batch_shape=torch.Size([]), event_shape=torch.Size([]), validate_args=None)
```
- Members and functions:
```python
batch_shape
cdf(value)
entropy()
log_prob()
mean()
perplexity()
rsample() # reparamatrized
sample_n() # generate n samples
stddev
variance
```
	- Exponential Family
	- Bernoulli
	- Beta
	- Binomial
	- Categorical
	- Cauchy, HalfCauchy
	- Chi2
	- Dirichlet
	- Exponential
	- FisherSnedecor
	- Gamma
	- Geometric
	- Gumbel
	- HalfNormal
	- Laplace
	- LogNormal
	- Multinomial
	- Normal
	- Pareto
	- Poisson
	- StudentT
	- Uniform
	- Weibull
- KL Divergence, implement with decorator
```python
@register_kl(Normal, Normal)
def kl_normal_normal(p, q):
    # insert implementation here
```
- Transforms
```python
class torch.distributions.transforms.Transform(cache_size=0)
   inv()
   sign()
```