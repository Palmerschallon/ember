import numpy as np
import torch
import torch.nn as nn

class NeuralToken:
    """Token that carries semantic weight"""
    def __init__(self, value, embedding):
        self.value = value
        self.embedding = embedding

class ThoughtVector(nn.Module):
    """Encodes thoughts as high-dimensional vectors"""
    def __init__(self, dim=512):
        super().__init__()
        self.encoder = nn.TransformerEncoder(
            nn.TransformerEncoderLayer(dim, 8), 
            num_layers=6
        )
