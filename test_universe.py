"""
Test for Universe Factory - Ticket 2 (Deterministic Generation)
"""
from backend.universe_factory import UniverseFactory


def test_determinism():
    """Test that same seed produces same universe"""
    u1 = UniverseFactory.from_seed(42, 10)
    u2 = UniverseFactory.from_seed(42, 10)
    
    # Check that universes are identical
    assert u1['seed'] == u2['seed'], "Seeds should match"
    assert len(u1['entities']) == len(u2['entities']), "Entity count should match"
    
    for i in range(len(u1['entities'])):
        e1 = u1['entities'][i]
        e2 = u2['entities'][i]
        
        assert e1['id'] == e2['id'], f"Entity {i} ID mismatch"
        assert e1['type'] == e2['type'], f"Entity {i} type mismatch"
        assert e1['x'] == e2['x'], f"Entity {i} x position mismatch"
        assert e1['y'] == e2['y'], f"Entity {i} y position mismatch"
        assert e1['size'] == e2['size'], f"Entity {i} size mismatch"
        assert e1['color'] == e2['color'], f"Entity {i} color mismatch"
    
    print("✓ Determinism test passed - same seed produces identical universe")


def test_different_seeds():
    """Test that different seeds produce different universes"""
    u1 = UniverseFactory.from_seed(42, 10)
    u2 = UniverseFactory.from_seed(123, 10)
    
    # Should have same structure but different content
    assert len(u1['entities']) == len(u2['entities']), "Entity count should match"
    
    # At least one entity should be different
    differences = 0
    for i in range(len(u1['entities'])):
        e1 = u1['entities'][i]
        e2 = u2['entities'][i]
        
        if (e1['x'] != e2['x'] or e1['y'] != e2['y'] or 
            e1['type'] != e2['type'] or e1['color'] != e2['color']):
            differences += 1
    
    assert differences > 0, "Different seeds should produce different universes"
    print(f"✓ Different seeds test passed - {differences}/{len(u1['entities'])} entities differ")


def test_universe_structure():
    """Test that generated universe has correct structure"""
    universe = UniverseFactory.from_seed(42, 50)
    
    # Check top-level structure
    assert 'seed' in universe, "Universe should have seed"
    assert 'entities' in universe, "Universe should have entities"
    assert 'bounds' in universe, "Universe should have bounds"
    
    # Check entities
    assert len(universe['entities']) == 50, "Should have requested number of entities"
    
    # Check first entity structure
    entity = universe['entities'][0]
    required_fields = ['id', 'type', 'x', 'y', 'size', 'color']
    for field in required_fields:
        assert field in entity, f"Entity should have {field} field"
    
    # Check entity types are valid
    valid_types = ['star', 'planet', 'asteroid', 'nebula']
    for entity in universe['entities']:
        assert entity['type'] in valid_types, f"Invalid entity type: {entity['type']}"
    
    print("✓ Structure test passed - universe has correct format")


if __name__ == '__main__':
    print("Running Universe Factory tests...")
    print()
    
    test_determinism()
    test_different_seeds()
    test_universe_structure()
    
    print()
    print("All tests passed! ✓")
