class Config:
  def __init__(self):
    # General settings
    self.environment_path = "./Tennis_Linux/Tennis.x86_64"
    self.num_agents = 2
    self.random_seed = 2 
    self.state_size = None
    self.action_size = None

    self.buffer_size = int(1e6) # replay buffer size
    self.batch_size = 512       # minibatch size
    self.gamma = 0.99           # discount factor
    self.tau = 1e-3             # tau for soft update of target parameters
    self.lr_actor = 3e-4        # learning rate of the actor 
    self.lr_critic = 5e-4       # learning rate of the critic
    self.weight_decay = 0.0     # L2 weight decay
    self.update_every = 5
    

