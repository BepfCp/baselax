import haiku as hk
from haiku import nets
from typing import List

def build_network(num_actions: int, hidden_dims: List[int] ) -> hk.Transformed:
    """Factory for a simple MLP network for approximating Q-values."""

    def q(obs):
        network = hk.Sequential([
            hk.Flatten(),
            nets.MLP([*hidden_dims, num_actions])
        ])
        return network(obs)

    return hk.without_apply_rng(hk.transform(q))
