# Reinforcement Learning

## Policy Gradient
- Loss definition: -sum(log(p) * R)
- Policy, returns a probability after softmax
```python
class Policy(nn.Module):
    def __init__(self):
        super(Policy, self).__init__()
        self.affine1 = nn.Linear(4, 128)
        self.dropout = nn.Dropout(p=0.6)
        self.affine2 = nn.Linear(128, 2)

        self.saved_log_probs = []
        self.rewards = []

    def forward(self, x):
        x = self.affine1(x)
        x = self.dropout(x)
        x = F.relu(x)
        action_scores = self.affine2(x)
        return F.softmax(action_scores, dim=1)
```
- Select action from, and save the log-prob and reward trajectory in its own class member??:
```python
from torch.distributions import Categorical

def select_action(state):
    state = torch.from_numpy(state).float().unsqueeze(0)
    probs = policy(state)
    m = Categorical(probs)
    action = m.sample()
    policy.saved_log_probs.append(m.log_prob(action))
    return action.item()
```
- Loop over episode, one trajectory each update:
```python
for t in range(1, 10000):  # Don't infinite loop while learning
    action = select_action(state)
    state, reward, done, _ = env.step(action)
    if args.render:
        env.render()
    policy.rewards.append(reward)
    ep_reward += reward
    if done:
        break
```
- Reinforce:
```python
R = 0
policy_loss = []
returns = []
for r in policy.rewards[::-1]:
    R = r + args.gamma * R
    returns.insert(0, R)
returns = torch.tensor(returns)
returns = (returns - returns.mean()) / (returns.std() + eps)
for log_prob, R in zip(policy.saved_log_probs, returns):
    policy_loss.append(-log_prob * R)
optimizer.zero_grad()
policy_loss = torch.cat(policy_loss).sum()
policy_loss.backward()
optimizer.step()
del policy.rewards[:]
del policy.saved_log_probs[:]
```

## Actor Critic
- Model with shared representation
```python
class Policy(nn.Module):
    def __init__(self):
        super(Policy, self).__init__()
        self.affine1 = nn.Linear(4, 128)
        self.action_head = nn.Linear(128, 2)
        self.value_head = nn.Linear(128, 1)

        self.saved_actions = []
        self.rewards = []

    def forward(self, x):
        x = F.relu(self.affine1(x))
        action_scores = self.action_head(x)
        state_values = self.value_head(x)
        return F.softmax(action_scores, dim=-1), state_values
```
- Select action: save state as well
```python
def select_action(state):
    state = torch.from_numpy(state).float()
    probs, state_value = model(state)
    m = Categorical(probs)
    action = m.sample()
    model.saved_actions.append(SavedAction(m.log_prob(action), state_value))
    return action.item()
```
- Loop over episode, same as PG
- Returns, normalized across the trajectory
```python
returns = []
for r in model.rewards[::-1]:
    R = r + args.gamma * R
    returns.insert(0, R)
returns = torch.tensor(returns)
returns = (returns - returns.mean()) / (returns.std() + eps)
```
- Value loss + PG:
```python
for (log_prob, value), R in zip(saved_actions, returns):
    advantage = R - value.item()
    policy_losses.append(-log_prob * advantage)
    value_losses.append(F.smooth_l1_loss(value, torch.tensor([R])))
```
