# Random Number Generators

## mt19937
```cpp
#include <random>
// random seed by Mersenne Twister algorithm
std::mt19937 impl_;

float x = std::uniform_real_distribution<float>(0, 1)(impl_);

std::gamma_distribution<float> distribution(alpha);
sample = distribution(impl_);
```

## others
```cpp
std::normal_distribution<double>
int32 dim = std::uniform_int_distribution<int32>;
std::uniform_int_distribution<int> random_int(1, 5);
std::bernoulli_distribution random_bool;
std::shuffle();
std::uniform_real_distribution<float> distribution(-1.0f, 1.0f);
```